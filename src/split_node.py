from re import split

from enums import TextType
from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter):

    if not old_nodes or not isinstance(old_nodes,list) or not all(isinstance(node, TextNode) for node in old_nodes):
        raise ValueError("Old_nodes must be a populated list of TextNode objects")
    

    new_nodes = []
    
    match delimiter:
        case "**":
            split_type = TextType.BOLD
        case "*":
            split_type = TextType.ITALIC
        case "`":
            split_type = TextType.CODE
        case _:
            raise ValueError("Invalid delimiter type. Must use: **, *, or `")
        
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax, missing opening or closing delimiter")
        
        for i in range(len(sections)):
            if i % 2 == 0:
                if not sections[i]:
                    continue
                new_nodes.append(TextNode(sections[i], TextType.TEXT))   
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
            continue
        current_text = node.text
        for link in links:                    
            extracted = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if extracted[0]:
                new_nodes.append(TextNode(extracted[0], TextType.TEXT))
                
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = extracted[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
        
                
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text:            
            continue
        
        imgs = extract_markdown_images(node.text)
        if not imgs:
            new_nodes.append(node)
            continue
        current_text = node.text
        for img in imgs:                    
            extracted = current_text.split(f"![{img[0]}]({img[1]})", 1)
            if extracted[0]:
                new_nodes.append(TextNode(extracted[0], TextType.TEXT))
                
            new_nodes.append(TextNode(None, TextType.IMAGE, img[1], img[0]))
            current_text = extracted[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
        
                
    return new_nodes