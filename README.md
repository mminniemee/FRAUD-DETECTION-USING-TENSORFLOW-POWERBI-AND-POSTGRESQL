# FRAUD-DETECTION-USING-TENSORFLOW-POWERBI-AND-POSTGRESQL
This project combines data engineering, machine learning, and business intelligence dashboards to simulate how banks can proactively monitor and flag suspicious activity.A Financial Fraud Detection System that detects suspicious transactions using a **Feedforward Neural Network**. 

load_into_database.py is used to load the csv file in postgresql.
In the branch "notebooks" there are jupyter notebooks used for analysis, cleaning and deep learning.

## 🚀 Features

- 🧠 **Feedforward Neural Network** (TensorFlow/Keras) trained on the [PaySim Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)
- 🗃️ **PostgreSQL** database to store transactions and fraud prediction results
- 📊 **Power BI Dashboard** for data visualizations:
  - Total number of frauds
  - Percentage of frauds
  - Gauge for probability score
  - Fraud probability distribution

## 📁 Tech Stack

| Layer            | Tech Used                        |
|------------------|----------------------------------|
| Backend          | Python, Pandas, TensorFlow, Keras|
| Database         | PostgreSQL                       |
| Visualizations   | Power BI                         |
| IDE & Tools      | VS Code, Jupyter Notebook        |

## 🧠 Model Info

- **Architecture**: Feedforward Neural Network (Dense layers)
- **Input Features**: Transaction amount, oldbalanceOrg, newbalanceOrig, transaction type (encoded), etc.
- **Output**: Binary prediction — fraud or not fraud
- **Probability Score**: Used for ranking or thresholding predictions

![dashboard](https://github.com/user-attachments/assets/2c87897a-6e1b-415d-8083-d52e7eeeb90f)

