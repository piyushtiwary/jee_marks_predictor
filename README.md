# JEE Marks Predictor

Welcome to the **JEE Marks Predictor** project! This is a fun tool designed to predict JEE (Joint Entrance Examination) marks based on rank and percentile.

---

## Components

### **Model Training Script (`model.py`)**

- **Purpose:** Trains a Random Forest Regressor model to predict JEE marks.
- **How It Works:**
  - **Input:** Loads the dataset (`data.csv`).
  - **Processing:** Splits the dataset, trains the model, and makes predictions.
  - **Output:** Prints actual and predicted values.

### **Dataset (`data.csv`)**

- **Purpose:** Contains the dataset for training the model. 

---

## Optional: Data Generation Script


- **Purpose:** Generates a dataset from range values in `range.txt`.
- **How It Works:**
  - **Input:** Reads range data from `range.txt`.
  - **Processing:** Converts ranges into evenly spaced values.
  - **Output:** Appends data to `data.csv`.

---

## How to Use

1. **Train the Model:** Run `model.py` with the included dataset.
2. **Testing the Model:** Modify and uncomment test values in `model.py`.

---

## Data Source

The dataset is generated from online range data. View the original data [here](https://blog.vidyamandir.com/a-complete-overview-of-jee-main-2022-marks-vs-rank-vs-percentile/).

---

## Contributing

Feel free to fork the repository and submit pull requests. Open an issue for questions or problems.

---

## Note

This project is intended for learning purposes and is not a professional tool.


