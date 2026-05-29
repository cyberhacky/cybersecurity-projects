# SQL Date and Numeric Filtering Lab

## Investigating Security Events Using SQL Date, Time, and Numeric Filters

---

# Overview

In this lab, I applied advanced SQL filtering techniques within the MariaDB environment to investigate authentication events related to a simulated security incident. The investigation focused on filtering login attempts using dates, times, and event identifiers to isolate relevant records and improve the efficiency of incident analysis.

As a cybersecurity analyst, the ability to filter large datasets is critical when investigating suspicious activity. Security logs often contain thousands of events, making it necessary to narrow searches using operators such as `>`, `<`, `>=`, `<=`, and `BETWEEN`.

This project demonstrates practical experience using SQL operators to investigate authentication activity and identify records relevant to a security incident.

---

# Objectives

* Retrieve login attempts occurring after a specific date
* Filter authentication records within a defined date range
* Investigate login activity occurring outside normal business hours
* Analyze security events using numeric event identifiers
* Apply SQL comparison operators to security investigations
* Improve incident response and log analysis skills

---

# Environment

| Component             | Details                     |
| --------------------- | --------------------------- |
| Database              | MariaDB                     |
| Database Name         | organization                |
| Table Used            | log_in_attempts             |
| Operating Environment | Linux Bash Shell            |
| Investigation Type    | Authentication Log Analysis |

---

# Task 1 – Retrieve Login Attempts After a Certain Date

## Query Login Attempts After May 9, 2022

### SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_date > '2022-05-09';
```

### Purpose

The purpose of this query was to identify all authentication events that occurred after May 9, 2022. This allowed the investigation to focus on activity occurring after the suspected incident date.

### Analysis

The query returned **125 login attempts** that occurred after **2022-05-09**. Narrowing authentication records to activity occurring after a specific date is a common incident response technique used to focus investigations on events that occurred after a suspected compromise or security alert.

### Key Findings

* 125 login attempts occurred after 2022-05-09.
* Date filtering significantly reduced the investigation scope.
* Relevant authentication activity was isolated for review.

### What I Learned

Through this exercise, I learned how SQL comparison operators such as `>` can be used to investigate authentication events occurring after a specific date. These techniques are essential when investigating security incidents and narrowing large datasets to a relevant timeframe.

---

## Query Login Attempts On or After May 9, 2022

### SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_date >= '2022-05-09';
```

### Purpose

This query expanded the investigation scope by including events that occurred on the incident date itself.

### Analysis

Including **2022-05-09** increased the result set to **165 login attempts**. This demonstrated how including a single day can significantly affect the volume of records available for analysis and highlights the importance of defining investigation timelines accurately.

### Key Findings

* 165 login attempts occurred on or after 2022-05-09.
* Including the incident date expanded the investigation scope.
* Timeline accuracy is critical during incident investigations.

### What I Learned

I learned the difference between the `>` and `>=` operators and how small changes in filtering logic can significantly impact the records returned during a security investigation.

---

# Task 2 – Retrieve Logins Within a Date Range

## Filter Login Attempts Between Two Dates

### SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';
```

### Purpose

The objective of this query was to limit the investigation to a specific timeframe surrounding the security incident.

### Analysis

Filtering authentication records between **2022-05-09** and **2022-05-11** returned **123 login attempts**. Restricting the investigation to a defined timeframe provided a focused view of authentication activity surrounding the incident period.

Reviewing a smaller set of records improves investigation efficiency and reduces the likelihood of overlooking relevant events hidden within larger datasets.

### Key Findings

* 123 authentication events occurred during the investigation period.
* Date range filtering reduced unnecessary records.
* Focused datasets improve investigation efficiency.

### What I Learned

This task improved my understanding of the `BETWEEN` operator and its use in filtering records within a specified date range. I learned how date-based filtering helps security analysts focus on activity occurring during an incident window while reducing unnecessary data.

---

# Task 3 – Investigate Logins at Certain Times

## Retrieve Login Attempts Before Normal Business Hours

### SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00';
```

### Purpose

The purpose of this query was to identify users accessing systems before normal working hours.

### Analysis

Authentication events occurring outside standard business hours may indicate unusual user behavior, compromised accounts, or unauthorized access attempts. Time-based filtering provides valuable context when reviewing authentication activity.

### What I Learned

I learned how time-based filtering can support threat hunting and incident investigations by identifying anomalous login behavior outside normal business hours.

---

## Retrieve Login Attempts Between 06:00 and 07:00

### SQL Query

```sql
SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00';
```

### Purpose

This query narrowed the investigation to a specific one-hour window immediately before business operations began.

### Analysis

The investigation focused on authentication activity occurring outside standard business hours. Login attempts between **06:00:00** and **07:00:00** were isolated to identify potentially unusual user behavior before the start of the normal workday.

The earliest login observed within this timeframe occurred at **06:01:31**. Examining authentication events during off-hours can help identify compromised accounts, unauthorized access attempts, or employees accessing systems outside normal operating procedures.

### Key Findings

* Early morning authentication activity was successfully isolated.
* The earliest login attempt occurred at **06:01:31**.
* Time-based filtering is valuable for identifying potentially suspicious activity.

### What I Learned

I learned how to use the `BETWEEN` operator with time values to isolate specific login windows. This skill is valuable when investigating unusual authentication activity occurring during non-business hours.

---

# Task 4 – Investigate Login Attempts by Event ID

## Retrieve Events with IDs Greater Than or Equal to 100

### SQL Query

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100;
```

### Purpose

The objective was to investigate a subset of authentication events based on their event identifier values.

### Analysis

Filtering by event ID can help analysts focus on specific event ranges associated with alerts, incidents, or batches of security logs. This approach improves investigation speed when reviewing large volumes of records.

### What I Learned

I learned how numeric filtering can improve efficiency when investigating large volumes of security events and authentication logs.

---

## Retrieve Events with IDs Between 100 and 150

### SQL Query

```sql
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150;
```

### Purpose

This query further narrowed the event scope to a smaller range of security records.

### Analysis

Event identifiers were used to narrow the investigation to a targeted subset of authentication records.

Within the filtered results:

* The third returned record was associated with the login date **2022-05-09**
* The fifth returned record belonged to the user **eraab**
* The seventh returned record belonged to the user **tmitchel**

These findings demonstrate how event identifiers can be used to quickly locate and review specific authentication events during security investigations.

### Key Findings

* Event ID filtering reduced the volume of authentication records requiring review.
* The filtered dataset contained users from multiple departments and locations.
* Event-based filtering improved investigation precision and efficiency.

### What I Learned

This task taught me how to filter records using numeric values and event identifiers. I learned that event IDs can be used to quickly isolate specific groups of security events without reviewing an entire log dataset.

---

# Investigation Summary

The SQL investigation demonstrated how date, time, and numeric filters can be used to efficiently analyze authentication activity during a security incident.

### Investigation Findings

* 125 login attempts occurred after the incident date.
* 165 login attempts occurred on or after the incident date.
* 123 authentication events occurred within the defined investigation window.
* Early-morning login activity was successfully isolated for review.
* The earliest observed login during the specified timeframe occurred at **06:01:31**.
* Event ID filtering enabled rapid identification of specific authentication records and users.

These techniques mirror real-world security operations workflows where analysts must quickly reduce large datasets into manageable and relevant records for investigation.

---

# Overall Learning Outcome

## What I Learned From This Lab

This lab strengthened my ability to use SQL as a tool for cybersecurity investigations. I gained practical experience filtering authentication logs using dates, times, and numeric identifiers to locate relevant security events. I also developed a better understanding of how security analysts reduce large datasets into manageable records during incident response, threat hunting, and security monitoring activities.

### Skills Developed

* Date-based security log analysis
* Time-based authentication investigation
* Numeric filtering using event identifiers
* SQL comparison operators (`>`, `<`, `>=`, `<=`)
* Range filtering using `BETWEEN`
* Security event investigation and log analysis
* Database querying within a MariaDB environment

These skills are directly applicable to Security Operations Center (SOC) environments, incident response investigations, threat hunting, and security monitoring activities.

---

# Key Takeaways

* Applied comparison operators (`>`, `<`, `>=`) to investigate authentication activity.
* Used `BETWEEN` to isolate records within defined date and event ranges.
* Analyzed login activity occurring outside normal business hours.
* Investigated authentication records using event identifiers.
* Improved proficiency in SQL-based security investigations and log analysis.
* Strengthened practical skills applicable to incident response, threat hunting, and SOC operations.

---

# Conclusion

This lab provided hands-on experience applying SQL operators to investigate authentication activity within a database environment. By filtering records using dates, times, and numeric identifiers, I was able to efficiently isolate relevant events and reduce investigation scope.

These SQL techniques are foundational skills for cybersecurity professionals involved in security monitoring, threat hunting, digital forensics, and incident response. The ability to accurately retrieve and analyze security-related data is critical for identifying suspicious activity and supporting effective security operations.

---

# Author

## Cornelius Donkor

**Cybersecurity Professional | Security Analyst | SQL & Linux Enthusiast**
