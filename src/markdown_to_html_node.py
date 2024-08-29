from enums import BlockType
from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block_type)
        children = text_to_textnodes(block)
        print(children)
        block_node = ParentNode(block_type.value, children)
        
