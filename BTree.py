class BTreeNode:
    def __init__(self, keys, n, leaf, children):
        self.keys = keys  # An array of keys
        self.t = 2  # degree - minimum degree (defines the range for number of keys)
        self.children = children  # An array of child pointers
        self.n = n  # Current number of keys
        self.leaf = leaf  # Is true when node is leaf. Otherwise false

    def __init__(self, leaf):
        self.leaf = leaf
        self.n = 0

    # Function to traverse all nodes in a subtree rooted with this node
    def traverse(self):
        # There are n keys and n+1 children, travers through n keys
        # and first n children
        for i in range(0, self.n):
            # If this is not leaf, then before printing key[i],
            # traverse the subtree rooted with child C[i].
            if not self.leaf:
                self.children[i].traverse()
            print(" " + self.keys[i])

        # Print the subtree rooted with last child
        if not self.leaf:
            self.children[self.n].traverse()

    # Function to search key k in subtree rooted with this node
    def search(self, k):
        # Find the first key greater than or equal to k
        i = 0
        while i < self.n and k > self.keys[i]:
            i += 1

        # If the found key is equal to k, return this node
        if self.keys[i] == k:
            return self

        # If the key is not found here and this is a leaf node
        if self.leaf:
            return None

        # Go to the appropriate child
        return self.children[i].search(k)


class BTree:
    # Constructor (Initializes tree as empty)
    def __init__(self):
        self.root = None
        self.t = 2  # Minimum degree

    # function to traverse the tree
    def traverse(self):
        if self.root is not None:
            self.root.traverse()

    def search(self, k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)
