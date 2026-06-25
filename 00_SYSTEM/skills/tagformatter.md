---
name: tagformatter
description: Standardizes note tags across the workspace to match the format of a reference example note.
---

# Instructions

You are tasked with standardizing tags for all Markdown files in this vault. Follow these steps:

1. **Locate the Reference Note**:
   - Look in `00_SYSTEM/skills/examples` (or ask the user if they want to specify a different file).
   - Analyze the tagging format:
     - Are the tags at to bottom of the file?
     - Are tags formatted in a specific casing (e.g., lowercase, kebab-case)?
     - Are there inline tags (e.g., `#tag-name`) in the body that should be moved?
     - Are there redundant tags (e.g., `#math/calculus` and `#calculus`)

2. **Standardize Workspace Notes**:
   - Scan all Markdown files in the workspace (excluding `/00_SYSTEM` and other configuration folders).
   - Parse each note's and content.
   - Re-format the tags to match the pattern of the reference note.
   - Preserve all other frontmatter attributes and the note's body content intact.

3. **Verify and Preview**:
   - Show the user a preview of the changes (diffs) for a few sample files before applying them vault-wide.
