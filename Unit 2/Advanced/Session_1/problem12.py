from typing import Dict


def num_of_time_portals(portals, destination):
    sum: int = 0
    size: int = len(portals)
    for i in range(0, size):
        for j in range(0, size):
            if (portals[i] + portals[j]) == destination and i != j:
                sum += 1
    return sum


portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
