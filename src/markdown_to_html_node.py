import re

from enums import BlockType
from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    heading_char = '#'
    #headings = (BlockType.H1, BlockType.H2, BlockType.H3, BlockType.H4, BlockType.H5, BlockType.H6)
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block_type)
        new_block = re.sub(fr'^(({heading_char}){{0,6}} |>|\* |\- |\d+\. )', '', block, flags=re.MULTILINE)
        if block_type == BlockType.QUOTE:
            quote_text_nodes = process_quote(new_block)
            
        #children = text_to_textnodes(new_block.split('\n'))
        #print(children)
        #block_node = ParentNode(block_type.value, children)


def process_quote(block):
    lines = block.split('\n')
    quote_lines = []
    for line in lines:
        quote_lines.append(text_to_textnodes(line))
    return quote_lines