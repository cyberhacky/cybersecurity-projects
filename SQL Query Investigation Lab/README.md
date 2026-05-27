# SQL Query Investigation Lab

## Investigating Employee Devices and Login Activity Using SQL

---

# Overview

In this lab, I used SQL queries within the MariaDB shell to retrieve, analyze, and organize security-related data from the `organization` database. The investigation focused on employee devices requiring updates and login activity monitoring to identify potential unusual behavior.

This project demonstrates foundational cybersecurity data analysis skills using SQL, including querying databases, selecting relevant fields, and sorting event data for security investigations.

---

# Objectives

- Retrieve employee device information from a database
- Identify device operating systems and patch status
- Investigate user login activity across locations
- Review login attempts outside expected working hours
- Organize login data chronologically using `ORDER BY`
- Strengthen SQL skills used in cybersecurity operations

---

# Environment

| Component | Details |
|---|---|
| Database | MariaDB |
| Database Name | organization |
| Tables Used | machines, log_in_attempts |
| Operating Environment | Linux Bash Shell |

---

# Task 1 – Retrieve Employee Device Data

## 1. Retrieve All Device Information

### SQL Query


SELECT *
FROM machines;
```

### Purpose

Retrieved all available device information from the `machines` table to assess organizational assets requiring updates.

---

## 2. Retrieve Device ID and Email Client

### SQL Query


SELECT device_id, email_client
FROM machines;
```

### Purpose

Identified email clients installed on organizational devices for software review and update verification.

---

## 3. Retrieve Operating System and Patch Information

### SQL Query


SELECT device_id, operating_system, OS_patch_date
FROM machines;
```

### Purpose

Reviewed operating systems and patch dates to determine whether devices required security updates.

---

# Task 2 – Investigate Login Activity

## 1. Retrieve Login Attempt Locations

### SQL Query


SELECT event_id, country
FROM log_in_attempts;
```

### Purpose

Investigated login attempt origins to identify connections from unexpected geographic locations.

---

## 2. Review Login Dates and Times

### SQL Query


SELECT username, login_date, login_time
FROM log_in_attempts;
```

### Purpose

Analyzed login activity to determine whether authentication attempts occurred outside standard working hours.

---

## 3. Retrieve All Login Attempt Data

### SQL Query


SELECT *
FROM log_in_attempts;
```

### Purpose

Obtained complete visibility into login events for further investigation and correlation.

---

# Task 3 – Order Login Attempt Data

## 1. Sort Login Attempts by Date

### SQL Query


SELECT *
FROM log_in_attempts
ORDER BY login_date;
```

### Purpose

Organized login attempts chronologically to improve visibility into user activity trends.

---

## 2. Sort Login Attempts by Date and Time

### SQL Query

```sql
SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
```

### Purpose

Further refined event sequencing by sorting login attempts according to both date and time.

---

# Lab Analysis Findings

## What email client is returned in the third row?

**Answer:** `Email Client 2`

---

## What is the patch date of the first entry?

**Answer:** `2021-09-01`

---

## Were any login attempts made from Australia?

**Answer:** No.

All login attempts originated from:

- USA
- CAN / CANADA
- MEX / MEXICO

No login attempts from Australia were identified.

---

## What username is returned in the fifth row?

**Answer:** `jrahel`

---

## What are the username and login date of the first record returned?

| Username | Login Date |
|---|---|
| jrahel | 2022-05-09 |

---

## What are the username and login time of the first record returned by the ordered query?

| Username | Login Time |
|---|---|
| bsand | 00:19:11 |

---

# Investigation Summary

The SQL investigation revealed:

- Multiple organizational devices using different email clients
- Several systems with outdated operating system patch dates
- Login activity originating only from approved geographic regions
- Chronological ordering improved visibility into authentication patterns and user activity timelines

These findings demonstrate practical cybersecurity analysis using SQL for security monitoring and authentication investigations.

---

# Skills Demonstrated

- SQL database querying
- Data retrieval and filtering
- Security log investigation
- Authentication activity analysis
- Database table analysis
- Sorting and organizing security data
- MariaDB command-line usage

---

# Cybersecurity Relevance

Security analysts frequently use SQL to investigate authentication logs, identify suspicious activity, and monitor device security posture.

Understanding how to query databases efficiently is essential for:

- Threat hunting
- Incident response
- Security monitoring
- Vulnerability management
- Compliance auditing

This lab strengthened practical experience in analyzing organizational security data through structured SQL queries.

---

# Key Takeaways

- Learned how to retrieve specific and complete datasets from SQL databases
- Practiced analyzing authentication events for anomalies
- Used SQL sorting techniques to improve event investigation workflows
- Gained hands-on experience with MariaDB in a cybersecurity context

---

# Conclusion

This lab provided practical experience in using SQL for cybersecurity investigations. By querying device and login activity data, I developed foundational skills required for security operations, threat analysis, and system monitoring.

These techniques form the basis for more advanced database investigations and security analytics workflows.

---

# Author

## Cornelius Donkor

**Cybersecurity Professional | Security Analyst | SQL & Linux Enthusiast**
