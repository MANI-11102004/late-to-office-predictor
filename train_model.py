import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("late_to_office_dataset.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# ==========================================
# 2. Select Features and Target
# ==========================================

X = df[[
    "distance_km",
    "time_left_minutes"
]]

y = df["will_be_late"]


# ==========================================
# 3. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ==========================================
# 4. Feature Scaling
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ==========================================
# 5. Logistic Regression Model
# ==========================================

lr = LogisticRegression(
    random_state=42
)

lr.fit(
    X_train_scaled,
    y_train
)


# ==========================================
# 6. Logistic Regression Evaluation
# ==========================================

lr_predictions = lr.predict(X_test_scaled)

lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

print("\nLogistic Regression")
print("-------------------")
print("Accuracy:", lr_accuracy)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        lr_predictions
    )
)


# ==========================================
# 7. Decision Tree
# ==========================================

dt = DecisionTreeClassifier(
    random_state=42
)

dt.fit(
    X_train_scaled,
    y_train
)

dt_predictions = dt.predict(X_test_scaled)

dt_accuracy = accuracy_score(
    y_test,
    dt_predictions
)

print("\nDecision Tree")
print("-------------")
print("Accuracy:", dt_accuracy)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        dt_predictions
    )
)


# ==========================================
# 8. Save Logistic Regression Model
# ==========================================

joblib.dump(
    lr,
    "late_to_office_model.pkl"
)


# ==========================================
# 9. Save Scaler
# ==========================================

joblib.dump(
    scaler,
    "scaler.pkl"
)


print("\n================================")
print("Model and scaler saved!")
print("================================")

print("late_to_office_model.pkl")
print("scaler.pkl")