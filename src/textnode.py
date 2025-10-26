from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type # Member of TextType enum
        self.url = url # Defualt of None

    def __eq__(self, other): # Compare two TextNode Objects and determine if all properties are equal
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
                )
    
    def __repr__(self): # Retrun a string representation of TextNode => TextNode(TEXT, TEXT_TYPE, URL)
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'