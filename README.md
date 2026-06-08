# EEG Brainwave Diagnostic Dashboard

A real-time Machine Learning web application that classifies human emotional states using 2,548 channels of EEG brainwave data.

## Developer Context
This is my foundational Machine Learning deployment project, built during my first year of B.tech studying Computer Science with AI and Machine Learning. My objective was to move beyond just Jupyter Notebooks and build a complete, end to end MLOps pipeline handling high dimensional data, preventing data leakage and deploying a user interface.

https://github.com/user-attachments/assets/9aefce05-dcb6-47a1-8424-4595aa2fd9d0

## Dataset Acknowledgement
This project utilizes the "EEG Brainwave Dataset: Feeling Emotions" sourced from Kaggle (authored by Jordan J. Bird). The original dataset provides statistical features (like mean and Fast Fourier Transforms) pre-extracted from raw EEG time-series data, allowing this project to focus directly on downstream classification architecture and MLOps deployment.

## Real World Utility
While this is just a prototype, the underlying architecture mirrors real Brain-Computer interface applications:

* **Clinical Diagnostics:** Translating raw electrical frequencies to assist in non-verbal patient monitoring.
* **Neuromarketing:** Analyzing subconscious emotional reactions to stimuli in real-time.
* **Focus and Fatigue Tracking:** Real-Time monitoring of cognitive load for safety critical environments (eg. pilots, drivers).

## Architecture and Tech Stack
* **Frontend UI:** Streamlit (Python)
* **Machine Learning:** Scikit-learn (Random Forest Classifier)
* **Data Pipeline:** Pandas and NumPy
* **Serialization:** Joblib

## Engineering Features
* **High Dimensional Data Processing:** The model ingests and classifies 2,548 individual FFT voltage features per patient.
* **Strict Data Isolation:** Implemented a rigid `train_test_split` architecture, separating 80% of the dataset for training and compiling a secure `test_emotions.csv` for live web interface.
* **Live UI Rendering:** The dashboard parses raw 1D array data to a simulated real-time 2D waveform signal chart for immediate visual diagnosis.

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/abhigyaa11/EEG_ML_project.git
```

2. Install the requirements
```bash
pip install -r requirements.txt
```

3. Boot up the local web server
```bash
python -m streamlit run app.py
```
