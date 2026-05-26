import unittest
from main import Order, SinglyLinkedList


class TestOrderProcessing(unittest.TestCase):

    # Normal Case 1
    def test_append_orders(self):
        linked_list = SinglyLinkedList()

        linked_list.append(Order(1, "Alice", "Keyboard"))
        linked_list.append(Order(2, "Bob", "Mouse"))

        self.assertEqual(len(linked_list.display()), 2)

    # Normal Case 2
    def test_reverse_orders(self):
        linked_list = SinglyLinkedList()

        linked_list.append(Order(1, "Alice", "Keyboard"))
        linked_list.append(Order(2, "Bob", "Mouse"))

        linked_list.reverse()

        orders = linked_list.display()

        self.assertIn("Bob", orders[0])

    # Normal Case 3
    def test_display_orders(self):
        linked_list = SinglyLinkedList()

        linked_list.append(Order(1, "Alice", "Keyboard"))

        orders = linked_list.display()

        self.assertEqual(len(orders), 1)

    # Edge Case 1
    def test_reverse_empty_list(self):
        linked_list = SinglyLinkedList()

        linked_list.reverse()

        self.assertEqual(linked_list.display(), [])

    # Edge Case 2
    def test_reverse_single_order(self):
        linked_list = SinglyLinkedList()

        linked_list.append(Order(1, "Alice", "Keyboard"))

        linked_list.reverse()

        orders = linked_list.display()

        self.assertEqual(len(orders), 1)

    # Edge Case 3
    def test_display_empty_list(self):
        linked_list = SinglyLinkedList()

        self.assertEqual(linked_list.display(), [])


if __name__ == "__main__":
    unittest.main()
