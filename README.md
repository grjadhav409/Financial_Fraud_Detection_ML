# Financial Fraud Detection using Machine Learning

This project is aimed at building a machine learning model to detect financial fraud using classification techniques. The project has achieved 92% accuracy with the random forest algorithm. It has also conducted detailed exploratory data analysis (EDA) to handle outliers and balance the data to ensure generalized model building. Finally, the project has been deployed on AWS using Docker containers and implemented CI/CD pipelines and MLOps practices, leveraging technologies such as Git for versioning, Scikit-learn for model building, and Kafka and MongoDB for data storage and retrieval.

## Table of Contents
- Problem Statement
- Dataset Description
- Exploratory Data Analysis
- Data injection
- Data Validation
- Feature Engineering
- Model Building
- Model Deployment
- Conclusion

## Problem Statement:
The problem of financial fraud is a major concern for banks and financial institutions. Fraudulent activities such as identity theft, account takeover, and money laundering can result in significant financial losses. The goal of this project is to build a machine learning model that can detect financial fraud with high accuracy.

## Dataset Description:
The dataset used in this project is obtained from Kaggle. It contains 6 million transactions with 11 features including the transaction amount, the time of the transaction, and the type of transaction (debit or credit). The dataset is highly imbalanced, with only 0.17% of the transactions being fraudulent.

## Exploratory Data Analysis:
The EDA phase involved analyzing the dataset to understand the distribution of the features and the relationships between them. Outliers were handled by removing transactions that were more than three standard deviations away from the mean. The data was also balanced using the SMOTE (Synthetic Minority Over-sampling Technique) algorithm to increase the number of fraudulent transactions.

## Feature Engineering:
The feature engineering phase involved creating new features from the existing ones to improve the performance of the model. For example, the time feature was converted to a cyclical feature to capture the periodic nature of transactions. The transaction amount was also scaled using a logarithmic transformation to reduce the effect of extreme values.

## Model Building:
The model building phase involved training and testing various machine learning models such as logistic regression, decision tree, and random forest. The random forest algorithm was selected as the final model due to its high accuracy of 92%. The model was also evaluated using metrics such as precision, recall, and F1 score.

## Model Deployment:
The final model was deployed on AWS using Docker containers. The CI/CD pipeline was implemented using GitHub Actions to automate the deployment process. The MLOps practices were implemented using technologies such as Kafka and MongoDB for data storage and retrieval.

## Conclusion:
In conclusion, this project has successfully built a machine learning model to detect financial fraud with high accuracy. The project has also implemented CI/CD pipelines and MLOps practices to automate the deployment process and ensure smooth operations. The project can be further improved by incorporating more advanced machine learning algorithms and incorporating more features to improve the accuracy of the model.