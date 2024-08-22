

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

        if not value or not isinstance(value, str):
            raise ValueError("LeafNode value must be a non-empty string")
        
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
    
        
        