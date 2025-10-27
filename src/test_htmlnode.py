# python

import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    # Although tests do not incorporate all possibilities, they attempted to cover edge cases and 
    # be representative of the overall class.

    def test_all_defaults(self):
        node = HTMLNode()
        # Checks None on each argument
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_children_are_recorded(self):
        # Create Child and Parent Nodes
        child1 = HTMLNode(tag="em", value="hi")
        child2 = HTMLNode(tag="strong", value="there")
        parent = HTMLNode(tag="p", children=[child1, child2])
        # Tests on Nodes
        self.assertIsInstance(parent.children, list)  # Asserts the parent nodes children argument is a list
        self.assertIs(parent.children[0], child1)  # Asserts first child in list is child1
        self.assertIs(parent.children[1], child2)  # Asserts second child in list is child2

    def test_props_to_html_none(self):
        node = HTMLNode(tag="a", props=None)
        self.assertEqual(node.props_to_html(), "")  # Asserts a node with props=None will produce an empty string via props_to_html method

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://www.boot.dev", "target": "_blank"})
        prop_string = node.props_to_html()
        self.assertTrue(prop_string.startswith(" "))  # Check for leading space
        self.assertIn('href="https://www.boot.dev"', prop_string)  # Check Format of First
        self.assertIn('target="_blank"', prop_string)  # Check Format of Second

    def test_props_to_html_single(self):
        node = HTMLNode(tag="img", props={"alt": "x"})
        self.assertEqual(node.props_to_html(), ' alt="x"') # Check for leading Space

    def test_to_html_raises(self):
        node = HTMLNode(tag="p", value="Project Time on Boot.Dev!")
        # Test that class method to_html raises the right error
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr_includes_all_fields_no_url(self):
        node = HTMLNode(tag='p', value='Project Time on Boot.Dev!')
        repr_string = repr(node)
        # Testing completed on pieces to make testing changes to code easier as overall Formatting may be modified
        self.assertIn("HTMLNode", repr_string)
        self.assertIn("tag", repr_string)
        self.assertIn("<p>", repr_string)
        self.assertIn("value", repr_string)
        self.assertIn("Project Time on Boot.Dev!", repr_string)
        self.assertIn("children", repr_string)
        self.assertIn("props", repr_string)

    def test_repr_includes_all_fields_child_url(self):
        child1 = HTMLNode(tag='b', value='Project Time')
        child2 = HTMLNode(tag='a', value='Boot.Dev', props={"href": "https://www.boot.dev", "target": "_blank"})
        parent = HTMLNode(tag='p', value='Project Time on Boot.Dev!', children=[child1, child2])
        repr_string_child1 = repr(child1)
        repr_string_child2 = repr(child2)
        repr_string_parent = repr(parent)
        # Testing completed on pieces to make testing changes to code easier as overall Formatting may be modified 
        # Test Headings in all repr strings
        for repr_string in (repr_string_child1, repr_string_child2, repr_string_parent):
            self.assertIn("HTMLNode", repr_string)
            self.assertIn("tag", repr_string)
            self.assertIn("value", repr_string)
            self.assertIn("children", repr_string)
            self.assertIn("props", repr_string)
        # Test contents of Tags, Values on each repr
        self.assertIn("<b>", repr_string_child1)
        self.assertIn("<a>", repr_string_child2)
        self.assertIn("<p>", repr_string_parent)
        self.assertIn("Project Time", repr_string_child1)
        self.assertIn("Boot.Dev", repr_string_child2)
        self.assertIn("Project Time on Boot.Dev!", repr_string_parent)
        # Test Children included in repr
        self.assertIn("children=None", repr_string_child1)
        self.assertIn("children=None", repr_string_child2)
        self.assertIn("<b>", repr_string_parent)  # Parents keep the full repr from their children in their repr
        self.assertIn("<a>", repr_string_parent)  # Parents keep the full repr from their children in their repr
        # Test Props included in repr
        self.assertIn("props=None", repr_string_child1)
        self.assertIn("'href': 'https://www.boot.dev'", repr_string_child2)
        self.assertIn("'target': '_blank'", repr_string_child2)
        self.assertIn("props=None", repr_string_parent)

    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Boot.Dev", props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="_blank">Boot.Dev</a>')

    def test_leaf_to_html_code(self):
        node = LeafNode(tag="code", value='print("Hello World!")')
        self.assertEqual(node.to_html(), '<code>print("Hello World!")</code>')

    def test_leaf_without_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()