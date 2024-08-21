

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
        super().__init__(tag=tag, value=value, props=props)
        self.children = None
        self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.children = children
        self.value = None

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag!")
        if not self.children:
            raise ValueError("Children Required!")
        
        content = ''.join(list(map(lambda x: x.to_html(), self.children)))
        return f"<{self.tag}>{content}</{self.tag}>"


        
    
        
        