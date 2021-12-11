class Node:
    data=None
    next_node=None

    def __init__(self,data):
        self.data=data
    
    def __repr__(self):   #### for printing data that we initialized in constructor
        return "<Node data: %s>" % self.data        
    
class linked_list:

    """
    Going to impplement singly linked_list
    """
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        return self.head==None

    def size(self):
        current=self.head
        count=0
        while current:
            current=current.next_node
            count=count+1
        return count
    def add(self,data):
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    
    def __repr__(self):

        nodes=[]
        current=self.head
        while current:
            if (current is self.head):
                nodes.append("<Head is> %s" % current.data)
            elif (current.next_node is None ):
                nodes.append("<tail is %s" % current.data)
            else:
                nodes.append("Data is %s" % current.data)
            current=current.next_node
        return '->'.join(nodes)

l=linked_list()
l.add(23)
l.add(24)
print(l.size())
