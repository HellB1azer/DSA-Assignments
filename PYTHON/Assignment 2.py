class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class Stack:
    def __init__(self,n=50):
        self.head=None
        self.size=n
        self.cnt=0
        self.ops=["+","-","*","/","^","%"]
        self.pri = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def isFull(self):
        if self.cnt==self.size:
            return 1
        return 0
    
    def push(self,data):
        if self.isFull():
            print("Stack is Full!")
            return
        
        if self.isEmpty():
            self.head=node(data)
            self.cnt+=1
            return
        
        new=node(data,self.head)
        self.head=new
        self.cnt+=1
    
    def pop(self):
        if self.isEmpty():
            print("Empty")
            return
        
        poped=self.head
        if self.head is None:
            self.head=None
            return poped.data
        self.head=self.head.next
        self.cnt-=1
        return poped.data
    
    def top(self):
        if self.isEmpty():
            print("Empty Stack!")
            return
        return self.head.data
    
    def rev_exp(self,exp):
        exp=exp[::-1]
        l=[]
        for i in exp:
            l.append(i)
        
        for i in range(len(l)):
            if l[i]=='(':
                l[i]=')'
            elif l[i]==')':
                l[i]='('
        exp=""
        for i in l:
            exp+=i
        return exp
    
    def inftopost(self,exp):
        post=""
        for i in exp:
            if ((i not in self.ops) and (i!='(' and i!=')')):
                post+=i
            elif i=="(":
                self.push(i)
            elif i==")":
                while (not self.isEmpty() and self.top()!="("):
                    post+=self.pop()
                self.pop()
            else:
                #self.push(i)
                while (not self.isEmpty() and self.top()!="(" and self.pri[i]<self.pri[self.top()]):
                    #print(i)
                    post+=self.pop()
                self.push(i)
        while not self.isEmpty():
            post+=self.pop()
        return post
    
    def inftopre(self,exp):
        exp=self.rev_exp(exp)
        exp=self.inftopost(exp)
        exp=self.rev_exp(exp)
        return exp
    
    def dis(self):
        if self.head is None:
            print("Empty Stack")
            return
        
        temp=self.head
        
        while temp is not None:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print()
    
print("******************* Linked List *******************")
opt=10
while(opt):
    s1=Stack()
    print("\n1. Push\n2. Pop\n3. Display\n4. Infix to Postfix\n5. Infix to Prefix\n0. Exit\n")
    opt=int(input("Enter your option: "))
    if opt==1:
        val=int(input("Enter Value to Insert: "))
        s1.push(val)
    elif opt==2:
        print("Value Poped:",s1.pop())
    elif opt==3:
        s1.dis()
    elif opt==4:
        s2=Stack()
        exp=input("Enter Infix Expression: ")
        print(s2.inftopost(exp))
    elif opt==5:
        s2=Stack()
        exp=input("Enter Infix Expression: ")
        print(s2.inftopre(exp))
print("EXIT")