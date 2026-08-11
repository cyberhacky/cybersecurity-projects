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

Windows 11

Sysmon

Elastic Agent / Filebeat

Elasticsearch

Kibana Discover

Elastic Security Detection Rule

Security Alert

## Step 1: Install and Configure Sysmon

The first step in building the detection was to install and configure **Microsoft Sysmon (System Monitor)** on the Windows 11 endpoint.

Sysmon was required because the detection depends on detailed Windows process creation telemetry. In particular, the detection uses **Sysmon Event ID 1 (Process Create)** to identify the execution of `powershell.exe` and inspect its command-line arguments.

### Why Sysmon?

Windows process creation events provide important information about processes running on an endpoint. Sysmon extends this visibility by recording detailed process activity, including fields such as:

- Process name
- Process executable path
- Process ID
- Parent process
- Parent process ID
- User account
- Command-line arguments
- Process creation timestamp

This telemetry provides the data required by the Elastic detection rule.

### Sysmon Setup

Sysmon was installed on the Windows 11 lab machine and configured to monitor process creation activity.

After installation, the Sysmon service was started and verified to ensure that it was actively generating telemetry.

The relevant Sysmon event channel used for validation was:

Microsoft-Windows-Sysmon/Operational

 I used the following PowerShell command to verify that Sysmon was generating Process Create events after installing:
Get-WinEvent -FilterHashtable @{LogName="Microsoft-Windows-Sysmon/Operational"; Id=1} -MaxEvents 5

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det1.png?raw=true)

This confirmed that Sysmon was successfully running and generating the process creation telemetry required for the detection.

## Step 2: Verify Elastic Agent and Sysmon Connectivity

After configuring Sysmon, the next step was to verify that the **Elastic Agent** was running and able to collect the Sysmon telemetry generated on the Windows 11 endpoint.

The Elastic Agent is responsible for collecting the Sysmon events and forwarding them to the Elastic environment for indexing and analysis.

### Verify Elastic Agent Status

The Elastic Agent service was first checked to confirm that it was running correctly on the Windows 11 endpoint.

Get-Service | Where-Object {$_.Name -match "filebeat|elastic"} | Select-Object Name,DisplayName,Status,StartType

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det2.png?raw=true)

 & "C:\Program Files\Elastic\Agent\elastic-agent.exe" status

 ![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det3.png?raw=true)

 
## Step 3: Add the Windows Integration

After verifying that the Elastic Agent was running, the next step was to add the **Windows integration** to the Agent policy.

The Windows integration provides the configuration required for collecting Windows event logs, including the Sysmon operational event channel used by this detection.

### Add the Windows Integration

In Kibana, navigate to:

Fleet

Agent policies

Windows Agent Policy

Add integration

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det4.png?raw=true)

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det5.png?raw=true)

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det7.png?raw=true)

In the Select Integration search bar, type Windows and select it.

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det8.png?raw=true)

After selecting Windows, leave the default configuration unchanged because it already includes the Sysmon Operational event log. Then click Add integration. 

Now that the Windows integration is configured to collect Sysmon telemetry through the Elastic Agent, the next step is to create the detection rule.

In Kibana, navigate to:

Security → Rules → Detection rules (SIEM)

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detection.png?raw=true)

After clicking Detection rules (SIEM) click Create a rule

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/det.png?raw=true)

In the Create new rule window, select the first rule type, Custom query.

The Custom query rule type allows us to use KQL or Lucene to search the indexed telemetry and define the conditions that should trigger our detection.

For this detection, we will use a Custom query because we want to specifically identify PowerShell process creation events containing an encoded-command argument.

### Configure the Rule Source

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect24.png?raw=true)

Select Index Patterns as the rule's data source and include the Sysmon index:

logs-windows.sysmon_operational-*

This ensures that the detection rule searches the Elasticsearch indices containing the Windows Sysmon telemetry collected from the endpoint.

### Define the Custom Query

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect25.png?raw=true)

Under Custom query, enter the KQL query used to identify encoded PowerShell execution:

event.provider:"Microsoft-Windows-Sysmon"
and event.code:"1"
and process.name:"powershell.exe"
and process.args:"-e"

The query looks for Sysmon Process Creation events (Event ID 1) where the created process is powershell.exe and the process arguments contain the -e parameter associated with PowerShell encoded-command execution.

## Configure the Detection Rule

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect3.png?raw=true)

This query identifies Sysmon Process Creation events where powershell.exe is executed with the -e argument.
After defining the index pattern and custom query, the next step was to configure the detection rule itself.

### Rule Definition

The rule was configured as a **Custom Query** rule using the Sysmon telemetry and KQL query defined in the previous step.

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect4.png?raw=true)

### Rule Metadata or About rule
The rule was given the name:

PowerShell Encoded Command Execution

The description explains the purpose of the detection:

Detects Windows PowerShell process creation events where an encoded command argument is used. Encoded PowerShell commands can obscure command content and are commonly associated with defense evasion and execution techniques.

The default severity was set to Medium to indicate that the behavior warrants investigation but does not, by itself, establish that malicious activity has occurred.

### Rule Tags

I added Tags to make the detection easier to categorize and identify during security operations.

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect5.png?raw=true)

 I used these tags:

PowerShell
Sysmon
Windows
MITRE ATT&CK
T1059.001
Encoded Command
Detection Engineering

To tags associate the detection with the technology being monitored, the telemetry source, the relevant operating system, the MITRE ATT&CK technique, and the detection-engineering use case.

### Schedule the Detection Rule

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect6.png?raw=true)

I configured the rule to execute every 5 minutes.

An additional 1-minute look-back period was configured to reduce the possibility of missing events that arrive shortly before or during a rule execution.

The schedule was therefore configured as:

Execution interval: 5 minutes
Additional look-back time: 1 minute

This means Elastic periodically evaluates the configured query against recent telemetry and generates an alert when matching events are identified.

The next step is to configure rule actions and connectors, such as email or other notification channels, to notify analysts when the detection generates an alert. For this lab, we will leave the connector configuration unchanged and proceed by clicking Create & enable rule.

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect7.png?raw=true)


Now that the detection rule has been created and enabled, the next step is to test the rule by executing a controlled encoded PowerShell command and verifying that the activity is detected and generates a security alert.

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect8.png?raw=true)
![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/Elastic-SIEM-Series/Detection%20Engieering/Detection%20In%20Elasticsearch%20with%20Sysmon/detect9.png?raw=true)

### Testing the Detection with Atomic Red Team


To validate the detection rule, I used **Atomic Red Team** to execute a controlled simulation of **MITRE ATT&CK technique T1059.001 – PowerShell** on the Windows 11 lab endpoint.

### What is Atomic Red Team?

**Atomic Red Team** is a library of small, focused security tests that map to techniques in the **MITRE ATT&CK** framework. These tests allow security practitioners to simulate adversary behaviors in a controlled environment and determine whether their security controls, such as endpoint telemetry, SIEM detections, and alerting rules, can identify the activity.

### Why use Atomic Red Team?

Atomic Red Team was used because the detection is mapped to **T1059.001 – PowerShell.** Rather than manually executing an arbitrary test command, an Atomic Red Team test provides a structured and repeatable way to simulate PowerShell-related adversary behavior.

For this validation, the objective was to confirm the complete detection workflow:

Atomic Red Team Test
        ↓
PowerShell Execution
        ↓
Sysmon Event ID 1
        ↓
Elastic Agent
        ↓
Elasticsearch
        ↓
Elastic Detection Rule
        ↓
Security Alert


