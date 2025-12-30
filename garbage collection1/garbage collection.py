import gc
class Test:
    def __init__(self, value):
        self.value = value
        print(f"Object {self.value} created")

    def __del__(self):
        print(f"Object {self.value} deleted")

# # Enable garbage collection
gc.enable()

# # Create object
 
obj = Test(25)

# # Store object inside a list
container = [obj]

# # Remove references
del obj
container.clear()

print("Running garbage collector...")
collected = gc.collect()

print(f"Garbage collected objects: {collected}")


