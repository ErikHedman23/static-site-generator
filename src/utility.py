from leafnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not isinstance(text_node, TextNode):
        raise TypeError("text_node must be a TextNode instance")

    tag_map = {
        TextType.Bold: "b",
        TextType.Italic: "i",
        TextType.Code: "code",
        TextType.Link: "a",
        TextType.Image: "img",
    }

    if text_node.text_type not in TextType:
        raise ValueError("Unsupported TextType")
    
    if text_node.text_type == TextType.Text:
        return LeafNode(tag=None, value=text_node.text)
    
    tag = tag_map.get(text_node.text_type)

    props = {}
    value = text_node.text
    
    if text_node.text_type == TextType.Link:
        props['href'] = text_node.url
    elif text_node.text_type == TextType.Image:
        props['src'] = text_node.url
        props['alt'] = text_node.text
        value = ""

    return LeafNode(tag=tag, value=value, props=props)