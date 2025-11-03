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
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        # Ensure No Value allowed
        super().__init__(tag=tag, value=None, children=children, props=props)
        # Ensure Tag can't be None
        if tag is None:
            raise ValueError("A ParentNode must have a tag.")
        # Ensure Children can't be None or be an empty list []
        if children is None or len(children) == 0: 
            raise ValueError("A ParentNode must have at least one child.")
        # Ensures each Child is a HTMLNode B4 calling .to_html
        for child in children:
            if not isinstance(child, HTMLNode): 
                raise ValueError("Children must be instances of HTMLNode.")

    def to_html(self):
        # Ensure Tag have not been manipulated to None since creation of ParentNode
        if not self.tag:
            raise ValueError("ParentNode must have tag to render to html.")
     
        # Opening HTML Tag of Parent
        html_string = f"<{self.tag}{self.props_to_html()}>"

        # Iterate over all Children to continue html_string
        for child in self.children:
            html_string += child.to_html() # Add child to html string
           
        # Close the HTML Tag    
        html_string += f"</{self.tag}>"

        return html_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
