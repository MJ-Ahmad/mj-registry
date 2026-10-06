import os
import sys
import shutil

def selective_file_ops(src_dir, dest_dir=None, files=None, move=False, delete=False):
    """
    src_dir: উৎস ডিরেক্টরি
    dest_dir: গন্তব্য ডিরেক্টরি (কপি/মুভের জন্য দরকার)
    files: নির্দিষ্ট ফাইলগুলোর লিস্ট
    move: True হলে ফাইলগুলো মুভ হবে
    delete: True হলে ফাইলগুলো ডিলেট হবে
    """

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    if not files:
        print("No specific files provided.")
        return

    if not delete:
        os.makedirs(dest_dir, exist_ok=True)

    for file_name in files:
        src_path = os.path.join(src_dir, file_name)

        if not os.path.exists(src_path):
            print(f"File not found: {src_path}")
            continue

        if delete:
            os.remove(src_path)
            print(f"Deleted: {src_path}")
        else:
            dest_path = os.path.join(dest_dir, file_name)
            if move:
                shutil.move(src_path, dest_path)
                print(f"Moved: {src_path} → {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} → {dest_path}")

    print("✅ Operation complete.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python selective_file_ops.py <src_dir> <dest_dir> <file1,file2,...> [--move] [--delete]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    files = sys.argv[3].split(",")

    move_flag = "--move" in sys.argv
    delete_flag = "--delete" in sys.argv

    selective_file_ops(src_dir, dest_dir, files, move=move_flag, delete=delete_flag)

