import streamlit as st
import requests
import time

# Page config
st.set_page_config(
    page_title="Puregrowth",
    page_icon="https://i.imgur.com/kqYJzjX.png",
    layout="centered"
)

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

# Firebase URLs
moisture_url = "https://puregrowth-31987-default-rtdb.asia-southeast1.firebasedatabase.app/moisture.json"
command_url = "https://puregrowth-31987-default-rtdb.asia-southeast1.firebasedatabase.app/command.json"

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
            st.rerun()
else:
    st.success(f"Welcome back, {st.session_state.username}!")
    plant_name = st.text_input("🌼 Name your plant:", "My Little Greeny")

    st.markdown(f"##### Hello, {st.session_state.username} 👋")
    st.markdown(f"**'{plant_name}'** is waiting for your care 💧")
    st.markdown("---")

    # Get real moisture level from Firebase
    try:
        moisture_level = int(requests.get(moisture_url).text)
    except:
        moisture_level = 0

    st.markdown("🛠 Sensor reading received from Arduino Uno R4 WiFi.")
    st.markdown(f"📊 **Soil Moisture Level**: `{moisture_level}`")

    if moisture_level < 30:
        st.error("⚠️ Soil is too dry.")
        st.info("A notification has been sent to your phone 📲")

        ignore = st.checkbox("Ignore notification")

        if ignore:
            st.warning("⏳ Waiting 5 minutes before automatic watering...")
            time.sleep(2)
            st.success("✅ Automatic watering triggered 💦")
            requests.put(command_url, data='"water_now"')
        else:
            st.markdown("💧 **Manual Watering**")
            water_amount = st.slider("Select amount of water to send (ml)", 50, 500, 200)
            if st.button("Time for a splash 💦"):
                requests.put(command_url, data='"water_now"')
                st.success(f"🌊 {water_amount}ml of water sent to {plant_name}!")
    elif moisture_level < 70:
        st.info("😊 Soil moisture is in a good range.")
    else:
        st.success("🌧️ Soil is well-watered. No need to water now.")

    st.markdown("---")
    st.caption("🌱 Made with 💚 by Eureka Syndicate")
