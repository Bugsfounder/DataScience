import math

location = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6762, 139.6503),
}


def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # calculate distance
    distance = ((lat2 - lat1) ** 2) + ((lon2 - lon1) ** 2)

    distance = math.sqrt(distance)

    return distance


print(calculate_distance(location["London"], location["Tokyo"]))
