"""Tests unitaires File"""
from data_structures.queue import Queue

def test_queue_enqueue():
    q = Queue()
    q.enqueue("station42")
    assert len(q.items) == 1  # Couvre ligne append()

def test_queue_dequeue():
    q = Queue()
    q.enqueue("test")
    result = q.dequeue()
    assert result == "test"
    assert q.is_empty()  # Couvre ligne pop(0)

def test_queue_size():
    q = Queue()
    q.enqueue("1")
    q.enqueue("2")
    assert q.size() == 2  # Couvre ligne len()

def test_queue_peek():
    q = Queue()
    q.enqueue("test")
    assert q.peek() == "test"  # Couvre ligne items[0]

def test_queue_empty_dequeue():
    """Test dequeue file vide"""
    q = Queue()
    assert q.dequeue() is None  # Couvre ligne 15

def test_queue_peek_empty():
    """Test peek file vide""" 
    q = Queue()
    assert q.peek() is None  # Couvre ligne 29