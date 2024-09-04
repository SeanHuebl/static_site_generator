from enum import Enum

# Define text styles that are allowed in the markdown content
class TextType(Enum):
    """
    Enum for different types of inline text formatting in Markdown.

    This Enum is used to represent various text formatting options 
    that are allowed within a Markdown document, such as bold, italic, 
    code snippets, links, and images.
    """
    TEXT = 'text'       # Plain text
    BOLD = 'bold'       # Bold text, typically wrapped with ** in Markdown
    ITALIC = 'italic'   # Italic text, typically wrapped with * in Markdown
    CODE = 'code'       # Inline code, wrapped with backticks `
    LINK = 'link'       # Hyperlinks, represented by [text](url) in Markdown
    IMAGE = 'image'     # Images, represented by ![alt text](url) in Markdown
    
# Define block elements that are allowed in the markdown content
class BlockType(Enum):
    """
    Enum for different types of block elements in Markdown.

    This Enum is used to represent various block elements that can be 
    part of a Markdown document, such as headers, code blocks, quotes, 
    lists, and paragraphs.
    """
    H1 = 'h1'                       # Header level 1, represented by # in Markdown
    H2 = 'h2'                       # Header level 2, represented by ## in Markdown
    H3 = 'h3'                       # Header level 3, represented by ### in Markdown
    H4 = 'h4'                       # Header level 4, represented by #### in Markdown
    H5 = 'h5'                       # Header level 5, represented by ##### in Markdown
    H6 = 'h6'                       # Header level 6, represented by ###### in Markdown
    CODE = 'code'                   # Code block, typically wrapped with triple backticks ```
    QUOTE = 'blockquote'            # Block quote, represented by > in Markdown
    LIST_UNORDERED = 'ul'           # Unordered list, represented by - or * in Markdown
    LIST_ORDERED = 'ol'             # Ordered list, represented by numbers followed by a period in Markdown
    PARAGRAPH = 'p'                 # Paragraph, typically plain text separated by a blank line in Markdown
