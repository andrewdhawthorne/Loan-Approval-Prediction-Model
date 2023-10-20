# Loan-Approval-Prediction-Model
## Team: Deep Learning Deviants 
### Team Members:
Elizabeth Lawal | Ryan Blais | Jenipher Flores | Fidel Carrillo | Andrew Hawthorne 

### 01. Project Overview:
The objective is to use loan approval data to develop a supervised machine learning model to predict whether or not a loan application will be approved based on past approvals/rejections. 

#### Dataset:
Loan-Approval-Prediction-Dataset: https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset
**Features to Consider for Loan Status** - Accepted or Rejected

Csv dataset contains 4269 rows of loan approval data with the following columns: 
<img width="900" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/Jenipher's_branch/Visualizations/Loan%20DF.JPG"> 

### 02. Exploratory Analysis:
**Correlation Matrix:**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/Ryan's_Branch/Visualizations/CorrelationMartix.png"> 

**Income Distribution:**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/Ryan's_Branch/Visualizations/IncomeDistribution.png"> 

**Credit Score by Loan Amount:**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/main/Visualizations/CSvLA_AorRPlot.png"> 

### 03. Surpervised Learning:
#### Models Attempted:
- Random Forest 
- KN Neighbors 
- Decision Tree 
- Logistic Regression 

#### Model used: Logistic Regression Model (by Andrew)
#### Variables: 
- Target (y): 'loan_status' (Approved or Rejected)
- Non-target/feature variables: 'loan_id'
- Features (X): remaining 11 columns 

#### Actions: 
- Stripped leading/trailing whitespaces in column names
- Dropped ‘loan_id’ column as it is not beneficial 
- Used `pd.get_dummies` to encode categorical variables ('education' and 'self_employed')
- Split data into training and testing sets
- Scaled the data using `StandardScaler`
- Created & trained the model and made predictions 
- Optimization attempts were made by adjusting the features included, but the highest score was with keeping all of the features

#### Results: 
**Accuracy:** 90%

**Precision:** 'Approved' - 93%, 'Rejected' - 87%

**Recall:** 'Approved' - 92%, 'Rejected' - 87%

**Logistic Regression Feature Importance:**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/main/Visualizations/lr_feature_importance.png"> 

### 04. Model Results:
#### Classification Report:
**Final accuracy score: 90%**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/Jenipher's_branch/Visualizations/Classification%20Report.JPG"> 

**Confusion Matrix**

<img width="500" src="https://github.com/andrewdhawthorne/Loan-Approval-Prediction-Model/blob/AH-branch/Figures/lg_confusion_matrix.png"> 

#### Takeaways:
**Key Feature: Credit Score**
**Data Limitations:** 
- Loan types are not specified 
- Additional factors, such as foreclosures or bankruptcies, that were not included 
- Debt-to-income ratio 
- Interest rates 
- Demographics 

#### Sources:
1. ChatGPT (visualizations & model troubleshooting )
2. 01-Ins_Summary_Statistics - Matplotlib, day 3 (normality tests)
3. 04-Stu_Predicting_Diabetes - Supervised Learning, day 1 (logistic regression model)
4. 05-Ins_Random_Forest - Supervised Learning, day 2 (randon forest model)
5. 20-Supervised-Learning homework assigntment - Credit Risk Classification (logistic regression model)


