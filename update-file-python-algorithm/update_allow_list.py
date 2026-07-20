"""
update_allow_list.py

Author: Cornelius Donkor
Repository: cybersecurity-projects

Description:
This script automates the process of updating an IP allow list by
removing IP addresses that should no longer have access to restricted
resources.

Workflow:
1. Read the allow list from a text file.
2. Convert the contents into a Python list.
3. Remove unauthorized IP addresses.
4. Write the updated allow list back to the file.

This project demonstrates practical Python automation for
cybersecurity administration tasks.
"""


def update_allow_list(import_file, remove_list):
    """
    Updates an allow list by removing specified IP addresses.

    Args:
        import_file (str):
            Path to the allow list text file.

        remove_list (list):
            List of IP addresses to remove.

    Returns:
        int:
            Number of IP addresses removed.
    """

    try:
        # Read allow list
        with open(import_file, "r") as file:
            ip_addresses = file.read().split()

        original_count = len(ip_addresses)

        # Remove unauthorized IP addresses
        ip_addresses = [
            ip
            for ip in ip_addresses
            if ip not in remove_list
        ]

        removed_count = original_count - len(ip_addresses)

        # Rewrite the file
        with open(import_file, "w") as file:
            file.write("\n".join(ip_addresses))

        return removed_count

    except FileNotFoundError:
        print(f"[ERROR] File not found: {import_file}")
        return 0

    except PermissionError:
        print(f"[ERROR] Permission denied: {import_file}")
        return 0

    except Exception as error:
        print(f"[ERROR] {error}")
        return 0


def main():
    """
    Main program execution.
    """

    allow_file = "allow_list.txt"

    remove_list = [
        "192.168.97.225",
        "192.168.158.170",
        "192.168.201.40",
        "192.168.58.57",
    ]

    print("=" * 50)
    print("Updating Allow List")
    print("=" * 50)

    removed = update_allow_list(allow_file, remove_list)

    print(f"\nRemoved {removed} IP address(es).\n")

    print("Updated Allow List")
    print("-" * 50)

    with open(allow_file, "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
