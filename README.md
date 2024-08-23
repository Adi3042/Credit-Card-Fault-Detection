### Credit_Card_Fault_Detection 💳

#### Overview

Credit_Card_Fault_Detection is an open-source project designed to identify fraudulent credit card transactions. Utilizing advanced machine learning models and an intuitive web application, this project offers an effective solution for detecting anomalies and potential fraud in credit card activity.

![Credit Card Image](https://cdn.prod.website-files.com/5fbe376a36d4106214faaf3c/62200f9fbd736d0bb2002721_20220302-Credit%20Card%20Fraud%20Detection_Blog%20Thumbnail%20Image.png)

#### Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Contributions](#contributions)

### Introduction 🌟

Welcome to Credit_Card_Fault_Detection! This project helps detect potentially fraudulent credit card transactions by analyzing various transaction attributes. Whether you're a financial analyst or a security professional, this tool offers a reliable way to enhance fraud detection efforts.

### Features 🚀

##### Data Processing and Transformation 📊

Our project includes comprehensive data processing and transformation features to handle raw transaction data effectively, ensuring high-quality input for our fraud detection models.

![Data Processing](https://github.com/user-attachments/assets/676b732b-908d-4d8f-9ff9-283a7f4d406a)

### Advanced Fraud Detection Models 🤖

The system utilizes sophisticated machine learning models to detect fraudulent transactions. These models are designed to identify anomalies with high accuracy.

#### Web Application 🌐

The project includes a web-based interface for easy interaction with the fraud detection system. Users can input transaction details and receive predictions through a user-friendly web application.

- **Input Form:** Users can enter transaction details such as credit limit, demographic information, payment history, and bill amounts.
- **Fraud Detection Prediction:** The application applies a trained machine learning model to predict the likelihood of fraud.
- **User-Friendly Interface:** The web app features a clean and intuitive design for straightforward data entry and result viewing.
- **Background Image:** The app incorporates a visually appealing background to enhance the user experience.

### Getting Started 🛠️

The dataset used in the Credit Card Fault Detection project contains various attributes related to credit card transactions. This dataset is utilized to train machine learning models for detecting fraudulent activities.

#### Attributes in the Dataset:

- `LIMIT_BAL`: Credit limit of the cardholder.
- `SEX`: Gender of the cardholder (e.g., male, female).
- `EDUCATION`: Level of education of the cardholder (e.g., graduate, undergraduate).
- `MARRIAGE`: Marital status of the cardholder (e.g., married, single).
- `AGE`: Age of the cardholder.
- `PAY_0` to `PAY_6`: Payment status for the past 6 months (-1 = pay duly, 1 = payment delay for one month, 2 = payment delay for two months, etc.).
- `BILL_AMT1` to `BILL_AMT6`: Bill statement amount for the past 6 months.
- `PAY_AMT1` to `PAY_AMT6`: Amount paid in the past 6 months.
- `default payment next month`: Indicator of whether the cardholder defaulted on payment in the next month (1 = yes, 0 = no).

### Prerequisites 📋

Ensure you have the following prerequisites before using this project:

- Python (3.7 or higher)
- Required dependencies (install with `pip install -r requirements.txt`)
- Access to a web browser 🌐

### Technologies Used:

- Front-End: HTML, CSS
- Back-End: Python (Flask framework)
- Machine Learning: Logistic Regression, Random Forest, Neural Networks

### Installation 💻

##### Step 1 - Clone the repository to your local machine using Git:

```bash
git clone https://github.com/YourUsername/Credit-Card-Fault-Detection.git
cd Credit-Card-Fault-Detection
```

##### Step 2 - Create a conda environment

```bash
conda create -p venv python==3.8
conda activate venv/
```

##### Step 3 - Install the requirements

Open your terminal and execute the following command:

```bash
pip install -r requirements.txt
```

##### Step 4 - Run the application server

Open your terminal and execute the following command:

```bash
python application.py
```

##### Step 5 -

1. Visit the web app: http://127.0.0.1:5000/
2. Enter the transaction details in the input form.
3. Click the "Check for Fraud" button.
4. Receive a prediction on whether the transaction is likely to be fraudulent.

### Contributions:

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, feel free to create a pull request or open an issue.
