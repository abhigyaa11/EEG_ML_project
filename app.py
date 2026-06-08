import streamlit as st
import joblib
import pandas as pd
import random 
from sklearn.metrics import classification_report, confusion_matrix


model = joblib.load("eeg_brain.pkl") # loading the AI our model
df = pd.read_csv("test_emotions.csv") # loading the database

# st.write("System Status: AI and database successfully loaded into the web.")

# Designing the dashboard-------------------------------------------------------------------------------------------------------

st.title("EEG Diagnostic Dashboard")
st.markdown("### Real Time patient emotional state classifier using brainwaves")
st.markdown("---")
st.sidebar.header("Control panel")
st.sidebar.info("Click the button below to take in a random patients EEG brainwave scan")


# Live interface---------------------------------------------------------------------------------------------------------------
if st.sidebar.button("scan incoming patient"):

    # pick a random row from out dataframe
    random_index = random.randint(0, len(df) - 1)

    # extract the data of the patient at random index without the label ie the answer
    patient_data = df.drop("label", axis = 1).iloc[random_index].values
    patient_state = df.iloc[random_index]["label"]

    # display the data
    st.write("#### hardware data stream incoming...")
    st.write(f"**patient ID:**{random_index}")
    # visualising the wave of eeg
    wave_sample = patient_data[500:600]
    st.line_chart(wave_sample)

    # prediting the real data
    prediction = model.predict([patient_data])[0]
    col1, col2 = st.columns(2)

    with col1:
        if prediction == patient_state:
            # success gives a green box 
            st.success(f"AI Prediction: {prediction}")
        else:
            # error gives a red box
            st.error(f"AI Prediction: {prediction}")

    with col2:
        # info gives a neutral blue box
        st.info(f"True Patient State: {patient_state}")

    if prediction == patient_state:
        st.balloons()

        # We calculate predictions for the whole test dataset so we can show the stats
        X_test = df.drop("label", axis=1)
        y_test = df["label"]
        y_pred = model.predict(X_test)

        st.sidebar.markdown("---")
        st.sidebar.write("### Model Performance Metrics")
        
        with st.sidebar.expander("View Full Report"):
            st.text(classification_report(y_test, y_pred))

