# Python Assignment — Part 3  
## Product Explorer & Error-Resilient Logger

This project demonstrates file handling, API integration, and exception handling in Python by building a small product explorer and logging system.


The program interacts with a public API, processes data, writes results to files, and handles errors gracefully. It simulates real-world application behavior with proper error handling and logging.


##  Tasks Implemented

### Task 1 — File Read & Write
- Created a file `python_notes.txt` and wrote multiple lines
- Appended additional lines to the file
- Read and displayed file content with line numbers
- Counted total number of lines
- Implemented keyword search (case-insensitive)


### Task 2 — API Integration
- Fetched product data from DummyJSON API
- Displayed product details in table format
- Filtered products with rating ≥ 4.5 and sorted by price
- Retrieved products by category (laptops)
- Sent a POST request to simulate product creation


### Task 3 — Exception Handling
- Implemented safe division function with error handling
- Built a safe file reader with try-except-finally
- Handled API errors such as connection issues and timeouts
- Added input validation for product lookup


### Task 4 — Logging System
- Created `error_log.txt` to log errors with timestamps
- Logged connection errors and HTTP errors
- Demonstrated logging by triggering errors intentionally
- Displayed log file content at the end


## Files Included

- `part3_api_files.py` → Main Python program
- `python_notes.txt` → Generated file from Task 1
- `error_log.txt` → Log file generated during execution
