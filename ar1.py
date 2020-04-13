#coding: utf-8

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            self.root = Node(data)
        else:
            self.root = None

    #Percurso em ordem simétrica
    def simetric_traversal(self, node=None):
        if node:
            if node.left:
                print('(', end='')
                self.simetric_traversal(node.left)
            print(node, end='')
            if node.right:
                self.simetric_traversal(node.right)
                print(')', end='')
        else:
            self.simetric_traversal(self.root)

if __name__ == '__main__':
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('e')
    n8 = Node('c')
    n9 = Node('d')

    n2.left = n1
    n2.right = n3
    n3.left = n4
    n3.right = n5
    n5.left = n6
    n5.right = n7
    n6.left = n8
    n6.right = n9

    tree.root = n2

    print(tree.simetric_traversal())
