import streamlit as st

# Dictionary with tourist guide links for each state
tourist_guides = {
    "Manipur": "https://www.google.com/maps/search/tourist+guides+in+manipur/@24.7899385,93.5977092,10z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Tripura": "https://www.google.com/maps/search/tourist+guides+in+tripura/@23.6948154,90.9774763,10z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Arunachal Pradesh": "https://www.google.com/maps/search/tourist+guides+in+arunachal+pradesh/@23.614937,86.005168,6z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Assam": "https://www.google.com/maps/search/tourist+guides+in+assam/@26.443125,91.6264452,8z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Mizoram": "https://www.google.com/maps/search/tourist+guides+in+mizoram/@25.4335371,91.4920204,10z?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Meghalaya": "https://www.google.com/maps/search/tourist+guides+in+meghalaya/@25.4335371,91.4920204,10z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D",
    "Nagaland": "https://www.google.com/maps/search/tourist+guides+in+nagaland/@25.3778153,89.1780782,7z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDIyNC4wIKXMDSoASAFQAw%3D%3D"
}

# Streamlit Page Configuration
st.set_page_config(page_title="🌍 Northeast India Tourist Guides", layout="wide")

# Custom CSS for UI styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .state-title {
            font-size: 24px;
            font-weight: bold;
            color: #000000;
        }
        .guide-card {
            padding: 15px;
            border-radius: 10px;
            background-color: white;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .guide-link {
            color: #007BFF;
            font-weight: bold;
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True)

# Title & Introduction
st.markdown("<h1 style='text-align: center; color: #007BFF;'>🌍 Northeast India Tourist Guides</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Find professional tourist guides for each state in Northeast India.</p>", unsafe_allow_html=True)

# Sidebar for selecting states
st.sidebar.title("📍 Select States")
selected_states = st.sidebar.multiselect(
    "Choose states for tourist guides:",
    options=list(tourist_guides.keys()),
    default=["Manipur", "Assam"]  # Default selection
)

# Display links for selected states
col1, col2 = st.columns(2)  # Two-column layout

for i, state in enumerate(selected_states):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
            <div class='guide-card'>
                <h3 class='state-title'>📌 {state}</h3>
                <a class='guide-link' href="{tourist_guides[state]}" target="_blank">🔗 Find Guides in {state}</a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")  # Divider for better readability
