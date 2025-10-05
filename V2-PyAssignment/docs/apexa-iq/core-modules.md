---
id: core-modules
title: Core Modules
---

## 6. Core Modules

### 6.1 Unified Dashboard

The ApexaIQ Dashboard serves as the central command center, providing real-time visibility into your IT environment.

**Key Components:**

**Asset Summary Panel**
- **Total Assets:** Complete count of discovered devices
- **Active/Inactive Status:** Current operational state
- **Discovery Trends:** Historical asset discovery patterns
- **Shadow IT Indicators:** Newly discovered unauthorized assets

**ApexaIQ Score**
- **Composite Metric:** Overall IT hygiene rating (0-1000 scale)
- **Categories:** 
  - Poor (0-300): Critical issues require immediate attention
  - Average (301-700): Moderate risk, improvement needed
  - Good (701-850): Well-managed environment
  - Genius (851-1000): Exceptional IT hygiene
- **Trend Analysis:** Historical score progression with improvement tracking
- **Component Breakdown:** Individual scores for vulnerabilities, obsolescence, and compliance

**Vulnerability Score Dashboard**
- **Severity Classification:**
  - **Critical\:** Immediate action required (CVSS 9.0-10.0)
  - **High:** Priority remediation (CVSS 7.0-8.9)
  - **Medium:** Planned remediation (CVSS 4.0-6.9)
  - **Low:** Routine maintenance (CVSS 0.1-3.9)
- **Visual Indicators:** Color-coded severity levels with trend arrows
- **EPSS Integration\:** Exploit Prediction Scoring System for prioritization
<!-- -->
**IT Hygiene Metrics**
- **Obsolescence Tracking:** Assets at End-of-Life (EOL) or End-of-Maintenance (EOM)
- **Maintenance Status:** Expired support contracts and warranty tracking
- **Compliance Status:** Adherence to internal policies and regulatory requirements
- **Patch Management:** Missing critical updates and security patches

### 6.2 Comprehensive Inventory Management

**6.2.1 Device Inventory**

Provides detailed visibility into all discovered devices across the IT infrastructure.

**Device Categories:**
- **Servers:** Physical and virtual servers
- **Workstations:** Desktop and laptop computers
- **Network Equipment:** Routers, switches, firewalls, access points
- **Mobile Devices:** Smartphones, tablets, and wearables
- **IoT Devices:** Internet of Things and smart devices
- **Printers and Peripherals:** Network-attached devices

**Device Information:**
- **Identity:** Hostname, IP address, MAC address
- **Technical Specifications:** OS version, hardware specs, manufacturer
- **Network Details:** Subnet, VLAN, network segment
- **Security Status:** Individual ApexaIQ Risk Score, vulnerability count
- **Operational Status:** Last seen, connectivity status, performance metrics

**Risk Assessment Per Device:**
- **ApexaIQ Risk Score:** Individual device risk rating
- **Vulnerability Count:** Number of identified security issues
- **Obsolescence Status:** EOL/EOM warnings
- **Compliance Level:** Adherence to security policies

**6.2.2 User Account Management**

Comprehensive user identity and access management visibility.

**User Information Tracking:**
- **Identity Details:** Username, full name, email address, department
- **Account Status:** Active, inactive, locked, disabled
- **Access Patterns:** Last login, access frequency, unusual activity
- **Credential Health:** Password age, complexity compliance, expiration status

**Security Indicators:**
- **Stale Accounts:** Users with extended inactivity periods
- **Expired Passwords:** Overdue password changes
- **Privileged Access:** Administrative and elevated permissions
- **Multi-Factor Authentication:** MFA enrollment status

**Risk Metrics:**
- **New Users:** Recently created accounts requiring verification
- **Access Anomalies:** Unusual login patterns or locations
- **Dormant Accounts:** Long-term inactive accounts posing security risks

**6.2.3 Software Asset Management**

Complete visibility into all software installations across the environment.

**Software Catalog Integration:**
- **Master Repository:** Centralized database of all recognized software titles
- **Version Tracking:** Detailed version information and update status
- **Vendor Information:** Publisher details and support contact information
- **License Management:** Installation counts vs. licensed quantities

**Vulnerability Intelligence:**
- **CVE Mapping:** Direct linkage to National Vulnerability Database (NVD)
- **CVSS Scoring:** Industry-standard severity ratings
- **CPE Identification:** Common Platform Enumeration for precise identification
- **Patch Availability:** Available updates and security patches

**Lifecycle Management:**
- **End-of-Life Tracking:** Software approaching or past EOL dates
- **End-of-Support:** Vendor support termination dates
- **Upgrade Pathways:** Migration options for obsolete software
- **Business Impact:** Critical application dependencies

### 6.3 Advanced Vulnerability Management

**6.3.1 Vulnerability Discovery and Classification**

**Automated Vulnerability Detection:**
- **Continuous Scanning:** Regular vulnerability assessment cycles
- **Multi-Source Intelligence:** Integration with multiple vulnerability databases
- **Real-Time Updates:** Immediate notification of new vulnerabilities
- **Asset Correlation:** Automatic matching of vulnerabilities to specific assets

**Classification Standards:**
- **CVE Integration:** Common Vulnerabilities and Exposures database
- **CVSS Scoring:** Industry-standard severity ratings
- **CWE Mapping:** Common Weakness Enumeration categorization
- **EPSS Scoring:** Exploit Prediction Scoring for prioritization

**6.3.2 Remediation Automation**

**Automated Remediation Workflows:**
- **One-Click Remediation:** Single-click vulnerability resolution
- **Workflow Orchestration:** Multi-step remediation processes
- **Patch Management:** Automated update deployment
- **Configuration Changes:** Security setting adjustments

**Remediation Tracking:**
- **Progress Monitoring:** Real-time remediation status
- **Success Validation:** Verification of successful fixes
- **Rollback Capabilities:** Ability to reverse changes if needed
- **Documentation:** Automatic documentation of remediation actions

**6.3.3 Risk Prioritization**

**Intelligent Risk Scoring:**
- **Business Context:** Consideration of asset criticality
- **Threat Intelligence:** Current threat landscape analysis
- **Exploit Availability:** Known exploitation in the wild
- **Environmental Factors:** Network exposure and access controls

**Priority Matrix:**
- **Critical Path Analysis:** Vulnerabilities in critical systems
- **Attack Surface Assessment:** Exposure level evaluation
- **Cascading Risk:** Potential for lateral movement
- **Compliance Impact:** Regulatory requirement implications

### 6.4 Configuration and Automation Engine

**6.4.1 Rule Management System**

**Pre-Feed Enrichment Rules:**
- **Customization:** Client-specific data enrichment requirements
- **Manual Configuration:** Tailored rules based on organizational needs
- **Data Enhancement:** Additional context and metadata addition
- **Quality Improvement:** Data accuracy and completeness enhancement

**Post-Feed Classification Rules:**
- **Automated Processing:** Fully automated asset categorization
- **Machine Learning:** Intelligent classification algorithms
- **Consistency:** Standardized asset categorization across environments
- **Scalability:** Handles large-scale asset environments

**Remediation Rules:**
- **Action Automation:** Automated response to identified issues
- **Workflow Integration:** Connection to existing IT processes
- **Escalation Procedures:** Automatic escalation for critical issues
- **Audit Trails:** Complete record of automated actions

**6.4.2 Tagging and Categorization**

**Dynamic Tagging System:**
- **Automated Tagging:** Rule-based tag assignment
- **Manual Tagging:** User-defined categorization
- **Hierarchical Tags:** Multi-level organizational structure
- **Bulk Operations:** Mass tagging and categorization

**Business Alignment:**
- **Department Tags:** Organizational unit assignment
- **Function Tags:** Business purpose categorization
- **Criticality Tags:** Business importance levels
- **Location Tags:** Geographic and facility-based grouping

**6.4.3 Advanced Automation Features**

**Clone Jobs:**
- **Configuration Replication:** Duplicate successful configurations
- **Multi-Environment:** Deploy consistent rules across regions
- **Template Management:** Standardized deployment patterns
- **Version Control:** Track configuration changes

**Feed History:**
- **Activity Logging:** Complete record of all data collection activities
- **Performance Metrics:** Collection efficiency and success rates
- **Error Tracking:** Identification and resolution of issues
- **Audit Compliance:** Detailed logs for compliance requirements

**Duplication Management:**
- **Asset Deduplication:** Identify and merge duplicate entries
- **Conflict Resolution:** Handle conflicting asset information
- **Data Quality:** Maintain clean, accurate asset database
- **Reporting:** Track and report on deduplication activities
