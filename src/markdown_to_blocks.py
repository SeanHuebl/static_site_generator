import re

from enums import BlockType

def markdown_to_blocks(markdown):
    if not isinstance(markdown, str) or not markdown:
        raise ValueError("Markdown argument must be a non-empty string")
    block_strings = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if not block:
            continue
        block_strings.append(block.strip())
    return block_strings

def block_to_block_type(block):
    heading = check_heading_block(block)
    if heading:
        return heading
    
            
        
            
def check_heading_block(block):
    headings = (BlockType.H1, BlockType.H2, BlockType.H3,
                BlockType.H4, BlockType.H5, BlockType.H6)
    heading_char = '#'
    
    match = re.match(fr'^({heading_char}){{0,6}}', block)
    
    if not match.group():
        return None
    
    else:
        return headings[len(match.group(0)) - 1].value    
    
    
    
def check_code_block(block):
    delimiter = '```'
    sections = block.split(delimiter)
    print(sections)
    