# SQL Query Filtering Lab

## Filtering SQL Queries for Cybersecurity Investigations



# Overview

In this lab, I applied SQL filtering techniques within the MariaDB shell to retrieve targeted security-related information from the `organization` database. The investigation focused on employee devices, operating systems, department information, and office locations to support security operations and organizational asset management.

This project demonstrates practical cybersecurity data analysis using SQL filters such as `WHERE` and `LIKE` to efficiently locate specific records within a database.


# Objectives

- Retrieve organization machine information
- Filter devices by operating system
- Identify employees in specific departments
- Investigate employee office locations
- Use SQL filtering operators such as `WHERE` and `LIKE`
- Strengthen SQL investigation and database querying skills


# Environment

| Component | Details |
|---|---|
| Database | MariaDB |
| Database Name | organization |
| Tables Used | machines, employees |
| Operating Environment | Linux Bash Shell |


# Task 1 – List All Organization Machines

## Retrieve Device IDs and Operating Systems

### SQL Query


SELECT device_id, operating_system
FROM machines;


### Purpose

Retrieved device identifiers and operating systems for all organizational machines to support asset visibility and security update planning.


# Task 2 – Retrieve Machines Running OS 2

## Filter Machines by Operating System

### SQL Query

SELECT device_id, operating_system
FROM machines
WHERE operating_system = 'OS 2';


### Purpose

Identified all machines running `OS 2` so the security team could prioritize system updates and vulnerability remediation.


# Task 3 – List Employees in Specific Departments

## Retrieve Employees in the Finance Department

### SQL Query

SELECT *
FROM employees
WHERE department = 'Finance';


### Purpose

Retrieved employee information from the Finance department to support privacy notice distribution and handling of confidential financial information.


## Retrieve Employees in the Sales Department

### SQL Query

SELECT *
FROM employees
WHERE department = 'Sales';


### Purpose

Retrieved employee information from the Sales department for department-specific communication and administrative tasks.


# Task 4 – Identify Employee Machines

## Identify the Employee Using Office South-109

### SQL Query

SELECT *
FROM employees
WHERE office = 'South-109';


### Purpose

Identified the employee assigned to office `South-109` so the security team could send an alert regarding a machine issue.


## Retrieve All Employees in the South Building

### SQL Query

SELECT *
FROM employees
WHERE office LIKE 'South%';

### Purpose

Retrieved all employees located in the South building to investigate organization-wide issues affecting multiple machines in that location.


### Analysis

The query returned 200 organizational machine records, indicating the total number of systems tracked within the database inventory.


### Analysis

A total of 80 systems were identified running `OS 2`, which allowed the security team to prioritize operating system updates and remediation efforts.


### Analysis

The first employee record returned from the Sales department query belonged to employee ID '1003'.


### Analysis

The query identified 33 employees assigned to the Sales department.

---

# Incident Response Investigation


### Analysis

The employee assigned to the affected machine located in office 'South-109' was identified as 'jlansky' from the Finance department.


### Analysis

The first employee returned from the South building query belonged to the Finance department.


# Investigation Summary

The SQL filtering investigation revealed:

- Organizational machines operating on multiple operating systems
- Devices requiring updates based on operating system versions
- Department-specific employee information for administrative and security notifications
- Office-based employee identification for incident response activities
- Efficient use of SQL filtering techniques to narrow investigation scope
- Total organizational machine inventory consisted of 200 systems
- 80 systems were identified running `OS 2`
- 33 employees were identified in the Sales department
- Affected employee systems were successfully identified for incident response follow-up

These findings demonstrate how SQL filters can improve the speed and accuracy of cybersecurity investigations and organizational asset management.

---

# Skills Demonstrated

- SQL filtering with `WHERE`
- Pattern matching using `LIKE`
- Database investigation techniques
- Security asset management
- Employee and device identification
- Data retrieval and filtering
- MariaDB command-line usage
- Operating system investigation
- Security incident response support
- SQL-based asset tracking

---

# Cybersecurity Relevance

Security analysts frequently use SQL filters to locate systems, users, and security events relevant to ongoing investigations. Efficient filtering reduces investigation time and improves operational visibility.

These skills are critical for:

- Threat hunting
- Incident response
- Vulnerability management
- Asset inventory management
- Security operations
- Compliance investigations
- Security auditing
- System monitoring

This lab strengthened practical experience in filtering SQL queries for cybersecurity analysis and operational investigations.

---

# Key Takeaways

- Learned how to apply filters to SQL queries using 'WHERE'
- Practiced narrowing search results to retrieve relevant information efficiently
- Used the `LIKE` operator for pattern matching in database investigations
- Improved SQL investigation workflows for cybersecurity operations
- Gained hands-on experience with MariaDB database filtering techniques
- Identified systems requiring operating system updates
- Investigated employee office assignments during a simulated incident response scenario

---

# Conclusion

This lab provided practical experience in filtering SQL queries to retrieve targeted security and organizational data. By using SQL filtering operators such as 'WHERE' and 'LIKE', I improved my ability to efficiently investigate systems, employees, and office locations within a database environment.

The investigation successfully identified vulnerable systems, department-specific employees, and office locations associated with affected machines. These foundational SQL investigation skills are essential for cybersecurity analysts involved in monitoring, incident response, asset management, and security operations.

This project further strengthened practical cybersecurity investigation capabilities using SQL-based database analysis techniques.

---

# Author

## Cornelius Donkor

**Cybersecurity Professional | Security Analyst | SQL & Linux Enthusiast**
