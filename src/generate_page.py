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
    

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    with open(from_path, 'r') as md_file:
        markdown_contents = md_file.read()
    
    with open(template_path, 'r') as template_file:
        template_contents = template_file.read()

    html_node = markdown_to_html_node(textwrap.dedent(markdown_contents))

    html_string = html_node.to_html()

    title = extract_title(markdown_contents)
    full_html = template_contents.replace('{{ Title }}', title).replace('{{ Content }}', html_string)
    
    with open(destination_path, 'w') as f:
        f.write(full_html)
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)

    for content in contents:
        src_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_page_recursive(src_path, template_path, dest_path)
        elif os.path.isfile(src_path):
            dest_path = dest_path.replace('.md', '.html')
            generate_page(src_path, template_path, dest_path)