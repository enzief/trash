class BTreeNode:
    def __init__(self, leaf):
        self.t = 2  # degree - minimum degree (defines the range for number of keys)
        self.n = 0
        self.keys = [None] * (2 * self.t - 1)
        self.children = [None] * (2 * self.t)  # An array of child pointers
        self.leaf = leaf

    # Function to traverse all nodes in a subtree rooted with this node
    def traverse(self):
        # There are n keys and n+1 children, travers through n keys
        # and first n children
        for i in range(0, self.n):
            # If this is not leaf, then before printing key[i],
            # traverse the subtree rooted with child C[i].
            if not self.leaf:
                self.children[i].traverse()
            print(" " + str(self.keys[i]))

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

    def insertNonFull(self, k):
        # Initialize index as index of rightmost element
        i = self.n - 1

        # If this is a leaf node
        if self.leaf:
            # The following loop does two things
            # a) Finds the location of new key to be inserted
            # b) Moves all greater keys to one place ahead
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1

            # Insert the new key at found location
            self.keys[i + 1] = k
            self.n += 1
        else:  # If this node is not leaf
            # Find the child which is going to have the new key
            while i >= 0 and self.keys[i] > k:
                i -= 1

            # See if the found child is full
            if self.children[i + 1].n == 2 * self.t - 1:
                # If the child is full, then split it
                self.splitChild(i + 1, self.children[i + 1])

                # After split, the middle key of C[i] goes up and
                # C[i] is splitted into two. See which of the two
                # is going to have the new key
                if self.keys[i + 1] < k:
                    i += 1
            self.children[i + 1].insertNonFull(k)

    # A utility function to split the child y of this node
    # Note that y must be full when this function is called
    def splitChild(self, i, y):
        # Create a new node which is going to store (t-1) keys
        # of y
        z = BTreeNode(y.leaf)
        z.n = self.t - 1

        # Copy the last (t-1) keys of y to z
        for j in range(0, self.t - 1):
            z.keys[j] = y.keys[j + self.t]

        # Copy the last t children of y to z
        if not y.leaf:
            for j in range(0, self.t):
                z.children[j] = y.children[j + self.t]

        # Reduce the number of keys in y
        y.n = self.t - 1

        # Since this node is going to have a new child,
        # create space of new child
        for j in range(self.n, i, -1):
            self.children[j + 1] = self.children[j]

        # Link the new child to this node
        self.children[i + 1] = z

        # A key of y will move to this node. Find the location of
        # new key and move all greater keys one space ahead
        for j in range(self.n - 1, i - 1, -1):
            self.keys[j + 1] = self.keys[j]

        # Copy the middle key of y to this node
        self.keys[i] = y.keys[self.t - 1]

        # Increment count of keys in this node
        self.n += 1


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

    # The main function that inserts a new key in this B-Tree
    def insert(self, k):
        # If tree is empty
        if self.root is None:
            # Allocate memory for root
            self.root = BTreeNode(True)
            self.root.keys[0] = k  # Insert key
            self.root.n = 1  # Update number of keys in root
        else:  # If tree is not empty
            # If root is full, then tree grows in height
            if self.root.n == 2 * self.t - 1:
                # Allocate memory for new root
                s = BTreeNode(False)

                # Make old root as child of new root
                s.children[0] = self.root

                # Split the old root and move 1 key to the new root
                s.splitChild(0, self.root)

                # New root has two children now. Decide which of the
                # two children is going to have new key
                i = 0
                if s.keys[0] < k:
                    i += 1
                s.children[i].insertNonFull(k)

                # Change root
                self.root = s
            else:  # If root is not full, call insertNonFull for root
                return self.root.insertNonFull(k)
