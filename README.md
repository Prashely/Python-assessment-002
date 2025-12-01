# Python Assessment: Collection Processing & Algorithms

**Time Limit:** 90 Minutes
**Topic:** Python Lists, Dictionaries, Loops, Functions & Test Driven Development (TDD)

## 📋 Overview

Welcome to the **Data Analytics** assessment. You have been tasked with building analytics functions for a Sales Database, implementing statistical calculations, and creating a Smart Inventory System.

This is an **invigilated assessment**. You are required to demonstrate not just your ability to write code, but your ability to write **tests** for that code.

## 📂 File Structure

* `analytics.py` 📝 **(EDIT THIS)**
    * This file contains the empty functions you need to complete.
    * **Do not rename** any functions or the file itself.
* `test_inventory.py` 🆕 **(CREATE THIS)**
    * You must create this file from scratch.
    * This file will contain the Unit Tests for Question 6.

## 🚀 Instructions

### Section A: List Processing (Questions 1-3)
Work with lists of numbers and strings. You'll need loops, conditionals, and list methods.

### Section B: Dictionary Operations (Questions 4-5)
Process dictionaries representing real-world data. Requires iteration, key-value manipulation, and aggregation.

### Section C: The Inventory Manager (Question 6)
**This section requires Test Driven Development (TDD).**

1. Read the requirements for `check_inventory_status` in `analytics.py`.
2. **BEFORE** you write the logic, create a new file named `test_inventory.py`.
3. Implement the `TestInventory` class and write tests for all scenarios.
4. Once your tests are written, go back to `analytics.py` and write the code to pass them.

## 🧪 How to Run Your Tests

```bash
python test_inventory.py
```

---

## 📝 Question Details

### SECTION A: List Processing

**Question 1: `filter_sales_above_threshold(sales: list, threshold: int)`**
- Given a list of sales amounts (integers), return a NEW list containing only values above the threshold
- Do NOT modify the original list
- Example: `filter_sales_above_threshold([100, 250, 75, 300], 150)` → `[250, 300]`
- Return empty list if no values qualify

**Question 2: `count_product_codes(codes: list, prefix: str)`**
- Given a list of product codes (strings) and a prefix (string)
- Count how many codes START with the given prefix (case-sensitive)
- Example: `count_product_codes(["PROD-001", "PROD-002", "SERV-001"], "PROD")` → `2`
- Return `0` if no matches found

**Question 3: `calculate_moving_average(numbers: list, window_size: int)`**
- Calculate the average of the LAST `window_size` elements in the list
- Example: `calculate_moving_average([10, 20, 30, 40, 50], 3)` → `40.0` (average of 30, 40, 50)
- If the list has fewer elements than window_size, use all available elements
- Return the average as a float rounded to 2 decimal places
- Return `0.0` for empty list

### SECTION B: Dictionary Operations

**Question 4: `get_top_seller(sales_data: dict)`**
- Given a dictionary where keys are employee names and values are sales totals
- Example: `{"Alice": 5000, "Bob": 7500, "Carol": 6000}`
- Return the NAME of the employee with the highest sales
- If dictionary is empty, return `"No Data"`
- If there's a tie, return the name that appears first alphabetically

**Question 5: `merge_inventory(warehouse_a: dict, warehouse_b: dict)`**
- Given two dictionaries representing product quantities in two warehouses
- Keys are product IDs (strings), values are quantities (integers)
- Return a NEW dictionary with combined quantities for each product
- Example:
  ```python
  warehouse_a = {"PROD-001": 50, "PROD-002": 30}
  warehouse_b = {"PROD-002": 20, "PROD-003": 40}
  # Result: {"PROD-001": 50, "PROD-002": 50, "PROD-003": 40}
  ```
- If a product exists in only one warehouse, include it with its quantity
- Return empty dictionary if both inputs are empty

### SECTION C: Inventory Management (TDD)

**Question 6: `check_inventory_status(stock_level: int, reorder_point: int, max_capacity: int, daily_sales: int)`**

Create `test_inventory.py` with class `TestInventory` and implement tests FIRST.

**Parameters:**
- `stock_level`: Current units in stock
- `reorder_point`: Threshold that triggers reorder
- `max_capacity`: Maximum warehouse capacity
- `daily_sales`: Average units sold per day

**Logic Tree:**

1. **INPUT VALIDATION:**
   - If ANY parameter is negative: return `"Invalid Input"`
   - If stock_level > max_capacity: return `"Invalid Input"`

2. **OVERSTOCKED:**
   - If stock_level > (max_capacity * 0.9): return `"OVERSTOCKED"`
   - This means stock is above 90% of capacity

3. **CRITICAL (Urgent Reorder):**
   - If stock_level < (reorder_point * 0.5): return `"CRITICAL"`
   - This means stock is below 50% of the reorder point

4. **REORDER NEEDED:**
   - If stock_level <= reorder_point: return `"REORDER"`

5. **LOW STOCK (Warning):**
   - If daily_sales > 0 AND stock_level / daily_sales < 7: return `"LOW STOCK"`
   - This means stock will run out in less than 7 days at current sales rate
   - Handle division by zero (if daily_sales is 0, skip this check)

6. **OPTIMAL:**
   - All other cases: return `"OPTIMAL"`

**Example Test Cases to Include:**
- Negative values
- Stock exactly at reorder point
- Stock at exactly 90% capacity
- Zero daily sales
- Stock level exactly 6.9 days worth
- Stock level exactly 7 days worth

---

## ⚠️ Important Notes

- Use list comprehensions where appropriate (but loops are acceptable)
- Do NOT use external libraries (no `numpy`, `pandas`, etc.)
- Dictionary iteration: use `.items()`, `.keys()`, `.values()` as needed
- For Question 6, test ALL edge cases and boundary conditions
- Round floating point results to 2 decimal places where specified
- Do NOT modify input parameters unless explicitly told to

---

## 📊 Grading Breakdown

- Section A (Q1-Q3): 30 points (10 each)
- Section B (Q4-Q5): 30 points (15 each)
- Section C (Q6): 40 points
  - Test file creation: 10 points
  - Test coverage: 15 points
  - Function implementation: 15 points

**Total: 100 points**

Good luck! 
