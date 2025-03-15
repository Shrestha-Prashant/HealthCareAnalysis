# CMS Part D Data Analysis Queries

This document contains the SQL queries used to analyze the CMS Part D data stored in a PostgreSQL database. Each query is designed to answer specific questions about prescriber performance, drug prescription patterns, cost trends, age-based insights, and geographical variations. The queries are presented with their purpose and SQL code.

## 1. Unique Prescriber Count
**Purpose:** Determine the total number of unique prescribers in the dataset to establish the scale of healthcare providers.

**Query:**
```sql
SELECT COUNT(DISTINCT prscrbr_npi) AS PRESCRIBER_COUNT 
FROM cms;
```

## 2. Counting Unique Drugs by Generic Name
**Purpose:** Calculate the number of unique generic drugs prescribed to understand the diversity of treatments.

**Query:**
```sql
SELECT COUNT(DISTINCT Gnrc_Name) AS GENERIC_COUNT 
FROM cms;
```

## 3. Top 10 Prescribers by Total Drug Cost
**Purpose:** Identify the top 10 prescribers with the highest total drug costs to highlight potential outliers for cost management.

**Query:**
```sql
SELECT 
    prscrbr_npi,
    prscrbr_last_org_name AS last_name, 
    prscrbr_first_name AS first_name, 
    ROUND(SUM(tot_drug_cst::numeric), 2) AS total_drug_cost
FROM cms
GROUP BY prscrbr_npi, prscrbr_last_org_name, prscrbr_first_name
ORDER BY total_drug_cost DESC
LIMIT 10;
```

## 4. Top 10 Most Prescribed Drugs by Total Claims
**Purpose:** Find the 10 most frequently prescribed drugs by total claims to identify common treatments and potential cost-saving opportunities.

**Query:**
```sql
SELECT 
    gnrc_name AS drug_name, 
    SUM(tot_clms) AS total_claims
FROM cms
GROUP BY gnrc_name
ORDER BY total_claims DESC
LIMIT 10;
```

## 5. Most Prescribed Drug in Each State
**Purpose:** Determine the most prescribed drug in each state to highlight regional variations in prescription practices.

**Query:**
```sql
SELECT 
    c.prscrbr_state_abrvtn AS state, 
    c.gnrc_name AS drug_name, 
    m.max_clms AS prescribed_drugs
FROM cms c 
INNER JOIN (
    SELECT 
        prscrbr_state_abrvtn, 
        MAX(tot_clms) AS max_clms 
    FROM cms 
    GROUP BY prscrbr_state_abrvtn
) m
ON c.prscrbr_state_abrvtn = m.prscrbr_state_abrvtn 
AND c.tot_clms = m.max_clms;
```

## 6. Top Drug Prescribed by Each Prescriber Type
**Purpose:** Identify the most prescribed drug for each prescriber type to examine specialization and prescribing trends.

**Query:**
```sql
SELECT 
    c.prscrbr_type AS Prescriber_type, 
    c.gnrc_name AS drug_name, 
    m.max_clms AS prescribed_drugs
FROM cms c 
INNER JOIN (
    SELECT 
        prscrbr_type, 
        MAX(tot_clms) AS max_clms 
    FROM cms 
    GROUP BY prscrbr_type
) m
ON c.prscrbr_type = m.prscrbr_type 
AND c.tot_clms = m.max_clms;
```

## 7. Average Cost Per Claim for Each Brand of a Generic Drug
**Purpose:** Calculate the average cost per claim for each brand of a generic drug to compare costs and identify cost-saving opportunities.

**Query:**
```sql
SELECT 
    Gnrc_Name, 
    Brnd_Name, 
    ROUND(AVG(Tot_Drug_Cst / Tot_Clms)::numeric, 3) AS avg_cost_per_claim 
FROM cms 
GROUP BY Gnrc_Name, Brnd_Name 
ORDER BY Gnrc_Name, avg_cost_per_claim DESC;
```

## 8. Top 10 Drugs Most Prescribed to Patients Aged 65 and Over
**Purpose:** Find the top 10 drugs with the highest prescription ratios for patients aged 65 and over to inform elderly care strategies.

**Query:**
```sql
SELECT 
    Gnrc_Name, 
    SUM(GE65_Tot_Clms) AS total_claims_ge65, 
    SUM(Tot_Clms) AS total_claims, 
    ROUND((SUM(GE65_Tot_Clms) * 1.0 / SUM(Tot_Clms))::numeric, 3) AS ratio_ge65 
FROM cms 
GROUP BY Gnrc_Name 
ORDER BY ratio_ge65 DESC;
```

## 9. Prescribers with Above-Average Cost Per Claim
**Purpose:** Identify prescribers with an average cost per claim above the overall average.

**Query:**
```sql
SELECT 
    prscrbr_npi, 
    prscrbr_last_org_name,
    prscrbr_first_name,
    SUM(tot_drug_cst) / SUM(tot_clms) AS avg
FROM cms 
GROUP BY prscrbr_npi, prscrbr_last_org_name, prscrbr_first_name
HAVING SUM(tot_drug_cst) / SUM(tot_clms) > (
    SELECT SUM(tot_drug_cst) / SUM(tot_clms) 
    FROM cms
);
```

## 10. States Sorted by Average Total Drug Cost Per Prescriber
**Purpose:** Rank states by their average total drug cost per prescriber.

**Query:**
```sql
SELECT 
    c.prscrbr_state_abrvtn, 
    ROUND(AVG(c.per_prscrbr_tot_drug_cst)::numeric, 3) AS avg_tot_drug_cst_per_prescriber
FROM (
    SELECT 
        prscrbr_state_abrvtn,
        prscrbr_npi,
        SUM(tot_drug_cst) AS per_prscrbr_tot_drug_cst 
    FROM cms 
    GROUP BY prscrbr_state_abrvtn, prscrbr_npi
) AS c
GROUP BY c.prscrbr_state_abrvtn
ORDER BY avg_tot_drug_cst_per_prescriber DESC;
```