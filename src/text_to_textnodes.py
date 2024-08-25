from split_node import *
from textnode import *
import re

def text_to_textnodes(raw_text):
    text = TextNode(raw_text, 'text')
    delimiters = ('**', '*', '`')
    
    nodes = split_nodes_delimiter([text], delimiters[2])
    nodes_v2 = split_nodes_delimiter(nodes, delimiters[0])
    nodes_v3 = split_nodes_delimiter(nodes_v2, delimiters[1])
    nodes_v4 = split_nodes_link(nodes_v3)
        


    print(nodes_v4)

