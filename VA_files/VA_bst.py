"""
Solutions to module VA bst

Student: Agnes Leth
Mail: agnes-leth@live.se
"""
import random
import math
class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)
    
    def height(self):                 #     returns the height of the tree       
            def _height(n):
                if n is None:
                    return 0
                else:
                    return 1 + max(_height(n.left), _height(n.right))
                
            n = self.root
            return _height(n)
    

    def ipl(self):   #internal path lenght 
        def _ipl(n, level):
            if n is None:
                return 0
            else: 
                return level + _ipl(n.left, level + 1) + _ipl(n.right, level + 1)
        
        n = self.root
        level = 1

        return _ipl(n, level)
                

def random_tree(n):                               # Useful
    t = BST()
    for _ in range(n):
        t.insert(random.random())
    return t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print("ipl:", t.ipl())

    print("n, Height, IPL/n, 1.39 * log2(n)")
    for k in range(1, 10):
        n = 1000 * (2**k)
        t = random_tree(n)
        ipl = t.ipl()
        height = t.height()
        print(f"{n}, {height}, {ipl / n}, {1.39 * math.log2(n)}")


if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?
Well, as the ratio IPL/n approches the theoretical value.

What can you guess about the height?
The height of the tree increases with the number of nodes, seems to grow approximately logarithmically with n 
Bc of the randomness its a greate variability


"""
