# E-Commerce Order Processing System

## Project Overview

This project demonstrates an E-Commerce Order Processing System built in Python using a Singly Linked List data structure.

Customer orders are stored in the sequence they are received, and the system includes functionality to reverse the linked list so the newest orders can be processed first.

---

# Features

- Add orders to the linked list
- Display all stored orders
- Reverse the linked list in-place
- Unit testing with Python `unittest`
- Time and space complexity analysis

---

# Classes

## Order Class

Stores:

- Order ID
- Customer Name
- Order Details

## Node Class

Represents a single node in the linked list.

## SinglyLinkedList Class

Includes the following methods:

- `append()`
- `display()`
- `reverse()`

---

# Time Complexity

## append()

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## display()

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## reverse()

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

The reverse operation is efficient because it modifies node pointers directly without creating another list.

---

# Test Cases

## Normal Cases

1. Append multiple orders
2. Reverse the linked list
3. Display stored orders

## Edge Cases

1. Reverse an empty list
2. Reverse a single-node list
3. Display an empty list

---

# How to Run

## Run Main Program

```bash
python3 main.py
```

## Run Unit Tests

```bash
python3 -m unittest test_main.py
```

---

# Flowchart / Diagram Explanation

Orders are connected sequentially in the linked list.

### Before Reversal

```text
Head → Order1 → Order2 → Order3 → None
```

### After Reversal

```text
Head → Order3 → Order2 → Order1 → None
```

---

# Clarifying Questions

1. Should duplicate order IDs be permitted?
2. Should orders support deletion?
3. Should search functionality be added?
4. Should timestamps be stored with orders?
5. Should data persist in a database?
