class DogNotFoundError(Exception):
    pass

def find_dog(dog_name):
    available_dogs = ["Buddy", "Max", "Bella"]
    
    if dog_name not in available_dogs:
        raise DogNotFoundError(f"{dog_name} is not available for adoption.")
    else:
        print(f"{dog_name} is ready for adoption!")

try:
    find_dog("Muffy")  # Change this input to test different outputs
except DogNotFoundError as e:
    print("Error:", e) 
