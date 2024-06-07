Project Description
Automated Analysis and Visualization of Flight Delays Dataset

This project aimed to automate the process of downloading, transforming, and cleaning a dataset of flight delays from the Kaggle website and represent its impact in Power BI. A comprehensive analysis of 5.82 million rows of data across 40 fields was conducted to determine various metrics, including flight volume variations, departure delay percentages and times, cancellation causes, and flight reliability of airlines. The project encompassed the entire ETL (Extract, Transform & Load) process and visualization using data sourced from Kaggle.

Key Stages:

Stage 1: Data Acquisition

Developed a Python script to create a live connection to the Kaggle website through an API for downloading the dataset.
Configured the script to overwrite existing files with each execution, ensuring the data remains current.
Stage 2: Data Preparation

Loaded the downloaded data into Power BI and utilized DAX language to create a Date Dimension, essential for time-based analysis.
Stage 3: Data Cleaning

Performed data cleaning operations to remove irrelevant information and ensure data quality.
Stage 4: Data Modeling

Defined the fact table and dimensions, establishing a star schema to facilitate efficient data analysis.
Stage 5: Dashboard Creation

Created four comprehensive dashboards containing recommended analyses:
- Analysis of flight volume variations by month and day of the week.
- Examination of departure delay percentages in 2015, including average delay times for delayed flights.
- Evaluation of the percentage of delayed flights throughout the year, with a specific focus on flights departing from Boston (BOS).
- Overview of flight cancellations in 2015, including the percentage attributed to weather and airline/carrier issues.
- Assessment of airline reliability in terms of on-time departures.
The project's primary challenge was to ensure full automation, enabling seamless and timely analysis of flight delay data to derive actionable insights.
