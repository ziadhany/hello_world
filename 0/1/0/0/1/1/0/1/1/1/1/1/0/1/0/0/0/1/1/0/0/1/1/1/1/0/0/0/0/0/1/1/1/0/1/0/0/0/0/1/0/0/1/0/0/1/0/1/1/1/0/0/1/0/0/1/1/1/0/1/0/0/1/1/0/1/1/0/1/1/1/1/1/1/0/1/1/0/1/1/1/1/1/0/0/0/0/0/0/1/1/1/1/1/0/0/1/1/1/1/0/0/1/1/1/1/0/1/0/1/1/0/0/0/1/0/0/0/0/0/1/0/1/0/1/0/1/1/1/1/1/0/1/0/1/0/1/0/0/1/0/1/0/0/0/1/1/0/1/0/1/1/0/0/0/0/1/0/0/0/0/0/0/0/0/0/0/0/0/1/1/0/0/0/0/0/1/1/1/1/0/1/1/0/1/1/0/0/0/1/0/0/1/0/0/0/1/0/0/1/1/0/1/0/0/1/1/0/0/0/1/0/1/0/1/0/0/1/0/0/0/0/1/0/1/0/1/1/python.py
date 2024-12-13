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
        try:
            current_dir = os.path.join(current_dir, f"{random.randint(0, 1)}")
            if not os.path.exists(current_dir):
                os.makedirs(current_dir)
        except:
            pass
            break
    return current_dir

# Generate the deepest directory structure
deepest_dir = create_nested_dirs(root_dir, max_depth)

# Generate 10,000 files at the deepest directory
while c < 5:
    # Generate random YAML content
    yaml_content = {
        "id": random.randint(1000, 9999),
        "name": f"RandomName{random.randint(1, 100)}",
        "attributes": {
            "color": random.choice(["red", "blue", "green", "yellow"]),
            "size": random.choice(["small", "medium", "large"]),
            "price": random.randint(10, 100),
        },
        "tags": [f"tag{random.randint(1, 10)}" for _ in range(random.randint(2, 5))],
    }

    # Generate a unique final file path
    final_path = os.path.join(deepest_dir, f".")

    # Write the YAML content to the file
    with open(final_path, "w") as f:
        yaml.dump(yaml_content, f)

    c += 1
