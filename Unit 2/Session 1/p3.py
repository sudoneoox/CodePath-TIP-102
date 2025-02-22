# Problem 3: Ticket Sales
#
# A dictionary ticket_sales is used to map ticket type to number of tickets sold.
# Return the total number of tickets of all types sold.
#

from typing import Dict


def total_sales(ticket_sales: Dict) -> int:
    # Empty dict is defined as None is python
    if ticket_sales is None:
        return 0
    return sum(ticket_sales.values())


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

print("Expected Output: 4500")
