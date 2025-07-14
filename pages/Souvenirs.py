import streamlit as st
import sqlite3
from PIL import Image
import os

# Function to get the highest score from scores table
def get_high_score():
    db_path = "Dataset and Database/scores.db"
    if not os.path.exists(db_path):
        return 0  # Return 0 if database file doesn't exist
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(points) FROM scores")
        max_score = cursor.fetchone()[0] or 0  # Default to 0 if no value is found
        conn.close()
        return max_score
    except Exception as e:
        st.error(f"Error accessing {db_path}: {e}")
        return 0

# Fetch max score from scores.db
max_score = get_high_score()
initial_points = 100 + (max_score // 100) * 100  # Base 100 + 100 per 100 score points

# Initialize session state for points and badges
if "points" not in st.session_state:
    st.session_state.points = initial_points  # Set points dynamically
if "purchased_badges" not in st.session_state:
    st.session_state.purchased_badges = set()

# Badge data
badges = [
    {"name": "Meghalaya", "image": "Meghalaya Badge.png"},
    {"name": "Manipur", "image": "Manipur Badge.png"},
    {"name": "Nagaland", "image": "Nagaland Badge.png"},
    {"name": "Arunachal Pradesh", "image": "Arunachal Pradesh Badge.png"},
    {"name": "Assam", "image": "Assam Badge.png"},
    {"name": "Tripura", "image": "Tripura Badge.png"},
    {"name": "Mizoram", "image": "Mizoram Badge.png"},
]

badge_price = 100  # Cost per badge

st.title("🎖️ Souvenir Shop")
st.markdown("### Collect badges and spend your points!")

# Display points
st.subheader(f"💰 Points: {st.session_state.points}")

# Display progress bar
total_badges = len(badges)
collected_badges = len(st.session_state.purchased_badges)
progress = collected_badges / total_badges
st.progress(progress)

# Show badge collection progress
st.markdown(f"**🏅 Badges Collected: {collected_badges}/{total_badges}**")

# Layout for two badges per row
col1, col2 = st.columns(2)

for index, badge in enumerate(badges):
    col = col1 if index % 2 == 0 else col2  # Alternate between columns

    # Load image
    image_path = f"Badges/{badge['image']}"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((120, 120))
        col.image(img, caption=badge["name"], use_container_width=True)
    else:
        col.warning(f"Image not found: {image_path}")

    # Purchase button
    if badge["name"] not in st.session_state.purchased_badges:
        if col.button(f"Buy ({badge_price} pts)", key=badge["name"]):
            if st.session_state.points >= badge_price:
                st.session_state.points -= badge_price
                st.session_state.purchased_badges.add(badge["name"])
                st.success(f"✅ Purchased {badge['name']} Badge!")

                # Refresh progress bar
                collected_badges = len(st.session_state.purchased_badges)
                st.rerun()
            else:
                st.error("❌ Not enough points!")

# Completion Message
if collected_badges == total_badges:
    st.success("🏆 **You've collected all the badges! Your collection is complete!** 🎉")
