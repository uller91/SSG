import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    #tests_self
    '''
    dummy = TextNode("Text node", TextType.BOLD, "url")
    print(dummy.__repr__())

    dummy_2 = TextNode("Text node 2", TextType.CODE, )
    print(dummy_2.__repr__())
    '''

""" 
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq_enum(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node3)

    def test_not_eq_link(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, "http")
        self.assertNotEqual(node, node4)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node5)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is another text node", TextType.LINK, "what?")
        self.assertNotEqual(node, node6)
"""

if __name__ == "__main__":
    unittest.main()