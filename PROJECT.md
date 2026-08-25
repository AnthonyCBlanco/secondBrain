# Project: Calculus 2 Study Notes System

## Architecture
The system consists of a structured knowledge vault in Obsidian markdown format, cross-linked via WikiLinks, following strict semantic headers and metadata tagging, validated by an automated Python test suite.

### Target Location
`c:\Users\Antho\secondBrain\01_SPACES\SCHOOL\Math\Calculus`

### Topic Modules & Scope
1. **Module 1: Techniques of Integration**
   - `Integration by Parts.md`
   - `Trigonometric Integrals.md`
   - `Trigonometric Substitution.md`
   - `Partial Fractions.md`
   - `Improper Integrals.md`

2. **Module 2: Applications of Integration**
   - `Volume by Disks and Washers.md`
   - `Volume by Cylindrical Shells.md`
   - `Arc Length.md`
   - `Surface Area of Revolution.md`
   - `Work and Physical Applications.md`

3. **Module 3: Sequences and Infinite Series**
   - `Sequences and Limits.md`
   - `Infinite Series and Divergence Test.md`
   - `Integral and Comparison Tests.md`
   - `Alternating Series and Absolute Convergence.md`
   - `Ratio and Root Tests.md`
   - `Power Series and Radius of Convergence.md`
   - `Taylor and Maclaurin Series.md`

4. **Module 4: Parametric Equations and Polar Coordinates**
   - `Parametric Equations and Calculus.md`
   - `Polar Coordinates and Curves.md`
   - `Calculus in Polar Coordinates.md`

5. **Module 5: Test Infrastructure & Verification Harness**
   - `verify_calculus2_notes.py`: Automated validator checking:
     1. Existence of at least 15 target notes.
     2. Exact presence of `### Idea`, `### Formally`, `### Example`, `### Related`.
     3. Tags `#math/calculus #spring2026` at bottom.
     4. At least one Obsidian-style `[[...]]` wikilink per note.
     5. Math content validity (LaTeX notation `$...$` and `$$...$$`).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Vault & Structure Exploration | Inspect existing notes, vault links, and note conventions | None | PLANNED |
| M2 | Test Infrastructure Specification & Runner | Design and write verification script | None | PLANNED |
| M3 | Notes Implementation (Modules 1-4) | Author all 20 Calculus 2 markdown notes with required headers & tags | M1 | PLANNED |
| M4 | Test Execution & Review Verification | Execute verification script, review formatting, wikilinks, and math | M2, M3 | PLANNED |
| M5 | Challenger Stress-Testing | Adversarial validation of math rigor, link integrity, and edge cases | M4 | PLANNED |
| M6 | Forensic Integrity Audit | Static and dynamic audit verifying authenticity and zero hardcoding | M5 | PLANNED |
| M7 | Final Completion & Victory Notification | Notify Sentinel for final acceptance | M6 | PLANNED |

## Interface Contracts & Note Schema
Every generated note MUST conform to the exact structure:
```markdown
## <Topic Name>

### Idea
<Intuitive conceptual explanation with geometric / physical context>

### Formally
<Rigorous mathematical definition, formulas in LaTeX ($...$ and $$...$$), theorems, conditions>

### Example
<Fully worked out step-by-step mathematical example with complete intermediate steps>

### Related
- [[<Related Calculus 1 or Calculus 2 Note 1>]]
- [[<Related Calculus 1 or Calculus 2 Note 2>]]
- [[<Related Calculus 1 or Calculus 2 Note 3>]]

---
#math/calculus #spring2026
```

## Code Layout
- Notes directory: `c:\Users\Antho\secondBrain\01_SPACES\SCHOOL\Math\Calculus\`
- Test script: `c:\Users\Antho\secondBrain\01_SPACES\SCHOOL\Math\Calculus\verify_calculus2_notes.py`
- Agent metadata: `c:\Users\Antho\secondBrain\.agents\`
