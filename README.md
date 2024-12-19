# 🕹️ Prediction of Purchase Decisions in Free-to-Play (F2P) Games

This repository contains a machine learning project aimed at predicting whether a player will make an in-game purchase in Free-to-Play (F2P) games. By analyzing player behavior data, this project helps to understand patterns and factors influencing purchase decisions, providing valuable insights for game developers and marketers.

## Main Idea

In Free-to-Play (F2P) games, understanding player behavior is crucial to predicting whether a player will spend money on in-game purchases. This project leverages machine learning techniques to predict player spending based on several features, including demographics, playtime, and engagement level. The dataset used contains features like player age, gender, playtime, sessions per week, and in-game achievements. The target variable is whether the player made an in-game purchase or not.

The goal of this project is to:
1. **Predict in-game purchase behavior**: Using machine learning models like Logistic Regression, Decision Trees, and Random Forest.
2. **Handle class imbalances**: Implementing techniques like SMOTE, Tomek Links, and ADASYN to address the imbalance in the dataset.
3. **Improve model performance**: Experimenting with different feature engineering and resampling techniques to optimize model accuracy.

### Overview of the Project

- **Data Preprocessing**: Handling missing values, encoding categorical features, and scaling numerical values.
- **Feature Engineering**: Creating new features based on player behavior to improve prediction.
- **Modeling**: Training multiple machine learning models to predict purchase decisions.
- **Evaluation**: Comparing model performance using accuracy, precision, recall, and F1-score.

## Conclusion

This project shows that with the right preprocessing, feature engineering, and resampling techniques, machine learning models can effectively predict in-game purchase behavior, which can be valuable for game developers to optimize monetization strategies.

## Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/your-username/Prediction-of-Purchase-Decisions-in-F2P-Games.git
cd Prediction-of-Purchase-Decisions-in-F2P-Games
pip install -r requirements.txt
