# Activity: Find Files with Linux Commands

## Overview

This lab focused on using essential Linux shell commands to navigate the Linux file system, locate files, and analyze file contents through the command-line interface (CLI). The activity simulated tasks commonly performed by cybersecurity analysts when investigating logs, reviewing user reports, and accessing system information remotely without a graphical interface.

---

# Objectives

During this activity, the following objectives were completed:

* Displayed the current working directory using Linux commands
* Listed files and directories within directories
* Navigated between directories using relative paths
* Read and analyzed the contents of text files
* Reviewed server log files for warnings and errors
* Practiced Linux CLI navigation skills used in cybersecurity operations

---

# Linux Commands Used

| Command | Purpose                           |
| ------- | --------------------------------- |
| `pwd`   | Display current working directory |
| `ls`    | List files and directories        |
| `cd`    | Change directory                  |
| `cat`   | Display file contents             |
| `head`  | Display first lines of a file     |

---

# Investigation Process

## Task 1 — Get Current Directory Information

The `pwd` command was used to confirm the current working directory:

```bash
pwd
```

Output:

```bash
/home/analyst
```

The `ls` command displayed the contents of the directory:

```bash
ls
```

Directories discovered:

* logs
* projects
* reports
* temp

This confirmed there were four directories inside `/home/analyst`.

---

## Task 2 — Change Directory and List Subdirectories

Navigated into the reports directory:

```bash
cd reports
```

Listed directory contents:

```bash
ls
```

The subdirectory discovered was:

```bash
users
```

---

## Task 3 — Locate and Read File Contents

Navigated into the users directory:

```bash
cd users
```

Displayed files:

```bash
ls
```

Files identified:

* Q1_added_users.txt
* Q1_deleted_users.txt

Displayed file contents:

```bash
cat Q1_added_users.txt
```

The report contained:

* employee IDs
* usernames
* departments

Key findings included:

* User `aezra` works in Human Resources
* User `mreed` belongs to Information Technology with employee ID `1104`

---

## Task 4 — Analyze Server Logs

Navigated to the logs directory:

```bash
cd ~/logs
```

Displayed file names:

```bash
ls
```

Located log file:

```bash
server_logs.txt
```

Displayed the first 10 lines:

```bash
head server_logs.txt
```

---

# Log Analysis Findings

The log file contained:

* informational messages
* warnings
* authentication errors

Examples observed:

* Incorrect password attempts
* Incorrect username attempts
* Storage usage warnings
* Password expiration notifications

A total of **three warning messages** were identified in the first 10 log entries.

---

# Cybersecurity Relevance

This activity demonstrates foundational Linux skills used by cybersecurity professionals during:

* log analysis
* incident investigations
* system auditing
* user account reviews
* remote server management

Security analysts frequently rely on the CLI because it allows:

* faster navigation
* automation
* remote administration
* scripting capabilities
* efficient log analysis without a graphical interface

---

# Skills Demonstrated

* Linux File System Navigation
* Command-Line Interface (CLI) Usage
* Log Analysis
* File Inspection
* Security Investigation Techniques
* Linux System Administration Fundamentals
* Basic Threat Detection

---

# Conclusion

This lab strengthened practical Linux command-line skills that are essential in cybersecurity operations. By navigating directories, locating files, reading reports, and analyzing server logs, the activity demonstrated how Linux commands support real-world security investigations and system administration tasks.
