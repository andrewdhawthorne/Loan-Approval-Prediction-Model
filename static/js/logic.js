// Function to validate the form before submission
function validateForm() {
    var annualIncome = document.getElementById("income_annum").value;
    var loanAmount = document.getElementById("loan_amount").value;

    if (isNaN(annualIncome) || isNaN(loanAmount)) {
        alert("Please enter valid numbers for Annual Income and Loan Amount.");
        return false; // Prevent form submission
    }

    // Additional validation can be added here if needed

    return true; // Allow form submission if inputs are valid
}

// Function to make an AJAX request to predict the loan approval
function predictLoanApproval() {
    // Get form data
    var formData = new FormData(document.getElementById("loan-form"));

    // Make an AJAX request to the Flask server
    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Display the prediction result on the page
        document.getElementById("prediction-result").textContent = data;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}