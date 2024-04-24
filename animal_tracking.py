import random
from shapely.geometry import Point,Polygon

def simulate_gps_data(area_polygon):
    """Simulate GPS data for an animal within the specified area."""
    min_x, min_y, max_x, max_y = area_polygon.bounds
    while True:
        # Generate random coordinates within the area bounds
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        point = Point(x, y)
        if area_polygon.contains(point):
            return point

if __name__ == "__main__":
    # Example area polygon (replace with actual area boundaries)
    area_polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])

    # Simulate GPS data for a single animal
    animal_position = simulate_gps_data(area_polygon)
    print("Initial Animal Position:", animal_position)
