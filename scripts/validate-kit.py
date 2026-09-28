#!/usr/bin/env python3
"""Validate this kit's internal references and structural contracts.

    python3 scripts/validate-kit.py

Exits non-zero and lists every problem found. Uses only the standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = KIT_ROOT / "template"
PIPELINES = TEMPLATE / "_workspace" / "pipelines"

REQUIRED_STAGE_SECTIONS = ["Inputs", "Do NOT load", "Process", "Audit", "Artifacts"]
GATE_SECTIONS = {"Gate", "Review gate"}

# Paths an agent creates at run time; they cannot exist in the template.
RUNTIME_PATH = re.compile(r"_workspace/(runs/(active|archive)/.+|backlog/items/.+|artifacts/[^/]+/.+)")
PLACEHOLDER = re.compile(r"[<>*{}]|YYYY|NN_")
WORKSPACE_PATH = re.compile(r"`(_workspace/[^`\s]+)`")
STAGE_CONTRACT = re.compile(r"`(stages/[^`\s]+\.md)`")
NESTED_HANDOFF = re.compile(r"runs/active/<run-slug>/stages/[^`\s/]+/")

FORBIDDEN_TEXT = {
    "_workspace/outputs": "legacy outputs layout",
    "`output/`": "legacy run output folder",
    "workspace-kit-public": "old public repository",
    "canonical/": "private source tooling",
    "sync-workspaces": "private source tooling",
    "migrate-workspace": "private source tooling",
    "templates/devops": "private source path",
    "/Users/": "machine-specific path",
    "/home/": "machine-specific path",
    "opencode": "runtime adapter",
    "OpenCode": "runtime adapter",
}
# The ICM paper names its own Layer 0 file; only the alignment doc may say so.
RUNTIME_NAME_ALLOWED = {Path("docs/concepts/icm-alignment.md")}
RUNTIME_NAMES = ("CLAUDE.md", "Claude")
FORBIDDEN_PATHS = {".opencode", "CLAUDE.md", "node_modules", "__pycache__", ".venv"}
SELF = Path("scripts/validate-kit.py")


def text_files() -> list[Path]:
    return sorted(
        p for p in KIT_ROOT.rglob("*")
        if p.is_file() and ".git" not in p.relative_to(KIT_ROOT).parts and p.suffix in {".md", ".py", ".txt", ""}
    )


def check_forbidden(problems: list[str]) -> None:
    for path in KIT_ROOT.rglob("*"):
        rel = path.relative_to(KIT_ROOT)
        if ".git" in rel.parts:
            continue
        if path.name in FORBIDDEN_PATHS:
            problems.append(f"{rel}: forbidden file or directory")
    for path in text_files():
        rel = path.relative_to(KIT_ROOT)
        if rel == SELF or rel == Path("LICENSE"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for needle, why in FORBIDDEN_TEXT.items():
            if needle in text:
                problems.append(f"{rel}: contains {needle!r} ({why})")
        if rel not in RUNTIME_NAME_ALLOWED:
            for name in RUNTIME_NAMES:
                if name in text:
                    problems.append(f"{rel}: contains {name!r} (runtime-specific name)")


def check_workspace_paths(problems: list[str]) -> None:
    for path in sorted(TEMPLATE.rglob("*.md")):
        rel = path.relative_to(KIT_ROOT)
        for match in WORKSPACE_PATH.finditer(path.read_text(encoding="utf-8")):
            ref = match.group(1)
            if PLACEHOLDER.search(ref) or RUNTIME_PATH.match(ref):
                continue
            if not (TEMPLATE / ref.rstrip("/")).exists():
                problems.append(f"{rel}: references missing {ref}")


def check_pipelines(problems: list[str]) -> None:
    for pipeline in sorted(p for p in PIPELINES.iterdir() if p.is_dir()):
        spec = pipeline / "PIPELINE.md"
        rel_pipeline = pipeline.relative_to(KIT_ROOT)
        if not spec.is_file():
            problems.append(f"{rel_pipeline}: missing PIPELINE.md")
            continue
        routed = {
            ref for ref in STAGE_CONTRACT.findall(spec.read_text(encoding="utf-8"))
            if not PLACEHOLDER.search(ref)
        }
        if not routed:
            problems.append(f"{rel_pipeline}/PIPELINE.md: routes no stage contracts")
        for contract in sorted(routed):
            if not (pipeline / contract).is_file():
                problems.append(f"{rel_pipeline}/PIPELINE.md: routes missing {contract}")
        on_disk = {p.relative_to(pipeline).as_posix() for p in (pipeline / "stages").glob("*/*.md")}
        for orphan in sorted(on_disk - routed):
            problems.append(f"{rel_pipeline}: stage contract not routed by PIPELINE.md: {orphan}")
        for contract in sorted(on_disk):
            text = (pipeline / contract).read_text(encoding="utf-8")
            headings = re.findall(r"^## (.+)$", text, re.M)
            for section in REQUIRED_STAGE_SECTIONS:
                if section not in headings:
                    problems.append(f"{rel_pipeline}/{contract}: missing '## {section}'")
            if not GATE_SECTIONS & set(headings):
                problems.append(f"{rel_pipeline}/{contract}: missing '## Gate' or '## Review gate'")
            if NESTED_HANDOFF.search(text):
                problems.append(f"{rel_pipeline}/{contract}: stage handoff is not flat under stages/")


def check_routing(problems: list[str]) -> None:
    table = TEMPLATE / "_workspace" / "map" / "routing-table.md"
    text = table.read_text(encoding="utf-8")
    shipped = {p.name for p in PIPELINES.iterdir() if p.is_dir()}
    routed = set(re.findall(r"_workspace/pipelines/([^/`]+)/PIPELINE\.md", text))
    for name in sorted(shipped - routed):
        problems.append(f"template/_workspace/map/routing-table.md: pipeline not routed: {name}")
    routes = TEMPLATE / "_workspace" / "map" / "routes"
    routed_workflows = set()
    for route in routes.glob("*.md"):
        routed_workflows |= set(re.findall(r"_workspace/workflows/[^`\s]+\.md", route.read_text(encoding="utf-8")))
    workflows = TEMPLATE / "_workspace" / "workflows"
    for wf in sorted(workflows.rglob("*.md")):
        ref = "_workspace/" + wf.relative_to(TEMPLATE / "_workspace").as_posix()
        if wf.name != "README.md" and ref not in routed_workflows:
            problems.append(f"{wf.relative_to(KIT_ROOT)}: workflow not reachable from any route file")


def main() -> int:
    problems: list[str] = []
    if not (TEMPLATE / "AGENTS.md").is_file():
        problems.append("template/AGENTS.md: missing")
    check_forbidden(problems)
    check_workspace_paths(problems)
    check_pipelines(problems)
    check_routing(problems)
    if problems:
        print(f"{len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("Kit is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
