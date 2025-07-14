import streamlit as st
import json
import os
from datetime import datetime

# File to store blog data
BLOG_FILE = "Dataset and Database/blog_data.json"

# Ensure the JSON file exists
if not os.path.exists(BLOG_FILE):
    with open(BLOG_FILE, "w") as f:
        json.dump([], f)

# Load blog posts
def load_posts():
    try:
        with open(BLOG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save new blog post
def save_post(title, content):
    posts = load_posts()
    new_post = {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    posts.insert(0, new_post)  # Add new post at the top
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=4)

# Delete a blog post
def delete_post(index):
    posts = load_posts()
    if 0 <= index < len(posts):
        del posts[index]
        with open(BLOG_FILE, "w") as f:
            json.dump(posts, f, indent=4)
        st.rerun()

# Streamlit UI
st.set_page_config(page_title="📖 My Blog", layout="wide")
st.title("📖 My Personal Blog")

# Sidebar for adding a new post
st.sidebar.header("📝 Add a New Blog Post")
title = st.sidebar.text_input("Title")
content = st.sidebar.text_area("Content (supports Markdown)")
if st.sidebar.button("Post"):
    if title and content:
        save_post(title, content)
        st.sidebar.success("Post added successfully!")
        st.rerun()
    else:
        st.sidebar.error("Title and Content are required!")

# Search Functionality
search_query = st.text_input("🔍 Search Posts", "")
posts = load_posts()

if search_query:
    posts = [post for post in posts if search_query.lower() in post["title"].lower()]

# Display blog posts
if not posts:
    st.info("No blog posts found.")

for index, post in enumerate(posts):
    with st.container():
        st.markdown(f"## {post['title']}")
        st.markdown(f"🗓️ *{post['date']}*")
        st.markdown(post["content"])
        
        # Delete Button
        if st.button("❌ Delete", key=f"del_{index}"):
            delete_post(index)

        st.markdown("---")

# Custom CSS for styling
st.markdown("""
    <style>
        .block-container { max-width: 750px; }
        h1 { color: #4CAF50; }
        h2 { color: #333; }
        .stButton>button { background-color: #ff4d4d; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)
