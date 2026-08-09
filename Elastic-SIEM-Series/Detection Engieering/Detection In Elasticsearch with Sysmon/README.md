# Detection #1: PowerShell Encoded Command Execution

## Detection Objective

The objective of this detection is to identify the execution of PowerShell commands using the `-EncodedCommand` (`-e`) parameter on Windows endpoints.

PowerShell encoded commands can conceal the actual command content from casual inspection and may be used by attackers as part of command execution and defense-evasion activity. The detection therefore monitors Windows Sysmon Process Creation events (Event ID 1) for `powershell.exe` processes where the `-e` argument is present.

The detection was developed and tested in a controlled Windows 11 lab environment using Elastic Security, Elastic Agent/Filebeat, and Sysmon. A controlled encoded PowerShell command was executed to validate that the telemetry was generated, ingested into Elastic, matched by the detection rule, and ultimately produced a security alert.

The primary objective was to validate the complete detection pipeline:

Windows endpoint → Sysmon → Elastic Agent → Elastic Security → Detection Rule → Security Alert

The detection is mapped to MITRE ATT&CK technique **T1059.001 – PowerShell** and is intended to provide analysts with an initial signal for investigating potentially suspicious PowerShell execution.

## Tools Used

The detection was developed, tested, and validated using the following tools and technologies:

| Tool / Technology | Purpose |
|---|---|
| **Windows 11** | Endpoint used to generate and validate PowerShell process execution telemetry. |
| **Sysmon** | Generated Windows process creation telemetry, specifically **Event ID 1**, for `powershell.exe`. |
| **Elastic Agent / Filebeat** | Collected and forwarded Windows/Sysmon telemetry into Elasticsearch. |
| **Elasticsearch** | Stored and indexed the endpoint telemetry used by the detection rule. |
| **Elastic Security** | Used to create, execute, and validate the custom detection rule and generate security alerts. |
| **Kibana Discover** | Used to query and inspect Sysmon events and verify the collected telemetry before creating the detection. |
| **PowerShell** | Used to generate controlled PowerShell execution activity, including an encoded command for detection validation. |

### Detection Pipeline

```text
Windows 11
    ↓
Sysmon
    ↓
Elastic Agent / Filebeat
    ↓
Elasticsearch
    ↓
Kibana Discover
    ↓
Elastic Security Detection Rule
    ↓
Security Alert
