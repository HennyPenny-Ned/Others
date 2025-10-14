import yaml
import os

try:
    with open("project_config.yml", "r") as f:
        config = yaml.safe_load(f)
        if config is None:
            raise ValueError("YAML file is empty or invalid.")
except Exception as e:
    print(f"Error loading YAML: {e}")
    exit(1)

# Create folders
for folder in config.get("folders", []):
    os.makedirs(folder, exist_ok=True)
    print(f"Generating {folder} folder...")

# Create files
for file in config.get("files", []):
    file_path = os.path.join(".", file)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    print(f"Generating {file} file...")
    with open(file_path, "w") as f:
        f.write("")  # Create empty file