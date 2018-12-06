class Node():
    '''节点类'''
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    '''树类'''

    def __init__(self,root=None):
        self.root = root

    def add(self,elem):
        '''为树添加节点'''
        node = Node(elem)
        if self.root ==None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)

            #对已有的节点进行层次遍历
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preoder(self,root):
        '''递归实现先序遍历'''
        if root == None:
            return
        print(root.elem)
        self.preoder(root.lchild)
        self.preoder(root.rchild)

    def breadth_travel(self,root):
        '''利用队列实现树的遍历'''
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


tree = Tree()
tree.add('A')
tree.add('B')
tree.add('C')
tree.add('D')
tree.preoder(tree.root)

# FlMhCCPCAI3hd99R0SZK0UBCQWyXi9VXvKeyp7ArijypsGW1A-kWGwLVUHw*Ch6NBDiWaIMQ8h0ZpuzB02gBNBX73Fpgkrqo-emSOxSuhn5QVpinvolquY0EYyVdgQreCq7NF7vKr-Jr8jzGmakoRZQuL-HvMvIUbQkG-E6FCPcWe8m3*a1XwpKPzZ3yYvUK5xE8dkY6oBjauQ3K8SVW24xiOHLcU6BIYYiIijC*pgcPvbxkml2r5XlDjfTpzhRH85A79GEiodIX5SQL1Ure4gTkZbV51aLY0S9D-NOVgkz-9b2Yli9n5Cf2UXiJxHDfohtWfU*ux7GTr1RASQsC4w__