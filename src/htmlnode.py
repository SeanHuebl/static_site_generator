

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
    
    def __init__(self, value):
        super().__init__(value=value)
        self.children = None
        self.value = value

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value

        