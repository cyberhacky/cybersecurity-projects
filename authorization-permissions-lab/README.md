#  Linux File Permissions & Authorization Lab

##  Overview

This cybersecurity lab demonstrates how to inspect, modify, and secure Linux file and directory permissions using authorization controls.

Authorization is a fundamental cybersecurity concept that determines which users or groups are allowed to access or modify specific system resources. Improper authorization settings can expose sensitive files, compromise system integrity, and create security vulnerabilities.

In this lab, Linux commands were used to analyze and secure the `/home/researcher2/projects` directory belonging to the `researcher2` user.

The `researcher2` account belongs to the `research_team` group and is responsible for managing project-related files stored in the `/home/researcher2/projects` directory.

The goal of this lab was to ensure that:

- Unauthorized users could not modify files
- Sensitive files remained private
- Hidden archived files were protected from modification
- Only the owner could access restricted directories

#  Objectives

By completing this lab, the following cybersecurity skills were demonstrated:

- Navigating Linux directories securely
- Inspecting Linux file permissions
- Identifying insecure authorization settings
- Managing hidden files
- Applying secure access controls using `chmod`
- Restricting unauthorized group and public access
- Securing sensitive directories and archived files
- Implementing the Principle of Least Privilege (PoLP)

---

# Environment

| Component | Details |
|---|---|
| Operating System | Linux |
| User | researcher2 |
| Group | research_team |
| Working Directory | /home/researcher2/projects |
| Primary Commands | ls, chmod, cd |

---

#  Cybersecurity Concepts

## Authorization

Authorization controls determine what authenticated users are permitted to do within a system.

Without proper authorization:
- Unauthorized users may access confidential data
- Critical files may be modified or deleted
- Systems may become vulnerable to attacks

Linux uses file and directory permissions to enforce authorization controls.

---

# Linux Permission Structure

Linux permissions follow a 10-character structure:


-rw-rw-r--


## Permission Breakdown

| Position | Meaning |
|---|---|
| 1 | File type (`-` = file, `d` = directory) |
| 2-4 | User permissions |
| 5-7 | Group permissions |
| 8-10 | Other/public permissions |

---

## Permission Symbols

| Symbol | Meaning |
|---|---|
|     r |  Read |
|     w |  Write |
|     x |  Execute |
|     - |  Permission not granted |



#  Task 1 — Inspect File & Directory Permissions

## Step 1: Navigate to the Projects Directory


cd projects


---

## Step 2: List Directory Contents


ls -l


### Initial Output

```bash
drwx--x--- 2 researcher2 research_team 4096 May 25 19:33 drafts
-rw-rw-rw- 1 researcher2 research_team   46 May 25 19:33 project_k.txt
-rw-r----- 1 researcher2 research_team   46 May 25 19:33 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 25 19:33 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 May 25 19:33 project_t.txt
```

---

## Findings

###  Security Issues Identified

| File | Issue |
|---|---|
| `project_k.txt` | Public write access enabled |
| `project_m.txt` | Group read access enabled |
| `drafts/` | Group execute access enabled |

---

## Step 3: Display Hidden Files

ls -la


### Hidden File Found

.project_x.txt


### Hidden File Permissions

-rw--w----


### Security Issue

The hidden file improperly allowed write permissions.

---

# Task 2 — Secure File Permissions

---

## Secure `project_k.txt`

### Problem

The file allowed all users to modify it.

### Original Permissions

-rw-rw-rw-

---

## Remove Public Write Access

### Command

chmod o-w project_k.txt


### Updated Permissions


-rw-rw-r--


###  Security Improvement

Unauthorized users can no longer modify the file.

---

#  Secure `project_m.txt`

### Problem

The file was intended to be restricted to the owner only.

### Original Permissions


-rw-r-----


---

## Remove Group Read Permissions

### Command


chmod g-r project_m.txt


### Updated Permissions


-rw-------


###  Security Improvement

Only the owner can access the file.

---

#  Task 3 — Secure Hidden File Permissions

## Analyze .project_x.txt`

### Original Permissions

-rw--w----


### Problem

The archived hidden file allowed write access.

---

## Security Requirement

- User: Read only
- Group: Read only
- No write access allowed



## Modify Permissions

### Command

chmod u-w,g+r,g-w .project_x.txt


### Updated Permissions


-r--r-----


###  Security Improvement

The archived file can no longer be modified.

---

#  Task 4 — Secure Directory Permissions

## Analyze `drafts/` Directory

### Original Permissions


drwx--x---


### Problem

The group had execute access to the directory.

---

## Remove Group Execute Permission

### Command

chmod g-x drafts


### Updated Permissions

drwx------


###  Security Improvement

Only the `researcher2` user can access the directory and its contents.

---

# Final Permission States

| File / Directory | Final Permissions | Security Status |
|---|---|---|
| `project_k.txt` | `-rw-rw-r--` | Secured |
| `project_m.txt` | `-rw-------` | Restricted |
| `.project_x.txt` | `-r--r-----` | Archived Securely |
| `drafts/` | `drwx------` | Owner Only |



#  Commands Used

| Command | Purpose |
|---|---|
| `cd projects` | Navigate to project directory |
| `ls -l` | List files and permissions |
| `ls -la` | Display hidden files |
| `chmod o-w` | Remove write access from others |
| `chmod g-r` | Remove group read access |
| `chmod u-w` | Remove user write access |
| `chmod g-w` | Remove group write access |
| `chmod g-x` | Remove group execute access |

---

# Security Best Practices Demonstrated

- Principle of Least Privilege (PoLP)
- Restricting public write access
- Protecting sensitive files
- Securing hidden archived files
- Limiting directory traversal permissions
- Managing authorization controls effectively

---

# Conclusion

This lab demonstrated how Linux file permissions are used to enforce authorization controls and secure sensitive system resources.

By inspecting and modifying file and directory permissions:
- Unauthorized access was removed
- Sensitive data was protected
- Security posture was strengthened

These skills are essential for:
- Linux system administration
- Cybersecurity operations
- Security hardening
- Access control management
- Incident prevention

Proper permission management is a foundational cybersecurity defense mechanism in Linux environments.

---

#  References

- Linux `chmod` Manual
- Linux File Permission Documentation
- UNIX/Linux Authorization Models
- Principle of Least Privilege (PoLP)

---

#  Author
## Cornelius Donkor

**Cybersecurity Linux Authorization & File Permission Lab**

