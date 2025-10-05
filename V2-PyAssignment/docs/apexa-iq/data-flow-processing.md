---
id: data-flow-processing
title: Data Flow & Processing
---

## 5. Data Flow & Processing

### 5.1 Data Flow Architecture

The ApexaIQ data flow follows a carefully orchestrated process designed to ensure data quality and actionable intelligence:

```
[Your Network] → [Accelerators] → [Raw Feed] → [Pre-Feed Rules] → [Dashboard] → [Post-Feed Rules] → [Classified Data] → [Enrichment] → [Reports]
```

![Flow of Data](./img/data-flow.png)

### 5.2 Stage-by-Stage Process

**Stage 1: Data Collection (Accelerators)**
- **Location:** Deployed in your network environment or AWS regions
- **Technology:** Python-based Docker containers
- **Methods:** NMAP scanning, WMI\(Windows Management Instrumentation\) queries, API integrations
- **Sources:** Network devices, security tools, cloud platforms, existing MDM systems
- **Frequency:** Automated 24-hour cycles via cronjobs

**Stage 2: Raw Feed Ingestion**
- **Purpose:** Initial data capture and validation
- **Process:** Raw data sent to ApexaIQ platform
- **Quality Control:** Data integrity checks and format validation

**Stage 3: Pre-Feed Rules (Automated)**
- **Function\:** Data cleaning and normalization
<!-- -->
- **Activities:**
  - Duplicate detection and merging
  - Data format standardization
  - Initial quality assessment
  - Conflict resolution using data source priority
- **Outcome:** Clean, consistent data ready for dashboard presentation

**Stage 4: Dashboard Presentation (SaaS)**
- **Interface:** Real-time web-based dashboard
- **Features:** Interactive visualizations, filtering, and search capabilities
- **Access Control:** Role-based views and permissions

**Stage 5: Post-Feed Rules (Automated)**
- **Purpose:** Data classification and categorization
- **Process:** Automated sorting into three core categories:
  - **Devices:** Physical and virtual machines, network equipment
  - **Users:** User accounts and access credentials
  - **Software:** Applications, operating systems, and licenses
- **Intelligence:** Risk scoring and vulnerability correlation

**Stage 6-8: Enrichment and User Input**
- **Enrichment Rules:** Custom rules based on client requirements
- **User Input:** Manual additions, corrections, and contextual information
- **Tagging:** Organizational and functional categorization

**Stage 9: Export and Integration**
- **Output Formats:** CSV, JSON, API feeds
- **Destinations:** S3 buckets, SIEM systems, other security tools
- **Scheduling:** Automated and on-demand exports

### 5.3 Data Source Priority Management

**Challenge:** Multiple sources may provide conflicting information about the same asset.

**Solution:** Data Source Priority system allows administrators to:
- **Rank Sources:** Establish hierarchy of trust
- **Resolve Conflicts:** Highest-priority source becomes "single source of truth"
- **Maintain Consistency:** Ensures reliable, consistent asset information
- **Adapt Over Time:** Adjust priorities based on source reliability

**Example Priority Hierarchy:**
1. MDM Database (highest priority)
2. Active Directory
3. NMAP Discovery
4. Manual Input
5. Legacy Systems (lowest priority)
