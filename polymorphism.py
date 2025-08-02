# Define different vehicle types with their own move behavior
class ToyotaCar:
    def move(self):
        print("🚗 Toyota car is driving on the highway.")

class YamahaBike:
    def move(self):
        print("🏍️ Yamaha bike is pedaling through the streets.")

class VolvoBus:  
    def move(self):
        print("🚌 Volvo bus is rolling down the road.")

# This function accepts any vehicle object and calls its move method
def start_moving(vehicle):
    print("Starting the vehicle...")
    vehicle.move()  # Polymorphism: calls the specific vehicle's move method
    print("-" * 40)  # Separator for clarity

# Create instances of each vehicle
toyota = ToyotaCar()
yamaha = YamahaBike()
volvo = VolvoBus() 

# Call the same function with different vehicle objects
start_moving(toyota)   # Calls ToyotaCar's move()
start_moving(yamaha)   # Calls YamahaBike's move()
start_moving(volvo)    # Calls VolvoBus's move()

