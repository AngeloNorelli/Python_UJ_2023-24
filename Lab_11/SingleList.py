class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    
    def remove_tail(self):      # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next 
            self.tail = current
            self.tail.next = None
        self.length -= 1
        return node

    def join(self, other):      # klasy O(1)
        if other.is_empty():
            return
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):            # czyszczenie listy
        self.head = self.tail = None
        self.length = 0

    def search(self, data):     # klasy O(n)
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_min(self):         # klasy O(n)
        if self.is_empty():
            return None
        min_node = self.head
        current = self.head.next
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        return min_node

    def find_max(self):         # klasy O(n)
        if self.is_empty():
            return None
        max_node = self.head
        current = self.head.next
        while current is not None:
            if current.data > max_node.data:
                max_node = current
            current = current.next
        return max_node

    def reverse(self):          # klasy O(n)
        prev_node = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head, self.tail = self.tail, self.head