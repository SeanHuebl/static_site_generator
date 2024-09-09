import re
from typing import List

from enums import BlockType
from htmlnode import LeafNode, ParentNode, text_node_to_html_node
from markdown_to_blocks import block_to_block_type, markdown_to_blocks 
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown: str) -> ParentNode:
    """
    Converts a Markdown document into a tree of HTML nodes.

    This function processes a Markdown string by splitting it into blocks, determining the type 
    of each block (e.g., heading, paragraph, list), and converting each block to an appropriate 
    HTML node structure. It returns a `ParentNode` representing a `<div>` element containing all 
    the HTML nodes created from the Markdown blocks.

    Args:
        markdown (str): A string containing the Markdown content to be converted.

    Returns:
        ParentNode: A `ParentNode` object representing a `<div>` containing the HTML nodes.

    Raises:
        ValueError: If a block type is not recognized or valid.
    """
    # Split the markdown into blocks to process each block separately.
    # This step is crucial because each block represents a distinct HTML element (e.g., paragraph, list).
    blocks = markdown_to_blocks(markdown)

    # Initialize an empty list to store the HTML nodes created from the Markdown blocks.
    # This will eventually be the children of the root `<div>` node.
    html_nodes = []

    # Define the character used for headings in Markdown.
    # This helps to clean up the heading syntax when converting to HTML.
    heading_char = '#'

    # Iterate over each block to determine its type and convert it to the corresponding HTML node.
    for block in blocks:

        # Determine the type of the block (e.g., heading, code, list) using `block_to_block_type`.
        # Knowing the block type is essential to know how to convert it to an HTML node.
        block_type = block_to_block_type(block)        

        # Clean up the block content by removing Markdown-specific syntax (e.g., `#` for headings, `>` for quotes).
        # This is necessary to isolate the text content that will be placed inside HTML tags.
        new_block = re.sub(fr'^(({heading_char}){{0,6}} |> ?|\* |\- |\d+\. |```)|```$', '', block, flags=re.MULTILINE)

        # Convert the cleaned block text into a list of `LeafNode` children.
        # This step breaks down the text content into smaller HTML components (e.g., spans, links).
        children = text_to_leafnode_children(new_block)
        
        # Match the determined block type and create the corresponding HTML node.
        # Each case handles a specific type of Markdown block, converting it to its HTML equivalent.
        match block_type:
            case BlockType.H1:
                html_nodes.append(ParentNode(BlockType.H1.value, children))  # Heading 1 (`<h1>`)
            case BlockType.H2:
                html_nodes.append(ParentNode(BlockType.H2.value, children))  # Heading 2 (`<h2>`)
            case BlockType.H3:
                html_nodes.append(ParentNode(BlockType.H3.value, children))  # Heading 3 (`<h3>`)
            case BlockType.H4:
                html_nodes.append(ParentNode(BlockType.H4.value, children))  # Heading 4 (`<h4>`)
            case BlockType.H5:
                html_nodes.append(ParentNode(BlockType.H5.value, children))  # Heading 5 (`<h5>`)
            case BlockType.H6:
                html_nodes.append(ParentNode(BlockType.H6.value, children))  # Heading 6 (`<h6>`)
            case BlockType.CODE:
                # Code blocks are wrapped in a `<pre>` tag to maintain formatting, with a nested `<code>` tag.
                html_nodes.append(ParentNode('pre', [ParentNode(BlockType.CODE.value, children)]))
            case BlockType.QUOTE:
                # Quote blocks are represented with a `<blockquote>` tag.
                html_nodes.append(ParentNode(BlockType.QUOTE.value, children))
            case BlockType.LIST_UNORDERED:
                # Unordered lists (`<ul>`) are converted by processing list items into `LeafNode` children.
                html_nodes.append(ParentNode(BlockType.LIST_UNORDERED.value, list_to_leafnode_children(new_block)))
            case BlockType.LIST_ORDERED:
                # Ordered lists (`<ol>`) are similarly converted, ensuring correct HTML list formatting.
                html_nodes.append(ParentNode(BlockType.LIST_ORDERED.value, list_to_leafnode_children(new_block)))
            case BlockType.PARAGRAPH:
                # Paragraphs are represented with a `<p>` tag containing text or inline elements.
                html_nodes.append(ParentNode(BlockType.PARAGRAPH.value, children))
            case _:
                # Raise an error if the block type is not recognized or is invalid.
                raise ValueError("BlockType not valid. Must be a value from the BlockType class under enums.py")

    # Wrap all HTML nodes in a root `<div>` element to provide a container for all converted content.
    return ParentNode('div', html_nodes)

def text_to_leafnode_children(block: str) -> List[LeafNode]:
    """
    Converts a block of text into a list of `LeafNode` children.

    This function takes a block of text and first converts it into smaller `TextNode` objects 
    using the `text_to_textnodes` function. Each `TextNode` is then converted to an `HTMLNode` 
    (specifically a `LeafNode`) using the `text_node_to_html_node` function. This is useful for 
    breaking down a block of text into smaller, renderable HTML elements.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        list: A list of `LeafNode` objects representing the HTML elements of the block's content.
    """
    # Initialize an empty list to store the resulting `LeafNode` objects.
    # This list will contain the final HTML nodes that represent the content of the block.
    leaf_nodes = []

    # Convert the block of text into `TextNode` objects using the `text_to_textnodes` function.
    # This step is essential to break down the text into smaller logical units like words, phrases, or inline elements.
    text_nodes = text_to_textnodes(block)

    # Iterate over each `TextNode` to convert them to `LeafNode` HTML elements.
    # This conversion ensures that each logical unit of text is appropriately wrapped in the correct HTML tag.
    for node in text_nodes:
        # Convert the `TextNode` to a `LeafNode` using `text_node_to_html_node`.
        # This step converts each logical unit into its corresponding HTML representation.
        leaf_nodes.append(text_node_to_html_node(node))
        
    # Return the list of `LeafNode` objects representing the HTML elements of the block's content.
    return leaf_nodes

def list_to_leafnode_children(block: str) -> List[LeafNode]:
    """
    Converts a markdown list block into a list of `LeafNode` children.

    This function processes a block of text that represents a markdown list, splits the text into 
    individual list items, and converts each item into `LeafNode` objects. It ensures that each 
    list item is wrapped in an `<li>` tag to match the HTML list structure.

    Args:
        block (str): A string representing a block of text in a markdown document that is formatted as a list.

    Returns:
        List[LeafNode]: A list of `LeafNode` objects where each represents an HTML `<li>` element.
    """
    # Initialize an empty list to store the resulting `LeafNode` objects for the list items.
    # This list will contain the final HTML nodes that represent each item in the markdown list.
    children_list: List[LeafNode] = []         

    # Split the block into lines, avoiding lines that are indented (to handle nested lists).
    # The regex `\n(?![\t ]| {4})` splits at newlines that are not followed by tabs, spaces, or indentation.
    # This helps differentiate between actual new list items and indented continuations or nested lists.
    lines = re.split(r'\n(?![\t ]| {4})', block)

    # Remove additional leading whitespace or tabs that indicate nested list items.
    # This cleanup step is essential to standardize the input for further processing.
    processed_lines = [re.sub(r'\n\t| {3,4}', '', line) for line in lines]

    # Iterate over each processed line to convert them to `LeafNode` HTML elements.
    # This step ensures that each list item is appropriately represented as a `<li>` in HTML.
    for line in processed_lines:

        # Replace any remaining newline characters within a line with HTML `<br>` for line breaks.
        # This conversion is necessary to maintain formatting within a single list item.
        line = line.replace('\n', '<br>\n')

        # Convert the cleaned line text into a list of `LeafNode` children using `text_to_leafnode_children`.
        # This breaks down each list item into smaller HTML components like text spans, links, etc.
        children = text_to_leafnode_children(line)

        # Iterate over the children to ensure they are properly wrapped in `<li>` tags.
        # This is required for HTML list items to be correctly formatted.
        for child in children:
            
            # If a child node doesn't already have a tag, set it to 'li' to denote a list item.
            # This ensures that each node is correctly wrapped for HTML rendering.
            if not child.tag:
                child.tag = 'li'
            
            # Append the child node (now correctly tagged) to the list of children.
            children_list.append(child)
    
    # Return the list of `LeafNode` objects representing the HTML elements of the list's content.
    return children_list