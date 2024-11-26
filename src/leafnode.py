from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag: str = None, value: str = None, props: dict[str, str] = None):
        if value == None or tag == None:
            raise ValueError("LeafNode must have a tag and a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be None")   
        if self.tag == None:
            return self.value.strip()
        if self.props == None:
            return f"<{self.tag}>{self.value.strip()}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value.strip()}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

        
