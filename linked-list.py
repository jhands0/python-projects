class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def ListPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

llist = LinkedList()
llist.headval = Node("gamer")
llist1 = Node("moment")
llist2 = Node("poggers")

llist.headval.nextval = llist1
llist1.nextval = llist2

llist.ListPrint()