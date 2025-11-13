# python

from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes, delimiter, text_type): 
    # Create an empty list for post conversion
    new_nodes = []

    for node in old_nodes:
        # If it is not TEXT type, then added w/o splitting
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # If it is TEXT type:
        text = node.text

        split_nodes = [] # Holds pieces of each old_node when split
        parts = text.split(delimiter)
        # print(f"Right Here -> {text} & {parts}") # <- Used in Testing


        # Check if we have an uneven number of parts (missing closing delimiter)
        # If only 1 delimiter instead of 2, or 3 instead of 4,
        # then there is an opening delimiter without a closing delimiter.
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: Missing delimiter for {delimiter}")

        # Iterate through the parts to form new nodes
        for i in range(len(parts)):
            # Skips adding empty text nodes. Example "" is considered a part when delimiter at start of text
            if parts[i] == "":
                continue
            # Even index = regular text Will always start with TextType.TEXT at index 0
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:  # Odd index: special text (bold, italic, code)
                split_nodes.append(TextNode(parts[i], text_type))
        
        # Add nodes created from each node in old_nodes to new_nodes
        new_nodes.extend(split_nodes) 

    return new_nodes

