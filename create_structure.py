import os

def create_project_structure():
    # Define the directory structure
    directories = [
        'src',
        'src/data',
        'src/models',
        'src/strategies',
        'src/utils',
        'src/api',
        'src/dashboard',
        'tests',
        'config',
        'logs'
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create an empty __init__.py file in each directory
        with open(os.path.join(directory, '__init__.py'), 'w') as f:
            pass
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
