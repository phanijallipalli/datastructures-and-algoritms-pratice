class Node:
    def __init__(self,num):
        self.value = num
        self.next = None


def insert_ll(root,ele):
    if root == None:
        root = Node(ele)
        return root
    else:
        temp = Node(ele)
        temp.next = root
        return temp
def create_linked_list(list):
    root = None
    for i in range(0,len(list)):
        root = insert_ll(root,list[i])
    return root




def display(root):
    while (root != None):
        print(root.value, end=" ")
        root = root.next


ll = create_linked_list([4,3,2,1])
print(display(ll))