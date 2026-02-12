class Node:
    """Noeud d'une liste chaînée"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Liste chaînée pour l'affichage des stations météo"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Ajoute un élément en fin de liste"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
    
    def display(self):
        """Affiche toutes les stations"""
        if not self.head:
            print("Liste vide")
            return
        
        print("-" * 60)
        print(f"{'#':<3} {'Nom Station':<75} {'Ville':<15}")
        print("-" * 60)
        
        current = self.head
        count = 1
        while current:
            station = current.data
            num = station.get('id_numero', 'N/A')
            name = str(station.get('id_nom', 'N/A'))[:85]
            ville = station.get('ville', 'N/A')
            print(f"{count:<3} {name:<75} {ville:<15}")
            current = current.next
            count += 1
        print("-" * 60)

    def __len__(self):
        return self.size
