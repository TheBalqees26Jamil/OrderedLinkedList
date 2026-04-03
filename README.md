# 🔗 Linked List Implementation in Python

## 📌 Overview

This project implements a **Singly Linked List** in Python with basic operations such as:

* Ordered insertion
* Deletion (Pop)
* Dynamic node creation

The list automatically maintains elements in **sorted order** during insertion.

---

## 🎯 Objective

The goal of this project is to understand how linked lists work internally and practice implementing core data structure operations from scratch.

---

## 🛠️ Technologies Used

* Python (No external libraries)

---

## ⚙️ Features

* Create nodes dynamically
* Insert elements in **sorted order**
* Prevent duplicate values
* Remove the last node (Pop operation)
* Interactive menu-driven program

---

## 🧠 How It Works

### 🔹 Node Structure

Each node contains:

* `number`: the stored value
* `next`: reference to the next node

---

### 🔹 Operations

#### 1. Ordered Insert

* Inserts a new node in the correct position
* Keeps the list sorted automatically
* Rejects duplicate values

#### 2. Pop

* Removes the **last node** from the list
* Handles edge cases:

  * Empty list
  * Single node list

-
## 💡 Example

### Insert nodes:

```
Enter number of nodes to create: 3
Node #1 → 5
Node #2 → 2
Node #3 → 7
```

### Result:

The list will be stored as:

```
2 → 5 → 7
```

### Pop:

```
This node's number deleted ----> 7
```

---

## 📁 Project Structure

```
OrderLinkedList/
│
├── main.py      # Implementation of linked list
└── README.md    # Documentation
```

---

## 🚀 Key Learning Points

* Understanding pointers (references)
* Recursive insertion
* Handling edge cases in data structures
* Building menu-driven CLI applications

---


## ⭐ Notes

* This is an educational project
* Can be extended with:

  * Display function (print list)
  * Search operation
  * Delete specific node
  * Doubly linked list implementation
