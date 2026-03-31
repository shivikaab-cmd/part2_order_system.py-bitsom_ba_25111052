# Python Assignment – Part 2: Data Structures (Order Management System)

## Overview

This project is part of my Python learning journey and focuses on understanding data structures such as lists and dictionaries.

In this assignment, I built a simple Order Management System that stores and manages customer orders. This helped me understand how real-world data is handled in Python programs.

---

## Objective

The main objective of this project is to:

- Learn how to use lists and dictionaries in Python
- Store structured data in an organized way
- Perform operations like adding, searching, and displaying data
- Apply loops and conditionals in a real-world scenario

---

## Problem Statement

The task is to create a simple system that manages customer orders.

Each order should contain:

- Order ID
- Customer Name
- List of Items purchased
- Total Price of the order

The program should allow the user to:

1. Add new orders  
2. View all orders  
3. Search for an order using Order ID  
4. Calculate total revenue from all orders  

---

## Approach

To solve this problem, I used the following approach:

1. Created an empty list to store all orders  
2. Used dictionaries to store each order's details  
3. Used a loop to allow continuous user interaction  
4. Applied conditional statements to perform different operations  

---

## Data Structures Used

### List
- Used to store multiple orders  
- Example:
  orders = []

### Dictionary
- Used to store details of each order  
- Example:
  order = {
      "order_id": 101,
      "customer_name": "John",
      "items": ["Pen", "Notebook"],
      "total": 200
  }

---

## Features Implemented

### Add Order
- User enters order details
- Data is stored in dictionary format
- Dictionary is added to the orders list

### View Orders
- Loop through the list
- Display each order clearly

### Search Order
- User enters Order ID
- Program checks each order
- Displays matching order

### Total Revenue
- Loop through all orders
- Add total values
- Display final revenue

---

## How to Run the Program

1. Open the project folder in VS Code  
2. Open the terminal  
3. Run the following command:

python part2_order_system.py

4. Follow the instructions shown in the terminal  

---

## Sample Flow

1. User selects "Add Order"  
2. Enters order details  
3. Order gets saved  
4. User selects "View Orders"  
5. All orders are displayed  

---

## Learning Outcomes

Through this assignment, I learned:

- How to use lists to store multiple data entries  
- How to use dictionaries to structure data  
- How to combine loops and conditions effectively  
- How real-world systems manage and process data  
- How to write clean and readable Python code  

---

## File Structure

python-assignment-part2/
│── part2_order_system.py
│── README.md

---

## Conclusion

This assignment helped me understand how Python data structures are used to build real-world applications. It improved my confidence in working with lists, dictionaries, and basic program logic.