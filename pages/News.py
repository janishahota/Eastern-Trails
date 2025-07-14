import streamlit as st
import feedparser
from bs4 import BeautifulSoup

# Define states in Northeast India
northeast_states = [
    "arunachal-pradesh", "assam", "manipur", "meghalaya", 
    "mizoram", "nagaland", "sikkim", "tripura"
]

# RSS feed source
rss_feed_url = "https://nenow.in/feed"

# Function to fetch and parse RSS feed
def fetch_news():
    return feedparser.parse(rss_feed_url)

# Function to remove <img> tags from the summary HTML
def remove_images_from_summary(summary):
    soup = BeautifulSoup(summary, 'html.parser')
    for img in soup.find_all('img'):
        img.decompose()
    return str(soup)

# Streamlit App Layout
st.set_page_config(page_title="📰 Northeast India News", layout="wide")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📰 Northeast India News</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Stay updated with the latest headlines from Northeast India.</p>", unsafe_allow_html=True)

# Sidebar for selecting state
st.sidebar.title("🌍 Filters")
selected_states = st.sidebar.multiselect(
    "Choose states to display news from:",
    options=northeast_states,
    default=["assam", "manipur", "meghalaya"]  # Default selection
)

# Fetch and display headlines
news_feed = fetch_news()

if not news_feed.entries:
    st.write("⚠️ No news available at the moment.")
else:
    for entry in news_feed.entries[:10]:  # Display top 10 headlines
        title = entry.title
        # Remove images from the summary before displaying
        summary = remove_images_from_summary(entry.summary)
        
        st.markdown(f"""
            <div style='padding: 15px; border-radius: 10px; background-color: white; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-bottom: 10px;'>
                <h4>{title}</h4>
                <p>{summary}</p>
                <a style='color: #ff4b4b; font-weight: bold;' href="{entry.link}" target="_blank">🔗 Read More</a>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
