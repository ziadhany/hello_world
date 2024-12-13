import os
import random
import yaml  # Ensure you have PyYAML installed: pip install PyYAML

# Counter for file creation
c = 0

# Desired file size in KB
size_kb = 1

# Calculate the file size in bytes
file_size = size_kb

# Root directory
root_dir = "./"
os.makedirs(root_dir, exist_ok=True)

# Maximum directory depth
max_depth = 4096

# Function to create a deeply nested directory path
def create_nested_dirs(base_dir, depth):
    current_dir = base_dir
    for i in range(depth):
        current_dir = os.path.join(current_dir, f"{i}")
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
            
            # Generate random YAML content
            yaml_content = {
                "id": random.randint(0, 9999),
            }

            with open(current_dir + f".yaml", "w") as f:
                yaml.dump(yaml_content, f)
            
    return current_dir

# Generate the deepest directory structure
deepest_dir = create_nested_dirs(root_dir, max_depth)


