import streamlit as st
import time

# Set page config (must be first Streamlit command)
st.set_page_config(page_title="Team Activity", layout="wide")

# Ensure the correct environment is used
try:
    import micropip
except ModuleNotFoundError:
    st.warning("Micropip module not found. Ensure you are using the correct Streamlit environment.")

# Sidebar
with st.sidebar:
    st.markdown("## Eastern Trails")
    st.markdown("### Platform Navigation")
    st.button("📊 Dashboard")
    st.button("💬 Chats")
    st.button("✅ All Tasks (12)")
    st.button("📂 Projects")
    st.markdown("### Settings")
    st.button("💲 Billing")
    st.button("🌍 Explore")
    st.markdown("---")
    st.image("https://via.placeholder.com/100", width=50)
    st.markdown("*Andrew D.*")
    st.caption("admin@gmail.com")

# Main content
st.title("Team Activity")
st.markdown("Below is a summary of tasks.")

# Filters
filter_col1, filter_col2, filter_col3, _ = st.columns([1, 1, 1, 5])
with filter_col1:
    st.button("All")
with filter_col2:
    st.button("Pending")
with filter_col3:
    st.button("In Progress")

# Search bar
search_query = st.text_input("Search all tasks…", "")

# Task activity timeline
activities = [
    {"name": "Rudy Fernandez", "action": "Completed", "task": "Budgeting", "time": "4m ago"},
    {"name": "Rudy Fernandez", "action": "Started", "task": "Activity Plan", "time": "4m ago"},
    {"name": "Abigail Rojas", "action": "Assigned", "task": "Rudy Fernandez to Activity Plan", "time": "4m ago"},
    {"name": "Abigail Rojas", "action": "Created a project", "task": "Budgeting", "time": "4m ago"},
    {"name": "Liz Ambridge", "action": "Sent a plan update for", "task": "Travel Plan", "time": "4m ago"},
    {"name": "Project Started", "action": "", "task": "", "time": "12d ago"}
]

st.markdown("### Team Activity")
for activity in activities:
    with st.container():
        st.markdown(
            f"{activity['name']}** {activity['action']} *{activity['task']}* "
            f"<span style='float: right; color: gray'>{activity['time']}</span>",
            unsafe_allow_html=True
        )
        st.divider()

# Footer
st.markdown("<br><br><p style='text-align: right; color: gray;'>Built in Streamlit</p>", unsafe_allow_html=True)
