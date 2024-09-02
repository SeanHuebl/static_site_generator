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
    
    code = check_code_block(block)
    if code:
        return code
            
    quote = check_quote_block(block)
    if quote:
        return quote
        
    un_or_list = check_unordered_list_block(block)
    if un_or_list:
        return un_or_list
    
    or_list = check_ordered_list_block(block)
    if or_list:
        return or_list
    
    return BlockType.PARAGRAPH

def check_heading_block(block):
    headings = (BlockType.H1, BlockType.H2, BlockType.H3,
                BlockType.H4, BlockType.H5, BlockType.H6)
    heading_char = '#'
    
    match = re.match(fr'^({heading_char}){{0,6}}', block)
    
    if not match.group():
        return None
    
    else:
        return headings[len(match.group(0)) - 1]    
    
    
    
def check_code_block(block):
    delimiter = '```'
    sections = block.split(delimiter)

    if len(sections) <= 1:
        return None
    if len(sections) % 2 == 0:
        raise ValueError("Missing opening or closing ```")
    
    return BlockType.CODE

def check_quote_block(block):   
    
    if not re.match(r'^>', block):
        return None
    
    lines = block.split('\n')

    for line in lines:
        if not re.match(r'^>', line):
            raise ValueError('All lines within a quote block must start with >')
    
    return BlockType.QUOTE

def check_unordered_list_block(block):
    if not re.match(r'^\* |^- ', block):
        return None
    
    lines = block.split('\n')     

    for line in lines:
        if re.match(r'^ {4}', line):
            continue
        if not re.match(r'^\* |^- ', line):
            raise ValueError('Every line in an unordered list must start with * or - followed by a space')
    return BlockType.LIST_UNORDERED    

def check_ordered_list_block(block):
    if not re.match(r'^1\. ', block):
        return None
    
    lines = block.split('\n')
    n = 1
    for line in lines:
        if not re.match(fr'^{n}\. ', line):
            raise ValueError('Ordered lists must start at 1 and increment by 1, followed by a .')
        n += 1
    return BlockType.LIST_ORDERED