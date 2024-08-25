from textnode import TextNode
from extract import *
from re import split

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    if not old_nodes or not isinstance(old_nodes,list) or not all(isinstance(node, TextNode) for node in old_nodes):
        raise ValueError("Old_nodes must be a populated list of TextNode objects")
    

    new_nodes = []
    
    match delimiter:
        case "**":
            split_type = 'bold'
        case "*":
            split_type = 'itallic'
        case "`":
            split_type = 'code'
        case _:
            raise ValueError("Invalid delimiter type. Must use: **, *, or `")
        
    for node in old_nodes:

        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax, missing opening or closing delimiter")
        
        for i in range(len(sections)):
            if i % 2 == 0:
                if not sections[i]:
                    continue
                new_nodes.append(TextNode(sections[i], 'text'))   
            else:
                new_nodes.append(TextNode(sections[i], split_type))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if not node.text:
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        
        regex_string = '('
        for i in range(len(links)):
            alt, url = '', ''
            alt, url = links[i][0], links[i][1]
            if i == 0:
                regex_string += f'\[{alt}\]\({url}\)'
            else:
                regex_string += f'|\[{alt}\]\({url}\)'
        regex_string += ')'

        results = re.split(regex_string, node.text)

        for i in range(len(results)):

            if not results[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(results[i], 'text'))
            else:
                alt, url = extract_markdown_links(results[i])[0]    
                new_nodes.append(TextNode(alt, 'link', url))
        if not new_nodes:
            raise ValueError("new_nodes must not be empty")
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if not node.text:
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        
        regex_string = '('
        for i in range(len(links)):
            alt, url = '', ''
            alt, url = links[i][0], links[i][1]
            if i == 0:
                regex_string += f'\!\[{alt}\]\({url}\)'
            else:
                regex_string += f'|\!\[{alt}\]\({url}\)'
        regex_string += ')'

        results = re.split(regex_string, node.text)

        for i in range(len(results)):

            if not results[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(results[i], 'text'))
            else:
                alt, url = extract_markdown_links(results[i])[0]    
                new_nodes.append(TextNode(alt, 'image', url))        
    return new_nodes