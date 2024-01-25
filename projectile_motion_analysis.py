import math
import pandas as pd
import matplotlib.pyplot as plt

class ProjectileMotion:
    def __init__(self, planet_gravities=None):
        # Initialize the ProjectileMotion class with a list of planet gravities
        self.planets_gravities = planet_gravities or [3.7, 8.87, 9.8, 3.71, 24.79, 10.44, 8.87, 11.15]
        # Initialize variables to store user input and calculated values
        
    def get_user_input(self):
        # Get user input for the planet, initial height, initial velocity, launch angle
        g = int(input("Select the planet your object is at:\n "
                      "1. Mercury\n 2. Venus\n 3. Earth\n 4. Mars\n 5. Jupiter\n "
                      "6. Saturn\n 7. Uranus\n 8. Neptune\n")) - 1  # Subtract 1 to match the list index
        initial_height = float(input("Initial height: "))
        initial_velocity = float(input("Initial velocity: "))
        launch_angle = float(input("Launch angle: "))
        gravitational_acceleration = self.planets_gravities[g]

        return initial_height, initial_velocity, launch_angle, gravitational_acceleration
    
    def validate_input(self, initial_velocity, initial_height, launch_angle, gravitational_acceleration):
        # Validate the user input to ensure it meets the required criteria
        if not all(isinstance(val, (int, float)) for val in [initial_velocity, initial_height, launch_angle, gravitational_acceleration]):
            raise ValueError("All inputs must be numeric (int or float).")
        
        if any(val < 0 for val in [initial_velocity, initial_height]):
            raise ValueError("Initial velocity and height cannot be negative.")
        
        if not (0 <= launch_angle <= 90):
            raise ValueError("Launch angle must be between 0 and 90 degrees.")
    
    def calculate_trajectory(self, initial_velocity, initial_height, launch_angle, gravitational_acceleration):
        # Calculate the trajectory using physics equations
        theta = math.radians(launch_angle)
        time_of_flight = (2 * initial_velocity * math.sin(theta)) / gravitational_acceleration
        max_height = (initial_velocity ** 2 * (math.sin(theta)) ** 2) / (2 * gravitational_acceleration) + initial_height
        horizontal_reach = initial_velocity * math.cos(theta) * time_of_flight
        time_intervals = 100  # Increase this value for smoother trajectory
        delta_t = time_of_flight / time_intervals
        trajectory_x = []
        trajectory_y = []

        # Calculate trajectory points at different time intervals
        for t in range(time_intervals + 1):
            x = initial_velocity * math.cos(theta) * t * delta_t
            y = initial_height + initial_velocity * math.sin(theta) * t * delta_t - 0.5 * gravitational_acceleration * (t * delta_t) ** 2
            trajectory_x.append(x)
            trajectory_y.append(y)

        return time_of_flight, max_height, horizontal_reach, trajectory_x, trajectory_y

    def display_results(self, time_of_flight, max_height, horizontal_reach, trajectory_x, trajectory_y):
        # Display the simulation results and plot the trajectory
        print(f"Time of flight: {time_of_flight} seconds")
        print(f"Maximum Height: {max_height} meters")
        print(f"Horizontal Reach: {horizontal_reach} meters")

        # Plotting the trajectory
        plt.figure(figsize=(8, 6))
        plt.plot(trajectory_x, trajectory_y)
        plt.title('Projectile Motion')
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Distance (m)')
        plt.grid(True)
        plt.show()

    def run_simulation(self):
        # Run the entire simulation process
        initial_height, initial_velocity, launch_angle, gravitational_acceleration = self.get_user_input()
        self.validate_input(initial_velocity, initial_height, launch_angle, gravitational_acceleration)
        time_of_flight, max_height, horizontal_reach, trajectory_x, trajectory_y = self.calculate_trajectory(
            initial_velocity, initial_height, launch_angle, gravitational_acceleration
        )
        self.display_results(time_of_flight, max_height, horizontal_reach, trajectory_x, trajectory_y)

def main():
    # Create an instance of the ProjectileMotion class
    # Implement user interface to allow multiple simulations and comparisons
    projectile_motion = ProjectileMotion()

    # Run the simulation
    projectile_motion.run_simulation()

if __name__ == "__main__":
    main()
