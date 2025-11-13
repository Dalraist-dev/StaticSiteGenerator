# python

import unittest
from converter import split_nodes_delimiter
from textnode import TextNode, TextType



class TestSplitNodesDelimiter(unittest.TestCase):

# Although tests do not incorporate all possibilities, they attempted to cover edge cases and 
# be representative of all Text Types, as well as placement within the original Text Node.

    def test_split_bolded_middle(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)    
        self.assertEqual(
            new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
            ]
            )
    # Although in this test and others, new_nodes prints as:
    # [TextNode("This is text with a ", text, None), TextNode("bolded phrase", bold, None), TextNode(" in the middle", text, None)]
    # It is still equal to the above despite being "text, None" vs "TextType.Text" without the None.
    # This is due to the Enum Class making the two equal and None is equal to not including anything.

    def test_split_italic_start(self):
        node = TextNode("_Italic phrase_ at the start of the text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)              
        self.assertEqual(
            new_nodes, [
            TextNode("Italic phrase", TextType.ITALIC),
            TextNode(" at the start of the text", TextType.TEXT),
            ]
            )

    def test_split_code_end(self):
        node = TextNode("This is text that ends with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)              
        self.assertEqual(
            new_nodes, [
            TextNode("This is text that ends with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            ]
            )
    
    def test_split_code_multiple_same(self):
        node = TextNode("This is a phrase with **bolded text** in two **different** locations", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)              
        self.assertEqual(
            new_nodes, [
            TextNode("This is a phrase with ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            TextNode(" in two ", TextType.TEXT),
            TextNode("different", TextType.BOLD),
            TextNode(" locations", TextType.TEXT),
            ]
            )
        
    def test_split_code_multiple_different(self):
        node = TextNode("This is a phrase with **bolded text**, _italic text_, and a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)              
        self.assertEqual(
            new_nodes, [
            TextNode("This is a phrase with ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(", and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            ]
            )
        
# Testing if not TextType.TEXT
    def test_split_not_text_texttype(self):
        node = TextNode("This is a bolded phrase", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)        
        self.assertEqual(
            new_nodes, [
            TextNode("This is a bolded phrase", TextType.BOLD),
            ]
            )

# The following test to ensure proper error handling


    def test_split_code_without_both_delimiters(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text without both `code delimiters", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE) 

    

if __name__ == "__main__":
    unittest.main()