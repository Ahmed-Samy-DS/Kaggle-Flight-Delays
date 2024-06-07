Project Description

Automate the process of downloading, transforming, and cleaning a dataset of flight delays from the Kaggle website, and represent the impact in Power BI. 
Analyzed 5.82 million rows of data across 40 fields to determine flight volume variations, departure delay percentages and times, cancellation causes, and flight reliability of airlines. This project covered the entire process from ETL (Extract, Transform & Load) to visualization using data from Kaggle.


The challenge of this project was to make it as fully automated as possible.

Stage 1:
Create a live connection to the Kaggle website through an API by writing a Python code to make a request for downloading the dataset. In the same code, define the destination of the downloaded files so that each time the code runs, it will overwrite the old ones.

Stage 2:
Load the data into Power BI and create a Date Dimension using the DAX language.

Stage 3:
Clean the data and remove unimportant information.

Stage 4:
Define the fact table and dimensions and create a star schema.

Stage 5:
Create 4 dashboards including recommended analyses:

How does the overall flight volume vary by month? By day of the week?
What percentage of flights experienced a departure delay in 2015? Among those flights, what was the average delay time, in minutes?
How does the percentage of delayed flights vary throughout the year? What about for flights leaving from Boston (BOS) specifically?
How many flights were canceled in 2015? What percentage of cancellations were due to weather? What percentage were due to the airline/carrier?
Which airlines seem to be the most and least reliable in terms of on-time departure?