from pathlib import Path
import subprocess

def read_file(path: str) -> str:
    try:
        return Path(path.strip()).read_text(encoding="utf-8")
    except Exception as e:
        return f"Error in reading file: {e}"

def write_file(path: str, content: str) -> str:
    try:
        Path(path.strip()).write_text(content.strip(), encoding="utf-8")
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error in writing file: {e}"

def edit_file(path: str, old_text: str, new_text: str) -> str:
    try:
        file = Path(path.strip())

        if not file.exists():
            return f"Error: File does not exist at {path}"

        content = file.read_text(encoding="utf-8")

        if old_text not in content:
            return "Error: old_text was not in the file"

        new_content = content.replace(old_text, new_text, 1)

        file.write_text(new_content, encoding="utf-8")

        return f"Successfully edited file {path}"

    except Exception as e:
        return f"Error while editing file: {e}"


def delete_file(path: str) -> str:
    try:
        file = Path(path.strip())

        if not file.exists():
            return f"Error: File does not exist: {file}"

        file.unlink()

        return f"Successfully deleted {path}"

    except Exception as e:
        return f"Error while deleting file: {e}"

def list_directory(path: str = ".") -> str:
    try:
        directory = Path(path)

        if not directory.exists():
            return f"Error: Directory does not exist: {path}"

        if not directory.is_dir():
            return f"Error: Not a directory: {path}"

        items = []

        for item in directory.iterdir():
            if item.is_dir():
                items.append(f"[DIR] {item.name}")
            else:
                items.append(f"[FILE] {item.name}")

        return "\n".join(items)

    except Exception as e:
        return f"Error: {e}"


def execute_command(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )

        return (
            f"EXIT CODE: {result.returncode}\n\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )

    except subprocess.TimeoutExpired:
        return "ERROR: Command timed out after 30 seconds"
    except Exception as e:
        return f"ERROR: {e}"