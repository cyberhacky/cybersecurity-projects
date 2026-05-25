# Linux Log Filtering and File Analysis with grep

## Overview

This lab focused on using the `grep` command and command piping in Linux to efficiently search, filter, and analyze information stored within files and directories. The activity simulated common cybersecurity tasks such as investigating server logs, locating user-related files, and filtering data during system investigations.

As a cybersecurity analyst, the ability to quickly locate and analyze information through the Linux command line is essential during incident response, threat hunting, log analysis, and security auditing.

---

## Objectives

During this activity, the following objectives were completed:

- Navigated Linux directories using shell commands
- Used `grep` to search log files for error messages
- Used piping (`|`) to filter command output
- Located files containing specific strings in their names
- Searched user files for usernames and department information
- Practiced Linux command-line investigation techniques

---

## Linux Commands Used

| Command | Purpose |
|---------|---------|
| `cd` | Change directories |
| `ls` | List files and directories |
| `grep` | Search for specific text patterns |
| `|` | Pipe command output to another command |

---

# Investigation Process

## Task 1 — Search for Error Messages in a Log File

### Navigated to the logs directory

```bash
cd logs


## Task 1 — Search for Error Messages in a Log File

### Searched the `server_logs.txt` file for all lines containing the word `error`

```bash
grep error server_logs.txt
```

### Results

```text
2022-09-28 13:56:22 error The password is incorrect
2022-09-28 15:56:22 error The username is incorrect
2022-09-28 16:56:22 error The password is incorrect
2022-09-29 13:56:22 error An unexpected error occurred
2022-09-29 15:56:22 error Unauthorized access
2022-09-29 16:56:22 error Unauthorized access
```

### Findings

- A total of six error entries were discovered
- Multiple failed authentication attempts were detected
- Unauthorized access attempts were identified
- Log filtering helps analysts rapidly identify suspicious activity

### Security Relevance

These findings demonstrate how `grep` can assist cybersecurity professionals in identifying authentication failures and suspicious events during investigations.

---

# Task 2 — Find Files Containing Specific Strings

## Navigated to the users directory

```bash
cd /home/analyst/reports/users
```

## Filtered filenames containing `Q1`

```bash
ls | grep Q1
```

### Matching Files

```text
Q1_access.txt
Q1_added_users.txt
Q1_deleted_users.txt
```

### Findings

- Three files contained the string `Q1`
- Piping allows analysts to efficiently narrow command output

---

## Searched for files containing the word `access`

```bash
ls | grep access
```

### Matching Files

```text
Q1_access.txt
Q2_access.txt
Q3_access.txt
Q4_access.txt
```

### Findings

- Four files contained the word `access`
- Pattern matching is useful when analyzing large directories

### Security Relevance

Filtering filenames enables analysts to quickly locate relevant reports, access records, and investigation data during audits and incident response operations.

---

# Task 3 — Search File Contents

## Displayed all files in the directory

```bash
ls
```

## Searched for the username `jhill` in the deleted users report

```bash
grep jhill Q2_deleted_users.txt
```

### Result

```text
1025    jhill    Sales
```

### Findings

- User `jhill` was located in the deleted users report
- The user belonged to the Sales department

---

## Searched for users in the Human Resources department

```bash
grep "Human Resources" Q4_added_users.txt
```

### Results

```text
1151    sshah    Human Resources
1145    mrosa    Human Resources
```

### Findings

- Two Human Resources users were added
- `grep` can filter records containing spaces using quotation marks

### Security Relevance

Searching user reports helps analysts investigate account activity, monitor changes to user access, and support identity and access management investigations.

---

# Key Takeaways

- Used `grep` to efficiently filter Linux logs
- Applied piping for command chaining and output filtering
- Investigated user activity records
- Performed basic log analysis and auditing
- Practiced command-line investigation workflows
- Improved Linux-based cybersecurity investigation skills

---

# Cybersecurity Relevance

This lab demonstrates how Linux filtering tools support cybersecurity operations, including:

- Log analysis
- Threat investigation
- User account auditing
- Incident response
- Data filtering and pattern matching
- Efficient command-line investigations

Security professionals frequently use `grep` during:

- SOC investigations
- SIEM log analysis
- Threat hunting
- Forensics investigations
- Access auditing
- System administration

---

# Skills Demonstrated

- Linux Command-Line Navigation
- File Filtering with `grep`
- Command Piping in Linux
- Log Analysis Techniques
- User Data Investigation
- Pattern Matching
- Security Investigation Workflow
- Linux Administration Fundamentals

---

# Conclusion

This activity strengthened practical Linux investigation skills by using `grep` and command piping to search logs, locate files, and analyze user data. The lab demonstrated how cybersecurity professionals efficiently filter and retrieve important information during investigations, security monitoring, and system auditing activities.

The ability to quickly search and analyze data within Linux environments is a foundational skill for cybersecurity analysts, SOC teams, and penetration testers.
