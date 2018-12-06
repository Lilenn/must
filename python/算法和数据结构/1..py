# class SingleNode():
#     '''单链表节点'''
#
#     def __init__(self,item):
#         # item 存放数据元素
#         self.item = item
#         #next 存放下一个节点的标识
#         self.next = None
#
# class SingleLinkList():
#     '''单链表'''
#
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''判断列表是否为空'''
#         return self._head == None
#
#     def length(self):
#         '''链表长度'''
#         count = 0
#         # head 初始化时指向头节点
#         head = self._head
#
#         # 尾节点指向None，当没有达到尾部时执行
#         while head != None:
#             count += 1
#             # 将head后移一个节点
#             head = head.next
#         return count
#
#     def travel(self):
#         '''遍历链表'''
#         head = self._head
#
#         while head !=None:
#             print(head.item)
#             head = head.next
#         print('complete!')
#
#     def add(self,item):
#         '''头部添加元素'''
#         #先创建一个保存item的节点
#         node = SingleNode(item)
#         # 将新增的节点的next指向原有的头部节点，就是self._head指向的位置
#         node.next = self._head
#         #将链表的头_head 指向新的节点
#         self._head = node
#
#     def append(self,item):
#         '''向尾部追加节点'''
#         node =SingleNode(item)
#
#         #先判断链表是否为空
#         if self.is_empty():
#             self._head = node
#         else:
#             cur = self._head
#             while cur.next !=None:
#                 cur = cur.next
#         cur.next = node
#
#     def insert(self,pos,item):
#         '''指定位置添加元素'''
#         # 指定位置pos在第一个元素之前，向头部插入
#         if pos <= 0:
#             self.add(item)
#         # 指定位置pos在最后一个元素知乎，向尾部插入
#         elif pos > (self.length() - 1):
#             self.append(item)
#         # 向中间插入，找到指定位置
#         else:
#             node = SingleNode(item)
#             count = 0
#             #pre 用来指向指定位置pos 的前一个位置pos -1 ，初始 _head 移动到指定的位置
#             pre = self._head
#             while count < (pos - 1 ):
#                 count += 1
#                 pre = pre.next
#             #先将新节点的node的next指向插入位置的节点
#             node.next = pre.next
#             #将插入位置的前一个节点的next指向新节点
#             pre.next = node
#     def remove(self,item):
#         '''删除节点'''
#         cur = self._head
#         pre = None
#
#         while cur != None:
#             #找到指定元素
#             if cur.item == item:
#                 #如果第一个就是删除的节点
#                 if not pre:
#                     self._head = cur.next
#                 else:
#                     pre.next = cur.next
#                     break
#             else:
#                 #继续向链表后移动节点
#                 pre = cur
#                 cur = cur.next
#
#     def search(self,item):
#         '''链表查找节点是否存在，返回True 或者False'''
#         cur = self._head
#         while cur != None:
#             if cur.item == item:
#                 return True
#             cur = cur.next
#         return False
#
# if __name__ == '__main__':
#     ll = SingleLinkList()
#     ll.add(1)
#     ll.add(2)
#     ll.append(4)
#     ll.travel()

class Node():
    '''双向链表节点'''
    def __init__(self,item):
        self.item = item
        self.next  =None
        self.prev = None

class DLinkeList():
    '''双向链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head == None

    def length(self):
        '''返回链表长度'''
        cur = self._head
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('complete!')

    def add(self,item):
        '''头部插入元素'''
        node =Node(item)
        if self.is_empty():
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head指向node
            self._head = node

    def append(self,item):
        '''向尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            # 如果链表为空，将_head指向node
            self._head = node
        else:
            #初始化指针
            cur = self._head
            while cur.next !=None:
                cur = cur.next

            #将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def search(self,item):
        '''查找元素是否存在'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self,pos,item):
        '''在指定位置添加节点'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            #移动指针到指定的位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            #将node节点的prev指向cur
            node.prev = cur
            #将node节点的next指向下一个节点
            node.next = cur.next
            #将cur的下一个节点的prev指向node
            cur.next.prev = node
            #将cur的next指向node
            cur.next = node

    def remove(self,item):
        '''删除指定位置元素'''
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next 指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next


if __name__ == '__main__':
    ll = DLinkeList()
    ll.add(1)
    ll.add(3)
    ll.insert(0,4)
    ll.travel()
