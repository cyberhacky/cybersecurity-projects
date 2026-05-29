# SQL Join Investigation Lab

## Investigating Employee, Device, and Authentication Data Using SQL Joins

---

# Overview

In this lab, I applied SQL JOIN operations within a MariaDB database environment to investigate relationships between employees, assigned devices, and authentication records. The investigation focused on combining data from multiple related tables to obtain a complete view of organizational assets and user activity.

As a cybersecurity analyst, information is often distributed across multiple database tables. Employee information may reside in one table, device inventories in another, and authentication logs in a separate table. SQL joins allow analysts to connect these related datasets through shared fields, enabling comprehensive investigations and more efficient security analysis.

This project demonstrates practical experience using INNER JOIN, LEFT JOIN, and RIGHT JOIN operations to correlate employee records, device assignments, and authentication events during a simulated security incident investigation.

---

# Objectives

* Identify employees and their assigned machines
* Correlate device inventory records with employee information
* Locate machines that are not assigned to users
* Identify employees without assigned devices
* Combine authentication logs with employee records
* Apply relational database concepts to cybersecurity investigations
* Develop practical SQL join and data correlation skills

---

# Environment

| Component             | Details                              |
| --------------------- | ------------------------------------ |
| Database              | MariaDB                              |
| Database Name         | organization                         |
| Tables Used           | employees, machines, log_in_attempts |
| Operating Environment | Linux Bash Shell                     |
| Investigation Type    | Asset and Authentication Correlation |

---

# Task 1 – Match Employees to Their Machines

## Retrieve Machine Inventory

### SQL Query

```sql
SELECT *
FROM machines;
```

### Purpose

The initial query was used to review the complete machine inventory stored within the organization database. Understanding the available device records was necessary before correlating machine data with employee records.

### Analysis

While the machine inventory provided valuable information about organizational assets, it did not identify which employee was assigned to each device. Additional data correlation was required to associate devices with users.

---

## Perform an Inner Join Between Machines and Employees

### SQL Query

```sql
SELECT *
FROM machines
INNER JOIN employees
ON machines.device_id = employees.device_id;
```

### Purpose

The purpose of this query was to identify which employees were assigned to specific machines by linking the two tables through their common `device_id` field.

### Analysis

The INNER JOIN returned only records where a matching `device_id` existed in both tables. This ensured that only valid employee-device relationships were included in the results.

This type of correlation is commonly used during asset investigations, vulnerability management, and incident response activities where analysts need to determine device ownership.

### Key Findings

* The INNER JOIN returned **185 records**.
* Employee-device assignments were successfully identified.
* Devices without assigned users were excluded from the results.
* Only matching records between both tables were returned.

### What I Learned

I learned how INNER JOIN operations can be used to correlate related information stored in separate tables. This technique is essential when investigating device ownership and asset accountability during security operations.

---

# Task 2 – Identify Unassigned Machines and Employees

## Perform a Left Join

### SQL Query

```sql
SELECT *
FROM machines
LEFT JOIN employees
ON machines.device_id = employees.device_id;
```

### Purpose

The purpose of this query was to retrieve all machine records, including devices that were not assigned to any employee.

### Analysis

The LEFT JOIN returned every record from the machines table while including matching employee information where available. Any machines without assigned users appeared with NULL values in employee-related columns.

This approach helps identify unmanaged assets, orphaned systems, or inventory discrepancies.

### Key Findings

* All organizational machines were included in the results.
* The username value in the final record returned was **NULL**.
* Unassigned devices were successfully identified.
* Asset inventory visibility was improved.

### What I Learned

I learned how LEFT JOIN operations can be used to identify assets that lack associated ownership information. This is valuable for asset management and security auditing activities.

---

## Perform a Right Join

### SQL Query

```sql
SELECT *
FROM machines
RIGHT JOIN employees
ON machines.device_id = employees.device_id;
```

### Purpose

The objective of this query was to retrieve all employee records, including employees who did not have a device assigned.

### Analysis

The RIGHT JOIN ensured that every employee record was returned, regardless of whether a matching machine assignment existed.

This type of analysis helps identify employees who may require equipment provisioning or highlights inconsistencies in asset assignment records.

### Key Findings

* The final username returned by the query was **areyes**.
* Employees without assigned devices remained visible.
* Personnel inventory reconciliation was improved.

### What I Learned

I learned how RIGHT JOIN operations allow analysts to preserve all records from a specified table while identifying missing relationships in connected datasets.

---

# Task 3 – Correlate Login Attempts with Employee Records

## Perform an Inner Join Between Employees and Login Attempts

### SQL Query

```sql
SELECT *
FROM employees
INNER JOIN log_in_attempts
ON employees.username = log_in_attempts.username;
```

### Purpose

The purpose of this query was to combine employee information with authentication logs to identify which employees generated login activity.

### Analysis

The INNER JOIN used the shared `username` field to correlate employee records with authentication events. This provided a unified view of users and their associated login attempts.

Correlating authentication logs with employee records is a common task during incident response investigations, threat hunting exercises, and security monitoring operations.

### Key Findings

* The INNER JOIN returned **200 records**.
* Employee records were successfully correlated with authentication activity.
* User attribution for login events was established.
* Authentication investigations became more efficient through data correlation.

### What I Learned

I learned how authentication logs can be linked directly to employee records using SQL joins. This capability is critical during incident investigations where user attribution is required.

---

# Investigation Summary

The SQL join investigation demonstrated how multiple tables can be connected to create a more complete view of organizational assets and user activity.

## Investigation Findings

* Employee-device relationships were successfully identified.
* The employee and machine INNER JOIN returned **185 records**.
* Unassigned devices were discovered through a LEFT JOIN.
* Employees without assigned machines were identified through a RIGHT JOIN.
* Authentication events were correlated with employee records.
* The employee and login attempt INNER JOIN returned **200 records**.

These techniques mirror real-world cybersecurity workflows where analysts routinely combine information from multiple sources to investigate incidents and maintain visibility into organizational systems.

---

# Overall Learning Outcome

## What I Learned From This Lab

This lab strengthened my understanding of relational databases and the practical use of SQL joins during cybersecurity investigations. I gained hands-on experience combining datasets to correlate users, devices, and authentication activity.

The investigation demonstrated how SQL joins enable analysts to move beyond isolated data sources and develop a complete operational picture of organizational assets and user behavior.

---

# Skills Developed

* SQL INNER JOIN operations
* SQL LEFT JOIN operations
* SQL RIGHT JOIN operations
* Relational database analysis
* Asset inventory correlation
* Authentication log correlation
* User attribution investigations
* Device ownership analysis
* Database relationship mapping
* MariaDB query development

These skills are directly applicable to Security Operations Center (SOC) environments, incident response investigations, threat hunting activities, asset management programs, and enterprise security monitoring.

---

# Key Takeaways

* Used INNER JOIN to correlate related records across tables.
* Applied LEFT JOIN to identify unassigned assets.
* Applied RIGHT JOIN to identify employees without assigned devices.
* Linked authentication records to employee information.
* Improved understanding of relational database structures.
* Strengthened practical SQL skills for cybersecurity investigations.
* Developed techniques commonly used in incident response and asset management.

---

# Conclusion

This lab provided practical experience using SQL joins to connect employee records, device inventories, and authentication logs. By leveraging INNER JOIN, LEFT JOIN, and RIGHT JOIN operations, I was able to correlate data across multiple tables and gain a comprehensive view of organizational assets and user activity.

These skills are essential for cybersecurity professionals responsible for incident response, asset management, threat hunting, security monitoring, and forensic investigations. The ability to combine related datasets efficiently enables analysts to investigate security events with greater speed, accuracy, and context.

---

# Author

## Cornelius Donkor

**Cybersecurity Professional | Security Analyst | SQL & Linux Enthusiast**
