# Health Care Data Analysis
#### Author: Prashant Shrestha

The project aims to analyze the CMS Part D data. Some dashboards are also made in this project for visualization.

### Tech Stack
- Storage: Psql
- Cleaning: Pandas, Psql
- Visualization: Tableau



### Data Source
- Source of raw data is from [CMS](https://data.cms.gov/provider-summary-by-type-of-service).
- Data used is [Medicare Part D Prescribers - by Provider and Drug](https://data.cms.gov/search?keywords=Medicare%20Part%20D%20Prescribers%20-%20by%20Provider%20and%20Drug&sort=Relevancy).
- General description of data is present at data/dataDescription


### Data Processing Steps (Summary)
1. **Data Extraction**: Extracted raw CMS Part D data from the source CSV file using Pandas, processing it in chunks to handle large data volumes efficiently.
2. **Data Cleaning**: Removed rows with null values in key summarized data columns and dropped irrelevant columns to focus on meaningful data for analysis.
3. **Data Storage**: Loaded the cleaned data chunks into a PostgreSQL database for efficient storage and querying.
4. **Data Analysis**: Performed SQL-based analyses in PostgreSQL to investigate prescriber performance, drug prescription patterns, cost trends, age-based insights, and geographical variations. Detailed findings are documented in `docs/findings.md`.

### Analysis and Findings
The project includes a comprehensive analysis of the CMS Part D data, with key findings summarized in `docs/findings.md`. Notable insights include:
- Identification of high-cost prescribers and drugs, highlighting potential areas for cost reduction.
- Regional variations in prescription practices, particularly the dominance of the Varicella-Zoster vaccine in many states.
- Age-specific prescription patterns, showing drugs exclusively prescribed to patients aged 65 and over.
- Cost comparisons between brand and generic drugs, revealing significant price variations.