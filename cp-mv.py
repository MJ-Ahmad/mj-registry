import os
import sys
import shutil

def move_or_copy_files(src_dir, dest_dir, move=False, remove=False):
    """
    src_dir: উৎস ডিরেক্টরি
    dest_dir: গন্তব্য ডিরেক্টরি
    move: True হলে ফাইলগুলো মুভ হবে, False হলে কপি হবে
    remove: True হলে src_dir থেকে ফাইলগুলো রিমুভ হবে (কপি করার পর)
    """

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    os.makedirs(dest_dir, exist_ok=True)

    files = os.listdir(src_dir)
    if not files:
        print("No files found in source directory.")
        return

    for file_name in files:
        src_path = os.path.join(src_dir, file_name)
        dest_path = os.path.join(dest_dir, file_name)

        if os.path.isfile(src_path):
            if move:
                shutil.move(src_path, dest_path)
                print(f"Moved: {src_path} → {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} → {dest_path}")

            if remove and not move:
                os.remove(src_path)
                print(f"Removed original: {src_path}")

    print("✅ Operation complete.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python move_copy_files.py <src_dir> <dest_dir> [--move] [--remove]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    move_flag = "--move" in sys.argv
    remove_flag = "--remove" in sys.argv

    move_or_copy_files(src_dir, dest_dir, move=move_flag, remove=remove_flag)

