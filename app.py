from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name)

# Load your pre-trained logistic regression model
model = LogisticRegression()
model.load('your_model.pkl')  # Replace 'your_model.pkl' with the actual model file

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML file for the input form

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        annual_income = float(request.form['annual_income'])
        loan_amount = float(request.form['loan_amount'])

        # Prepare the input data for prediction
        input_data = pd.DataFrame({'income_annum': [annual_income], 'loan_amount': [loan_amount]})

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