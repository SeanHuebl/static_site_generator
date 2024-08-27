from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class BlockType(Enum):
    H1 = '#'
    H2 = '##'
    H3 = '###'
    H4 = '####'
    H5 = '#####'
    H6 = '######'
    CODE = '```'
    QUOTE = '>'
    LIST_UNORDERED = ('*', '-')
    LIST_ORDERED = '. '
    PARAGRAPH = None