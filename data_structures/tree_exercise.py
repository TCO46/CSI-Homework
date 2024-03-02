class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
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

    def print_tree(self, options):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if options == "name":
            print(prefix + self.data)
        elif options == "both":
            print(prefix + self.data + '(' + self.designation + ')')
        else:
            print(prefix + self.designation)

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_management_tree():
    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(TreeNode)

    ceo = TreeNode("Nilupul", "CEO")


    return root


if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree()
