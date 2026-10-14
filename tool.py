import hashlib
import os
import json

HASH_FILE = "file_hashes.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    return {}


def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


def register_file():
    filepath = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(filepath):
        print("Error: File not found!")
        return
import hashlib
import os
import json

HASH_FILE = "file_hashes.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    return {}


def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


def register_file():
    filepath = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(filepath):
        print("Error: File not found!")
        return

    hashes = load_hashes()
hashes[os.path.abspath(filepath)] = calculate_hash(filepath)
    save_hashes(hashes)

    print("File registered successfully!")
    print("SHA-256 hash:", hashes[os.path.abspath(filepath)])


def check_file():
    filepath = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(filepath):
        print("Error: File not found!")
        return

    hashes = load_hashes()
    filepath = os.path.abspath(filepath)

    if filepath not in hashes:
        print("File not registered. Register it first.")
        return

    current_hash = calculate_hash(filepath)

    if current_hash == hashes[filepath]:
        print("INTEGRITY VERIFIED: File is unchanged.")
    else:
        print("WARNING: File has been modified!")
        print("Expected hash:", hashes[filepath])
        print("Current hash: ", current_hash)


def main():
    while True:
        print("\n===== FILE INTEGRITY CHECKER =====")
        print("1. Register file")
        print("2. Check file integrity")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_file()
        elif choice == "2":
            check_file()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
