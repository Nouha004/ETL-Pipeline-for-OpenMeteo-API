# ETL Pipeline for OpenMeteo API
A mini project of an ETL Pipeline for OpenMeteo API for my BI portfolio

In this project I extracted data from an API called OpenMeteo to a Json file 
![image](https://github.com/user-attachments/assets/4382f608-18c7-4ca0-9f7f-09f77b85dc8f)

Then I affected some changes / Transfromations (Tempearature unit, Date Format ... )
![image](https://github.com/user-attachments/assets/00692b3d-db8c-41d8-bb7a-1dd0c75344d8)

Finally I loaded the pandas dataframe to a postgres database using SqlAlchemy's engine
![image](https://github.com/user-attachments/assets/6f03fb93-c379-4d4c-80da-98de384fcbcb)

here is the final Result (After Adding Average Values by dayusing SQL to ease the analysis later)
![image](https://github.com/user-attachments/assets/789a81e4-8851-4bfd-a9b1-487cbf44efed)

