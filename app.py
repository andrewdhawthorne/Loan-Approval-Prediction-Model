from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

# Load pre-trained logistic regression model
loaded_model = joblib.load('logistic_regression_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        annual_income = float(request.form['income_annum'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        cibil_score = float(request.form['cibil_score'])
        no_of_dependents = float(request.form['no_of_dependents'])
        residential_assets_value = float(request.form['residential_assets_value'])
        commercial_assets_value = float(request.form['commercial_assets_value'])
        luxury_assets_value = float(request.form['luxury_assets_value'])
        bank_asset_value = float(request.form['bank_asset_value'])

        # Prepare the input data for prediction
        input_data = pd.DataFrame({'income_annum': [annual_income], 'loan_amount': [loan_amount], 
                                   'loan_term': [loan_term], 'cibil_score': [cibil_score],
                                   'no_of_dependents': [no_of_dependents], 'residential_assets_value': [residential_assets_value],
                                   'commercial_assets_value': [commercial_assets_value], 'luxury_assets_value': luxury_assets_value,
                                    'bank_asset_value': bank_asset_value})

        # Standardize the input data if necessary
        scaler = StandardScaler()
        input_data = scaler.transform(input_data)

        # Make a prediction
        prediction = model.predict(input_data)

        # Return the result to the user
        if prediction[0] == 1:
            result = "Approved"
        else:
            result = "Not Approved"

        return f"Loan Status: {result}"

if __name__ == '__main__':
    app.run()