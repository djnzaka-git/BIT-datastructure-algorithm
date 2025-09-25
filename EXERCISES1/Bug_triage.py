
# Project 102: Bug Report Triage
# BIT Department – Sept 2025

import array   # for fixed-size arrays


# 1. INTEGERS: Generate or input values
bug_counts = [12, 25, 8, 15, 30]  # Example bug counts from different modules

total_bugs = sum(bug_counts)
average_bugs = total_bugs / len(bug_counts)
min_bugs = min(bug_counts)
max_bugs = max(bug_counts)


# 2. STRINGS: Formatted report with f-strings
report = (
    f"Bug Report Triage Summary\n"
    f"Total Bugs: {total_bugs}\n"
    f"Average Bugs per Module: {average_bugs:.2f}\n"
    f"Minimum Bugs: {min_bugs}\n"
    f"Maximum Bugs: {max_bugs}\n"
)
print(report)


# 3. BOOLEANS: Apply threshold condition
threshold = 18
status = "Above Standard" if (average_bugs > threshold and max_bugs > 20) else "Below Standard"
print(f"Status: {status}")


# 4. LISTS: Add, remove, sort, and display
bug_list = ["UI Bug", "Crash Issue", "Performance Lag", "Security Flaw"]
print("\nOriginal Bug List:", bug_list)

bug_list.append("Memory Leak")              # Add
if "Performance Lag" in bug_list:           # Remove
    bug_list.remove("Performance Lag")
bug_list = sorted(set(bug_list))            # Sort + remove duplicates
print("Updated Bug List:", bug_list)


# 5. ARRAYS: Using 'array' module
bug_array = array.array("i", bug_counts)
print(f"\nSum from Array: {sum(bug_array)}")


# 6. DICTIONARIES: List of records
bug_records = [
    {"id": 1, "name": "UI Bug", "value": 10},
    {"id": 2, "name": "Crash Issue", "value": 20},
    {"id": 3, "name": "Performance Lag", "value": 15},
]

bug_records[0]["value"] = 12                              # Update one record
bug_records = [rec for rec in bug_records if rec["id"] != 2]  # Delete id=2

total_value = sum(rec["value"] for rec in bug_records)    # Compute total
print("\nUpdated Bug Records:", bug_records)
print("Total Value across records:", total_value)
