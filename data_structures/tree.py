class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Devices")

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("Iphone"))

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("ThinkPad"))
    laptop.add_child(TreeNode("Mac"))

    root.add_child(phone)
    root.add_child(laptop)

    # print(laptop.get_level())
    return root


if __name__ == "__main__":
    root = build_product_tree()
    # print(root.get_level())
    root.print_tree()
    pass
