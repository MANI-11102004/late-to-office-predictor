import streamlit as st
import pandas as pd
import joblib


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Late to Office Predictor",
    page_icon="🚗",
    layout="centered"
)


# ==========================================
# Custom CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 2.6rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    .result-card {
        padding: 1.2rem;
        border-radius: 14px;
        margin-top: 1rem;
        border: 1px solid rgba(128,128,128,0.25);
    }

    div.stButton > button {
        width: 100%;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.65rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# Load Model and Scaler
# ==========================================

@st.cache_resource
def load_model():

    model = joblib.load(
        "late_to_office_model.pkl"
    )

    scaler = joblib.load(
        "scaler.pkl"
    )

    return model, scaler


model, scaler = load_model()


# ==========================================
# Header
# ==========================================

st.markdown(
    '<div class="main-title">🚗 Late to Office Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict whether you are likely to reach the office on time.'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.header("ℹ️ About")

    st.write(
        """
        This application uses a Machine Learning model
        to predict whether a person is likely to be late
        based on:

        • Distance from home

        • Time remaining
        """
    )

    st.divider()

    st.caption(
        "Model: Logistic Regression"
    )

    st.caption(
        "Features: Distance + Time Left"
    )


# ==========================================
# User Input
# ==========================================

st.subheader("📍 Trip Details")


col1, col2 = st.columns(2)


with col1:

    distance = st.number_input(
        "Distance (km)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.1
    )


with col2:

    time_left = st.number_input(
        "Time left (minutes)",
        min_value=1,
        max_value=180,
        value=30,
        step=1
    )


st.caption(
    "Enter the distance from home and the time remaining."
)


# ==========================================
# Prediction Button
# ==========================================

if st.button(
    "🔮 Predict",
    type="primary"
):

    # Create DataFrame
    input_data = pd.DataFrame(
        {
            "distance_km": [distance],
            "time_left_minutes": [time_left]
        }
    )


    # Scale input
    input_scaled = scaler.transform(
        input_data
    )


    # Prediction
    prediction = model.predict(
        input_scaled
    )[0]


    # Probability
    probabilities = model.predict_proba(
        input_scaled
    )[0]


    on_time_probability = probabilities[0]

    late_probability = probabilities[1]


    # ==========================================
    # Results
    # ==========================================

    st.divider()

    st.subheader("📊 Prediction")


    if prediction == 1:

        st.error(
            "⚠️ You are likely to be late."
        )

    else:

        st.success(
            "✅ You are likely to reach on time."
        )


    # ==========================================
    # Probability Metrics
    # ==========================================

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "On-Time Probability",
            f"{on_time_probability * 100:.1f}%"
        )


    with col2:

        st.metric(
            "Late Probability",
            f"{late_probability * 100:.1f}%"
        )


    # ==========================================
    # Confidence
    # ==========================================

    confidence = max(
        on_time_probability,
        late_probability
    )


    st.write("### Confidence")

    st.progress(
        confidence
    )


    st.write(
        f"Model confidence: **{confidence * 100:.1f}%**"
    )


    # ==========================================
    # Input Summary
    # ==========================================

    st.write("### 📋 Input Summary")

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Distance",
            f"{distance:.1f} km"
        )


    with col2:

        st.metric(
            "Time Left",
            f"{time_left} min"
        )


# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "Educational Machine Learning Project • "
    "Logistic Regression • Streamlit"
)