import os
import re
import textwrap

from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """
    Parses a markdown document to find the first level-1 heading (`# heading`) and extracts the heading text.

    This function searches for the first occurrence of a Markdown heading starting with `#` 
    and returns the text following the `#` character. If no such heading is found, an exception is raised.

    Args:
        markdown (str): The markdown document, as a single string.

    Returns:
        str: The extracted heading text without the leading `#`.

    Raises:
        Exception: If no level-1 heading is found in the markdown document.
    """
    # Search for the first match of a level-1 heading (`# heading`) in the markdown document.
    # The text after the `#` is captured in a group for extraction.
    title = re.match(r'^# (.*?)$', markdown, re.MULTILINE)

    # If a title is not found, raise an exception to notify the user that the document lacks an H1 heading.
    if not title:
        raise Exception("Markdown does not contain a title / H1 heading")

    # Return the captured group, which contains the heading text without the `#`.
    return title.group(1)
    
def generate_page(from_path: str, template_path: str, destination_path: str) -> None:
    """
    Generates an HTML page from a Markdown file using a specified HTML template.

    This function reads a Markdown file, converts its contents to HTML, 
    and uses a provided HTML template to generate a complete HTML page. 
    The template must contain placeholders `{{ Title }}` and `{{ Content }}` 
    which will be replaced with the extracted title and converted HTML content.

    Args:
        from_path (str): The path to the Markdown file to be converted.
        template_path (str): The path to the HTML template file containing placeholders.
        destination_path (str): The path where the generated HTML page will be saved.

    Returns:
        None
    """
    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    try:
        # Read the Markdown file contents. Reading the entire file at once as the Markdown file is expected to be small.
        with open(from_path, 'r', encoding='utf-8') as md_file:
            markdown_contents = md_file.read()
        
        # Read the HTML template file contents. Template should contain placeholders for title and content.
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_contents = template_file.read()

    except FileNotFoundError as e:
        print(f"Error: {e}")  # Log the specific file that was not found.
        return
    except IOError as e:
        print(f"Error reading file: {e}")  # Log general input/output errors for better debugging.
        return

    # Convert Markdown content to an HTML node object for easier manipulation and conversion.
    html_node = markdown_to_html_node(textwrap.dedent(markdown_contents))

    # Generate an HTML string from the HTML node object. This allows for further templating.
    html_string = html_node.to_html()

    # Extract the title from the Markdown contents. A valid Markdown file should have a top-level heading as the title.
    try:
        title = extract_title(markdown_contents)
    except Exception as e:
        print(f"Error extracting title: {e}")  # Inform the user if the title extraction fails.
        return

    # Replace the placeholders in the template with the extracted title and generated HTML content.
    # This ensures the generated page has the correct title and content embedded in the provided HTML template.
    full_html = template_contents.replace('{{ Title }}', title).replace('{{ Content }}', html_string)
    
    # Write the complete HTML to the destination file. This completes the page generation process.
    try:
        with open(destination_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
    except IOError as e:
        print(f"Error writing to file: {e}")  # Log errors encountered during file writing to inform the user.

def generate_page_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    """
    Recursively generates HTML pages from Markdown files within a directory and its subdirectories.

    This function traverses a given directory, converting each Markdown file it finds into an HTML file 
    using a specified HTML template. It replicates the directory structure in the destination path and 
    saves the generated HTML files accordingly.

    Args:
        dir_path_content (str): The path to the directory containing the Markdown content.
        template_path (str): The path to the HTML template file used for generating HTML pages.
        dest_dir_path (str): The path to the destination directory where the generated HTML files will be saved.

    Returns:
        None
    """
    # Get the list of files and directories in the current content directory.
    # This is necessary to know what items to process and convert.
    contents = os.listdir(dir_path_content)

    # Iterate over each item in the current directory to handle both files and subdirectories.
    for content in contents:
        
        # Construct the full source path for the current item to know where it is in the filesystem.
        src_path = os.path.join(dir_path_content, content)

        # Construct the full destination path to replicate the directory structure in the output location.
        dest_path = os.path.join(dest_dir_path, content)

        # Check if the current item is a directory to handle it recursively.
        if os.path.isdir(src_path):

            # Ensure the destination directory exists to maintain the same structure as the source.
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)  # Create the destination directory if it doesn't exist.

            # Recursively call the function to handle the contents of the subdirectory.
            # This allows processing of nested directories, ensuring all Markdown files are converted.
            generate_page_recursive(src_path, template_path, dest_path)

        # If the current item is a Markdown file, convert it to HTML.
        elif os.path.isfile(src_path) and src_path.endswith('.md'):

            # Replace the '.md' extension with '.html' to generate the correct output file type.
            # This ensures the converted HTML file is saved with an appropriate name.
            dest_path = dest_path.replace('.md', '.html')

            # Call the function to generate the HTML page using the provided Markdown and template paths.
            # This performs the actual conversion and templating for the current Markdown file.
            generate_page(src_path, template_path, dest_path)