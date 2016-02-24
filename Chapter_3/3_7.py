'''
An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) if all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like.
Create the data structure to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the built-in LinkedList data structure.
'''
class petNode:
    def __init__(self, species=None, nextNode=None):
        self.Species = species
        self.nextNode = nextNode
    def set_next(self, node):
        self.nextNode = node
    def get_next(self):
        return self.nextNode
    def set_species(self, Species):
        self.Species = Species
    def get_species(self):
        return self.Species
class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
        self.tail_node = head_node
    def insert(self, node):
        if self.head_node == None:
            self.head_node = self.tail_node = node
        self.tail_node.set_next(node)
        self.tail_node = node
    def displayList(self):
        queue = []
        current = self.head_node
        while current:
            queue.append(current.get_species())
            current = current.get_next()
        print queue
    def dequeueAny(self):
        if self.head_node == None: return None
        current = self.head_node
        self.head_node = current.get_next()
        return current.get_species()
    def dequeueDog(self):
        if self.head_node == None: return None
        current = self.head_node
        prev = None
        while current:
            if current.get_species() == "Dog":
                if prev == None:
                    self.head_node = current.get_next()
                    return current.get_species()
                prev.set_next(current.get_next())
                return current.get_species()
            prev = current
            current = current.get_next()
    def dequeueCat(self):
        if self.head_node == None: return None
        current = self.head_node
        prev = None
        while current:
            if current.get_species() == "Cat":
                if prev == None:
                    self.head_node = current.get_next()
                    return current.get_species()
                prev.set_next(current.get_next())
                return current.get_species()
            prev = current
            current = current.get_next()
class petQueue:
    def __init__(self):
        self.petQueue = LinkedList()
    def enqueue(self, species):
        new_node = petNode(species)
        self.petQueue.insert(new_node)
    def dequeueAny(self):
        return self.petQueue.dequeueAny()
    def dequeueDog(self):
        return self.petQueue.dequeueDog()
    def dequeueCat(self):
        return self.petQueue.dequeueCat()
    def displayList(self):
        return self.petQueue.displayList()
        
myPetQueue = petQueue()
pets = ["Dog", "Cat", "Dog", "Cat", "Cat", "Dog"]
for i in pets:
    myPetQueue.enqueue(i)
myPetQueue.displayList()
myPetQueue.dequeueAny()
myPetQueue.displayList()
myPetQueue.dequeueDog()
myPetQueue.dequeueCat()
myPetQueue.displayList()
