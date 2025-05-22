# MySQL User Data Seeder

This script (`seed.py`) automates the process of creating a MySQL database, setting up a `user_data` table, and populating it with user information from a CSV file.

## Features

- Connects to a local MySQL server.
- Creates a database named `ALX_prodev` if it does not exist.
- Creates a `user_data` table with fields: `user_id`, `name`, `email`, and `age`.
- Reads user data from a CSV file (`user_data.csv`).
- Inserts user data into the table, skipping duplicate emails.

## Requirements

- Python 3.10+
- MySQL server running locally
- Python packages:
  - `mysql-connector-python`
  - `csv` (standard library)
  - `uuid` (standard library)

## Usage

1. **Install dependencies:**
   ```sh
   pip install mysql-connector-python
   ```

2. **Prepare your CSV file:**
   - Place a `user_data.csv` file in the same directory as `seed.py`.
   - The CSV should have a header row: `name,email,age`
   - Example:
     ```
     name,email,age
     John Doe,john@example.com,30
     Jane Smith,jane@example.com,25
     ```

3. **Edit database credentials:**
   - Update the `user` and `password` fields in [`seed.py`](python-generators-0x00/seed.py) to match your MySQL setup.

4. **Run the script:**
   ```sh
   python seed.py
   ```

## Notes

- The script skips inserting users with duplicate emails.
- Make sure your MySQL server is running and accessible.

