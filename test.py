myList=[]

class MyObject:
    def __init__(self, message, list):
        self.message=message
        self.list=list
    
    def talk(self):
        print(self.message) 
    
    def remove(self):
        self.list.remove(self)

test1= MyObject("Hiii !!!", myList)
myList.append(test1)
print(myList)
myList[0].talk()
test1.talk()

test1.remove()
print(myList)

test1.talk()

