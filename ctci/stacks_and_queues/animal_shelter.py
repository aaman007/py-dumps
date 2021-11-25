"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in LinkedList data structure.
"""

from collections import deque


class ShelterDS:
    def __init__(self):
        self.timestamp = 0
        self.cats = deque([])
        self.dogs = deque([])

    def enqueue(self, animal, animal_type):
        if animal_type == 'cat':
            self.cats.append((animal, self.timestamp))
        else:
            self.dogs.append((animal, self.timestamp))
        self.timestamp += 1

    def dequeue_any(self):
        if not self.dogs:
            return self.cats.popleft()[0]
        elif not self.cats:
            return self.cats.popleft()[0]
        if self.cats[0][1] < self.dogs[0][1]:
            return self.cats.popleft()[0]
        return self.dogs.popleft()[0]

    def dequeue_dog(self):
        return self.dogs.popleft()[0]

    def dequeue_cat(self):
        return self.cats.popleft()[0]


class Animal:
    def __init__(self, name, order=None):
        self.name = name
        self.order = order

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.order < other.order

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        self.cats = deque([])
        self.dogs = deque([])
        self.timestamps = 0

    def enqueue(self, animal):
        animal.set_order(self.timestamps)
        self.timestamps += 1

        if isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_any(self):
        if not self.cats:
            return self.dequeue_dog()
        elif not self.dogs:
            return self.dequeue_cat()
        return self.dequeue_dog() if self.dogs[0] < self.cats[0] else self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.popleft()

    def dequeue_cat(self):
        return self.cats.popleft()

