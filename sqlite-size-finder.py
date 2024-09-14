import os
import sqlite3

def get_size(start_path):
    """Calculate the total size of all files in a directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Check if the file exists to avoid broken symbolic links
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    """Format size in GB if it exceeds 1 GB, otherwise in MB."""
    size_gb = size / (1024 * 1024 * 1024)
    if size_gb >= 1:
        return f"{size_gb:.2f} GB"
    else:
        size_mb = size / (1024 * 1024)
        return f"{size_mb:.2f} MB"

def create_database(db_path):
    """Create or overwrite an SQLite database and a table for folder sizes."""
    # Check if the database already exists, and remove it if it does
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Existing database {db_path} removed.")

    # Create the new database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE folder_sizes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            folder_name TEXT NOT NULL,
            size TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"New database {db_path} created.")

def insert_data(db_path, data):
    """Insert folder size data into the database."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany('''
        INSERT INTO folder_sizes (folder_name, size)
        VALUES (?, ?)
    ''', data)
    conn.commit()
    conn.close()

def list_folder_sizes(path, db_path):
    folder_sizes = []
    
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            size = get_size(folder_path)
            size_str = format_size(size)
            size_gb = size / (1024 * 1024 * 1024)  # Store size in GB for sorting
            folder_sizes.append((folder_name, size_str, size_gb))
    
    # Sort folders by size in GB (third element in the tuple)
    folder_sizes.sort(key=lambda x: x[2], reverse=True)
    
    # Remove size in GB from the tuple for insertion into the database
    folder_sizes = [(folder, size_str) for folder, size_str, _ in folder_sizes]
    
    # Create or overwrite the database and insert data
    create_database(db_path)
    insert_data(db_path, folder_sizes)

# Path to your folder
folder_path = r"C:\Users\sherwin\OneDrive - University of Perpetual Help System JONELTA"

# Path to the SQLite database file
db_path = r"C:\Users\sherwin\Desktop\pokemon-terminal-based-battle-system\!fl sutdio.db"

# List folder sizes and export to an SQLite database
list_folder_sizes(folder_path, db_path)
