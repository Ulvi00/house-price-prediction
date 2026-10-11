# House Price Prediction

A beginner machine learning project that predicts house prices based on property area and number of rooms using Linear Regression.

## Technologies

- Python
- Pandas
- Scikit-learn

## How It Works

1. Loads house data from `evler.csv`.
2. Splits the dataset into training and test sets.
3. Trains a Linear Regression model.
4. Evaluates predictions using Mean Absolute Error (MAE).
5. Retrains the model on the full dataset.
6. Predicts a price using the area and room count entered by the user.

The program also checks for invalid numeric input and non-positive values.

## Dataset

The dataset contains 4 sample houses:

| Area (m²) | Rooms | Price (AZN) |
|---|---|---|
| 60 | 2 | 70000 |
| 80 | 3 | 95000 |
| 100 | 3 | 115000 |
| 100 | 4 | 125000 |

## Run the Project

Install the required packages:

```bash
pip install pandas scikit-learn
```

Keep `main.py` and `evler.csv` in the same folder. Open a terminal in that folder and run:

```bash
python main.py
```

Enter the property area and number of rooms when prompted.

## Limitations

This is a learning project using a small sample dataset, not a real estate valuation tool.

The model is evaluated using 3 training samples and 1 test sample. This is insufficient to assess real-world accuracy. The reported MAE belongs to the initial model, before retraining on all 4 samples.
