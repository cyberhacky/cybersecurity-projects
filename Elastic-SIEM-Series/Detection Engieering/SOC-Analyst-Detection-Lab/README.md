# SOC Analyst Detection Lab

### Project Objective

The goal of this project is to build a practical SOC environment where I can work through security alerts the way a Tier 1 SOC analyst would in a real environment.

Rather than only learning how individual security events work, I want to understand the full investigation process: what happened, which system and user were involved, whether the activity is expected or suspicious, what evidence supports the conclusion, and what should happen next.

The lab uses Elastic Security, Windows Event Logs, Sysmon, and controlled security activity to collect and investigate endpoint telemetry. I will use these events to practice alert triage, threat identification, MITRE ATT&CK and Cyber Kill Chain analysis, detection development, validation, and writing clear investigation reports.

The project will grow through individual investigation exercises, starting with Windows authentication events and eventually moving into process execution, PowerShell, network activity, suspicious behavior, detection rules, and complete SOC investigations.

The objective is not simply to generate alerts. It is to develop the ability to investigate them, understand the evidence, make a defensible assessment, and document the investigation clearly.


# SOC Analyst Detection Lab

## Project Objective

## Lab Environment

## Architecture

## Objectives

## Exercises

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

## MITRE ATT&CK Mapping

## Lessons Learned

## Conclusion

# Exercise 01 — Windows Authentication Investigation

## Phase 3: Failed Authentication

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

```bash
smbclient -L //192.168.56.101 -U 'socuser'







