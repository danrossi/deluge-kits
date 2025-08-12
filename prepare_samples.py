from pathlib import Path
import os

def prepare_samples(root_dir):
    root_path = Path(root_dir)
    for file_path in root_path.rglob("*"): # Recursively finds all files and directories
        if file_path.is_dir():
            try:
                Path(os.path.join(file_path,".gitkeep")).touch()
            except OSError as e:
                print(f"Error touching {file_path}: {e}")

prepare_samples("SAMPLES")