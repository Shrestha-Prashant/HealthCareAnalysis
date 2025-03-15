# CMS Part D Data Analysis Findings

This document presents the findings from the analysis of the CMS Part D data, focusing on key questions about prescriber performance, drug prescription patterns, cost trends, age-based insights, and geographical variations. Each section includes the question (objective) and the corresponding finding, with tables provided where results are best presented in tabular form.

## 1. Scale of Prescribers
**Question:** What is the total number of unique prescribers in the dataset?

**Finding:** The dataset includes 552,142 unique prescribers, indicating a large and diverse population of healthcare providers, which provides a robust basis for detailed analysis.

## 2. Diversity of Drugs
**Question:** How many unique generic drugs are prescribed in the dataset?

**Finding:** There are 1,041 unique generic drugs, reflecting a wide variety of treatments and potential areas for cost and prescription pattern analysis.

## 3. High-Cost Prescribers by Total Drug Cost
**Question:** Who are the top 10 prescribers by total drug cost, and what are their costs?

**Finding:** The top prescribers by total drug cost have costs ranging from approximately $20 million to $48 million, with significant variation. This suggests potential outliers who may be prescribing high-cost specialty drugs or treating large patient volumes, warranting further investigation into their prescribing practices.

| Prescriber NPI | Last Name   | First Name | Total Drug Cost ($) |
|----------------|-------------|------------|---------------------|
| 1639279417     | Azad        | Armaghan   | 48,512,764.16       |
| 1356534994     | Davis       | Cedric     | 40,839,016.19       |
| 1285683755     | Champion    | Hunter     | 25,145,792.94       |
| 1336222504     | Morton      | Robert     | 24,485,497.79       |
| 1902831761     | Mcconnell   | John       | 20,766,215.42       |
| 1609936046     | Geary       | Maureen    | 18,342,266.29       |
| 1366754715     | Hinojosa    | Kim        | 17,736,705.13       |
| 1649365529     | Alul        | Rushdi     | 17,345,124.20       |
| 1871547596     | Garcia      | Elvin      | 17,052,048.59       |
| 1265429617     | Bogdasarian | John       | 16,812,166.18       |

## 4. Most Prescribed Drugs by Total Claims
**Question:** What are the top 10 most prescribed drugs by total claims?

**Finding:** The top drugs by claims are primarily used for chronic conditions (e.g., cholesterol, blood pressure, thyroid), indicating widespread use. High prescription volumes suggest potential cost-saving opportunities through generic substitution or bulk purchasing agreements.

| Drug Name             | Total Claims  |
|-----------------------|---------------|
| Atorvastatin Calcium  | 28,178,953    |
| Gabapentin            | 14,086,754    |
| Amlodipine Besylate   | 13,617,701    |
| Levothyroxine Sodium  | 12,862,794    |
| Lisinopril            | 10,606,087    |
| Hydrocodone/Acetaminophen | 10,161,713 |
| Omeprazole            | 9,368,946     |
| Metformin Hcl         | 8,417,973     |
| Losartan Potassium    | 7,124,437     |
| Metoprolol Succinate  | 7,038,492     |

## 5. Most Prescribed Drug in Each State
**Question:** What is the most prescribed drug in each state, and how many claims does it have?

**Finding:** The Varicella-Zoster vaccine (Shingrix) dominates as the most prescribed drug in most states, likely due to its use in preventing shingles in older adults. Exceptions like Kentucky and Louisiana, where hydrocodone/acetaminophen is most prescribed, may indicate regional differences in pain management practices or healthcare priorities.

| State | Drug Name                     | Prescribed Drugs (Claims) |
|-------|-------------------------------|---------------------------|
| RI    | Varicella-Zoster Ge/As01b/Pf  | 9,689                     |
| MI    | Varicella-Zoster Ge/As01b/Pf  | 57,030                    |
| AA    | Amoxicillin                   | 243                       |
| SD    | Varicella-Zoster Ge/As01b/Pf  | 2,809                     |
| OH    | Varicella-Zoster Ge/As01b/Pf  | 46,339                    |
| MO    | Varicella-Zoster Ge/As01b/Pf  | 30,437                    |
| NE    | Varicella-Zoster Ge/As01b/Pf  | 9,042                     |
| MP    | Losartan Potassium            | 203                       |
| SC    | Varicella-Zoster Ge/As01b/Pf  | 36,044                    |
| GU    | Atorvastatin Calcium          | 3,367                     |

*(Note: Only 10 sample shown.)*

## 6. Top Drug Prescribed by Each Prescriber Type
**Question:** What is the most prescribed drug by each prescriber type, and how many claims does it have?

**Finding:** The Varicella-Zoster vaccine is frequently the top drug for many prescriber types, especially primary care and specialties dealing with older patients. However, specialties like Addiction Medicine and Pain Management favor hydrocodone/acetaminophen, reflecting their focus on pain management, which may raise concerns about opioid prescribing practices.

| Prescriber Type                        | Drug Name                     | Prescribed Drugs (Claims) |
|----------------------------------------|-------------------------------|---------------------------|
| Acupuncturist                          | Levothyroxine Sodium          | 31                        |
| Addiction Medicine                     | Hydrocodone/Acetaminophen     | 2,743                     |
| Adult Congenital Heart Disease         | Atorvastatin Calcium          | 287                       |
| Allergy/ Immunology                    | Varicella-Zoster Ge/As01b/Pf  | 9,629                     |
| Ambulatory Surgical Center             | Ibuprofen                     | 65                        |
| Anesthesiology                         | Hydrocodone/Acetaminophen     | 8,973                     |
| Behavior Analyst                       | Atorvastatin Calcium          | 558                       |
| Cardiac Surgery                        | Clopidogrel Bisulfate         | 1,688                     |
| Cardiology                             | Varicella-Zoster Ge/As01b/Pf  | 7,776                     |
| Chiropractic                           | Azithromycin                  | 103                       |

*(Note: Only a sample of 10 prescriber type is shown.)*

## 7. Average Cost Per Claim for Each Brand of a Generic Drug
**Question:** What is the average cost per claim for each brand of a generic drug?

**Finding:** Significant cost variations exist between brands of the same generic drug, with specialty drugs (e.g., Abemaciclib, Acalabrutinib) showing average costs per claim in the thousands of dollars. This highlights potential cost-saving opportunities by favoring lower-cost brands or generics, particularly for high-cost treatments.

| Generic Name                   | Brand Name            | Avg Cost per Claim ($) |
|--------------------------------|-----------------------|------------------------|
| 0.9 % Sodium Chloride          | Sodium Chloride       | 20.792                 |
| Abacavir Sulfate/Lamivudine    | Abacavir-Lamivudine   | 237.694                |
| Abacavir/Dolutegravir/Lamivudi | Triumeq               | 3,693.855              |
| Abaloparatide                  | Tymlos                | 2,539.070              |
| Abatacept                      | Orencia Clickject     | 5,439.126              |
| Abatacept/Maltose              | Orencia               | 4,245.691              |
| Abemaciclib                    | Verzenio              | 14,872.521             |
| Abiraterone Acet,submicronized | Yonsa                 | 10,029.271             |
| Abiraterone Acetate            | Zytiga                | 10,288.895             |
| Abiraterone Acetate            | Abiraterone Acetate   | 2,530.048              |
| Acalabrutinib                  | Calquence             | 13,899.747             |
| Acalabrutinib Maleate          | Calquence             | 13,423.188             |
| Acamprosate Calcium            | Acamprosate Calcium   | 130.431                |
| Acarbose                       | Acarbose              | 65.743                 |
| Acebutolol Hcl                 | Acebutolol Hcl        | 60.337                 |
| Acetaminophen With Codeine     | Acetaminophen-Codeine | 10.132                 |

## 8. Drugs Most Prescribed to Patients Aged 65 and Over
**Question:** Which drugs have the highest prescription rates for patients aged 65 and over, and what is the ratio of claims for this age group?

**Finding:** Several drugs, including Exemestane (used for breast cancer) and Zoledronic Acid (used for osteoporosis), are exclusively prescribed to patients aged 65 and over, reflecting their use in age-related conditions. However, the low claim volumes suggest these are specialty drugs, and further analysis of high-volume drugs is needed to understand broader elderly care trends.

| Generic Name                   | Total Claims GE65 | Total Claims | Ratio GE65 |
|--------------------------------|-------------------|--------------|------------|
| Exemestane                     | 17,883            | 17,883       | 1.000      |
| Abacavir Sulfate/Lamivudine    | 157               | 157          | 1.000      |
| Zoledronic Acid/Mannitol-Water | 785               | 785          | 1.000      |
| Parenteral Amino Acid 20% No.1 | 273               | 273          | 1.000      |
| Carvedilol Phosphate           | 758               | 758          | 1.000      |

## 9. Prescribers with Above-Average Cost Per Claim
**Question:** Which prescribers have an average cost per claim above the overall average, and what are their average costs?

**Finding:** Prescribers with above-average costs per claim have averages ranging from approximately $27,000 to $35,000, significantly higher than the overall average (not shown but calculable). These prescribers may be prescribing high-cost specialty drugs or treating complex patients, warranting further investigation into their practices.

| Prescriber NPI | Last Name    | Avg Cost per Claim ($) |
|----------------|--------------|------------------------|
| 1336246107     | Lovera       | 35,220.86              |
| 1679970271     | Harding      | 31,913.60              |
| 1972894376     | Forster      | 31,412.21              |
| 1811987407     | Allen        | 30,504.33              |
| 1316145840     | Arora        | 29,729.08              |

## 10. States Sorted by Average Total Drug Cost Per Prescriber
**Question:** Which states have the highest average total drug cost per prescriber?

**Finding:** Puerto Rico (PR) has the highest average total drug cost per prescriber at approximately $88,532, followed by New York (NY) and Alabama (AL). This suggests significant regional variations in healthcare spending, potentially due to differences in patient demographics, drug prices, or prescribing practices.

| State | Avg Total Drug Cost per Prescriber ($) |
|-------|----------------------------------------|
| PR    | 88,532.075                             |
| NY    | 69,580.635                             |
| AL    | 67,632.976                             |
| MS    | 58,615.944                             |
| MO    | 57,063.987                             |