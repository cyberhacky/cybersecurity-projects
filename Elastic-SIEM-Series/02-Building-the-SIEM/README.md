# Building a Security Information and Event Management (SIEM) Platform with Elastic Security

## Overview

Security Information and Event Management (SIEM) platforms enable organizations to centralize logs, monitor infrastructure, detect threats, investigate security incidents, and respond to attacks from a single platform.

In this project, I built a production-style SIEM environment using the Elastic Stack. The environment collects telemetry from both Windows and Linux endpoints through Elastic Agent and Fleet, normalizes the data using the Elastic Common Schema (ECS), and provides centralized visibility into authentication activity, endpoint health, operating system events, and security logs.

Rather than focusing solely on deployment, this project demonstrates how a SIEM is configured, validated, and prepared for security operations.

---

## Objectives

- Configure a centralized SIEM platform
- Collect Windows and Linux logs
- Normalize events using ECS
- Validate data ingestion
- Build reusable data views
- Create KQL searches
- Prepare data for dashboards
- Build the foundation for threat detection and incident response

---

## Technologies Used

- Elasticsearch
- Kibana
- Elastic Security
- Fleet Server
- Elastic Agent
- Windows 11
- Ubuntu Linux
- Microsoft Azure
- TLS
- Elastic Common Schema (ECS)

---

## Lab Architecture

(Add architecture diagram here)

```

Windows Endpoint
        │
Elastic Agent
        │
        ▼
Fleet Server
        │
        ▼
Elasticsearch
        │
        ▼
Kibana
        │
        ▼
Security Operations Center

```

---

## Lab Environment

| Component | Purpose |
|-----------|----------|
| Ubuntu Server | Elasticsearch, Kibana, Fleet Server |
| Windows 11 | Endpoint |
| Elastic Agent | Endpoint telemetry |
| Fleet | Agent management |
| Elasticsearch | Log storage |
| Kibana | Visualization and investigation |

---

## Project Phases

- Phase 1 – Creating Data Views
- Phase 2 – Exploring Data with Discover
- Phase 3 – Building Saved Searches
- Phase 4 – Creating Visualizations
- Phase 5 – Building SOC Dashboards
- Phase 6 – Detection Engineering
- Phase 7 – Alerting
- Phase 8 – Threat Hunting

---

## Skills Demonstrated

- SIEM Administration
- Log Management
- Endpoint Monitoring
- Fleet Management
- Elastic Agent
- KQL
- ECS
- Security Monitoring
- Windows Event Analysis
- Linux Log Analysis

---

## Repository Structure

```
02-Building-the-SIEM/

README.md

architecture/

screenshots/

discover/

saved-searches/

kql/

visualizations/

dashboards/

detections/

alerts/

notes/
```
