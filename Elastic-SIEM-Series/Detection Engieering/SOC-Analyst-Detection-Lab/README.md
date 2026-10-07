# SOC Analyst Detection Lab

### Project Objective

The goal of this project is to build a practical SOC environment where I can work through security alerts the way a Tier 1 SOC analyst would in a real environment.

Rather than only learning how individual security events work, I want to understand the full investigation process: what happened, which system and user were involved, whether the activity is expected or suspicious, what evidence supports the conclusion, and what should happen next.

The lab uses Elastic Security, Windows Event Logs, Sysmon, and controlled security activity to collect and investigate endpoint telemetry. I will use these events to practice alert triage, threat identification, MITRE ATT&CK and Cyber Kill Chain analysis, detection development, validation, and writing clear investigation reports.

The project will grow through individual investigation exercises, starting with Windows authentication events and eventually moving into process execution, PowerShell, network activity, suspicious behavior, detection rules, and complete SOC investigations.

The objective is not simply to generate alerts. It is to develop the ability to investigate them, understand the evidence, make a defensible assessment, and document the investigation clearly.


## SOC Detection Lab

### Project Objective

### Lab Environment

### Architecture

### Objectives

### Exercises

### 01. Windows Authentication Investigation

### 02. Windows Process Investigation

### 03. PowerShell Investigation

### 04. Network Activity Investigation

### 05. Alert Triage

### 06. MITRE ATT&CK Analysis

### 07. Cyber Kill Chain Analysis

### 08. Detection Development

### 09. Detection Validation

### 10. SOC Investigation Reports

## Detection Methodology

### MITRE ATT&CK Mapping

### Lessons Learned

### Conclusion

## Exercise 01 - Windows Authentication Investigation

## Failed Authentication

### Objective

The objective of this phase was to generate a controlled failed Windows authentication attempt from the Kali Linux machine and investigate the resulting Windows Security Event Log in Elastic.

The exercise was designed to understand what evidence a SOC analyst can obtain from a failed authentication event, including:

- The affected account
- The source system
- The source IP address
- The authentication method
- The Windows logon type
- The reason authentication failed
- The relevant Windows event ID
- The information available for determining whether the activity requires further investigation

This was performed entirely within the isolated SOC detection lab.

---

## Lab Scenario

A controlled authentication attempt was performed from the Kali Linux machine against the Windows 11 lab endpoint using SMB.

### Source

- **Host:** Kali Linux
- **IP:** `192.168.56.102`

### Target

- **Host:** Windows11-Lab
- **IP:** `192.168.56.101`
- **Service:** SMB
- **Port:** TCP/445

### Account

- **Username:** `socuser`
- **Account type:** Local Windows standard user

A deliberately incorrect password was supplied during the authentication attempt.

The purpose was to generate a Windows failed-logon event that could then be investigated in Elastic.

---

## Attack Simulation

The authentication attempt was generated from Kali using:

'smbclient -L //192.168.56.101 -U 'socuser'

An incorrect password was intentionally entered.

This produced a failed SMB authentication attempt against the Windows endpoint.

Note: This was a controlled lab activity against a Windows VM created specifically for security monitoring and detection practice.

## Windows Security Event

Elastic ingested the resulting Windows Security event through the Elastic Agent.

## Event ID
4625

## Event Type

Failed Logon



| Field                  | Observed Value                       |
| ---------------------- | ------------------------------------ |
| Event ID               | `4625`                               |
| Event Action           | `logon-failed`                       |
| Event Category         | `authentication`                     |
| Event Outcome          | `failure`                            |
| Target User            | `socuser`                            |
| Target Domain          | `WORKGROUP`                          |
| Source IP              | `192.168.56.102`                     |
| Source Host            | `KALI`                               |
| Target Host            | `Windows11-lab`                      |
| Logon Type             | `3 - Network`                        |
| Authentication Package | `NTLM`                               |
| Logon Process          | `NtLmSsp`                            |
| Failure Reason         | `Unknown user name or bad password.` |
| Status                 | `0xc000006d`                         |
| SubStatus              | `0xc000006a`                         |
| Source Port            | `35276`                              |


## Elastic Event Evidence

The event was observed in the system.security data stream.

Relevant fields included:

agent.name = Windows11-lab
data_stream.dataset = system.security
event.code = 4625
event.action = logon-failed
event.category = authentication
event.outcome = failure

user.name = socuser
source.ip = 192.168.56.102
source.domain = KALI
source.port = 35276

winlog.logon.type = Network
winlog.event_data.AuthenticationPackageName = NTLM
winlog.event_data.TargetUserName = socuser
winlog.event_data.TargetDomainName = WORKGROUP
winlog.event_data.FailureReason = Unknown user name or bad password.


## Windows Security Event 4624

**Report Type:** Authentication Event Analysis

**Severity:** Informational / Low

**Classification:** Benign / Expected System Activity

**Event ID:** 4624 - Successful Logon

**Data Source:** Windows Security Event Log

**SIEM:** Elastic Security

**Host:** Windows11-lab


## Executive Summary
A Windows Security Event ID **4624** was observed on the Windows11-lab endpoint indicating that the **SYSTEM** account successfully established a logon session.
The event records a **Service logon (Logon Type 5)** initiated by the Windows services.exe process. The authentication used the **Negotiate** authentication package, and the resulting session received an elevated token.
No source network address, workstation name, or source port was recorded for this event.
Based on the available telemetry, the activity is assessed as benign and consistent with normal Windows service activity. The combination of SYSTEM, Logon Type 5, services.exe, and the absence of a remote source is not, by itself, indicative of malicious activity.

## Event Details
| Field | Observed Value |
|---|---|
| Event ID | `4624` |
| Event Action | `logged-in` |
| Event Category | `authentication` |
| Event Outcome | `success` |
| Event Type | `start` |
| Provider | `Microsoft-Windows-Security-Auditing` |
| Channel | `Security` |
| Host | `Windows11-lab` |
| Host IP | `192.168.56.101` |
| User | `SYSTEM` |
| User Domain | `NT AUTHORITY` |
| User SID | `S-1-5-18` |
| Logon Type | `5 - Service` |
| Logon ID | `0x3e7` |
| Authentication Package | `Negotiate` |
| Logon Process | `Advapi` |
| Elevated Token | `Yes` |
| Virtual Account | `No` |
| Impersonation Level | `Impersonation` |
| Process | `C:\Windows\System32\services.exe` |
| Process ID | `836` |
| Source IP | Not present |
| Source Port | Not present |
| Workstation | Not present |


## Timeline
The log record contains the following timestamps:
| Timestamp | Field | Value |
|---|---|---|
| `2026-10-06 18:59:12.789Z` | `@timestamp` | Event document timestamp |
| `2026-10-06 16:11:09.249Z` | `event.created` | Event creation time |
| `2026-10-06 16:11:17.000Z` | `event.ingested` | Elastic ingestion time |

For investigation purposes, the report therefore records the timestamps exactly as provided by Elastic.

## Subject Account
The event identifies the account requesting the logon as:

Account Name:   WINDOWS11-LAB$

Account Domain: WORKGROUP

Security ID:    S-1-5-18

Logon ID:       0x3e7


The new logon session was created for:

Account Name:         SYSTEM

Account Domain:      NT AUTHORITY

Security ID:         S-1-5-18

Logon ID:            0x3e7


The important distinction is that this is not a remote socuser authentication.
This event represents the Windows SYSTEM account establishing a service logon session.


