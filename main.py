from animal_tracking import simulate_gps_data
from village_input import get_village_boundaries
from shapely.geometry import Polygon
import time
# Import the send_email_notification function
from send_email_notification import send_email_notification

def check_buffer_zone(animal_position, buffer_zones):
    """Check if the animal position is within any buffer zone."""
    for index, zone in enumerate(buffer_zones, start=1):
        if zone.contains(animal_position):
            return index
    return None

if __name__ == "__main__":
    # Example area polygon (replace with actual area boundaries)
    area_polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])

    # Get village boundaries and buffer zones
    num_villages = int(input("Enter the number of village boundaries: "))
    village_boundaries, buffer_zones = get_village_boundaries(num_villages)

    # Track animal movements
    while True:
        # Simulate GPS data for each animal
        animal_positions = [simulate_gps_data(area_polygon) for _ in range(len(village_boundaries))]

        # Check if any animal enters the buffer zone of a village boundary
        for i, animal_position in enumerate(animal_positions, start=1):
            village_number = check_buffer_zone(animal_position, buffer_zones)
            if village_number:
                message = f"Animal {i} entered Buffer Zone of Village {village_number}!"
                send_email_notification("01projectautomation@gmail.com", "prasannack1001@gmail.com", "Animal Alert",
                                        message, "smtp.gmail.com", 587, "01projectautomation@gmail.com",
                                        "ityi fwtt rzzp azre")
                # break
        # Delay for 5 seconds before updating positions again
        time.sleep(5)
