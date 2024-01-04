class LinkedList:

    class node:
        data = None
        pointer = None

    start = None

    def add(self,item):
        try:
            #Check memory overflow
            new_node = LinkedList.node()
            new_node.data = item
            current_node = self.start
            #List is empty
            if current_node == None:
                new_node.pointer = None
                self.start = new_node
            else:
                #Item becomes new start item
                if item < current_node.data:
                    self.start = new_node
                    new_node.pointer = current_node
                else:
                    #Find correct position in the list
                    while current_node != None and current_node.data < item:
                        previous_node = current_node
                        current_node = current_node.pointer
                    new_node.pointer = previous_node.pointer
                    previous_node.pointer = new_node
            return True
        except:
            return False

    def delete(self,item):
        current_node = self.start
        #Check the list is not empty
        if current_node != None:
            #Item is the start node
            if item == current_node.pointer:
                self.start = current_node.pointer
            else:
                #Find item in list
                while current_node != None and item != current_node.data:
                    previous_node = current_node
                    current_node = current_node.pointer
                    previous_node.pointer = current_node.pointer

    def output(self):
        items = []
        current_node = self.start
        if current_node != None:
            #Visit each node
            while current_node != None:
                items.append(current_node.data)
                current_node = current_node.pointer
        return items

items = ["Florida","Georgia","Delaware","Alabama","California"]
l = LinkedList()
for index in range(0,len(items)):
    l.add(items[index])
    print(l.output())