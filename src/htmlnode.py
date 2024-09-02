from enums import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        properties = []
        for k,v in self.props.items():
            properties.append(f' {k}="{v}"')
        
        return "".join(properties)
    
    def __repr__(self) -> str:
        
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 
         
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        
        if not isinstance(value, str):
            raise ValueError("LeafNode value must be a string")
        
        if props is not None and not isinstance(props, dict):
            raise ValueError("props must be either a dictionary or None")
        
        super().__init__(tag=tag, value=value, props=props)        

    def to_html(self):        
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self) -> str:
        
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        
        if not isinstance(children, list) or not children:
            raise ValueError("Children must be a populated list")
        
        if not isinstance(children, list) or not all(isinstance(child, (ParentNode, LeafNode)) for child in children):
            raise ValueError("Children must be a non-empty list of ParentNode or LeafNode objects")
            
        if not isinstance(tag, str) or not tag:
            raise ValueError("Tag must be a populated string")  
            
        super().__init__(tag=tag, children=children, props=props)       
    

    def to_html(self):       
        
        html_string = []
        html_string.append(f"<{self.tag}>")

        for child in self.children:
            html_string.append(child.to_html())

        html_string.append(f"</{self.tag}>")
        return ''.join(html_string)    
    
    def __repr__(self) -> str:
        
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
def text_node_to_html_node(text_node):
    accepted_types = (TextType.TEXT, TextType.BOLD, TextType.ITALIC, TextType.CODE, TextType.LINK, TextType.IMAGE)

    if text_node.text_type not in accepted_types:
        raise Exception(f"Text type not supported. Must be one of the following {accepted_types}")
        
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt_text})
        case _:
            raise ValueError(f"Unexpected type encountered. Accepted types: {accepted_types}")
        
        