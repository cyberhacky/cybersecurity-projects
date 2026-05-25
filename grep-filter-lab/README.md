Activity: Filter with grep
Overview

This lab focused on using the grep command and piping in Linux to efficiently search for specific information within files and directories. The activity simulated common cybersecurity tasks such as analyzing server logs, locating user-related files, and filtering data for investigations.

As a cybersecurity analyst, being able to quickly search and filter information is essential during incident investigations, log analysis, and system audits.

Objectives

During this activity, the following objectives were completed:

Navigated Linux directories using shell commands
Used grep to search log files for error messages
Used piping (|) to filter command output
Located files containing specific strings in their names
Searched user files for usernames and department information
Practiced Linux command-line investigation techniques

Linux Commands Used

| Command | Purpose                           |                                        |
| ------- | --------------------------------- | -------------------------------------- |
| `cd`    | Change directories                |                                        |
| `ls`    | List files and directories        |                                        |
| `grep`  | Search for specific text patterns |                                        |
| `       | ` (pipe)                          | Send command output to another command |

Investigation Process
Task 1 — Search for Error Messages in a Log File

Navigated to the logs directory:

cd logs

Searched the server_logs.txt file for all lines containing the word error:

grep error server_logs.txt
Results

The following error messages were identified:

2022-09-28 13:56:22 error The password is incorrect
2022-09-28 15:56:22 error The username is incorrect
2022-09-28 16:56:22 error The password is incorrect
2022-09-29 13:56:22 error An unexpected error occurred
2022-09-29 15:56:22 error Unauthorized access
2022-09-29 16:56:22 error Unauthorized access
Findings
A total of six error entries were discovered
Multiple failed authentication attempts were detected
Unauthorized access attempts were identified
Log filtering helps analysts rapidly identify suspicious events
Task 2 — Find Files Containing Specific Strings

Navigated to the users directory:

cd /home/analyst/reports/users

Used piping with grep to filter filenames containing Q1:

ls | grep Q1
Matching Files
Q1_access.txt
Q1_added_users.txt
Q1_deleted_users.txt
Findings
Three files contained the string Q1
Piping allows analysts to efficiently narrow command output

Searched for files containing the word access:

ls | grep access
Matching Files
Q1_access.txt
Q2_access.txt
Q3_access.txt
Q4_access.txt
Findings
Four files contained the word access
Pattern matching is useful when analyzing large directories
Task 3 — Search File Contents

Displayed all files in the directory:

ls

Searched for the username jhill in the deleted users report:

grep jhill Q2_deleted_users.txt
Result
1025    jhill    Sales
Findings
User jhill was located in the deleted users report
The user belonged to the Sales department

Searched for users in the Human Resources department:

grep "Human Resources" Q4_added_users.txt
Results
1151    sshah    Human Resources
1145    mrosa    Human Resources
Findings
Two Human Resources users were added
grep can filter records containing spaces using quotation marks
Cybersecurity Relevance

This lab demonstrates how Linux filtering tools support cybersecurity operations, including:

Log analysis
Threat investigation
User account auditing
Incident response
Data filtering and pattern matching
Efficient command-line investigations

Security professionals frequently use grep during:

SOC investigations
SIEM log analysis
Threat hunting
Forensics investigations
Access auditing
System administration
Skills Demonstrated
Linux Command-Line Navigation
File Filtering with grep
Piping Commands in Linux
Log Analysis Techniques
User Data Investigation
Pattern Matching
Security Investigation Workflow
Linux Administration Fundamentals
Conclusion

This activity strengthened practical Linux investigation skills by using grep and command piping to search logs, locate files, and analyze user data. The lab demonstrated how cybersecurity professionals efficiently filter and retrieve important information during investigations and security monitoring activities.
