class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def init(self, name, number):
        self.name = name
        self.number = number
    def str(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def init(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def init(self, size):
        self.size = size
        self.data = [None] * size
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size
    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)
        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while True:
                if current.key == key:
                    current.value.number = number
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if not current:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}:", end=" ")
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()
