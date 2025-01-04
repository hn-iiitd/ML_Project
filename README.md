# 🎰 Prediction of Purchase Decisions in Free-to-Play (F2P) Games

This project predicts in-game purchase decisions in F2P games using machine learning. We explore factors influencing player purchases, tackle data imbalance, engineer features, and implement robust models to improve prediction accuracy.

---

## 🔍 Project Overview

- *Motivation:* Analyze player behavior to predict purchases, aiding game developers in monetization strategies.
- *Dataset:* Kaggle dataset with 13 features, including age, gender, playtime, and engagement levels.
- *Target Variable:* InGamePurchases (1 for purchase, 0 for no purchase).

---

## 📊 Methodology

### *Data Preprocessing*
- Addressed class imbalance using:
  - *SMOTE*
  - *Tomek Links*
  - *SMOTE-ENN*
- Min-Max scaling for feature normalization.
- Dropped irrelevant features and applied one-hot/numerical encoding.

### *Feature Engineering*
- Added EstimatedAnnualIncome based on country and engagement level.

### *Models Implemented*
1. *Logistic Regression*
2. *Decision Tree*
3. *Random Forest* (Best model: Accuracy = 87% with Tomek Links)
4. *Naive Bayes*

### *Hyperparameter Optimization*
- Used GridSearchCV for the Random Forest model to achieve optimal performance.

---

## 📈 Results

- *Best Model:* Random Forest (Accuracy = 87%)
- *Evaluation Metrics:* 
  - Precision
  - Recall
  - F1 Score

![Accuracy Graph](https://github.com/hn-iiitd/ML_Project/blob/main/Screenshot%202025-01-04%20162802.png)
![ROC Curve](https://via.placeholder.com/500x300.png?text=ROC+Curve)

---

## 🛠 Tools & Technologies

- *Languages:* Python
- *Libraries:* Scikit-learn, Imbalanced-learn
- *Methods:* GridSearchCV, SMOTE, Tomek Links

---

## 🔗 References

1. [Dataset Source](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset)
2. [SMOTE-ENN Documentation](https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTEENN.html)
3. [Adaptive Synthetic Sampling (ADASYN)](https://www.activeloop.ai/resources/glossary/adaptive-synthetic-sampling-adasyn/)

---

## 📸 Visualizations

![Class Distribution](https://via.placeholder.com/500x300.png?text=Class+Distribution)
![Feature Correlation](https://via.placeholder.com/500x300.png?text=Feature+Correlation)

---

## 🚀 How to Run

1. Clone the repository:
   bash
   git clone https://github.com/hn-iiitd/ML_Project.git
   cd ML_Project
   
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Run the model:
   bash
   python src/main.py
   

---

## 🧑🏼‍💻 Contributors

- Harsh Hingorani
- Harsh Nangia
- Idhant Arora
- Madhav Kansil

Feel free to contribute and share feedback! 😊
