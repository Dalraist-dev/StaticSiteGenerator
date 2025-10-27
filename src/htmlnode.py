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
    


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        # Ensure No Children are allowed
        super().__init__(tag=tag, value=value, children=None, props=props)
        # Ensure Value can't be None
        if value is None:
            raise ValueError("A LeafNode must have a value.")
        
    def to_html(self):
        # Ensure Value has not been manipulated to None since creation of LeafNode
        if not self.value:
            raise ValueError("LeafNode must have a value to render html.")
        
        if self.tag is None:
            return self.value # Return raw unmodified text while lacking specific tag
        # Generate the HTML string
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"