
from pathlib import Path
import json
import uuid

HISTORY_FILE = Path.home() / ".renamekit_history.json"


def load_history():
    if not HISTORY_FILE.exists():
        return []
    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read rename history.")
        return []


def save_history(history):
    HISTORY_FILE.write_text(
        json.dumps(history, indent=2),
        encoding="utf-8",
    )


def get_files(folder, extension):
    files = [
        path for path in folder.iterdir()
        if path.is_file() and path.name != HISTORY_FILE.name
    ]

    if extension.strip():
        ext = extension.strip().lower()
        if not ext.startswith("."):
            ext = "." + ext
        files = [path for path in files if path.suffix.lower() == ext]

    return sorted(files, key=lambda path: path.name.lower())


def build_name(path, mode, value, extra=""):
    stem, suffix = path.stem, path.suffix

    if mode == "1":
        return f"{value}{path.name}"

    if mode == "2":
        return f"{stem}{value}{suffix}"

    if mode == "3":
        return f"{stem.replace(value, extra)}{suffix}"

    if mode == "4":
        return f"{value}_{int(extra):0{int(extra) + 0}d}{suffix}"

    if mode == "5":
        return f"{value}_{extra:0>3}{suffix}"

    return path.name


def create_plan(files, mode, value, extra):
    plan = []

    for index, path in enumerate(files, start=1):
        if mode == "4":
            new_name = f"{value}_{index:03d}{path.suffix}"
        else:
            new_name = build_name(path, mode, value, extra)

        target = path.with_name(new_name)
        if target != path:
            plan.append((path, target))

    return plan


def validate_plan(plan):
    # Windows filenames are case-insensitive in normal use.
    target_names = [str(target).casefold() for _, target in plan]

    if len(target_names) != len(set(target_names)):
        raise ValueError("Two or more files would have the same new name.")

    source_paths = {str(source).casefold() for source, _ in plan}

    for source, target in plan:
        if target.exists() and str(target).casefold() not in source_paths:
            raise ValueError(f"Target already exists: {target.name}")


def apply_plan(plan):
    """Rename in two phases to avoid collisions between source filenames."""
    temporary = []
    completed = []

    try:
        for source, target in plan:
            temp = source.with_name(f".renamekit-{uuid.uuid4().hex}.tmp")
            source.rename(temp)
            temporary.append((temp, target, source))

        for temp, target, source in temporary:
            temp.rename(target)
            completed.append((source, target))

    except Exception:
        # Best-effort rollback if any rename fails.
        for temp, target, source in reversed(temporary):
            try:
                if temp.exists():
                    temp.rename(source)
                elif target.exists():
                    target.rename(source)
            except OSError:
                print(f"Manual recovery may be needed for: {source}")
        raise

    return completed


def undo_last():
    history = load_history()

    if not history:
        print("There is no rename operation to undo.")
        return

    operation = history[-1]
    pairs = [
        (Path(item["new"]), Path(item["old"]))
        for item in operation
    ]

    try:
        validate_plan(pairs)
        apply_plan(pairs)
    except (OSError, ValueError) as error:
        print(f"Undo failed: {error}")
        return

    history.pop()
    save_history(history)
    print(f"Undo successful. Restored {len(pairs)} file(s).")


def main():
    print("\n=== RenameKit | Batch File Renamer ===\n")
    print("1. Add prefix")
    print("2. Add suffix")
    print("3. Find and replace text")
    print("4. Number files sequentially")
    print("5. Undo last rename")

    mode = input("\nChoose an option (1-5): ").strip()

    if mode == "5":
        undo_last()
        return

    if mode not in {"1", "2", "3", "4"}:
        print("Invalid option.")
        return

    folder_text = input("Folder path: ").strip().strip('"')
    folder = Path(folder_text).expanduser()

    if not folder.is_dir():
        print("That folder does not exist.")
        return

    extension = input(
        "Filter by extension (e.g. .jpg), or leave blank for all files: "
    ).strip()

    files = get_files(folder, extension)

    if not files:
        print("No matching files found.")
        return

    if mode == "1":
        value = input("Prefix to add: ")
        extra = ""
    elif mode == "2":
        value = input("Suffix to add (before extension): ")
        extra = ""
    elif mode == "3":
        value = input("Text to find: ")
        if not value:
            print("Search text cannot be empty.")
            return
        extra = input("Replace with: ")
    else:
        value = input("Filename prefix (e.g. image): ")
        extra = ""

    plan = create_plan(files, mode, value, extra)

    if not plan:
        print("No filenames would change.")
        return

    try:
        validate_plan(plan)
    except ValueError as error:
        print(f"\nSafety check failed: {error}")
        return

    print("\n--- Preview ---")
    for source, target in plan:
        print(f"{source.name}  ->  {target.name}")

    print(f"\n{len(plan)} file(s) will be renamed.")
    confirm = input("Apply these changes? Type YES to continue: ")

    if confirm != "YES":
        print("Cancelled. No files were changed.")
        return

    try:
        completed = apply_plan(plan)
        history = load_history()
        history.append([
            {"old": str(source), "new": str(target)}
            for source, target in completed
        ])
        save_history(history)
        print(f"\nSuccess! Renamed {len(completed)} file(s).")
    except (OSError, ValueError) as error:
        print(f"\nRename failed: {error}")


if __name__ == "__main__":
    main()
