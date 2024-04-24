from shapely.geometry import Polygon

def get_polygon_coordinates():
    """Prompt the user to enter coordinates for a polygon."""
    coordinates = []
    while True:
        try:
            x = input("Enter x coordinate (or 'done' to finish): ")
            if x == 'done':
                break
            x = float(x)
            y = float(input("Enter y coordinate: "))
            coordinates.append((x, y))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Check if the number of coordinates is sufficient and if the polygon is closed
    if len(coordinates) < 4 or coordinates[0] != coordinates[-1]:
        print("Invalid input. Please ensure the polygon is closed and has at least 4 coordinates.")
        return None

    return coordinates

def get_village_boundaries(num_villages):
    """Take input for village boundaries and create buffer zones."""
    village_boundaries = []
    buffer_zones = []
    for i in range(1, num_villages + 1):
        print(f"Enter coordinates for Village {i} boundary:")
        coordinates = get_polygon_coordinates()
        if coordinates:
            village_boundary = Polygon(coordinates)
            village_boundaries.append(village_boundary)
            # Define buffer zone size (in meters)
            buffer_size = 100  # Adjust as needed
            buffer_zone = village_boundary.buffer(buffer_size)
            buffer_zones.append(buffer_zone)
    return village_boundaries, buffer_zones

if __name__ == "__main__":
    num_villages = int(input("Enter the number of village boundaries: "))
    village_boundaries, buffer_zones = get_village_boundaries(num_villages)
    print("Village boundaries:", village_boundaries)
    print("Buffer zones:", buffer_zones)
