# python

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child Classes should implement this method")
    
    def props_to_html(self):  # Create a string to represent HTML attributes
        if self.props is None:
            return ""
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
        # Example: {"href": "https://www.google.com", "target": "_blank",}
        #          BECOMES
        #           href="https://www.google.com" target="_blank"
    
    def __repr__(self):
        return f'HTMLNode(tag=<{self.tag}>, value={self.value}, children={self.children}, props={self.props})'
    