import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Late to Office Predictor",
    page_icon="🚗",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    .info-box {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 1rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.7rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL
# =========================================================

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


# =========================================================
# HEADER
# =========================================================

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


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("ℹ️ About This Project")

    st.write(
        """
        This application uses Machine Learning to predict
        whether a person is likely to be late to the office.

        The prediction is based on:

        • Distance from home

        • Time remaining
        """
    )

    st.divider()

    st.subheader("🤖 Model")

    st.write("Logistic Regression")

    st.subheader("📊 Features")

    st.write("Distance (km)")
    st.write("Time Left (minutes)")

    st.divider()

    st.caption(
        "Built with Python, Scikit-learn and Streamlit"
    )


# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("📍 Enter Your Trip Details")

col1, col2 = st.columns(2)


with col1:

    distance = st.number_input(
        "🚗 Distance (km)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.1
    )


with col2:

    time_left = st.number_input(
        "⏱️ Time Left (minutes)",
        min_value=1,
        max_value=180,
        value=30,
        step=1
    )


st.write("")


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button(
    "🔮 Predict My Arrival",
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


    # Confidence
    confidence = max(
        on_time_probability,
        late_probability
    )


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.subheader("📊 Prediction Result")


    if prediction == 1:

        st.error(
            "⚠️ You are likely to be late."
        )

        explanation = (
            "Based on the distance and remaining time, "
            "the model predicts a higher chance of arriving late."
        )

    else:

        st.success(
            "✅ You are likely to reach on time!"
        )

        explanation = (
            "Based on the distance and remaining time, "
            "the model predicts a higher chance of arriving on time."
        )


    st.info(explanation)


    # =====================================================
    # PROBABILITIES
    # =====================================================

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "🟢 On-Time Probability",
            f"{on_time_probability * 100:.1f}%"
        )


    with col2:

        st.metric(
            "🔴 Late Probability",
            f"{late_probability * 100:.1f}%"
        )


    # =====================================================
    # CONFIDENCE
    # =====================================================

    st.write("### 🎯 Model Confidence")

    st.progress(
        confidence
    )

    st.write(
        f"The model's confidence is "
        f"**{confidence * 100:.1f}%**."
    )


    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.write("### 📋 Trip Summary")

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Distance",
            f"{distance:.1f} km"
        )


    with col2:

        st.metric(
            "Time Remaining",
            f"{time_left} min"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Late to Office Predictor • Machine Learning Project"
)