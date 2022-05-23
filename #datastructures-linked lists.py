class Node:
    def __init__(self,num):
        self.value = num
        self.next = None


def insert_ll(root,ele):
    if root == None:
        root = Node(ele)
        return root
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = Node(ele)
        return root
def create_linked_list(list):
    root = None
    for i in range(0,len(list)):
        root = insert_ll(root,list[i])
    return root




def display(root):
    while (root != None):
        print(root.value, end=" ")
        root = root.next

def reversed_linked_list(list):
    if (list.next == None):
        return list
    else:
        prev = None
        temp = list
        while (temp != None):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev


ll = create_linked_list([4,3,2,1])
print(display(ll))
ll2 = reversed_linked_list(ll)
print(display(ll2))