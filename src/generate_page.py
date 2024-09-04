import os
import re
import textwrap

from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown):
    title = re.match(r'^#{1} (.*?)$', markdown)
    if not title:
        raise Exception("Markdown does not contain a title / h1")
    else:
        return title.group(1)
    

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    with open(from_path, 'r') as md_file:
        markdown_contents = md_file.read()
    
    with open(template_path, 'r') as template_file:
        template_contents = template_file.read()

    html_node = markdown_to_html_node(textwrap.dedent(markdown_contents))

    html_String = html_node.to_html()
    print(html_String)
    title = extract_title(markdown_contents)