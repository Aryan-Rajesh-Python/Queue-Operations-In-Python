def isempty(que):
    if(len(que)==0):
        return True
    else:
        return False
def enqueue(que,ele):
    que.append(ele)
    print("Element is successfully pushed into the queue!")
def dequeue(que):
    if(isempty(que)):
        print("Queue is empty an you cannot pop the element now!")
    else:
        print("Element is popped out successfully!")
        print("Popped out element is: ",que.pop(0))
def peek(que):
    if(isempty(que)):
        print("Queue is empty and there is no element to display!")
    else:
        print("Displaying the top element in the queue!")
        print("Top element is: ",que[0])
def display(que):
    if(isempty(que)):
        print("Queue is empty and there is no element to display!")
    else:
        print("Displaying the queue!")
        print("Queue: ",que)
queue=[]
while(True):
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter the operation you want to perform on the queue: "))
    if(choice==1):
        element=int(input("Enter the element you want to push into the queue: "))
        enqueue(queue,element)
    if(choice==2):
        dequeue(queue)
    if(choice==3):
        peek(queue)
    if(choice==4):
        display(queue)
    elif(choice==5):
        print("You have successfully exited the program!")
        break