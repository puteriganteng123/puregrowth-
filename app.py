import streamlit as st
import time

# Page config
st.set_page_config(page_title="Puregrowth", page_icon="🌱", layout="centered")

# Styling
st.markdown("""
    <style>
        body {
            background-color: #f3f4f6;
            color: #1f2937;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton > button {
            background-color: #10b981;
            color: white;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-size: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Register/Login Section
st.title("🌿 Welcome to Puregrowth")
st.subheader("by **Eureka Syndicate**")

if 'registered' not in st.session_state:
    st.session_state.registered = False

if not st.session_state.registered:
    with st.form("register_form"):
        st.write("✨ Let's get you started!")
        username = st.text_input("Enter your name")
        password = st.text_input("Create a password", type="password")
        submitted = st.form_submit_button("Register")

        if submitted and username and password:
            st.session_state.username = username
            st.session_state.registered = True
            st.success("Registered successfully! 🌱")
            time.sleep(1)
            st.experimental_rerun()
else:
    st.success(f"Welcome back, {st.session_state.username}!")
    plant_name = st.text_input("🌼 Name your plant:", "My Little Greeny")

    st.markdown(f"##### Hello, {st.session_state.username} 👋")
    st.markdown(f"**'{plant_name}'** is waiting for your care 💧")

    st.markdown("---")
    moisture_level = st.slider("📊 Soil Moisture Level (%)", 0, 100, 50)

    st.markdown("🛠 Sensor reading received from Arduino uno R4 WiFi.")

    if moisture_level < 30:
        st.error("⚠️ Soil is too dry.")
        st.info("A notification has been sent to your phone 📲")

        ignore = st.checkbox("Ignore notification")

        if ignore:
            st.warning("⏳ Waiting 5 minutes before automatic watering...")
            time.sleep(2)  # simulate time delay
            st.success("✅ Automatic watering triggered 💦")
        else:
            st.markdown("💧 **Manual Watering**")
            water_amount = st.slider("Select amount of water to send (ml)", 50, 500, 200)
            if st.button(“Time for a splash 💦”:
                st.success(f"🌊 {water_amount}ml of water sent to {plant_name}!")
    elif moisture_level < 70:
        st.info("😊 Soil moisture is in a good range.")
    else:
        st.success("🌧️ Soil is well-watered. No need to water now.")

    st.markdown("---")
    st.caption("🌱 Made with 💚 by Eureka Syndicate")
