from typing import List

from enums import TextType
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode

def text_to_textnodes(raw_text: str) -> List[TextNode]:
    """
    Converts raw text into a list of `TextNode` objects by processing Markdown-style delimiters and syntax.

    This function takes raw text and processes it to identify different Markdown syntaxes such as bold (`**`), 
    italic (`*`), code (`` ` ``), links (`[text](url)`), and images (`![alt text](url)`). It returns a list of 
    `TextNode` objects where each object represents a portion of the text with its appropriate type.

    Args:
        raw_text (str): A string representing the raw text to be processed.

    Returns:
        List[TextNode]: A list of `TextNode` objects with appropriate text types based on Markdown formatting.
    """
    # Initialize the raw text as a `TextNode` object of type `TextType.TEXT`.
    # This represents the entire raw text as plain text before processing it for Markdown syntax.
    text = TextNode(raw_text, TextType.TEXT)

    # Define the delimiters to be processed in order: code (` ` `), bold (`**`), italic (`*`).
    # These delimiters correspond to different Markdown syntaxes that need to be converted to `TextNode` objects.
    # (`**`) is used first to prevent issues with (`*`).
    delimiters = ('**', '*', '`')
    
    # Split the `TextNode` objects by the code delimiter (` ` `).
    # This step converts inline code sections into `TextType.CODE`.
    nodes = split_nodes_delimiter([text], delimiters[2])

    # Further split the resulting `TextNode` objects by the bold delimiter (`**`).
    # This step converts bold sections into `TextType.BOLD`.
    nodes_v2 = split_nodes_delimiter(nodes, delimiters[0])

    # Finally, split the resulting `TextNode` objects by the italic delimiter (`*`).
    # This step converts italic sections into `TextType.ITALIC`.
    nodes_v3 = split_nodes_delimiter(nodes_v2, delimiters[1])        

    # Process the `TextNode` objects to identify and convert Markdown-style links.
    # This step converts link sections into `TextType.LINK`.
    nodes_v4 = split_nodes_link(nodes_v3)

    # Process the `TextNode` objects to identify and convert Markdown-style images.
    # This step converts image sections into `TextType.IMAGE`.
    nodes_v5 = split_nodes_image(nodes_v4)

    # Return the final list of `TextNode` objects with appropriate text types based on Markdown formatting.
    return nodes_v5
