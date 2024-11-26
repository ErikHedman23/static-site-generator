from __future__ import annotations

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag: str, children: list[HTMLNode] = None, props: dict[str, str] = None):
        if children == None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children == None:
            raise ValueError("ParentNode children cannot be None")
        if self.props == None:
            return f"<{self.tag}>{self.children_to_html()}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.children_to_html()}</{self.tag}>"
    
    def children_to_html(self):
        return "".join(child.to_html() for child in self.children)
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"