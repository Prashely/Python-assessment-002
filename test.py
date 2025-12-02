sales_data = {"Alice": 5000, "Bob": 7500, "A": 7500, "Carol": 6000}
def get_top_seller(sales_data):
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
    return sorted_dict[-1][0]


print(get_top_seller(sales_data))