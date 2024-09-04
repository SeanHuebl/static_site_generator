import os
import re
import textwrap

from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown):
    title = re.match(r'^# (.*?)$', markdown, re.MULTILINE)
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