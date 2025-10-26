from textnode import TextNode, TextType #Import Classes

def main():

    firstnode = TextNode("This text is bold!", TextType.BOLD)
    secondnode = TextNode("Link Anchor Text", TextType.LINK, "https://boot.dev")

    print(firstnode)
    print(secondnode)

if __name__ == "__main__":
    main()
