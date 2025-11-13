# python

import unittest
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):

# Although tests do not incorporate all possibilities, they attempted to cover edge cases and 
# be representative of all 6 current Text Types. Currently we have __eq__ and __repr__ functions.

    def test_eq1_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq1_nourl_texttypes(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq2_url(self):
        node = TextNode("Boot.Dev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Boot.Dev", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq2_url(self):
        node = TextNode("Boots", TextType.IMAGE, "https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp")
        node2 = TextNode("Boots", TextType.IMAGE, "https://blog.boot.dev/img/800/bootssalmonhoney.webp.webp")
        self.assertNotEqual(node, node2)

    def test_eq3_nonetypes(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a code node", TextType.CODE, None)
        self.assertEqual(node, node2)

    def test_not_eq3_strings(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr_no_url(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        expected = 'TextNode("This is a italic text node", italic, None)'
        self.assertEqual(repr(node), expected)

    def test_repr_with_url(self):
        node = TextNode("Boot.Dev", TextType.LINK, "https://www.boot.dev")
        expected = 'TextNode("Boot.Dev", link, https://www.boot.dev)'
        self.assertEqual(repr(node), expected)


# Test Method to conver TextNode to HTMLNode
class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_code(self):
        node = TextNode('print("This is code")', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 'print("This is code")')

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )


if __name__ == "__main__":
    unittest.main()