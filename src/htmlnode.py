from enums import TextType

class HTMLNode:
    """
    A base class for representing an HTML node.

    This class serves as the parent class for any specific HTML node-related classes. 
    It provides a blueprint for representing an HTML element with properties such as 
    the tag name, value, children, and attributes (props). Subclasses should implement 
    the `to_html` method to define how the node is rendered in HTML.

    Attributes:
        tag (str): The HTML tag associated with the node (e.g., 'div', 'p', 'a').
        value (str): The inner content or value of the HTML node (e.g., text content).
        children (list): A list of child nodes that are also instances of `HTMLNode`.
        props (dict): A dictionary of attributes (properties) for the HTML tag (e.g., `{'class': 'my-class'}`).

    Methods:
        to_html(): Abstract method that should be implemented by subclasses to return the HTML representation of the node.
        props_to_html(): Returns a string representation of the HTML node's properties.
        __repr__(): Returns a string representation of the `HTMLNode` object for debugging purposes.
    """

    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        """
        Initializes the HTMLNode with the provided tag, value, children, and props.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'div', 'p'). Defaults to None.
            value (str, optional): The text or value contained within the HTML node. Defaults to None.
            children (list, optional): A list of child `HTMLNode` objects. Defaults to None.
            props (dict, optional): A dictionary of HTML attributes. Defaults to None.
        """
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []  # Initialize as empty list if None
        self.props = props if props is not None else {}  # Initialize as empty dict if None

    def to_html(self):
        """
        Abstract method to be implemented by subclasses to define HTML rendering.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

    def props_to_html(self) -> str:
        """
        Converts the dictionary of properties (attributes) to a string suitable for an HTML tag.

        Returns:
            str: A string representation of the HTML node's properties (e.g., ' class="my-class" id="my-id"').
        """
        properties = []
        for k, v in self.props.items():
            properties.append(f' {k}="{v}"')
        
        return "".join(properties)

    def __repr__(self) -> str:
        """
        Provides a string representation of the `HTMLNode` instance for debugging purposes.

        Returns:
            str: A string representation showing the tag, value, children, and props.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
         
class LeafNode(HTMLNode):
    """
    A class to represent an HTML leaf node.

    The `LeafNode` class represents an HTML element that does not have any child nodes. 
    It extends the `HTMLNode` base class and implements the `to_html` method to render 
    the node as an HTML string. This class is useful for representing HTML elements such as 
    `<p>`, `<span>`, `<a>`, and others that do not contain nested HTML content.

    Attributes:
        tag (str): The HTML tag associated with the node (e.g., 'p', 'span', 'a').
        value (str): The inner content or value of the HTML node.
        props (dict, optional): A dictionary of attributes (properties) for the HTML tag (e.g., `{'class': 'my-class'}`).

    Methods:
        to_html(): Returns the HTML string representation of the leaf node.
        __repr__(): Returns a string representation of the `LeafNode` object for debugging purposes.
    """

    def __init__(self, tag: str, value: str, props: dict = None):
        """
        Initializes a `LeafNode` with the provided tag, value, and optional properties.

        Args:
            tag (str): The HTML tag name (e.g., 'p', 'span').
            value (str): The text or value contained within the HTML node. Must be a string.
            props (dict, optional): A dictionary of HTML attributes. Defaults to None.

        Raises:
            ValueError: If `value` is not a string or `props` is not a dictionary or None.
        """
        if not isinstance(value, str):
            raise ValueError("LeafNode value must be a string")

        if props is not None and not isinstance(props, dict):
            raise ValueError("props must be either a dictionary or None")
        
        # Initialize the parent `HTMLNode` with no children since this is a leaf node.
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        """
        Generates the HTML string representation of the leaf node.

        If the node has a tag and properties, the properties are included in the opening tag.
        If the node does not have a tag, only the value is returned.

        Returns:
            str: The HTML string representation of the leaf node.
        """
        # Return only the value if no tag is specified. This handles cases like text nodes.
        if not self.tag:
            return self.value
        
        # Return the HTML without properties if no properties are specified.
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        # Return the full HTML with properties if properties are specified.
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        """
        Provides a string representation of the `LeafNode` instance for debugging purposes.

        Returns:
            str: A string representation showing the tag, value, and props.
        """
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    """
    A class to represent an HTML parent node.

    The `ParentNode` class represents an HTML element that can have child nodes, either `LeafNode` or other 
    `ParentNode` instances. It extends the `HTMLNode` base class and implements the `to_html` method to render 
    the node and its children as an HTML string. This class is useful for representing HTML elements such as 
    `<div>`, `<ul>`, `<ol>`, and others that can contain nested HTML content.

    Attributes:
        tag (str): The HTML tag associated with the node (e.g., 'div', 'ul', 'ol').
        children (list): A list of child nodes that are instances of `LeafNode` or `ParentNode`.
        props (dict, optional): A dictionary of attributes (properties) for the HTML tag (e.g., `{'class': 'my-class'}`).

    Methods:
        to_html(): Returns the HTML string representation of the parent node, including its children.
        __repr__(): Returns a string representation of the `ParentNode` object for debugging purposes.
    """

    def __init__(self, tag: str, children: list, props: dict = None):
        """
        Initializes a `ParentNode` with the provided tag, children, and optional properties.

        Args:
            tag (str): The HTML tag name (e.g., 'div', 'ul').
            children (list): A non-empty list of child nodes that are instances of `LeafNode` or `ParentNode`.
            props (dict, optional): A dictionary of HTML attributes. Defaults to None.

        Raises:
            ValueError: If `children` is not a non-empty list or contains invalid child node types.
            ValueError: If `tag` is not a populated string.
        """
        # Ensure `children` is a list and contains at least one element; a parent node should have children.
        if not isinstance(children, list) or not children:
            raise ValueError("Children must be a populated list")

        # Verify that all children are instances of `ParentNode` or `LeafNode` to maintain HTML node consistency.
        if not all(isinstance(child, (ParentNode, LeafNode)) for child in children):
            raise ValueError("Children must be a non-empty list of ParentNode or LeafNode objects")
            
        # Ensure `tag` is a valid, non-empty string because HTML nodes require a valid tag name.
        if not isinstance(tag, str) or not tag:
            raise ValueError("Tag must be a populated string")
        
        # Call the parent `HTMLNode` constructor with the validated tag, children, and properties.
        # Using `super()` allows leveraging the base class functionality while adding specific logic for `ParentNode`.
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        """
        Generates the HTML string representation of the parent node, including its child nodes.

        This method recursively calls `to_html` on each child node to generate the complete HTML content.

        Returns:
            str: The HTML string representation of the parent node and its children.
        """
        # Begin the HTML representation with the opening tag.
        # If there are properties, they are included within the tag using `props_to_html`.
        html_string = [f"<{self.tag}{self.props_to_html()}>" if self.props else f"<{self.tag}>"]

        # Recursively generate HTML for each child node to maintain the nested structure.
        for child in self.children:
            html_string.append(child.to_html())  # Recursion allows generating HTML for arbitrarily nested structures.

        # Close the HTML tag to ensure well-formed HTML output.
        html_string.append(f"</{self.tag}>")
        return ''.join(html_string)

    def __repr__(self) -> str:
        """
        Provides a string representation of the `ParentNode` instance for debugging purposes.

        Returns:
            str: A string representation showing the tag, children, and props.
        """
        # Return a formatted string showing the important attributes for easier debugging and logging.
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    
def text_node_to_html_node(text_node):
    """
    Converts a text node to an appropriate HTML node.

    This function takes a `text_node` object and converts it to a corresponding `LeafNode` 
    based on its `text_type`. Supported types include plain text, bold, italic, code, link, 
    and image. If an unsupported `text_type` is encountered, an exception is raised.

    Args:
        text_node (object): The text node object containing `text_type`, `text`, `url`, and `alt_text` attributes.

    Returns:
        LeafNode: An instance of `LeafNode` representing the HTML element corresponding to the `text_node`.

    Raises:
        Exception: If `text_type` is not one of the accepted types.
        ValueError: If an unexpected `text_type` is encountered.
    """
    # Define the accepted text types that can be converted into HTML nodes.
    # This provides a clear boundary for what types are supported.
    accepted_types = (TextType.TEXT, TextType.BOLD, TextType.ITALIC, TextType.CODE, TextType.LINK, TextType.IMAGE)

    # Check if the provided text node has a valid type. Raise an exception if not.
    # This validation ensures that only supported text types are processed.
    if text_node.text_type not in accepted_types:
        raise Exception(f"Text type not supported. Must be one of the following {accepted_types}")
        
    # Use pattern matching to determine the appropriate HTML representation for each text type.
    # Pattern matching provides a clear and concise way to handle multiple conditions.
    match text_node.text_type:
        case TextType.TEXT:
            # Return a `LeafNode` without a tag for plain text.
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            # Use the `<b>` tag for bold text representation.
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            # Use the `<i>` tag for italic text representation.
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            # Use the `<code>` tag for code snippet representation.
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            # Use the `<a>` tag with an `href` attribute for hyperlink representation.
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            # Use the `<img>` tag with `src` and `alt` attributes for image representation.
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt_text})
        case _:
            # Catch-all for any unexpected types; should not be reached if validation works.
            raise ValueError(f"Unexpected type encountered. Accepted types: {accepted_types}")

        
        