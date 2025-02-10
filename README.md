# 📂 Folder Synchronizer

## 📖 Description

This program synchronizes two folders, ensuring that the replica folder is an identical copy of the source folder. It checks for differences between files and copies, updates, or removes them as needed. Additionally, it logs all changes in a log file.

## 🚀 Features

- Copies and updates modified files from the source folder to the replica folder.
- Removes files that are in the replica but not in the source.
- Maintains a detailed record of all performed actions.
- Performs synchronization at configurable intervals.

## 📌 Requirements

- Python 3.x

## ⚙️ How to Use

### 1️⃣ Install Python (if not already installed)

Download and install Python on your operating system: [Python Download](https://www.python.org/downloads/)

### 2️⃣ Run the program with the following arguments:

```sh
python teste.py <source_folder> <replica_folder> <interval> <log_file>
```

### 🔹 Example usage:

```sh
python teste.py /path/to/source /path/to/replica 60 sync.log
```

- `<source_folder>`: Path to the source folder.
- `<replica_folder>`: Path to the replica folder.
- `<interval>`: Synchronization interval in seconds.
- `<log_file>`: Path to the log file.

## 📝 Change Log

All performed changes are recorded in the specified log file.

## 🔍 Example Log Output:

```
[2025-02-10 12:00:00] Starting synchronization...
File copied/updated: /path/to/replica/file.txt
File removed: /path/to/replica/old_file.txt
[2025-02-10 12:00:05] Synchronization completed.
```

## 🛠️ Future Improvements

- Add support for different hash types (SHA-256, SHA-512).
- Implement a graphical user interface (GUI) for easier configuration.
- Create an option for bidirectional synchronization.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created by Simão Pires 🚀


