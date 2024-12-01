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
    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    if not isinstance(old_nodes, list):
        raise TypeError("old_nodes must be a list")

    if not isinstance(delimiter, str):
        raise TypeError("delimiter must be a string")

    if not isinstance(text_type, TextType):
        raise TypeError("text_type must be a TextType")
    
    tag_map = {
        TextType.Bold: "**",
        TextType.Italic: "*",
        TextType.Code: "`",
    }
    
    tag = tag_map[text_type]
    
    nodes = []
    for node in old_nodes:
        text = node.text
        if text == None:
            continue
        if delimiter == tag and delimiter in text:
            parts = text.split(delimiter)
            for index, part in enumerate(parts):
                if part:
                    if index % 2 == 0:
                        nodes.append(TextNode(part, TextType.Text))
                    else:
                        nodes.append(TextNode(part, text_type))
            continue
        nodes.append(node)
    return nodes
        