import yaml
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "project_config.yml")

try:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        if config is None:
            raise ValueError("YAML file is empty or invalid.")
except Exception as e:
    print(f"Error loading YAML: {e}")
    exit(1)

# Base directory for the project template
base_dir = os.path.join(script_dir, "ProjectTemplate")

# Create folders
for folder in config.get("folders", []):
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Generating {folder_path} folder...")

# Create files
for file in config.get("files", []):
    file_path = os.path.join(base_dir, file)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    print(f"Generating {file_path} file...")
    with open(file_path, "w") as f:
        f.write("")  # Create empty file
