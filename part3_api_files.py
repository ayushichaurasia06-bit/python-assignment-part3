
# Part 3: File I/O, APIs & Exception Handling

import requests
from datetime import datetime


# Task 1 — File Read & Write

print("\n--- Task 1: File Operations ---")

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Write file
with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("File written successfully.")

# Append lines
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions improve code reusability.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")
print("Lines appended.")

# Read file
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\nNumbered Lines:")
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

print(f"\nTotal lines: {len(lines)}")

# Keyword search
keyword = input("\nEnter keyword to search: ").lower()
found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")


# Task 2 — API Integration

print("\n--- Task 2: API Integration ---")

def log_error(function_name, message):
    with open("error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR in {function_name}: {message}\n")

# Fetch products
try:
    response = requests.get("https://dummyjson.com/products?limit=20", timeout=5)
    data = response.json()["products"]

    print("\nID | Title | Category | Price | Rating")
    print("-" * 60)

    for p in data:
        print(f"{p['id']:2} | {p['title'][:20]:20} | {p['category']:12} | ${p['price']:7} | {p['rating']}")

    # Filter + sort
    filtered = [p for p in data if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\nFiltered (rating >= 4.5):")
    for p in filtered:
        print(f"{p['title']} - ${p['price']}")

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("fetch_products", "ConnectionError")

except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("fetch_products", "Timeout")

except Exception as e:
    print("Error:", e)
    log_error("fetch_products", str(e))

# Category search
try:
    response = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    laptops = response.json()["products"]

    print("\nLaptops:")
    for p in laptops:
        print(f"{p['title']} - ${p['price']}")

except Exception as e:
    print("Error:", e)
    log_error("fetch_laptops", str(e))

# POST request
try:
    response = requests.post(
        "https://dummyjson.com/products/add",
        json={
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "Test product"
        },
        timeout=5
    )

    print("\nPOST Response:")
    print(response.json())

except Exception as e:
    print("POST Error:", e)
    log_error("post_product", str(e))

# Task 3 — Exception Handling

print("\n--- Task 3: Exception Handling ---")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

# Input validation loop
while True:
    user_input = input("\nEnter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    pid = int(user_input)

    if pid < 1 or pid > 100:
        print("Out of range.")
        continue

    try:
        res = requests.get(f"https://dummyjson.com/products/{pid}", timeout=5)

        if res.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", f"404 for ID {pid}")
        else:
            product = res.json()
            print(product["title"], "-", product["price"])

    except Exception as e:
        print("Error:", e)
        log_error("lookup_product", str(e))

# Task 4 — Logging Demo

print("\n--- Task 4: Logging ---")

# Trigger connection error
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    print("Triggered connection error")
    log_error("test_connection", str(e))

# Trigger HTTP error
res = requests.get("https://dummyjson.com/products/999")

if res.status_code != 200:
    print("Triggered HTTP error")
    log_error("test_http", f"{res.status_code} for product 999")

# Print log file
print("\nError Log Content:")
with open("error_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
