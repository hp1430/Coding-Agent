read_file_schema = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Read the contents of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to be read"
                }
            },
            "required": ["path"]
        }
    }
}

write_file_schema = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Create a new file or overwrite an existing file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to be created of overwritten"
                },
                "content": {
                    "type": "string",
                    "description": "Complete content to write"
                }
            },
            "required": ["path", "content"]
        }
    }
}

edit_file_schema = {
    "type": "function",
    "function": {
        "name": "edit_file",
        "description": "Replace a specific piece of text in an existing file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to be edited."
                },
                "old_text": {
                    "type": "string",
                    "description": "Existing text that should be replaced."
                },
                "new_text": {
                    "type": "string",
                    "description": "New text that should be added to file."
                }
            },
            "required": ["path", "old_text", "new_text"]
        }
    }
}

delete_file_schema = {
    "type": "function",
    "function": {
        "name": "delete_file",
        "description": "Delete a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to be deleted."
                }
            },
            "required": ["path"]
        }
    }
}

list_directory_schema = {
    "type": "function",
    "function": {
        "name": "list_directory",
        "description": "List files and directories inside a directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path. Defaults to current directory."
                }
            },
            "required": []
        }
    }
}

execute_command_schema = {
    "type": "function",
    "function": {
        "name": "execute_command",
        "description": "Execute a terminal command.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Terminal command to execute."
                }
            },
            "required": ["command"]
        }
    }
}

TOOLS_MENU = [
    read_file_schema,
    write_file_schema,
    edit_file_schema,
    delete_file_schema,
    list_directory_schema,
    execute_command_schema,
]