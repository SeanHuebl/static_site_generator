from textnode import TextNode
from extract import *

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
        links = extract_markdown_links(node.text)
        sections = node.text.split(f'[{alt}]({url})', 1)

        if len(links) == 1:
            alt, url = links[0][0], links[0][1] 

            if not sections[0]:
                new_nodes.append(TextNode(alt, 'link', url))
            else:
                new_nodes.append(TextNode(sections[0], 'text'))
                new_nodes.append(TextNode(alt, 'link', url))
            if not sections[1]:
                continue
            else:
                new_nodes.append(TextNode(sections[1], 'text'))
            
        else:
            if not extract_markdown_links(sections[1]):
                continue
            



            

        



        
        
        
    return new_nodes

        