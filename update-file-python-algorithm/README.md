# Update a File Through a Python Algorithm

## Overview

Managing access to restricted resources is a routine task in cybersecurity. One common approach is maintaining an allow list that specifies which IP addresses are permitted to access sensitive systems or data. As these permissions change over time, manually updating the allow list can become repetitive and prone to mistakes.

In this project, I developed a Python script that automates this process. The script reads an existing allow list from a text file, compares it against a list of IP addresses that should no longer have access, removes those addresses, and writes the updated list back to the file.

This project demonstrates how Python can be used to automate security administration tasks while reducing the risk of human error.

---

## Project Objectives

The primary objectives of this project were to:

- Read an allow list from a text file
- Parse the file contents into a Python list
- Compare the allow list against a removal list
- Remove unauthorized IP addresses
- Update the original file with the revised allow list
- Package the logic into a reusable Python function

---

## Skills Demonstrated

- Python programming
- File handling
- Access control management
- Security automation
- List manipulation
- Conditional statements
- Loops and iteration
- Function development

---

## Technologies Used

- Python 3
- Text files
- File I/O
- Lists
- Built-in string methods

---

## Project Workflow

### Reading the Allow List

The script begins by opening the `allow_list.txt` file in read mode and loading its contents into memory.

```python
with open(import_file, "r") as file:
    ip_addresses = file.read()
```

---

### Parsing the Data

Since the file contents are initially stored as a string, the script converts them into a list so each IP address can be processed individually.

```python
ip_addresses = ip_addresses.split()
```

---

### Removing Unauthorized IP Addresses

Each IP address in the removal list is checked against the allow list. If a match is found, the address is removed.

```python
for element in ip_addresses:

    if element in remove_list:

        ip_addresses.remove(element)
```

---

### Preparing the Updated List

Once the unauthorized addresses have been removed, the remaining list is converted back into a string so it can be written to the file.

```python
ip_addresses = " ".join(ip_addresses)
```

---

### Updating the Allow List

Finally, the script overwrites the original file with the updated list of authorized IP addresses.

```python
with open(import_file, "w") as file:

    file.write(ip_addresses)
```

---

## Complete Function

```python
def update_file(import_file, remove_list):

    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for element in ip_addresses:

        if element in remove_list:

            ip_addresses.remove(element)

    ip_addresses = " ".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(ip_addresses)
```

---

## Why This Matters

Access control is a fundamental security principle. As users, systems, or devices are decommissioned, their access should be removed promptly to reduce unnecessary exposure.

Automating this process offers several benefits:

- Reduces manual administrative effort
- Minimizes human error
- Helps maintain accurate access control lists
- Supports the principle of least privilege
- Improves consistency when updating security records

Although this project uses a simple text file for demonstration purposes, the same concepts can be applied to firewall allow lists, VPN access controls, network ACLs, and other administrative security tasks.

---

## Lessons Learned

This project strengthened my understanding of:

- Reading and writing files with Python
- Parsing structured text data
- Working with Python lists
- Using loops and conditional statements to automate tasks
- Building reusable functions for security workflows
- Applying Python to solve practical cybersecurity problems

---

## Repository Structure

```
update-file-python-algorithm/
│
├── README.md
├── update_allow_list.py
---

## Future Improvements

Possible enhancements to this project include:

- Logging all removed IP addresses to an audit log
- Validating IP address formats before processing
- Reading allow and remove lists from CSV files
- Supporting IPv6 addresses
- Adding exception handling for missing or inaccessible files
- Creating a command-line interface for easier execution

---

## References

This project was completed as part of the Google Cybersecurity Professional Certificate and expanded with additional documentation to showcase practical Python automation skills for cybersecurity.
