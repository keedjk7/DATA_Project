class node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linklist():
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def __str__(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" "+str(last.next.data)
            last=last.next
        return temp
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def dequeue(self):
        temp=self.head.data
        self.head=self.head.next
        return temp
    def size(self):
        size=0
        last=self.head
        while last is not None:
            last=last.next
            size=size+1
        return  size
    def sortMax(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data < last.next.data:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next
    def sortMin(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data > last.next.data:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next   
    def result(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" -> "+str(last.next.data)
            last=last.next
        return temp

ll = linklist()
inl = input("enter : ").split(" ")
for i in inl:
    ll.append(int(i))
ll.sortMax()
print(ll)
ll.sortMin()
print(ll)