import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            text=True,
            capture_output=True,
            check=True,
            timeout=30,
        )

        output_string = ""

        if result.returncode:
            output_string += f"Process exited with code {result.returncode}\n"

        if not result.stderr and not result.stdout:
            output_string += "No output produced\n"
        else:
            output_string += f"STDOUT: {result.stdout}\n"
            output_string += f"STDERR: {result.stderr}\n"

        return output_string

    except Exception as e:
        f"Error: executing Python file: {e}"
