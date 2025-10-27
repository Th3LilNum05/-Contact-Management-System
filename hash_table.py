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


#Design Memo
#This code meets the requirements for creating a simple hash table structure optimized for contact information storage and retrieval. The code structure consists of three classes: Contact, Node, and HashTable, each having its unique functionality for the system’s architecture. The Contact class contains a persons name and phone number, making it a sound and fully reproducible model for each entry. The Node class is essentially a node for use in a linked list, managing hash collisions for contact retrievals using chaining. The class contains a pair consisting of its key, defined by contact name, and its corresponding value, defined by an entry from the Contact class, pointing to the next node so that two different entries can occupy the same location in the hash index in case collisions happen. The major programming action is, however, found in the HashTable class, initializing an array to hold the nodes, using a simple hash function that adds code values for each unique contact name and expresses the total using modulus operations, thereby finding the corresponding index for each name in the array, also featuring methods for entry, searching, and printing. The ‘insert()’ function either places a new contact name-value pair entry or modifies any existing entry for a name that has previously been placed in the hash table, while ‘search()’ allows for quick retrieval for any name by linked lists at that particular index, found using the hash function. The ‘print_table()’ function gives a formatted perspective on the hash table for readability and display requirements. This code structure clearly applies fundamental concepts for effective use in hash tables, object-oriented programming, and linked lists for contact information storage and retrieval.
