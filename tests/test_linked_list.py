"""Tests unitaires Liste Chaînée"""
from data_structures.linked_list import LinkedList

def test_linked_list_append():
    """Test ajout élément"""
    ll = LinkedList()
    station = {"id_nom": "test", "id_numero": 99, "ville": "Test"}
    ll.append(station)
    assert len(ll) == 1

def test_linked_list_display():
    """Test affichage """
    ll = LinkedList()
    ll.append({"id_nom": "test1", "id_numero": 1, "ville": "Toulouse"})
    ll.append({"id_nom": "test2", "id_numero": 2, "ville": "Toulouse"})
    # L'affichage ne lève pas d'erreur
    ll.display()
