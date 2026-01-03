import os


def get_files_info(working_directory, directory="."):

    try:

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'

        list_of_files = []

        for file in os.listdir(target_dir):
            file_name = file
            file_size = os.path.getsize(os.path.join(target_dir, file))
            is_dir = os.path.isdir(os.path.join(target_dir, file))
            list_of_files.append(
                f"- {file_name}: file_size={file_size}, is_dir={is_dir}"
            )

        return "\n".join(list_of_files)
    except Exception as e:
        print(f"Error: {e}")
