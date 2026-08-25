"""
Calculus 2 Study Notes Verification Harness
File: verify_calculus2_notes.py
Author: Explorer 3 / Teamwork Calculus System
Description: Automated verification script for Calculus 2 study notes in Obsidian markdown format.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Optional, Tuple, Any

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==============================================================================
# CANONICAL TOPIC DEFINITIONS (CALCULUS 2 CURRICULUM - 20 CORE TOPICS)
# ==============================================================================

CANONICAL_MODULES: Dict[str, List[str]] = {
    "Module 1: Techniques of Integration": [
        "Integration by Parts.md",
        "Trigonometric Integrals.md",
        "Trigonometric Substitution.md",
        "Partial Fractions.md",
        "Improper Integrals.md",
    ],
    "Module 2: Applications of Integration": [
        "Volume by Disks and Washers.md",
        "Volume by Cylindrical Shells.md",
        "Arc Length.md",
        "Surface Area of Revolution.md",
        "Work and Physical Applications.md",
    ],
    "Module 3: Sequences and Infinite Series": [
        "Sequences and Limits.md",
        "Infinite Series and Divergence Test.md",
        "Integral and Comparison Tests.md",
        "Alternating Series and Absolute Convergence.md",
        "Ratio and Root Tests.md",
        "Power Series and Radius of Convergence.md",
        "Taylor and Maclaurin Series.md",
    ],
    "Module 4: Parametric Equations and Polar Coordinates": [
        "Parametric Equations and Calculus.md",
        "Polar Coordinates and Curves.md",
        "Calculus in Polar Coordinates.md",
    ],
}

ALL_CANONICAL_TOPICS: List[str] = [
    topic for topics in CANONICAL_MODULES.values() for topic in topics
]

CANONICAL_FILENAMES_NORM: Dict[str, str] = {
    name.lower(): name for name in ALL_CANONICAL_TOPICS
}
# Also support "Integration By Parts.md" (title case alias)
CANONICAL_FILENAMES_NORM["integration by parts.md"] = "Integration by Parts.md"

MIN_REQUIRED_NOTES: int = 15
REQUIRED_TAGS: List[str] = ["#math/calculus", "#spring2026"]
REQUIRED_HEADINGS: List[str] = ["### Idea", "### Formally", "### Example", "### Related"]

# ==============================================================================
# DATA STRUCTURES
# ==============================================================================

@dataclass
class ValidationIssue:
    severity: str  # "ERROR" or "WARNING"
    rule_id: str   # e.g., "R-HEAD-MISSING", "R-TAG-MISSING", "R-LINK-NONE", "R-MATH-NONE", "R-CONT-EMPTY-SEC"
    message: str
    line_number: Optional[int] = None
    context: Optional[str] = None

@dataclass
class NoteCheckResult:
    filename: str
    filepath: str
    is_canonical_topic: bool
    module: Optional[str]
    has_required_headings: bool = False
    has_required_tags: bool = False
    has_wikilinks: bool = False
    has_latex_math: bool = False
    has_clean_content: bool = False
    wikilink_count: int = 0
    wikilinks: List[str] = field(default_factory=list)
    unresolved_wikilinks: List[str] = field(default_factory=list)
    math_inline_count: int = 0
    math_block_count: int = 0
    issues: List[ValidationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not any(issue.severity == "ERROR" for issue in self.issues)

    @property
    def errors(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    @property
    def warnings(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "WARNING"]

@dataclass
class SuiteReport:
    total_scanned: int = 0
    total_calc2_discovered: int = 0
    passed_count: int = 0
    failed_count: int = 0
    warning_count: int = 0
    min_required: int = MIN_REQUIRED_NOTES
    count_check_passed: bool = False
    all_passed: bool = False
    results: List[NoteCheckResult] = field(default_factory=list)
    general_issues: List[ValidationIssue] = field(default_factory=list)


# ==============================================================================
# VALIDATION ENGINE
# ==============================================================================

class CalculusNoteValidator:
    """Validator for individual Calculus 2 Obsidian Markdown Notes."""

    RE_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
    RE_WIKILINK = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")
    RE_TAG = re.compile(r"(?:^|\s)(#[a-zA-Z0-9_\/-]+)")
    RE_MATH_BLOCK = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
    RE_MATH_INLINE = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)")
    RE_PLACEHOLDER = re.compile(
        r"(?:<[A-Za-z0-9\s_\-\/]+>|\bTODO\b|\bTBD\b|\bFIXME\b|\[placeholder\])",
        re.IGNORECASE
    )

    def __init__(self, target_dir: Path, vault_root: Optional[Path] = None):
        self.target_dir = target_dir
        self.vault_root = vault_root or self._infer_vault_root(target_dir)
        self.known_vault_notes: Set[str] = self._index_vault_notes()

    def _infer_vault_root(self, start_dir: Path) -> Path:
        curr = start_dir.resolve()
        for _ in range(5):
            if (curr / ".obsidian").exists() or (curr / "01_SPACES").exists():
                return curr
            if curr.parent == curr:
                break
            curr = curr.parent
        return start_dir.resolve()

    def _index_vault_notes(self) -> Set[str]:
        notes = set()
        search_root = self.vault_root if self.vault_root.exists() else self.target_dir
        for p in search_root.rglob("*.md"):
            notes.add(p.stem.lower())
            notes.add(p.name.lower())
        for topic in ALL_CANONICAL_TOPICS:
            stem = topic[:-3] if topic.endswith(".md") else topic
            notes.add(stem.lower())
            notes.add(topic.lower())
        return notes

    def is_calc2_candidate(self, filepath: Path, content: str) -> bool:
        """Determines if a markdown file is a Calculus 2 note candidate."""
        name_norm = filepath.name.lower()
        if name_norm in CANONICAL_FILENAMES_NORM:
            return True
        if "#spring2026" in content:
            return True
        return False

    def validate_file(self, filepath: Path) -> NoteCheckResult:
        """Runs the full validation suite on a single markdown file."""
        try:
            content = filepath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content = filepath.read_text(encoding="utf-8-sig")
            except Exception as e:
                res = NoteCheckResult(
                    filename=filepath.name,
                    filepath=str(filepath.resolve()),
                    is_canonical_topic=False,
                    module=None,
                )
                res.issues.append(ValidationIssue(
                    severity="ERROR",
                    rule_id="R-FILE-01",
                    message=f"Failed to read file encoding: {e}"
                ))
                return res

        lines = content.splitlines()
        name_norm = filepath.name.lower()
        is_canonical = name_norm in CANONICAL_FILENAMES_NORM
        
        module_name = None
        if is_canonical:
            canon_name = CANONICAL_FILENAMES_NORM[name_norm]
            for mod, topics in CANONICAL_MODULES.items():
                if canon_name in topics:
                    module_name = mod
                    break

        result = NoteCheckResult(
            filename=filepath.name,
            filepath=str(filepath.resolve()),
            is_canonical_topic=is_canonical,
            module=module_name,
        )

        # 1. Heading Checks
        self._check_headings(content, lines, result)

        # 2. Tag Checks
        self._check_tags(content, lines, result)

        # 3. Wikilink Checks
        self._check_wikilinks(content, lines, result)

        # 4. Math / LaTeX Checks
        self._check_math(content, lines, result)

        # 5. Content Quality & Placeholder Checks
        self._check_content_quality(content, lines, result)

        return result

    def _check_headings(self, content: str, lines: List[str], result: NoteCheckResult) -> None:
        """Verifies exact required headings: ### Idea, ### Formally, ### Example, ### Related."""
        found_headings: Dict[str, Tuple[int, str]] = {}
        for idx, line in enumerate(lines, start=1):
            m = self.RE_HEADING.match(line)
            if m:
                level_str, heading_text = m.groups()
                level = len(level_str)
                cleaned_text = heading_text.strip()
                if level == 3:
                    if cleaned_text == "Idea":
                        found_headings["Idea"] = (idx, line)
                    elif cleaned_text == "Formally":
                        found_headings["Formally"] = (idx, line)
                    elif cleaned_text.startswith("Example"):
                        found_headings["Example"] = (idx, line)
                    elif cleaned_text in ("Related", "Related Notes"):
                        found_headings["Related"] = (idx, line)
                elif level == 2 or level == 4:
                    if cleaned_text in ("Idea", "Formally", "Example", "Related", "Related Notes"):
                        result.issues.append(ValidationIssue(
                            severity="ERROR",
                            rule_id="R-HEAD-LEVEL",
                            message=f"Heading '{cleaned_text}' has wrong level 'H{level}' (expected '### {cleaned_text}')",
                            line_number=idx,
                            context=line
                        ))

        missing = []
        for req in ["Idea", "Formally", "Example", "Related"]:
            if req not in found_headings:
                missing.append(f"### {req}")

        if missing:
            result.has_required_headings = False
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-HEAD-MISSING",
                message=f"Missing required section heading(s): {', '.join(missing)}"
            ))
        else:
            result.has_required_headings = True
            order = ["Idea", "Formally", "Example", "Related"]
            line_numbers = [found_headings[k][0] for k in order]
            if line_numbers != sorted(line_numbers):
                result.issues.append(ValidationIssue(
                    severity="ERROR",
                    rule_id="R-HEAD-ORDER",
                    message="Headings out of order. Required sequence: ### Idea -> ### Formally -> ### Example -> ### Related"
                ))

    def _check_tags(self, content: str, lines: List[str], result: NoteCheckResult) -> None:
        """Verifies presence of required tags and bottom placement."""
        found_tags: Set[str] = set()
        tag_lines: Dict[str, int] = {}

        for idx, line in enumerate(lines, start=1):
            matches = self.RE_TAG.findall(line)
            for tag in matches:
                found_tags.add(tag)
                tag_lines[tag] = idx

        missing_tags = [t for t in REQUIRED_TAGS if t not in found_tags]
        if missing_tags:
            result.has_required_tags = False
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-TAG-MISSING",
                message=f"Missing required tag(s): {', '.join(missing_tags)}"
            ))
        else:
            result.has_required_tags = True
            related_line = None
            for idx, line in enumerate(lines, start=1):
                if line.strip().startswith("### Related"):
                    related_line = idx
                    break

            for req_tag in REQUIRED_TAGS:
                t_line = tag_lines.get(req_tag, 0)
                if related_line and t_line < related_line:
                    result.issues.append(ValidationIssue(
                        severity="ERROR",
                        rule_id="R-TAG-POS",
                        message=f"Tag '{req_tag}' at line {t_line} is placed before '### Related' (line {related_line}); tags must be at the bottom of the note",
                        line_number=t_line
                    ))

    def _check_wikilinks(self, content: str, lines: List[str], result: NoteCheckResult) -> None:
        """Verifies presence and resolution of [[...]] wikilinks."""
        links: List[str] = []
        raw_matches = self.RE_WIKILINK.findall(content)
        
        for target, _ in raw_matches:
            target_clean = target.strip()
            if "#" in target_clean:
                target_clean = target_clean.split("#")[0].strip()
            if target_clean:
                links.append(target_clean)

        result.wikilink_count = len(links)
        result.wikilinks = links

        if len(links) == 0:
            result.has_wikilinks = False
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-LINK-NONE",
                message="Note does not contain any Obsidian [[...]] wiki-links (at least 1 required)"
            ))
        else:
            result.has_wikilinks = True
            unresolved = []
            for link in links:
                link_norm = link.lower()
                stem_norm = link_norm[:-3] if link_norm.endswith(".md") else link_norm
                if stem_norm not in self.known_vault_notes and link_norm not in self.known_vault_notes:
                    unresolved.append(link)

            result.unresolved_wikilinks = unresolved
            if unresolved:
                result.issues.append(ValidationIssue(
                    severity="WARNING",
                    rule_id="R-LINK-UNRESOLVED",
                    message=f"Note contains {len(unresolved)} unindexed or external wiki-link target(s): {', '.join(unresolved[:5])}"
                ))

    def _check_math(self, content: str, lines: List[str], result: NoteCheckResult) -> None:
        """Verifies LaTeX math formulas and delimiter balance."""
        raw_double_dollars = content.count("$$")
        if raw_double_dollars % 2 != 0:
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-MATH-DELIM-BLOCK",
                message=f"Unbalanced display math delimiters ($$ count is {raw_double_dollars}, expected even)"
            ))

        content_no_code = re.sub(r"```[\s\S]*?```", "", content)
        content_no_blocks = re.sub(r"\$\$[\s\S]*?\$\$", "", content_no_code)
        
        for line_num, line in enumerate(content_no_blocks.splitlines(), start=1):
            clean_line = re.sub(r"\\\$", "", line)
            d_count = clean_line.count("$")
            if d_count % 2 != 0:
                result.issues.append(ValidationIssue(
                    severity="WARNING",
                    rule_id="R-MATH-DELIM-INLINE",
                    message=f"Odd number of inline '$' delimiters ({d_count}) on line {line_num}",
                    line_number=line_num,
                    context=line.strip()
                ))

        blocks = self.RE_MATH_BLOCK.findall(content)
        inlines = self.RE_MATH_INLINE.findall(content_no_code)

        result.math_block_count = len(blocks)
        result.math_inline_count = len(inlines)

        if len(blocks) == 0 and len(inlines) == 0:
            result.has_latex_math = False
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-MATH-NONE",
                message="Note does not contain any LaTeX mathematical formulas ($...$ or $$...$$)"
            ))
        else:
            result.has_latex_math = True

    def _check_content_quality(self, content: str, lines: List[str], result: NoteCheckResult) -> None:
        """Verifies section non-emptiness, placeholder absence, and markdown formatting."""
        placeholders_found = []
        for idx, line in enumerate(lines, start=1):
            matches = self.RE_PLACEHOLDER.findall(line)
            for m in matches:
                if m.startswith("<") and m.endswith(">"):
                    inner = m[1:-1].strip()
                    if inner.lower() in ("topic name", "example", "formula", "related note 1", "related note 2", "description", "intuitive conceptual explanation", "rigorous mathematical definition"):
                        placeholders_found.append((idx, m, line))
                else:
                    placeholders_found.append((idx, m, line))

        if placeholders_found:
            for line_no, ph, ctx in placeholders_found[:3]:
                result.issues.append(ValidationIssue(
                    severity="ERROR",
                    rule_id="R-CONT-PLACEHOLDER",
                    message=f"Placeholder token '{ph}' detected at line {line_no}",
                    line_number=line_no,
                    context=ctx.strip()
                ))

        sections = self._extract_sections(content)
        for sec_name in ["Idea", "Formally", "Example", "Related"]:
            if sec_name in sections:
                body = sections[sec_name].strip()
                if len(body) < 15:
                    result.issues.append(ValidationIssue(
                        severity="ERROR",
                        rule_id="R-CONT-EMPTY-SEC",
                        message=f"Section '### {sec_name}' body is suspiciously short or empty ({len(body)} characters)"
                    ))

        code_fence_count = sum(1 for line in lines if line.strip().startswith("```"))
        if code_fence_count % 2 != 0:
            result.issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-CONT-CODE-FENCE",
                message=f"Unbalanced code fences (found {code_fence_count} '```' markers)"
            ))

        result.has_clean_content = not any(
            issue.rule_id.startswith("R-CONT-") and issue.severity == "ERROR"
            for issue in result.issues
        )

    def _extract_sections(self, content: str) -> Dict[str, str]:
        """Extracts content between ### headings."""
        sections: Dict[str, str] = {}
        lines = content.splitlines()
        current_sec = None
        current_lines: List[str] = []

        for line in lines:
            if line.strip().startswith("### "):
                if current_sec:
                    sections[current_sec] = "\n".join(current_lines)
                h_name = line.strip()[4:].strip()
                if h_name.startswith("Example"):
                    current_sec = "Example"
                elif h_name in ("Related", "Related Notes"):
                    current_sec = "Related"
                else:
                    current_sec = h_name
                current_lines = []
            elif line.strip().startswith("---") and current_sec == "Related":
                if current_sec:
                    sections[current_sec] = "\n".join(current_lines)
                    current_sec = None
                    current_lines = []
            elif current_sec is not None:
                current_lines.append(line)

        if current_sec and current_lines:
            sections[current_sec] = "\n".join(current_lines)

        return sections


# ==============================================================================
# TEST HARNESS & RUNNER
# ==============================================================================

class CalculusVerificationSuite:
    """Orchestrates test execution across all Calculus 2 notes."""

    def __init__(self, target_dir: Path, vault_root: Optional[Path] = None, strict: bool = False):
        self.target_dir = target_dir
        self.vault_root = vault_root
        self.strict = strict
        self.validator = CalculusNoteValidator(target_dir, vault_root)

    def run(self) -> SuiteReport:
        report = SuiteReport()
        if not self.target_dir.exists():
            report.general_issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-SUITE-DIR",
                message=f"Target directory does not exist: {self.target_dir}"
            ))
            return report

        discovered_files: List[Path] = []
        for file in sorted(self.target_dir.glob("*.md")):
            report.total_scanned += 1
            try:
                content = file.read_text(encoding="utf-8", errors="ignore")
                if self.validator.is_calc2_candidate(file, content):
                    discovered_files.append(file)
            except Exception:
                continue

        report.total_calc2_discovered = len(discovered_files)
        report.count_check_passed = (len(discovered_files) >= MIN_REQUIRED_NOTES)

        if not report.count_check_passed:
            report.general_issues.append(ValidationIssue(
                severity="ERROR",
                rule_id="R-COUNT-INSUFFICIENT",
                message=f"Found {len(discovered_files)} Calculus 2 notes, but minimum required is {MIN_REQUIRED_NOTES} (Target: {len(ALL_CANONICAL_TOPICS)})"
            ))

        for file in discovered_files:
            res = self.validator.validate_file(file)
            report.results.append(res)
            if res.passed:
                report.passed_count += 1
            else:
                report.failed_count += 1
            report.warning_count += len(res.warnings)

        no_errors = (report.failed_count == 0 and len(report.general_issues) == 0)
        no_warnings = (report.warning_count == 0) if self.strict else True
        report.all_passed = no_errors and report.count_check_passed and no_warnings

        return report


# ==============================================================================
# REPORTING & FORMATTERS (ASCII-SAFE FOR ALL CONSOLES)
# ==============================================================================

class ConsoleColor:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    GRAY = "\033[90m"


def format_console_report(report: SuiteReport, verbose: bool = False) -> str:
    lines = []
    lines.append("=" * 80)
    lines.append("CALCULUS 2 STUDY NOTES AUTOMATED VERIFICATION SUITE")
    lines.append("=" * 80)
    lines.append(f"Target Directory      : {report.results[0].filepath if report.results else 'N/A'}")
    lines.append(f"Total Notes Discovered: {report.total_calc2_discovered} (Min Required: {report.min_required})")
    lines.append("-" * 80)

    for issue in report.general_issues:
        lines.append(f"[{issue.severity}] {issue.rule_id}: {issue.message}")

    for idx, res in enumerate(report.results, start=1):
        status_str = "PASS" if res.passed else "FAIL"
        canon_str = "[Canonical]" if res.is_canonical_topic else "[Custom]"
        lines.append(f" {idx:2d}. [{status_str}] {canon_str} {res.filename}")
        
        if verbose or not res.passed or res.warnings:
            lines.append(f"     |-- Headings : {'PASS' if res.has_required_headings else 'FAIL'} (Idea, Formally, Example, Related)")
            lines.append(f"     |-- Tags     : {'PASS' if res.has_required_tags else 'FAIL'} (#math/calculus #spring2026 at bottom)")
            lines.append(f"     |-- Wikilinks: {'PASS' if res.has_wikilinks else 'FAIL'} ({res.wikilink_count} links, {len(res.unresolved_wikilinks)} unresolved)")
            lines.append(f"     |-- LaTeX    : {'PASS' if res.has_latex_math else 'FAIL'} ({res.math_inline_count} inline, {res.math_block_count} block)")
            lines.append(f"     \\-- Content  : {'PASS' if res.has_clean_content else 'FAIL'} (No placeholders, valid bodies)")

            for err in res.errors:
                loc = f" (line {err.line_number})" if err.line_number else ""
                lines.append(f"         * [ERROR {err.rule_id}]{loc}: {err.message}")
            for warn in res.warnings:
                loc = f" (line {warn.line_number})" if warn.line_number else ""
                lines.append(f"         * [WARN  {warn.rule_id}]{loc}: {warn.message}")

    lines.append("=" * 80)
    lines.append("SUMMARY TEST RESULTS:")
    lines.append(f"  - Notes Discovered : {report.total_calc2_discovered} / {len(ALL_CANONICAL_TOPICS)} target (>= {report.min_required} required)")
    lines.append(f"  - Notes Passing    : {report.passed_count}")
    lines.append(f"  - Notes Failing    : {report.failed_count}")
    lines.append(f"  - Total Warnings   : {report.warning_count}")
    
    if report.all_passed:
        lines.append("\n[PASS] ALL CALCULUS 2 VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    else:
        lines.append("\n[FAIL] VERIFICATION FAILED - PLEASE RESOLVE DETECTED ISSUES ABOVE.")
    lines.append("=" * 80)
    return "\n".join(lines)


def generate_json_report(report: SuiteReport) -> str:
    """Emits structured JSON report for programmatic consumption."""
    raw = asdict(report)
    return json.dumps(raw, indent=2)


# ==============================================================================
# CLI ENTRY POINT
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Automated Verification Harness for Calculus 2 Obsidian Study Notes"
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=str(Path(__file__).parent.resolve()),
        help="Path to directory containing Calculus study notes (default: current script dir)",
    )
    parser.add_argument(
        "--vault-root",
        type=str,
        default=None,
        help="Path to Obsidian vault root for cross-note resolution (optional)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Display verbose diagnostics for passing checks",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output test report as JSON to stdout",
    )
    parser.add_argument(
        "--json-output",
        type=str,
        default=None,
        help="Save test report JSON to specified file path",
    )

    args = parser.parse_args()

    target_path = Path(args.dir).resolve()
    vault_root = Path(args.vault_root).resolve() if args.vault_root else None

    suite = CalculusVerificationSuite(
        target_dir=target_path,
        vault_root=vault_root,
        strict=args.strict,
    )

    report = suite.run()

    if args.json_output:
        out_path = Path(args.json_output).resolve()
        out_path.write_text(generate_json_report(report), encoding="utf-8")

    if args.json:
        print(generate_json_report(report))
    else:
        print(format_console_report(report, verbose=args.verbose))

    sys.exit(0 if report.all_passed else 1)


if __name__ == "__main__":
    main()
