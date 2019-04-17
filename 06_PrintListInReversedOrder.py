class CreateListNode:
    def __init__(self, x=None):
        self.value = x
        self.next = None


# class List:
#     def __init__(self, array):
#         self.tem_node = CreateListNode()
#         self.node = CreateListNode()
#         for i in array:
#             if not self.tem_node.value:
#                 self.tem_node = CreateListNode(i)
#                 self.node = self.tem_node
#             else:
#                 self.tem_node.next = CreateListNode(i)
#                 self.tem_node = self.tem_node.next
#
#     def get_list(self):
#         return self.node

def build_list(array):
    head = CreateListNode()
    temp_node = CreateListNode()
    for i in array:
        if not temp_node.value:
            temp_node = CreateListNode(i)
            head = temp_node
        else:
            temp_node.next = CreateListNode(i)
            temp_node = temp_node.next
    return head

def PrintListInReversedOrder(listNode):
    if listNode.next is not None:
        PrintListInReversedOrder(listNode.next)
        print listNode.value
    else:
        print listNode.value


if __name__ == '__main__':
    listes = build_list([7,8,3,4,5])
    PrintListInReversedOrder(listes)


