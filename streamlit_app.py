import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Agri Nexa - Smart Crop Predictor",
    page_icon="🌱",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

@st.cache_resource
def load_model_files():

    with open(BASE_DIR / "model.pkl", "rb") as f:
        model = pickle.load(f)

    scaler_path = BASE_DIR / "scaler.pkl"

    if not scaler_path.exists():
        scaler_path = BASE_DIR / "scaler(1).pkl"

    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler


try:
    model, scaler = load_model_files()

except Exception as e:
    st.error("Model loading failed.")
    st.error(str(e))
    st.stop()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f3fff7,
        #e8f8ee,
        #f8fffa
    );
}

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 50px;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #087846;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #6b7f75;
    font-size: 16px;
    margin-bottom: 35px;
}

.section-title {
    color: #075c3d;
    font-size: 24px;
    font-weight: 700;
}

.result-title {
    color: #087846;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🌱 Agri Nexa</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart Agricultural Production Optimization Engine'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🌾 Field Information</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the soil and environmental conditions to predict the most suitable crop."
)

st.divider()


# =========================================================
# INPUTS
# =========================================================

col1, col2 = st.columns(2)


# -------------------------
# SOIL
# -------------------------

with col1:

    st.subheader("🌿 Soil Conditions")

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=200.0,
        value=90.0,
        step=1.0
    )

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=200.0,
        value=60.0,
        step=1.0
    )

    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=250.0,
        value=40.0,
        step=1.0
    )

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1
    )


# -------------------------
# ENVIRONMENT
# -------------------------

with col2:

    st.subheader("☀️ Environmental Conditions")

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=25.0,
        step=0.5
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=1000.0,
        value=100.0,
        step=1.0
    )


st.write("")


# =========================================================
# BUTTONS
# =========================================================

predict_col, reset_col = st.columns([3, 1])


with predict_col:

    predict_button = st.button(
        "🚀 Predict Best Crop",
        type="primary",
        use_container_width=True
    )


with reset_col:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )


if reset_button:
    st.rerun()


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    try:

        # Create input data
        input_data = np.array([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        # Scale input
        scaled_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(scaled_data)[0]

        # =================================================
        # RESULT
        # =================================================

        st.divider()

        st.subheader("🤖 Crop Prediction")

        st.success("Prediction completed successfully!")

        st.markdown(
            f"# 🌾 {prediction}"
        )

        st.write(
            "This is the crop recommended by your trained machine-learning model."
        )


        # =================================================
        # FIELD SUMMARY
        # =================================================

        st.divider()

        st.subheader("📊 Field Summary")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🌿 Nitrogen",
                f"{N:.1f}"
            )

        with c2:
            st.metric(
                "🧪 Phosphorus",
                f"{P:.1f}"
            )

        with c3:
            st.metric(
                "🌱 Potassium",
                f"{K:.1f}"
            )

        with c4:
            st.metric(
                "⚗️ Soil pH",
                f"{ph:.1f}"
            )


        c5, c6, c7 = st.columns(3)

        with c5:
            st.metric(
                "🌡️ Temperature",
                f"{temperature:.1f} °C"
            )

        with c6:
            st.metric(
                "💧 Humidity",
                f"{humidity:.1f} %"
            )

        with c7:
            st.metric(
                "🌧️ Rainfall",
                f"{rainfall:.1f} mm"
            )


        # =================================================
        # MODEL CONFIDENCE
        # =================================================

        if (
            hasattr(model, "predict_proba")
            and hasattr(model, "classes_")
        ):

            probabilities = model.predict_proba(
                scaled_data
            )[0]

            results = list(
                zip(
                    model.classes_,
                    probabilities
                )
            )

            results.sort(
                key=lambda x: x[1],
                reverse=True
            )

            st.divider()

            st.subheader("🎯 Model Confidence")

            st.write(
                "Top crop predictions from the trained model:"
            )

            for crop, probability in results[:5]:

                percentage = probability * 100

                st.write(
                    f"**{crop} — {percentage:.2f}%**"
                )

                st.progress(
                    float(probability)
                )


        # =================================================
        # MODEL INFORMATION
        # =================================================

        st.divider()

        st.subheader("🧠 Prediction Information")

        info1, info2, info3 = st.columns(3)

        with info1:
            st.info(
                f"Model\n\n"
                f"**{type(model).__name__}**"
            )

        with info2:
            st.info(
                "Features\n\n"
                "**7 inputs**"
            )

        with info3:
            st.info(
                "Prediction\n\n"
                "**Crop recommendation**"
            )


        # =================================================
        # AGRICULTURE NOTE
        # =================================================

        st.warning(
            "🌱 Agri Nexa provides machine-learning based "
            "decision support. For actual farming decisions, "
            "also consider local soil testing, seasonal "
            "conditions, weather forecasts and agricultural "
            "expert advice."
        )


    except Exception as e:

        st.error("Prediction failed.")

        st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Agri Nexa • Smart Agricultural Production Optimization Engine"
)