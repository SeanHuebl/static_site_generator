import re
from typing import List

from enums import BlockType

def markdown_to_blocks(markdown: str) -> List[str]:
    """
    Splits a markdown document into individual blocks of text.

    This function takes a markdown string and splits it into separate blocks of text based 
    on double newline characters ('\n\n'). It trims any extra whitespace around each block 
    and returns a list of these cleaned blocks.

    Args:
        markdown (str): A markdown document as a non-empty string.

    Returns:
        list: A list of strings, where each string is a cleaned block of text from the markdown.

    Raises:
        ValueError: If the `markdown` argument is not a non-empty string.
    """
    # Validate input to ensure it is a non-empty string; this prevents processing invalid data.
    if not isinstance(markdown, str) or not markdown:
        raise ValueError("Markdown argument must be a non-empty string")

    # Initialize an empty list to store the individual blocks after processing.
    # This helps in storing cleaned and trimmed versions of each markdown block.
    block_strings = []

    # Split the markdown text into blocks using double newlines ('\n\n') as delimiters.
    # Double newlines signify the end of a paragraph or block in markdown.
    blocks = markdown.split('\n\n')

    # Iterate over each block to clean and process it.
    for block in blocks:

        # Skip empty blocks that may occur due to consecutive newlines.
        # This ensures that only meaningful content is included in the output.
        if not block:
            continue
        
        # Strip leading and trailing whitespace from each block to clean the text.
        # This helps maintain consistency and removes unnecessary spaces.
        block_strings.append(block.strip())

    # Return the list of cleaned and processed blocks.
    return block_strings


def block_to_block_type(block: str) -> BlockType:
    """
    Determines the type of a given markdown block.

    This function checks a markdown block against various possible block types such as 
    headings, code blocks, quotes, unordered lists, and ordered lists. It returns the 
    corresponding block type if a match is found; otherwise, it defaults to `BlockType.PARAGRAPH`.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The type of block determined for the given markdown block. Possible types 
                   include headings, code blocks, quotes, unordered lists, ordered lists, 
                   or a default paragraph.
    """
    # Check if the block is a heading by using `check_heading_block`.
    # Headings are often the most distinct and should be checked first.
    heading = check_heading_block(block)
    if heading:
        return heading
    
    # Check if the block is a code block using `check_code_block`.
    # Code blocks are typically fenced with backticks or indentation, making them distinct.
    code = check_code_block(block)
    if code:
        return code
            
    # Check if the block is a quote using `check_quote_block`.
    # Quotes often start with '>' and have a unique structure in markdown.
    quote = check_quote_block(block)
    if quote:
        return quote
        
    # Check if the block is an unordered list using `check_unordered_list_block`.
    # Unordered lists start with '-' or '*', and checking for them helps classify list content.
    un_or_list = check_unordered_list_block(block)
    if un_or_list:
        return un_or_list
    
    # Check if the block is an ordered list using `check_ordered_list_block`.
    # Ordered lists start with numbers followed by '.', helping to distinguish ordered content.
    or_list = check_ordered_list_block(block)
    if or_list:
        return or_list
    
    # Default to paragraph if no other block type matches.
    # This is the most generic type and represents plain text or unclassified content.
    return BlockType.PARAGRAPH


def check_heading_block(block: str) -> BlockType:
    """
    Checks if a markdown block is a heading and returns the corresponding heading block type.

    This function uses a regular expression to determine if a given block starts with one or more 
    '#' characters, which is the markdown syntax for headings. If a match is found, it returns the 
    corresponding heading type (`BlockType.H1` to `BlockType.H6`) based on the number of '#' characters. 
    If no heading is found, it returns None.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The block type representing the heading level (`BlockType.H1` to `BlockType.H6`), or 
                   None if the block is not a heading.
    """
    # Define possible heading types in markdown and their corresponding block types.
    # This allows for easy mapping of heading levels to block types.
    headings = (BlockType.H1, BlockType.H2, BlockType.H3,
                BlockType.H4, BlockType.H5, BlockType.H6)
    
    # The '#' character is used in markdown to denote headings; the number of '#' characters 
    # indicates the level of the heading.
    heading_char = '#'
    
    # Use a regular expression to match lines starting with 1 to 6 '#' characters.
    # The match helps identify if a block starts with a valid heading and determines its level.
    match = re.match(fr'^({heading_char}){{1,6}}', block)
    
    # If no match is found, return None to indicate that the block is not a heading.
    # This ensures that only valid headings are processed.
    if not match:
        return None
    
    # Calculate the heading level based on the length of the matched string.
    # The number of '#' characters corresponds directly to the heading level.
    return headings[len(match.group(0)) - 1]   
    
    
    
def check_code_block(block: str) -> BlockType:
    """
    Checks if a markdown block is a code block and returns the corresponding block type.

    This function identifies if a given block is a code block by checking for the presence 
    of the code block delimiter (`` ``` ``) in markdown. If the block is enclosed properly 
    with matching opening and closing delimiters, it is identified as a code block. If the 
    delimiters are improperly balanced, a ValueError is raised.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The block type `BlockType.CODE` if the block is identified as a code block, 
                   or None if it is not.

    Raises:
        ValueError: If the code block delimiters are improperly balanced.
    """
    # Define the code block delimiter used in markdown. This is important to identify the start and end of code blocks.
    delimiter = '```'

    # Split the block by the code block delimiter to separate the potential code sections.
    # The number of sections helps determine if the block is a code block and if delimiters are balanced.
    sections = block.split(delimiter)

    # If there is no delimiter present or delimiters do not enclose content properly, it's not a code block.
    # Returning None indicates that the block is not identified as a code block.
    if len(sections) <= 1:
        return None

    # If there is an even number of sections, it indicates an imbalance of delimiters.
    # Code blocks must have a matching opening and closing delimiter, hence the odd number of sections.
    if len(sections) % 2 == 0:
        raise ValueError("Missing opening or closing ```")

    # If all checks pass, the block is identified as a code block and returns `BlockType.CODE`.
    return BlockType.CODE

def check_quote_block(block: str) -> BlockType:   
    """
    Checks if a markdown block is a quote block and returns the corresponding block type.

    This function identifies if a given block is a quote block by checking if all lines 
    within the block start with the `>` character, which is the markdown syntax for blockquotes. 
    If all lines adhere to this format, it is identified as a quote block. If any line does not 
    start with `>`, a ValueError is raised.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The block type `BlockType.QUOTE` if the block is identified as a quote block, 
                   or None if it is not.

    Raises:
        ValueError: If any line within the block does not start with `>`.
    """
    # Check if the block starts with the '>' character, indicating a potential quote block.
    # If the first line doesn't start with '>', it's not a quote block, so return None.
    if not re.match(r'^>', block):
        return None
    
    # Split the block into lines to verify that all lines within the block are properly formatted as quotes.
    # This is necessary because a valid quote block requires each line to start with '>'.
    lines = block.split('\n')

    # Iterate over each line to ensure they all start with '>'.
    # If any line doesn't meet this condition, it indicates a malformed quote block.
    for line in lines:

        # Raise an error if any line does not start with the '>' character.
        # This strict validation ensures that the entire block conforms to the quote block format.
        if not re.match(r'^>', line):
            raise ValueError('All lines within a quote block must start with >')
    
    # If all lines pass the check, the block is confirmed as a quote block.
    # Returning `BlockType.QUOTE` indicates that the block is correctly identified.
    return BlockType.QUOTE

def check_unordered_list_block(block: str) -> BlockType:
    """
    Checks if a markdown block is an unordered list and returns the corresponding block type.

    This function identifies if a given block is an unordered list by checking if each line 
    starts with either `* ` or `- `, which are standard markers for unordered lists in markdown. 
    It also allows for nested list items indicated by four leading spaces. If any line does not 
    adhere to these rules, a ValueError is raised.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The block type `BlockType.LIST_UNORDERED` if the block is identified as an 
                   unordered list, or None if it is not.

    Raises:
        ValueError: If any line within the block does not start with `* ` or `- ` followed by a space.
    """
    # Check if the first line starts with a valid unordered list marker (`* ` or `- `).
    # If the first line doesn't match, it's not an unordered list block, so return None.
    if not re.match(r'^\* |^- ', block):
        return None
    
    # Split the block into lines to validate each line individually.
    # This is necessary because all lines in a markdown unordered list must be properly formatted.
    lines = block.split('\n')     

    # Iterate over each line to ensure they are correctly formatted for an unordered list.
    for line in lines:

        # Allow lines that start with four spaces for nested list items.
        # This ensures that nested unordered lists are correctly identified.
        if re.match(r'^ {4}', line):
            continue
        
        # Check that each line starts with a valid unordered list marker.
        # If not, raise an error to indicate improper formatting.
        if not re.match(r'^\* |^- ', line):
            raise ValueError('Every line in an unordered list must start with * or - followed by a space')
    
    # If all lines are correctly formatted, the block is confirmed as an unordered list.
    # Returning `BlockType.LIST_UNORDERED` indicates that the block is identified correctly.
    return BlockType.LIST_UNORDERED    

def check_ordered_list_block(block: str) -> BlockType:
    """
    Checks if a markdown block is an ordered list and returns the corresponding block type.

    This function identifies if a given block is an ordered list by checking if each line starts 
    with an incrementing number followed by `. `, which is the standard syntax for ordered lists 
    in markdown. It also allows for nested list items indicated by four leading spaces. If any 
    line does not adhere to these rules, a ValueError is raised.

    Args:
        block (str): A string representing a block of text in a markdown document.

    Returns:
        BlockType: The block type `BlockType.LIST_ORDERED` if the block is identified as an 
                   ordered list, or None if it is not.

    Raises:
        ValueError: If any line within the block does not start with an incrementing number 
                    followed by `. `.
    """
    # Check if the first line starts with '1. ', the standard start for ordered lists in markdown.
    # If the first line doesn't match, it's not an ordered list block, so return None.
    if not re.match(r'^1\. ', block):
        return None
    
    # Split the block into lines to validate each line individually.
    # This is necessary because all lines in a markdown ordered list must be properly formatted.
    lines = block.split('\n')

    # Initialize the expected starting number for the ordered list.
    # Markdown ordered lists typically start with 1 and increment by 1 for each subsequent item.
    n = 1

    # Iterate over each line to ensure they are correctly formatted for an ordered list.
    for line in lines:
        # Allow lines that start with four spaces for nested list items.
        # This ensures that nested ordered lists are correctly identified.
        if re.match(r'^ {4}', line):
            continue
        
        # Check that each line starts with the correct number followed by '. '.
        # If not, raise an error to indicate improper formatting.
        if not re.match(fr'^{n}\. ', line):
            raise ValueError('Ordered lists must start at 1 and increment by 1, followed by a .')
        
        # Increment the expected number for the next line to ensure sequential ordering.
        n += 1
    
    # If all lines are correctly formatted, the block is confirmed as an ordered list.
    # Returning `BlockType.LIST_ORDERED` indicates that the block is identified correctly.
    return BlockType.LIST_ORDERED