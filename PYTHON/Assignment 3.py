class Queue:
    def __init__(self,size):
        self.head=self.tail=-1
        self.size=size
        self.queue=[]
    
    def enqueue(self,data):
        if (((self.tail+1)%self.size)==self.head):
            print("Queue is Full!")
            return
        elif (self.head==-1):
            self.head=0
            self.tail=0
        else:
            self.tail=(self.tail+1)%self.size
        self.queue[self.tail]=data
    
    def dequeue(self):
        if (self.head==-1):
            print("Queue is Empty")
            return
        elif (self.head==self.tail):
            pop=self.queue[self.head]
            self.head=-1
            self.tail=-1
        else:
            pop=self.queue[self.head]
            self.head=(self.head+1)%self.size
        return pop
        
    def dis(self):
        if self.head==-1:
            print("Queue is Empty")
            return
        elif (self.tail >= self.head):
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=" ")
        else:
            for i in range(self.head,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.tail+1):
                print(self.queue[i],end=" ")
        print()

print("******************* Circular Queue *******************")
opt=10
q=Queue(0) #temp Queue
while(opt):
    print("\n1. Create Queue\n2. Enqueue\n3. Dequeue\n4. Display\n0. Exit\n")
    opt=int(input("Enter your option: "))
    if opt==1:
        size=int(input("Enter size of queue: "))
        q=Queue(size)
    elif opt==2:
        val=input("Enter Value to insert: ")
        q.enqueue(val)
    elif opt==3:
        pop=q.dequeue()
        if pop!=None:
            print("Value deleted:",pop)
    elif opt==4:
        q.dis()
print("EXIT")