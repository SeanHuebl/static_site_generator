from functools import reduce
import re

from enums import BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    heading_char = '#'

    for block in blocks:
        
        block_type = block_to_block_type(block)
        print(block_type)
        new_block = re.sub(fr'^(({heading_char}){{0,6}} |>|\* |\- |\d+\. |```)|```$', '', block, flags=re.MULTILINE)
        print(new_block)
        children = text_to_leafnode_children(new_block)
        
        match block_type:
            case BlockType.H1:
                html_nodes.append(ParentNode(BlockType.H1.value, children))
            case BlockType.H2:
                html_nodes.append(ParentNode(BlockType.H2.value, children))
            case BlockType.H3:
                html_nodes.append(ParentNode(BlockType.H3.value, children))
            case BlockType.H4:
                html_nodes.append(ParentNode(BlockType.H4.value, children))
            case BlockType.H5:
                html_nodes.append(ParentNode(BlockType.H5.value, children))
            case BlockType.H6:
                html_nodes.append(ParentNode(BlockType.H6.value, children))
            case BlockType.CODE:
                html_nodes.append(ParentNode(BlockType.CODE.value, children))
            case BlockType.QUOTE:         
                html_nodes.append(ParentNode(BlockType.QUOTE.value, children))
            case BlockType.LIST_UNORDERED:
                html_nodes.append(ParentNode(BlockType.LIST_UNORDERED.value, list_to_leafnode_children(new_block)))
            


def text_to_leafnode_children(block):
    leaf_nodes = []
    text_nodes = text_to_textnodes(block)
    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    return leaf_nodes

def list_to_leafnode_children(block):
    li_parents = []            
    lines = block.split('\n')
    for line in lines:
        children = text_to_leafnode_children(line)
        li_parents.append(ParentNode('li', children))
    return li_parents