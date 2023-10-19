# Loan-Approval-Prediction-Model
## Team Deep Learning Deviants 
### Team Members:
Elizabeth Lawal | Ryan Blais | Jenipher Flores | Fidel Carrillo | Andrew Hawthorne 

### Dataset:
Loan-Approval-Prediction-Dataset: https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset

### Overview:
The objective of this project is to use loan approval data to develop a supervised machine learning model to predict whether or not a loan application will be approved based on past approvals/rejections. 
The project consists of using a csv dataset with 4269 rows of loan approval data with the following columns: 
- loan_id
- no_of_dependants
- education
- self_employed
- income_annum
- loan_amount
- loan_term
- cibil_score
- residential_assets_value
- commercial_assets_value
- luxury_assets_value
- bank_assets_value
- loan_status

## Data Preprocessing for Logistic Regression Model:
### Variables: 
- Target (y): 'loan_status' (Approved or Rejected)
- Non-target/feature variables: 'loan_id'
- Features (X): remaining 11 columns 

### Actions: 
- Stripped leading/trailing whitespaces in column names
- Dropped ‘loan_id’ column as it is not beneficial 
- Used `pd.get_dummies` to encode categorical variables ('education' and 'self_employed')
- Split data into training and testing sets
- Scaled the data using `StandardScaler`

### Results 
**Accuracy:** 90%
**Precision:** 'Approved' - 93%, 'Rejected' - 87%
**Recall:** 'Approved' - 92%, 'Rejected' - 87%

### Model Optimization
- I repeated the same steps above but for features (X) I removed 'education' and 'self-employed' as their feature absolute magnitudes were the lowest; results were near identical except for the precision for 'Approved' dropped by one point. 
- Additional logistic regression models were tested by other group members, but the highest score remaints the one described above using all features with 90% accuracy. 

### Additional Models Tested
- I also ran a random forest model and the dataset and received 60% accuracy using all features and 98% accuracy by dropping 'education' and 'self_employed', neither results of which seemed reliable. 
- All models and optimized models tested are saved in the 'Models' folder
- Additional models were tested by other group members 

### Exploratory Analysis 
- Variable correlaton heatmap
- Distribution bar charts for 'education', 'self-employed', and 'loan_status'
- Frequency distribution histograms for 'income_annum', 'loan_amount', and 'cibil_score'
- Scatterplot of 'loan_amount' vs 'income_annum' colored by 'cibil_score'
- Distribution by 'loan_status' boxplots for 'income_annum', 'loan_amount', and 'cibil_score'

### Additional Figures
- Confusion matrix for logistic regression model
- Confusion matrix for optmized logistic regression model
- Feature importance for logistic regression model
- Feature importance for optimized logistic regression model
- Feature importance for random forest model
- Feature importance for optimized random forest model

### Sources:
ChatGPT (visualizations & model troubleshooting )
01-Ins_Summary_Statistics - Matplotlib, day 3 (normality tests)
04-Stu_Predicting_Diabetes - Supervised Learning, day 1 (logistic regression model)
05-Ins_Random_Forest - Supervised Learning, day 2 (randon forest model)
20-Supervised-Learning homework assigntment - Credit Risk Classification (logistic regression model)






### Factors to Consider to Choose Model:
What are various factors, such loan amount, loan term, and education level, that affect the outcome of a loan application? 


