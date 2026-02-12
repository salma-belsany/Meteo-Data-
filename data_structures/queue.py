class Queue:
    """File pour gérer les extractions API/CSV (FIFO)"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Ajoute en fin de file"""
        self.items.append(item)
        return True
    
    def dequeue(self):
        """Retire du début de file"""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        """Vérifie si la file est vide"""
        return len(self.items) == 0
    
    def size(self):
        """Taille de la file"""
        return len(self.items)
    
    def peek(self):
        """Premier élément sans le retirer"""
        if self.is_empty():
            return None
        return self.items[0]
