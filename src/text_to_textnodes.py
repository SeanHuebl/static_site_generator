import re

from enums import TextType
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode

def text_to_textnodes(raw_text):
    text = TextNode(raw_text, TextType.TEXT)
    delimiters = ('**', '*', '`')
    
    nodes = split_nodes_delimiter([text], delimiters[2])
    nodes_v2 = split_nodes_delimiter(nodes, delimiters[0])
    nodes_v3 = split_nodes_delimiter(nodes_v2, delimiters[1])        
    nodes_v4 = split_nodes_link(nodes_v3)
    nodes_v5 = split_nodes_image(nodes_v4)
    print(nodes_v5)

