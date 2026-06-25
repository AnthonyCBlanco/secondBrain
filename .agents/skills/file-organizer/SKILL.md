---
name: file-organizer
description: Organizes loose files in the vault into their appropriate folders (under Spaces, Timeline, or Atlas) based on their content, metadata, and tags, creating new subfolders if needed.
---

# Instructions

You are tasked with organizing unorganized files in this Obsidian vault. Follow these steps carefully:

## 1. Scan for Unorganized Files
- Identify files in the root folder or files marked as "unorganized" (or ask the user if they want to target a specific folder/inbox).
- Ignore system folders like `00_SYSTEM`, `.git`, `.obsidian`, `.agents`, `.claude`, or `.claudian`.

## 2. Determine the Appropriate Target Folder
For each file, read its content, tags, title, and metadata to classify it:
- **Timeline / Daily Notes**:
  - Files named after dates (e.g., `YYYY-MM-DD.md`) or containing diary/daily review content.
  - Target: `02_TIMELINE/DAILY NOTES/`
- **School**:
  - Notes containing course material, lecture notes, or tags like `#school/<course-name>` or `#class/<course-name>`.
  - Target: `01_SPACES/SCHOOL/<Course Name>/` (create the `<Course Name>` folder if it doesn't exist).
- **Projects**:
  - Notes containing active project plans, project tasks, or tags like `#project/<project-name>`.
  - Target: `01_SPACES/PROJECTS/<Project Name>/` (create the `<Project Name>` folder if it doesn't exist).
- **Personal**:
  - Journal entries, personal habits, hobbies, or general personal thoughts.
  - Target: `01_SPACES/PERSONAL/`
- **Atlas**:
  - Maps of content (MOCs), indices, or high-level reference maps.
  - Target: `03_ATLAS/`

## 3. Plan and Preview
- Create a list of proposed file moves:
  - Source path: `[file basename](file:///absolute/source/path)`
  - Destination path: `[file basename](file:///absolute/destination/path)`
- Present this plan to the user for approval before making any changes.

## 4. Execute and Verify
- After receiving approval, move the files to their target destinations.
- Automatically create any necessary parent/subdirectories.
- Ensure that any Obsidian internal Wikilinks (`[[Note Name]]`) remain intact and functional.
