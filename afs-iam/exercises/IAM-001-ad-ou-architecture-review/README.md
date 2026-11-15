# IAM-001 — Active Directory OU Architecture Review

## 1. Exercise Information

| Attribute | Details |
|---|---|
| Exercise ID | IAM-001 |
| Category | Identity and Access Management |
| Workstream | Active Directory Administration |
| Organization | Apex Financial Services |
| Domain | `corp.lab` |
| Domain Controller | AD-DC01 |
| Assessment Type | Read-only configuration review |
| Status | Planned |
| Authorization | Authorized AFS isolated lab |

## 2. Objective

Review the existing Active Directory Organizational Unit (OU) structure and compare it against the approved AFS Enterprise Cybersecurity Lab Master Blueprint.

Identify structural inconsistencies, misplaced objects and opportunities for improvement without modifying the directory.

## 3. Purpose and Security Relevance

A well-designed OU structure supports:

- Centralized identity administration.
- Logical departmental organization.
- Group Policy targeting.
- Delegated administration.
- Access management.
- Consistent enterprise directory governance.

Incorrect OU organization can complicate administration, policy application and access management.

## 4. Scope

**In scope:**
- AFS organizational root OU.
- Department OUs.
- Security sub-department OUs.
- Infrastructure OUs.
- Groups OUs.
- Service Accounts OU.
- Disabled Accounts OU.
- Existing object locations.

**Out of scope:**
- Creating or deleting OUs.
- Moving users or computers.
- Changing group memberships.
- Modifying Group Policy.
- Changing permissions or ACLs.

## 5. Prerequisites

- Administrative PowerShell access to AD-DC01.
- Active Directory PowerShell module.
- Operational `corp.lab` domain.
- Approved AFS Master Blueprint v1.1.
- Appropriate VM snapshot or backup before any later modification.

## 6. Initial Environment State

### Step 1 — Domain Controller Verification


**System:** AD-DC01

```powershell
hostname

Get-ADDomain | Select-Object DNSRoot, NetBIOSName, DomainMode

Get-Service NTDS, DNS
```

### Actual Results

![Image Alt](https://github.com/cyberhacky/cybersecurity-projects/blob/main/afs-iam/exercises/IAM-001-ad-ou-architecture-review/active.png?raw=true)

| Attribute | Observed Result |
|---|---|
| Hostname | AD-DC01 |
| DNSRoot | corp.lab |
| NetBIOSName | CORP |
| DomainMode | Windows2016Domain |
| NTDS service | Running |
| DNS service | Running |

### Analysis

The hostname and domain information match the established AFS environment.

Both Active Directory Domain Services (NTDS) and DNS services were observed in the Running state.

### Verification Status

**PASSED**

The domain controller and required services were verified as operational at the time of execution.

**Limitation:** This check does not independently validate DNS resolution, domain controller discovery, replication health or workstation connectivity.

## 7. Step-by-Step Methodology

### Step 1 — Import the Active Directory module

```powershell
Import-Module ActiveDirectory
```

### Step 2 — Retrieve the existing OU hierarchy

```powershell
Get-ADOrganizationalUnit `
  -SearchBase "OU=ApexFinancialServices,DC=corp,DC=lab" `
  -SearchScope Subtree `
  -Filter * |
Sort-Object DistinguishedName |
Select-Object Name, DistinguishedName |
Format-Table -AutoSize
```

### Step 3 — Inventory existing security groups

```powershell
Get-ADGroup `
  -SearchBase "OU=Groups,OU=ApexFinancialServices,DC=corp,DC=lab" `
  -SearchScope Subtree `
  -Filter * |
Sort-Object Name |
Select-Object Name, GroupScope, GroupCategory |
Format-Table -AutoSize
```

### Step 4 — Review object placement

Review the location of:
- Employee accounts.
- Computer accounts.
- Security groups.
- Service accounts.
- Administrative accounts.

### Step 5 — Compare against the approved architecture

Compare the actual directory structure against the AFS Master Blueprint v1.1.

Record:
- Matching structures.
- Missing OUs.
- Unexpected OUs.
- Structural deviations.
- Objects requiring further review.

### Step 6 — Document findings

Record all verified observations and supporting evidence.

Do not make directory changes under this exercise.

## 8. Expected Results

- A complete inventory of the AFS OU hierarchy.
- A list of existing security groups.
- Identification of structural differences.
- A documented recommendation for the next IAM activity.

These are expected outcomes, not confirmed findings.

## 9. Actual Results and Evidence

**Pending execution.**

Evidence will be added after the commands have been executed and their output reviewed.

## 10. Verification

Verification will establish that:
- The OU inventory completed successfully.
- The expected directory scope was queried.
- Group inventory was retrieved.
- Findings are supported by actual output.
- No directory configuration was modified.

## 11. Security Analysis

The review will evaluate whether the OU design supports centralized administration, appropriate Group Policy scope, separation of departments and least-privilege administration.

## 12. Limitations

This exercise is an OU architecture review. It does not establish effective user permissions, prove Group Policy application or validate all delegated administrative rights.

## 13. Cleanup and Rollback

No cleanup or rollback is required because the exercise is read-only.

## 14. Conclusion

**Status:** Planned.

The exercise will be marked completed only after execution, evidence collection, verification and documentation.

## 15. References

- AFS Enterprise Cybersecurity Lab Master Blueprint v1.1.
- Microsoft Active Directory Domain Services documentation.
- Microsoft Group Policy documentation.
