# ==========================================
# SECTION A: LIST PROCESSING
# ==========================================

def filter_sales_above_threshold(sales: list, threshold: int):
    """
    QUESTION 1
    ----------------------------------------
    Given a list of sales amounts (integers), return a NEW list containing 
    only values above the threshold.
    
    Example: filter_sales_above_threshold([100, 250, 75, 300], 150) → [250, 300]
    
    Logic:
    - Do NOT modify the original list
    - Return empty list if no values qualify
    - Use a loop or list comprehension
    """
    # TODO: Write your code here
    above_threshold = []
    for sale in sales:
        if sale > threshold:
            above_threshold.append(sale)
   
    return above_threshold


def count_product_codes(codes: list, prefix: str):
    """
    QUESTION 2
    ----------------------------------------
    Given a list of product codes (strings) and a prefix (string),
    count how many codes START with the given prefix (case-sensitive).
    
    Example: count_product_codes(["PROD-001", "PROD-002", "SERV-001"], "PROD") → 2
    
    Logic:
    - Return 0 if no matches found
    """
    # TODO: Write your code here
    counter = 0
    prefix_length = len(prefix)
    for product in codes:
        if product[0 : prefix_length] == prefix:
            counter += 1

    return counter
            


def calculate_moving_average(numbers: list, window_size: int):
    """
    QUESTION 3
    ----------------------------------------
    Calculate the average of the LAST window_size elements in the list.
    
    Example: calculate_moving_average([10, 20, 30, 40, 50], 3) → 40.0
    (average of last 3: 30, 40, 50)
    
    Logic:
    - If the list has fewer elements than window_size, use all available elements
    - Return the average as a float rounded to 2 decimal places
    - Return 0.0 for empty list
    """
    # TODO: Write your code here
    if window_size > len(numbers) and len(numbers) != 0:
        avg = sum(numbers) / len(numbers)
        return round(avg,2)
    
    elif window_size <= len(numbers) and len(numbers) != 0:
        avg = sum(numbers[ - window_size: ]) / window_size
        return round(avg,2)
    
    else:
        return 0.0
        


# ==========================================
# SECTION B: DICTIONARY OPERATIONS
# ==========================================

def get_top_seller(sales_data: dict):
    """
    QUESTION 4
    ----------------------------------------
    Given a dictionary where keys are employee names and values are sales totals,
    return the NAME of the employee with the highest sales.
    
    Example: {"Alice": 5000, "Bob": 7500, "Carol": 6000} → "Bob"
    
    Logic:
    - If dictionary is empty, return "No Data"
    - If there's a tie, return the name that appears first alphabetically
    """
    # TODO: Write your code here
    if not sales_data:
        return "No Data"
    
    sorted_dict = sorted(sales_data.items(), key = lambda x:(-x[1], x[0]))
    return sorted_dict[0][0]

def merge_inventory(warehouse_a: dict, warehouse_b: dict):
    """
    QUESTION 5
    ----------------------------------------
    Given two dictionaries representing product quantities in two warehouses,
    return a NEW dictionary with combined quantities for each product.
    
    Example:
    warehouse_a = {"PROD-001": 50, "PROD-002": 30}
    warehouse_b = {"PROD-002": 20, "PROD-003": 40}
    Result: {"PROD-001": 50, "PROD-002": 50, "PROD-003": 40}
    
    Logic:
    - If a product exists in only one warehouse, include it with its quantity
    - Return empty dictionary if both inputs are empty
    - Do NOT modify the original dictionaries
    """
    # TODO: Write your code here
    if not warehouse_a and not warehouse_b:
        return {}
    
    temp_dict = warehouse_a.copy()

    for key, value in warehouse_b.items():
        if key in temp_dict:
            temp_dict[key] += value
        else:
            temp_dict[key] = value

    return temp_dict


# ==========================================
# SECTION C: COMPLEX LOGIC & TDD
# ==========================================

def check_inventory_status(stock_level: int, reorder_point: int, max_capacity: int, daily_sales: int):
    """
    QUESTION 6 (THE INVENTORY MANAGER)
    ----------------------------------------
    Analyze inventory status based on multiple parameters.
    
    TODO: Using TDD, implement tests for the below functionality.
    Create `test_inventory.py` with class `TestInventory`.
    
    Parameters:
    - stock_level: Current units in stock
    - reorder_point: Threshold that triggers reorder
    - max_capacity: Maximum warehouse capacity
    - daily_sales: Average units sold per day
    
    Logic Tree:
    1. INPUT VALIDATION:
       - If ANY parameter is negative: return "Invalid Input"
       - If stock_level > max_capacity: return "Invalid Input"
       
    2. OVERSTOCKED:
       - If stock_level > (max_capacity * 0.9): return "OVERSTOCKED"
       
    3. CRITICAL (Urgent Reorder):
       - If stock_level < (reorder_point * 0.5): return "CRITICAL"
       
    4. REORDER NEEDED:
       - If stock_level <= reorder_point: return "REORDER"
       
    5. LOW STOCK (Warning):
       - If daily_sales > 0 AND stock_level / daily_sales < 7: return "LOW STOCK"
       
    6. OPTIMAL:
       - All other cases: return "OPTIMAL"
    """
    # TODO: Write your code here
    if stock_level < 0 or reorder_point < 0 or max_capacity < 0 or daily_sales < 0 or stock_level > max_capacity:
        return "Invalid Input"
    
    elif stock_level > (max_capacity * 0.9): 
        return "OVERSTOCKED"
    elif stock_level < (reorder_point * 0.5): 
        return "CRITICAL"
    elif stock_level <= reorder_point: 
        return "REORDER"
    elif daily_sales > 0 and stock_level / daily_sales < 7: 
        return "LOW STOCK"
    else:
        return "OPTIMAL"
        
    
    
    
