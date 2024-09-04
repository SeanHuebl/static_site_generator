import os
import shutil

from generate_page import generate_page_recursive

def copy_all_contents(source, destination):
    """
    Copies all files and directories from a source path to a destination path.

    This function handles both creating the destination path if it does not exist
    and clearing its contents if it does. It recursively copies all files and
    subdirectories from the source to the destination.

    Args:
        source (str): The relative or absolute path of the file(s) or directory(s) to be copied.
        destination (str): The relative or absolute path of the destination directory.

    Returns:
        None
    """

    # Ensure the source path exists; if it does not, raise an error to prevent unnecessary operations
    if not os.path.exists(source):
        raise ValueError('Source path does not exist. Please check the path and try again.')
    
    # If the destination path does not exist, create it to ensure it can receive copied contents
    if not os.path.exists(destination):
        os.mkdir(destination)
        # Start copying files and directories after creating the destination
        copy_files(source, destination)

    # If the destination path exists, clear its contents to avoid mixing old and new files
    else:
        remove_destination_dir_contents(destination)  # Remove existing contents to prevent conflicts
        copy_files(source, destination)  # Copy contents from source to destination
    
    print('Copy completed')

def copy_files(source, destination):
    """
    This function recursively searches through the source path for files to copy.

    This is the helper function for copy_all_contents().
    and creates directories / files in the destination path directory.

    Args:
        source (str): The relative path for the source directory or file.
        destination (str): The relative path for the destination directory.

    Returns:
        None.
    """

    # Retrieve all contents from the source path to determine what needs to be copied
    contents = os.listdir(source)

    # Loop through each item in the source to process both files and directories
    for content in contents:
        # Construct full paths to maintain the directory structure during the copy process
        src_path = os.path.join(source, content)
        dest_path = os.path.join(destination, content)

        # Check if the current item is a directory to handle it differently from files
        if os.path.isdir(src_path):
            # Ensure the corresponding directory exists in the destination to mirror the source structure
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            
            # Recursively copy the contents of the directory to handle nested files and directories
            copy_files(src_path, dest_path)

        # If the current item is a file, copy it directly to the destination path
        elif os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)

        # Raise an error for unexpected content types to avoid undefined behavior or data corruption
        else:
            raise ValueError(f"The path '{src_path}' is neither a file nor a directory.")
            
def remove_destination_dir_contents(destination_dir):   
    """
    Recursively deletes all files and directories within a specified directory.

    This helper function is used by `copy_all_contents()` to ensure that the destination 
    directory is empty before copying new content. It traverses the directory tree, removing 
    files first and then directories to avoid errors when trying to delete non-empty directories.

    Args:
        destination_dir (str): The relative or absolute path to the directory from which to 
        remove all contents.

    Returns:
        None
    """

    # List all contents in the destination directory to determine what needs to be removed
    contents = os.listdir(destination_dir)
    
    # Iterate over each item to handle both files and directories
    for content in contents:
        # Construct the full path to ensure accurate removal
        path = os.path.join(destination_dir, content)

        if os.path.isdir(path):
            # Recursively remove contents of the directory to ensure no files are left behind
            remove_destination_dir_contents(path)
            # After all contents are removed, remove the empty directory itself
            os.rmdir(path)

        elif os.path.isfile(path):
            # Directly remove the file as it's a leaf node in the directory tree
            os.remove(path)

        # Handle unexpected cases to avoid undefined behavior
        else:
            raise ValueError(f"The path '{path}' is neither a file nor a directory.")
    
        

def main():
    """
    Main function to execute the static site generation process.

    This function copies all static files to the public directory and then generates HTML pages 
    for each markdown file found in the content directory using a specified template.
    """

    # Ensure the 'public' directory is synchronized with 'static' contents 
    # to provide the latest static resources (e.g., CSS, JavaScript, images).
    copy_all_contents('./static', './public')

    # Generate HTML pages for each markdown file in 'content' to 'public' 
    # using the specified template, ensuring each page follows a consistent layout.
    generate_page_recursive('./content/', './template.html', './public/')



if __name__ == "__main__":
    main()