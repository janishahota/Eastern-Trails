import os
import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Build the logo path using os.path.join
logo_path = os.path.join("assets", "logo.png")

# Custom CSS for a light, Northeast India–inspired theme
st.markdown(
    """
    <style>
      /* Overall background */
      body {
         background-color: #E6F2E6;  /* Light earthy green */
      }
      /* Header styling */
      .header {
         background-color: #F5F5DC;  /* Off-white reminiscent of traditional textiles */
         padding: 15px 20px;
         border-bottom: 2px solid #ddd;
         display: flex;
         align-items: center;
      }
      .title-container {
         display: flex;
         align-items: center;
      }
      .logo {
         height: 60px;
      }
      .title {
         font-size: 32px;
         font-weight: bold;
         color: #2F3E46;
         margin-left: 15px;
      }
      /* Subtitle styling */
      .subtitle {
         text-align: center;
         font-size: 24px;
         color: #2F3E46;
         margin: 20px 0;
      }
      /* Styling for feature cards using Streamlit buttons */
      .stButton>button {
         font-size: 16px;
         height: 150px;
         width: 250px;
         background-color: #FFF8E7;  /* Soft warm cream */
         border: none;
         border-radius: 15px;
         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
         transition: transform 0.3s, box-shadow 0.3s;
         margin-bottom: 20px;
         white-space: pre-line;
         text-align: center;
      }
      .stButton>button:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0,0,0,0.2);
      }
    </style>
    """,
    unsafe_allow_html=True
)

#########################
# HEADER: Logo & Title  #
#########################
with st.container():
    # Use two columns: one for the logo and one for the title
    col_logo, col_title = st.columns([0.15, 0.85])
    with col_logo:
        # Load and display the logo using st.image()
        st.image(logo_path, width=60)
    with col_title:
      st.markdown(
    "<div align='center'><h1 style='display:inline-block; margin-left:-200px; font-size:32px; font-weight:bold; color:#2F3E46;'>Eastern Trails</h1></div>",
    unsafe_allow_html=True
)


# SUBTITLE
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

##############################
# FEATURE CARDS SECTION      #
##############################
st.markdown("### Explore Our Features")

# Define the card data: (Icon, Title, Description, Page filename)
cards = [
    ("📝", "Recommendation system", "Tailored Travel Suggestions to Plan Your Perfect Trip", "Package_Recommendation.py"),
    ("📝", "Blog", "Read travel stories and tips.", "Blog.py"),
    ("🤖", "Chatbot", "Get AI-powered travel recommendations.", "Chatbot.py"),
    ("👥", "Group Planning", "Plan trips with your friends.", "Group_Planning.py"),
    ("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "Souvenirs.py"),
    ("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "Tourist_Guide.py"),
    ("📅", "Travel Itinerary", "Plan your trip with customizable itineraries.", "Travel_Itinerary.py"),
    ("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "Trivia.py"),
    ("☀️", "Weather", "Stay informed with real-time weather updates.", "Weather.py"),
    ("📰", "News", "Get the latest travel news updates.", "News.py"),
]

# Arrange cards in rows of 3 columns
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(cards):
            icon, title, description, page = cards[idx]
            button_label = f"{icon} {title}\n\n{description}"
            with col:
                if st.button(button_label, key=title):
                    st.switch_page(f"pages/{page}")

# FOOTER
st.markdown("---")
st.write("Eastern trails, Estd 2025")
