from typing import List

from enums import TextType
from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str) -> List[TextNode]:
    """
    Splits a list of `TextNode` objects based on a specified delimiter and converts the resulting
    text sections into new `TextNode` objects with the appropriate text type (bold, italic, code).

    This function takes a list of `TextNode` objects and splits each node's text by a given delimiter 
    (`**`, `*`, or `` ` ``). It returns a new list of `TextNode` objects where each text section 
    between delimiters is converted to a corresponding text type.

    Args:
        old_nodes (List[TextNode]): A list of `TextNode` objects to be processed.
        delimiter (str): A string representing the delimiter (`**`, `*`, or `` ` ``) used to split the text.

    Returns:
        List[TextNode]: A list of new `TextNode` objects with appropriate text types based on the delimiter.

    Raises:
        ValueError: If `old_nodes` is not a populated list of `TextNode` objects.
        ValueError: If the `delimiter` is not one of the accepted types (`**`, `*`, or `` ` ``).
        ValueError: If there is an imbalance in the delimiters within the text.
    """
    # Validate input to ensure `old_nodes` is a non-empty list of `TextNode` objects.
    # This check prevents processing invalid data and ensures type consistency.
    if not old_nodes or not isinstance(old_nodes, list) or not all(isinstance(node, TextNode) for node in old_nodes):
        raise ValueError("old_nodes must be a populated list of TextNode objects")

    # Initialize an empty list to store the newly created `TextNode` objects.
    # This list will hold the processed nodes with the appropriate text types.
    new_nodes: List[TextNode] = []
    
    # Determine the `TextType` based on the provided delimiter.
    # This mapping helps convert the text sections into the correct `TextNode` type.
    match delimiter:
        case "**":
            split_type = TextType.BOLD
        case "*":
            split_type = TextType.ITALIC
        case "`":
            split_type = TextType.CODE
        case _:
            # Raise an error if the delimiter is not recognized or is invalid.
            raise ValueError("Invalid delimiter type. Must use: **, *, or `")
        
    # Iterate over each `TextNode` in the original list to process them.
    for node in old_nodes:

        # Skip nodes that are not of type `TextType.TEXT` since they do not need splitting.
        # This ensures only plain text nodes are processed for markdown-style formatting.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Split the text of the `TextNode` by the specified delimiter to separate the formatted sections.
        sections = node.text.split(delimiter)

        # Ensure that delimiters are balanced (odd number of sections implies a valid split).
        # An even number of sections indicates a missing opening or closing delimiter.
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax, missing opening or closing delimiter")
        
        # Iterate over each section to convert them into `TextNode` objects.
        for i in range(len(sections)):

            if i % 2 == 0:  # Plain text section
                # Skip empty sections that don't contribute meaningful content.
                if not sections[i]:
                    continue

                # Append plain text as `TextType.TEXT`.
                new_nodes.append(TextNode(sections[i], TextType.TEXT))   

            else:  # Formatted text section
                # Append formatted text with the corresponding `TextType` derived from the delimiter.
                new_nodes.append(TextNode(sections[i], split_type))
    
    # Return the list of newly created `TextNode` objects with appropriate types.
    return new_nodes

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    """
    Splits a list of `TextNode` objects based on the presence of Markdown-style links and converts
    them into new `TextNode` objects with appropriate text types (plain text or link).

    This function processes a list of `TextNode` objects, checks for Markdown links in the text, 
    and splits the text into separate nodes for plain text and links. Each link is represented 
    by a `TextNode` of type `TextType.LINK`, while the remaining text is represented as `TextType.TEXT`.

    Args:
        old_nodes (List[TextNode]): A list of `TextNode` objects to be processed.

    Returns:
        List[TextNode]: A list of new `TextNode` objects with appropriate text types 
                        (either `TextType.TEXT` or `TextType.LINK`).
    """
    # Initialize an empty list to store the newly created `TextNode` objects.
    # This list will hold the processed nodes with appropriate text types.
    new_nodes: List[TextNode] = []

    # Iterate over each `TextNode` in the original list to process them.
    for node in old_nodes:

        # Skip nodes that do not contain any text, as there is nothing to split or convert.
        # This ensures that only meaningful content is processed.
        if not node.text:            
            continue
        
        # Extract Markdown-style links from the node's text using `extract_markdown_links`.
        # This identifies links formatted as `[text](url)` and prepares them for conversion.
        links = extract_markdown_links(node.text)

        # If no links are found, add the node as-is to the new list.
        # This prevents unnecessary processing for nodes without links.
        if not links:
            new_nodes.append(node)
            continue

        # Initialize `current_text` to keep track of the remaining text after each link extraction.
        current_text = node.text

        # Iterate over each extracted link to split and convert the text into separate `TextNode` objects.
        for link in links:

            # Split the text at the first occurrence of the link to isolate the preceding text.
            # This helps separate plain text from the link for proper conversion.
            extracted = current_text.split(f"[{link[0]}]({link[1]})", 1)

            # If there is any text before the link, create a `TextNode` for it with `TextType.TEXT`.
            # This ensures that non-link text is correctly preserved and represented.
            if extracted[0]:
                new_nodes.append(TextNode(extracted[0], TextType.TEXT))
            
            # Create a `TextNode` for the link itself with `TextType.LINK`, including the link text and URL.
            # This converts the Markdown link into its structured form for HTML rendering.
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            # Update `current_text` to the remaining text after the link for further processing.
            current_text = extracted[1]

        # If there is any remaining text after processing all links, add it as a `TextNode`.
        # This step ensures that all parts of the original text are accounted for in the final output.
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    # Return the list of newly created `TextNode` objects with appropriate types.
    return new_nodes

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    """
    Splits a list of `TextNode` objects based on the presence of Markdown-style images and converts
    them into new `TextNode` objects with appropriate text types (plain text or image).

    This function processes a list of `TextNode` objects, checks for Markdown images in the text, 
    and splits the text into separate nodes for plain text and images. Each image is represented 
    by a `TextNode` of type `TextType.IMAGE`, while the remaining text is represented as `TextType.TEXT`.

    Args:
        old_nodes (List[TextNode]): A list of `TextNode` objects to be processed.

    Returns:
        List[TextNode]: A list of new `TextNode` objects with appropriate text types 
                        (either `TextType.TEXT` or `TextType.IMAGE`).
    """
    # Initialize an empty list to store the newly created `TextNode` objects.
    # This list will hold the processed nodes with appropriate text types.
    new_nodes: List[TextNode] = []

    # Iterate over each `TextNode` in the original list to process them.
    for node in old_nodes:

        # Skip nodes that do not contain any text, as there is nothing to split or convert.
        # This ensures that only meaningful content is processed.
        if not node.text:            
            continue
        
        # Extract Markdown-style images from the node's text using `extract_markdown_images`.
        # This identifies images formatted as `![alt text](url)` and prepares them for conversion.
        imgs = extract_markdown_images(node.text)

        # If no images are found, add the node as-is to the new list.
        # This prevents unnecessary processing for nodes without images.
        if not imgs:
            new_nodes.append(node)
            continue

        # Initialize `current_text` to keep track of the remaining text after each image extraction.
        current_text = node.text

        # Iterate over each extracted image to split and convert the text into separate `TextNode` objects.
        for img in imgs:
            
            # Split the text at the first occurrence of the image to isolate the preceding text.
            # This helps separate plain text from the image for proper conversion.
            extracted = current_text.split(f"![{img[0]}]({img[1]})", 1)

            # If there is any text before the image, create a `TextNode` for it with `TextType.TEXT`.
            # This ensures that non-image text is correctly preserved and represented.
            if extracted[0]:
                new_nodes.append(TextNode(extracted[0], TextType.TEXT))
            
            # Create a `TextNode` for the image itself with `TextType.IMAGE`, including the alt text and URL.
            # This converts the Markdown image into its structured form for HTML rendering.
            new_nodes.append(TextNode(None, TextType.IMAGE, img[1], img[0]))

            # Update `current_text` to the remaining text after the image for further processing.
            current_text = extracted[1]

        # If there is any remaining text after processing all images, add it as a `TextNode`.
        # This step ensures that all parts of the original text are accounted for in the final output.
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    # Return the list of newly created `TextNode` objects with appropriate types.
    return new_nodes