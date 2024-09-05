from typing import Optional

from enums import TextType

class TextNode:
    """
    Represents a text element with associated type and optional attributes for Markdown processing.

    A `TextNode` can represent plain text, formatted text (e.g., bold, italic), code, a link, or an image.
    Depending on its type, it may also contain additional attributes such as a URL or alt text.

    Attributes:
        text (str): The content of the text node.
        text_type (TextType): The type of the text (e.g., TEXT, BOLD, ITALIC, LINK, IMAGE).
        url (Optional[str]): The URL associated with the text node if it represents a link or image.
        alt_text (Optional[str]): The alternative text associated with the text node if it represents an image.
    """

    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None, alt_text: Optional[str] = None):
        """
        Initializes a `TextNode` with text, type, and optional attributes.

        Args:
            text (str): The content of the text node.
            text_type (TextType): The type of the text (e.g., TEXT, BOLD, ITALIC, LINK, IMAGE).
            url (Optional[str]): The URL associated with the text node if it represents a link or image. Defaults to None.
            alt_text (Optional[str]): The alternative text associated with the text node if it represents an image. Defaults to None.
        """
        # Initialize the text content of the node.
        self.text = text
        
        # Initialize the type of the text, which defines how it should be processed/rendered.
        self.text_type = text_type
        
        # Initialize the URL attribute, which is relevant for link or image types.
        self.url = url
        
        # Initialize the alternative text for the image type.
        self.alt_text = alt_text

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between this `TextNode` and another `TextNode` based on their attributes.

        Args:
            other (object): The other object to compare against.

        Returns:
            bool: True if the other object is a `TextNode` with the same attributes, False otherwise.
        """
        # Ensure the other object is a `TextNode` before comparing attributes.
        if not isinstance(other, TextNode):
            return False

        # Compare all relevant attributes for equality.
        return (self.text, self.text_type, self.url, self.alt_text) == (other.text, other.text_type, other.url, other.alt_text)

    def __repr__(self) -> str:
        """
        Provides a string representation of the `TextNode` object for debugging purposes.

        Returns:
            str: A string representation showing the text, type, URL, and alt text.
        """
        # Return a formatted string showing the important attributes for easier debugging and logging.
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url}, alt_text={self.alt_text})"