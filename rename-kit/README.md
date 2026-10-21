# 🏷️ RenameKit

A simple Python utility that batch renames files with prefixes, suffixes, find-and-replace, and sequential numbering, with a preview before applying changes.

Part of the [Tools](../README.md) repository — a collection of small, practical tools built one day at a time.

## ✨ Features

- Batch rename multiple files in a directory.
- Add custom prefixes and suffixes to filenames.
- Find and replace text in filenames.
- Rename files using sequential numbering.
- Filter files by extension.
- Preview filename changes before applying them.
- Protect against filename collisions.
- Undo previous renaming operations using rename history.
- Keep the original file contents unchanged.

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Python standard library

## 📋 Prerequisites

- Python 3.9 or later.
- Python installed and available in your terminal.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kumayl-Lokhandwala/Tools.git
cd Tools/rename-kit
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

RenameKit uses Python's standard library, so no additional packages are required unless your project specifies otherwise.

## ▶️ Usage

### 1. Run the script

From the `rename-kit` directory, run:

```bash
python rename_kit.py
```

### 2. Configure your renaming options

Choose the renaming operations you want to perform, such as:

- Adding a prefix or suffix.
- Replacing text in filenames.
- Applying sequential numbering.
- Filtering files by extension.

Use the directory and options supported by the script to configure your batch rename operation.

### 3. Preview and apply changes

Review the proposed filename changes before confirming the operation. RenameKit checks for filename collisions to help prevent accidental overwrites.

### 4. Undo changes

Use the available rename history to reverse a previous renaming operation when needed.

## 📁 Project Structure

```text
rename-kit/
├── README.md
├── rename_kit.py
└── tests/                 # Local tests (not included in the repository)
```

The `tests/` directory is kept locally and is not included in the published repository.

## ⚠️ Notes

- Always review the preview before confirming a batch rename.
- Back up important files before performing large renaming operations.
- Filename changes depend on the options and filters selected.
- Avoid modifying files in directories where you do not have the appropriate permissions.
- Keep the original files backed up if you may need to reverse changes manually.

## 🤝 Contributing

Found a bug or have an idea for improvement? Feel free to open an issue or submit a pull request.

## 📜 License

Refer to the license in the root of the repository.

---

**Built to keep file renaming simple.** 🛠️
