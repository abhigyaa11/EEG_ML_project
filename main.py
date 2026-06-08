<<<<<<< HEAD
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# reading and cleaning the data-------------------------------------------------------------------------------------
eeg_data = pd.read_csv("emotions.csv")
eeg_data = eeg_data.rename(columns = {"# mean_0_a" : "mean_0_a"})

# take the main table and drop the labels 
# this represents the brainwave data
X = eeg_data.drop("label", axis = 1)

# y represents the answers ie the labels
y = eeg_data["label"]

# check the dimentions
print(f"X (brainwaves) shape : {X.shape}")
print(f"y (answers) shape : {y.shape}")

# splitting the data into 80 (train) : 20 (test)---------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123, stratify=y)

# exporting the copy of testing data set to test later in the app
test_export = X_test.copy()
test_export["label"] = y_test
test_export.to_csv("test_emotions.csv", index = False)

# check the dimentions
print(f"training data: {X_train.shape}")
print(f"testing data: {X_test.shape}")

# training the AI----------------------------------------------------------------------------------------------------

# initialises the forest estimator tells 100 decision trees and state to be the same each time 123
rf_model = RandomForestClassifier(n_estimators= 100, random_state=123)

# fit takes the X train and y train data and forces the 100 trees to figure out the mathematical rules connecting them
print("Training the dataset...")
rf_model.fit(X_train, y_train)
print("Training complete")


# Evaluation and live inference simulation---------------------------------------------------------------------------

# first we will give the model the test data set and predict our y 
y_pred = rf_model.predict(X_test)

# now check the y_pred to the y_test
accuracy = accuracy_score(y_test, y_pred)
print(f"\nMODEL ACCURACY: {accuracy * 100:.2f} %\n")

# generate the confusion matrix that shows where the model succeeded or failed
print("\n CONFUSION MATRIX GRID: \n")
print(confusion_matrix(y_test, y_pred))

# generate the detailed performance report 
print("\n DETAILED PERFORMANCE REPORT: \n")
print(classification_report(y_test, y_pred))


# Real inference function-------------------------------------------------------------------------------------------
def predict_live_brainwaves(sensor_data): # we pass a 2D matrix since random forest was trained on the same
    prediction = rf_model.predict([sensor_data]) # passing 1 row 2D matrix
    return prediction[0] # since it has 1 row ie index 0 only

# Simulating a live patient reading from the test data eg row 42 using our function predict_live_brainwaves
sample = X_test.iloc[42].values # only extract the integer values from the 42nd row
condition = y_test.iloc[42]
guess = predict_live_brainwaves(sample)

print("PREDICTION SIMULATOR...")
print(f"realtime diagnostic output: {guess.upper()}")
print(f"actual score: {condition.upper()}")


# Serialization of result (saving the model)---------------------------------------------------------------------------

joblib.dump(rf_model, "eeg_brain.pkl")
print("Model saved successfully!")




      




=======
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# reading and cleaning the data-------------------------------------------------------------------------------------
eeg_data = pd.read_csv("emotions.csv")
eeg_data = eeg_data.rename(columns = {"# mean_0_a" : "mean_0_a"})

# take the main table and drop the labels 
# this represents the brainwave data
X = eeg_data.drop("label", axis = 1)

# y represents the answers ie the labels
y = eeg_data["label"]

# check the dimentions
print(f"X (brainwaves) shape : {X.shape}")
print(f"y (answers) shape : {y.shape}")

# splitting the data into 80 (train) : 20 (test)---------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123, stratify=y)

# exporting the copy of testing data set to test later in the app
test_export = X_test.copy()
test_export["label"] = y_test
test_export.to_csv("test_emotions.csv", index = False)

# check the dimentions
print(f"training data: {X_train.shape}")
print(f"testing data: {X_test.shape}")

# training the AI----------------------------------------------------------------------------------------------------

# initialises the forest estimator tells 100 decision trees and state to be the same each time 123
rf_model = RandomForestClassifier(n_estimators= 100, random_state=123)

# fit takes the X train and y train data and forces the 100 trees to figure out the mathematical rules connecting them
print("Training the dataset...")
rf_model.fit(X_train, y_train)
print("Training complete")


# Evaluation and live inference simulation---------------------------------------------------------------------------

# first we will give the model the test data set and predict our y 
y_pred = rf_model.predict(X_test)

# now check the y_pred to the y_test
accuracy = accuracy_score(y_test, y_pred)
print(f"\nMODEL ACCURACY: {accuracy * 100:.2f} %\n")

# generate the confusion matrix that shows where the model succeeded or failed
print("\n CONFUSION MATRIX GRID: \n")
print(confusion_matrix(y_test, y_pred))

# generate the detailed performance report 
print("\n DETAILED PERFORMANCE REPORT: \n")
print(classification_report(y_test, y_pred))


# Real inference function-------------------------------------------------------------------------------------------
def predict_live_brainwaves(sensor_data): # we pass a 2D matrix since random forest was trained on the same
    prediction = rf_model.predict([sensor_data]) # passing 1 row 2D matrix
    return prediction[0] # since it has 1 row ie index 0 only

# Simulating a live patient reading from the test data eg row 42 using our function predict_live_brainwaves
sample = X_test.iloc[42].values # only extract the integer values from the 42nd row
condition = y_test.iloc[42]
guess = predict_live_brainwaves(sample)

print("PREDICTION SIMULATOR...")
print(f"realtime diagnostic output: {guess.upper()}")
print(f"actual score: {condition.upper()}")


# Serialization of result (saving the model)---------------------------------------------------------------------------

joblib.dump(rf_model, "eeg_brain.pkl")
print("Model saved successfully!")




      




>>>>>>> ebbbae7 (First professional push from VS Code)
