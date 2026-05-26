class Order:
    def __init__(self, order_id, customer_name, order_details):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_details = order_details

    def __str__(self):
        return (
            f"Order ID: {self.order_id}, "
            f"Customer: {self.customer_name}, "
            f"Details: {self.order_details}"
        )


class Node:
    def __init__(self, order):
        self.order = order
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add order to end of linked list
    def append(self, order):
        new_node = Node(order)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Display orders
    def display(self):
        orders = []

        current = self.head

        while current:
            orders.append(str(current.order))
            current = current.next

        return orders

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


# Main Program
if __name__ == "__main__":

    order_list = SinglyLinkedList()

    # Create orders
    order1 = Order(101, "Paulina", "Laptop")
    order2 = Order(102, "Maria", "Phone")
    order3 = Order(103, "Carlos", "Headphones")

    # Append orders
    order_list.append(order1)
    order_list.append(order2)
    order_list.append(order3)

    # Display before reversal
    print("Orders Before Reversal:")

    for order in order_list.display():
        print(order)

    # Reverse linked list
    order_list.reverse()

    # Display after reversal
    print("\nOrders After Reversal:")

    for order in order_list.display():
        print(order)
