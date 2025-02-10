import os
import shutil
import hashlib
import time
import argparse
from datetime import datetime

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sync_folders(source, replica, log_file):
    with open(log_file, 'a') as log:
        log.write(f"\n[{datetime.now()}] Starting synchronization...\n")
        print(f"[{datetime.now()}] Starting synchronization...")
        
        if not os.path.exists(replica):
            os.makedirs(replica)
            log.write(f"Folder Created: {replica}\n")
            print(f"Folder Created: {replica}")

        source_files = {}
        for root, _, files in os.walk(source):
            for file in files:
                src_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_file_path, source)
                source_files[relative_path] = calculate_md5(src_file_path)

        replica_files = {}
        for root, _, files in os.walk(replica):
            for file in files:
                rep_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(rep_file_path, replica)
                replica_files[relative_path] = calculate_md5(rep_file_path)

        for relative_path, src_md5 in source_files.items():
            src_file_path = os.path.join(source, relative_path)
            rep_file_path = os.path.join(replica, relative_path)

            if (relative_path not in replica_files or
                    replica_files[relative_path] != src_md5):
                os.makedirs(os.path.dirname(rep_file_path), exist_ok=True)
                shutil.copy2(src_file_path, rep_file_path)
                log.write(f"File copied/updated: {rep_file_path}\n")
                print(f"File copied/updated: {rep_file_path}")

        for relative_path in set(replica_files) - set(source_files):
            rep_file_path = os.path.join(replica, relative_path)
            os.remove(rep_file_path)
            log.write(f"File removed: {rep_file_path}\n")
            print(f"File removed: {rep_file_path}")

        log.write(f"[{datetime.now()}] Synchronization completed.\n")
        print(f"[{datetime.now()}] Synchronization completed.")

def main():
    parser = argparse.ArgumentParser(description="Folder Synchronizer")
    parser.add_argument("source") # Source folder Path
    parser.add_argument("replica") # Replica Folder Path
    parser.add_argument("interval", type=int) # Synchronization interval in seconds
    parser.add_argument("log") # Log File Path
    args = parser.parse_args()

    while True:
        sync_folders(args.source, args.replica, args.log)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()