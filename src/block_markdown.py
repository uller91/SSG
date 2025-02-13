from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


def markdown_to_blocks(markdown):
    #print(markdown)
    split_markdown = markdown.split("\n\n")
    return_list = []
    for item in split_markdown:
        item = item.strip()
        if item != "":
            return_list.append(item)
    return return_list


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    
    if block[:3] == "```" and block[-3:] == "```":
        return "code"
    
    #next three blocks can be rewritten as line do not start with == text block
    lines = block.split("\n")
    counter = 0
    if lines[0][0] == ">":
        for line in lines:
            if line[0] == ">":
                counter += 1
        if counter == len(lines):
            return "quote"    
        
    if lines[0][:2] == "* ":
        for line in lines:
            if line[:2] == "* ":
                counter += 1
        if counter == len(lines):
            return "unordered_list"    
    if lines[0][:2] == "- ":
        for line in lines:
            if line[:2] == "- ":
                counter += 1
        if counter == len(lines):
            return "unordered_list"    
        
    if lines[0][:3] == "1. ":
        i = 1
        for line in lines:
            if line[:3] == f"{i}. ":
                counter += 1
                i += 1
        if counter == len(lines):
            return "ordered_list"    
    
    return "normal"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    marked_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                marked_blocks.append(heading_block_to_html_node(block))
            case "code":
                marked_blocks.append(code_block_to_html_node(block))
            case "quote":
                marked_blocks.append(quote_block_to_html_node(block))
            case "unordered_list":
                marked_blocks.append(block) #4
            case "ordered_list":
                marked_blocks.append(block) #5
            case "normal":
                marked_blocks.append(text_block_to_html_node(block))
    return marked_blocks
            
    
def heading_block_to_html_node(heading):
    if heading[:2] == "# ":
        return ParentNode("h1", text_to_children(heading[2:]))
    elif heading[:3] == "## ":
        return ParentNode("h2", text_to_children(heading[3:]))
    elif heading[:4] == "### ":
        return ParentNode("h3", text_to_children(heading[4:]))
    elif heading[:5] == "#### ":
        return ParentNode("h4", text_to_children(heading[5:]))
    elif heading[:6] == "##### ":
        return ParentNode("h5", text_to_children(heading[6:]))
    elif heading[:7] == "###### ":
        return ParentNode("h6", text_to_children(heading[7:]))


def code_block_to_html_node(code):
    return ParentNode("code", text_to_children(code[4:-4])) #assuming that the first line is "```\n" and the last line is "```"


def quote_block_to_html_node(quote):
    lines = quote.split("\n")
    cut_lines = ""
    for line in lines:
        cut_lines += "\n" + str(line[2:])
    return ParentNode("blockquote", text_to_children(cut_lines[1:])) #assumin that the quote line starts with "> "


def text_block_to_html_node(text):
    return ParentNode("p", text_to_children(text))
    

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    leafnodes = []
    for textnode in textnodes:
        leafnode = text_node_to_html_node(textnode)
        #print(leafnode)
        leafnodes.append(leafnode)
    return leafnodes