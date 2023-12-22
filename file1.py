class Node(object):
    def __init__(self, data, Next = None, Previous = None):
        self.data = data
        self.next = Next
        self.previous = Previous

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setTest(self, newPrevious):
        self.previous = 123
    
    # function for reading from file
    def readInput(filename) -> list[str]:
        with open(filename, 'r') as file:
            words = file.readlines()
            for i in range(len(words)):
                words[i] = words[i].strip()
            return words


class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        ''' This function checks whether the list is empty'''
        return self.head == None

    def insertFirst(self, data):
        ''' This function inserts a new node in the Linked List '''
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode

    def insertLast(self, data):
        newNode = Node(data)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        newNode.setPrevious(current)

    def getAllData(self):
        ''' This function displays the data elements of the Linked List '''
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return elements

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()


if __name__ == '__main__':
    myList = LinkedList()
    myList.insertFirst(1)
    myList.insertFirst(12)
    myList.insertFirst(32)
    myList.insertFirst(1)
    myList.insertFirst(12)
    myList.insertFirst(32)
    myList.insertFirst(22)
    myList.insertLast(2)
    myList.remove(12)
    print(myList.getAllData())
            if randint(0, 3) == 2:
            indexx = randint(0, len(final_result) - 1)
            # print(final_result)
            word = len(final_result[indexx][0])
            newdir = randint(0, 1)
            if newdir == 0:
                final_result[indexx][1] = [randint(0, 18), abs(randint(0, 19) - word), newdir]
            else:
                final_result[indexx][1] = [abs(randint(0, 19) - word), randint(0, 18), newdir]
        population_2.append(final_result)
    return population_2