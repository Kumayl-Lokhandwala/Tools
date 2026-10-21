# RenameKit

A lightweight batch file renaming utility built with Python's standard library.

## Features

- Preview filename changes before applying them
- Add prefixes and suffixes
- Find and replace filename text
- Number files sequentially
- Filter files by extension
- Undo the most recent rename operation
- Detect duplicate names and prevent accidental overwrites

## Requirements

- Python 3.10 or newer
- No external dependencies

## Run

```bash
python main.py
```

## Safety

Test on copies of your files first. RenameKit previews changes and requires
explicit confirmation before renaming files.

Rename history is stored locally in `~/.renamekit_history.json`.
