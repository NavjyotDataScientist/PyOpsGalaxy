import os
import shutil

# ✅ CHANGE THIS TO YOUR REAL USERNAME
downloads_folder = r"/Users/navjyot/Downloads"
organized_folder = r"/Users/navjyot/Organized"

# Step 1: File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc",  ".xls", ".ppt","ipynb"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}

# Step 2: Create main folder
os.makedirs(organized_folder, exist_ok=True)

# Step 3: Create category folders
for folder in file_types:
    os.makedirs(os.path.join(organized_folder, folder), exist_ok=True)

# Create Others folder
others_folder = os.path.join(organized_folder, "Others")
os.makedirs(others_folder, exist_ok=True)

# Step 4: Move files safely
for filename in os.listdir(downloads_folder):
    source_path = os.path.join(downloads_folder, filename)

    # Skip folders
    if not os.path.isfile(source_path):
        continue

    file_ext = os.path.splitext(filename)[1].lower()
    moved = False

    for category, extensions in file_types.items():
        if file_ext in extensions:
            dest_path = os.path.join(organized_folder, category, filename)

            # Handle duplicate file names
            if os.path.exists(dest_path):
                name, ext = os.path.splitext(filename)
                dest_path = os.path.join(
                    organized_folder, category, f"{name}_copy{ext}"
                )

            try:
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename} → {category}")
            except Exception as e:
                print(f"Skipped: {filename} ({e})")

            moved = True
            break

    if not moved:
        dest_path = os.path.join(others_folder, filename)
        try:
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename} → Others")
        except Exception as e:
            print(f"Skipped: {filename} ({e})")

print("✅ Files organized successfully!")
