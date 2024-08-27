


**Usage Instructions**

- 1 Start the system: Run start.py to initialize the Dynamic Multiprocessing system.
- 2 Prepare your module: Create a Python file (.py) with the following structure:
```
def start(shared_dict):
    print("I can see", shared_dict)  # Optional: for debugging
    # Your module logic here

if __name__ == '__main__':
    from os.path import basename
    from engine._mod_ import update
    update(basename(__file__), 'upload')  # Use 'delete' to remove the module
```
- 3 Add your module: Upload your Python file to the pool folder.
- 4 Activate your module: Run your Python file to register it with the system.
