import os
base_dir = "./Newdata"
def rename_files_in_directory(base_dir):
    """
    Rename image files sequentially in subdirectories of `base_dir`.

    Args:
        base_dir (str): Path to the base directory containing subdirectories with images.
    """
    for subfolder in os.listdir(base_dir):
        subfolder_path = os.path.join(base_dir, subfolder)

        if os.path.isdir(subfolder_path):  # Ensure it's a directory
            print(f"Processing folder: {subfolder}")
            for i, filename in enumerate(sorted(os.listdir(subfolder_path))):
                file_path = os.path.join(subfolder_path, filename)
                if os.path.isfile(file_path):  # Ensure it's a file
                    # Get the file extension
                    _, file_extension = os.path.splitext(filename)
                    # Create the new file name
                    new_filename = f"image{i}{file_extension}"
                    new_file_path = os.path.join(subfolder_path, new_filename)

                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} -> {new_file_path}")

if __name__ == "__main__":
    base_directory = "newData"  # Replace with the path to your base directory
    rename_files_in_directory(base_directory)
