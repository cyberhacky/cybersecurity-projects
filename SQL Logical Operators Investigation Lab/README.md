# SQL Logical Operators Investigation Lab

## Investigating Authentication Activity and Employee Records Using AND, OR, and NOT Filters

---

# Overview

In this lab, I applied SQL logical operators to investigate authentication activity and retrieve employee information from a MariaDB database. The investigation focused on using the `AND`, `OR`, and `NOT` operators to create more precise queries and efficiently locate records relevant to security operations and system administration tasks.

As a cybersecurity analyst, it is common to work with large datasets containing authentication logs, user records, asset inventories, and departmental information. Logical operators enable analysts to combine multiple conditions, identify specific events, and exclude irrelevant records, making investigations more efficient and accurate.

This project demonstrates practical experience using SQL logical operators to analyze login activity, investigate geographic authentication patterns, identify employees affected by security issues, and support organizational update management.

---

# Objectives

* Investigate failed login attempts occurring after business hours
* Review authentication activity during a specific incident timeframe
* Analyze login attempts originating outside approved geographic regions
* Identify employees based on department and office location
* Retrieve records for multiple departments simultaneously
* Exclude specific departments from security update operations
* Apply SQL logical operators to real-world cybersecurity investigations

---

# Environment

| Component             | Details                                   |
| --------------------- | ----------------------------------------- |
| Database              | MariaDB                                   |
| Database Name         | organization                              |
| Tables Used           | log_in_attempts, employees                |
| Operating Environment | Linux Bash Shell                          |
| Investigation Type    | Authentication and Employee Data Analysis |

---

# Task 1 – Investigate Failed Login Attempts After Business Hours

## SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
AND success = 0;
```

### Purpose

The objective of this query was to identify unsuccessful authentication attempts occurring after normal business hours. Since legitimate employee activity is generally expected during standard operating hours, failed logins occurring later in the evening may warrant additional investigation.

### Analysis

The query combined two conditions using the `AND` operator:

* Login attempts occurring after 18:00
* Authentication attempts marked as unsuccessful

This allowed the investigation to isolate records meeting both criteria simultaneously and remove unrelated authentication events from the dataset.

### Key Findings

* **19 failed login attempts** occurred after business hours.
* Authentication failures outside standard operating hours may indicate unauthorized access attempts.
* Combining multiple conditions significantly reduced investigation scope.

### What I Learned

I learned how the `AND` operator can be used to combine multiple conditions in a single query. This technique enables security analysts to isolate highly specific events and improve the accuracy of investigations.

---

# Task 2 – Investigate Login Activity on Specific Dates

## SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-08'
OR login_date = '2022-05-09';
```

### Purpose

The purpose of this query was to investigate authentication activity surrounding a suspected security event that occurred on May 9, 2022.

### Analysis

Using the `OR` operator allowed records from either date to be returned. This approach expanded the investigation window to include activity immediately preceding the suspected incident.

Reviewing events from both days provided additional context and improved visibility into potential suspicious behavior leading up to the event.

### Key Findings

* **75 login attempts** occurred during the two-day investigation window.
* The investigation included both the incident date and the preceding day.
* Expanding the timeframe improved contextual analysis.

### What I Learned

I learned how the `OR` operator can be used to retrieve records matching multiple conditions. This is particularly useful when analyzing events that span multiple dates or investigation periods.

---

# Task 3 – Investigate Login Attempts Outside Mexico

## SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

### Purpose

The objective of this query was to identify authentication attempts that originated outside Mexico.

### Analysis

The query used both the `NOT` and `LIKE` operators to exclude records containing either `MEX` or `MEXICO`.

Pattern matching ensured all Mexican-based authentication records were excluded while retaining all other geographic locations.

Geographic authentication analysis is commonly performed when investigating suspicious login activity originating from unexpected locations.

### Key Findings

* **144 login attempts** originated outside Mexico.
* Geographic filtering successfully isolated authentication activity from foreign regions.
* Pattern matching improved efficiency when working with multiple location formats.

### What I Learned

I learned how to combine the `NOT` and `LIKE` operators to exclude specific patterns from a dataset. This technique is useful during threat hunting and geographic anomaly investigations.

---

# Task 4 – Identify Marketing Employees in the East Building

## SQL Query

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
AND office LIKE 'East%';
```

### Purpose

The purpose of this query was to identify Marketing department employees located within East building offices for system update planning.

### Analysis

The query combined departmental and office location criteria using the `AND` operator. Only employees satisfying both requirements were returned.

This type of filtering is useful when security teams need to target specific groups of users or systems for updates, awareness campaigns, or incident response activities.

### Key Findings

* The first employee returned was **elarson**.
* Only Marketing employees located in East building offices were included.
* Multiple conditions improved query precision.

### What I Learned

I learned how multiple organizational attributes can be combined within a query to retrieve highly targeted employee records.

---

# Task 5 – Retrieve Employees in Finance or Sales

## SQL Query

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';
```

### Purpose

The objective of this query was to identify employees belonging to either the Finance or Sales departments for a planned system update.

### Analysis

Using the `OR` operator allowed records from either department to be returned in a single query. This eliminated the need to run separate searches for each department.

Department-based filtering is commonly used when performing security updates, policy enforcement, and compliance-related activities.

### Key Findings

* The first employee returned by the query was **lrodriqu**.
* Employees from both Finance and Sales departments were successfully identified.
* Departmental filtering simplified administrative operations.

### What I Learned

I learned how the `OR` operator enables analysts to retrieve records that satisfy one of several conditions, improving efficiency when working with multiple groups.

---

# Task 6 – Identify Employees Outside the Information Technology Department

## SQL Query

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

### Purpose

The purpose of this query was to identify employees who had not yet received a departmental update already completed for the Information Technology team.

### Analysis

The `NOT` operator excluded Information Technology employees and returned all remaining employee records.

Exclusion-based filtering is valuable when analysts need to identify systems, users, or departments requiring additional action while removing records already processed.

### Key Findings

* **161 employees** were identified outside the Information Technology department.
* Exclusion filtering efficiently reduced unnecessary records.
* The query simplified update management and planning.

### What I Learned

I learned how the `NOT` operator can be used to exclude specific criteria from query results. This technique is valuable when narrowing investigation scope or identifying assets requiring attention.

---

# Investigation Summary

The SQL investigation demonstrated how logical operators can be used to retrieve highly targeted information from large datasets.

### Investigation Findings

* 19 failed login attempts occurred after business hours.
* 75 authentication events occurred during the identified investigation period.
* 144 login attempts originated outside Mexico.
* Marketing employees located in East building offices were successfully identified.
* Finance and Sales department employees were isolated for update planning.
* 161 employees were identified outside the Information Technology department.

These techniques mirror real-world security operations workflows where analysts must combine multiple conditions to efficiently identify relevant information while excluding unrelated records.

---

# Overall Learning Outcome

## What I Learned From This Lab

This lab strengthened my understanding of SQL logical operators and their application in cybersecurity investigations. I gained practical experience combining multiple conditions to retrieve targeted information from large datasets and learned how logical filtering improves investigation efficiency.

### Skills Developed

* SQL logical operators (`AND`, `OR`, `NOT`)
* Pattern matching using `LIKE`
* Authentication log analysis
* Geographic login investigations
* Employee and department analysis
* Security event filtering
* Database-driven investigations
* MariaDB query development

These skills are directly applicable to Security Operations Center (SOC) investigations, threat hunting activities, compliance reviews, identity management, and security monitoring operations.

---

# Key Takeaways

* Applied logical operators to isolate security-related records.
* Combined multiple filters to improve investigation accuracy.
* Used pattern matching to analyze geographic authentication activity.
* Investigated employee and department information for security operations.
* Strengthened SQL investigation skills relevant to cybersecurity roles.
* Improved the ability to retrieve targeted information from large datasets.

---

# Conclusion

This lab provided hands-on experience using SQL logical operators to investigate authentication activity and employee records. By combining conditions with `AND`, `OR`, and `NOT`, I was able to efficiently identify relevant events, users, and departments while reducing unnecessary records.

These filtering techniques are essential skills for cybersecurity professionals involved in security monitoring, incident response, compliance auditing, threat hunting, and organizational security operations.

---

# Author

## Cornelius Donkor

**Cybersecurity Professional | Security Analyst | SQL & Linux Enthusiast**
