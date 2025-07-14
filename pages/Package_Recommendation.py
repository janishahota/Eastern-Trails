import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load trained model and scaler
model = joblib.load("Models/best_travel_recommender.pkl")
scaler = joblib.load("Models/scaler.pkl")

# Load dataset
df = pd.read_csv("Dataset and Database/Seven_Sisters_Travel_Packages_Cleaned_Encoded.csv")

# Define state mapping
state_mapping = ['Arunachal Pradesh', 'Assam', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Tripura']

# Define categorical mappings
label_mappings = {
    'Weather': ['Chilly', 'Pleasant', 'Rainy', 'Sunny'],
    'Budget Level': ['Low', 'Medium', 'High'],
    'Transportation Options': ['Low', 'Medium', 'High'],
    'Popularity': ['Low', 'Moderate', 'High'],
    'Season': ['Monsoon', 'Summer', 'Winter'],
    'Cultural Highlights': ['Art Exhibitions', 'Festival', 'Local Traditions']
}

# Features used for training
training_features = ['Budget (INR)', 'Reviews', 'Hotel Cost (INR)', 'Food Cost (INR)', 'Season']

# Streamlit UI
st.title("🌍 Travel Recommendation System")
st.markdown("Find the best travel package based on your preferences!")

# Sidebar for user input
st.sidebar.header("🔍 Enter Your Preferences")

# Categorical Inputs
user_input = {}
for feature, options in label_mappings.items():
    user_input[feature] = st.sidebar.selectbox(f"{feature}", options, index=0)

# Numeric Inputs
user_input["Budget (INR)"] = st.sidebar.slider("💰 Budget (₹)", 5000, 50000, 20000, step=1000)
user_input["Food Cost (INR)"] = st.sidebar.slider("🍽 Expected Daily Food Cost (₹)", 500, 5000, 2000, step=100)
user_input["Hotel Cost (INR)"] = st.sidebar.slider("🏨 Expected Per-Night Hotel Cost (₹)", 1000, 20000, 5000, step=500)
user_input["Reviews"] = st.sidebar.slider("⭐ Minimum Rating (1.0 to 5.0)", 1.0, 5.0, 4.0, step=0.1)

# Convert categorical inputs to numerical values
for feature, options in label_mappings.items():
    user_input[feature] = options.index(user_input[feature])

# Convert user input to DataFrame
input_df = pd.DataFrame([user_input])
input_df = input_df[training_features]

# Apply scaling
scaled_input = scaler.transform(input_df)

# Predict recommended travel state
predicted_state_index = model.predict(scaled_input)[0]

# Normalize numeric features
df['Normalized Budget'] = (df['Budget (INR)'] - df['Budget (INR)'].min()) / (df['Budget (INR)'].max() - df['Budget (INR)'].min())
df['Normalized Reviews'] = (df['Reviews'] - df['Reviews'].min()) / (df['Reviews'].max() - df['Reviews'].min())
df['Normalized Food Cost'] = (df['Food Cost (INR)'] - df['Food Cost (INR)'].min()) / (df['Food Cost (INR)'].max() - df['Food Cost (INR)'].min())
df['Normalized Hotel Cost'] = (df['Hotel Cost (INR)'] - df['Hotel Cost (INR)'].min()) / (df['Hotel Cost (INR)'].max() - df['Hotel Cost (INR)'].min())

# Normalize user input
user_normalized = {
    'Normalized Budget': (user_input['Budget (INR)'] - df['Budget (INR)'].min()) / (df['Budget (INR)'].max() - df['Budget (INR)'].min()),
    'Normalized Reviews': (user_input['Reviews'] - df['Reviews'].min()) / (df['Reviews'].max() - df['Reviews'].min()),
    'Normalized Food Cost': (user_input['Food Cost (INR)'] - df['Food Cost (INR)'].min()) / (df['Food Cost (INR)'].max() - df['Food Cost (INR)'].min()),
    'Normalized Hotel Cost': (user_input['Hotel Cost (INR)'] - df['Hotel Cost (INR)'].min()) / (df['Hotel Cost (INR)'].max() - df['Hotel Cost (INR)'].min())
}

# Compute similarity score
df['Season Match'] = (df['Season'] == user_input['Season']).astype(int)
df['Cultural Match'] = (df['Cultural Highlights'] == user_input['Cultural Highlights']).astype(int)

df['Similarity'] = (
    abs(df['Normalized Budget'] - user_normalized['Normalized Budget']) * 0.25 +  
    abs(df['Normalized Reviews'] - user_normalized['Normalized Reviews']) * 0.2 +  
    abs(df['Normalized Food Cost'] - user_normalized['Normalized Food Cost']) * 0.15 +  
    abs(df['Normalized Hotel Cost'] - user_normalized['Normalized Hotel Cost']) * 0.15 +  
    (1 - df['Season Match']) * 0.15 +  
    (1 - df['Cultural Match']) * 0.1  
)

# Filter the dataset to only include results from the predicted state
filtered_df = df[df['State'] == state_mapping[predicted_state_index]]

# If there are no matching states, fall back to the full dataset
if filtered_df.empty:
    filtered_df = df

# Get the best match within the predicted state
recommended_package = filtered_df.nsmallest(1, 'Similarity').to_dict(orient='records')[0]

# Decode categorical values
recommended_package_decoded = {}
for key, value in recommended_package.items():
    if key in label_mappings and isinstance(value, (int, np.integer)):          
        recommended_package_decoded[key] = label_mappings[key][value]      
    else:         
        recommended_package_decoded[key] = value

if 'State' in recommended_package and isinstance(recommended_package['State'], (int, np.integer)):
    recommended_package_decoded['State'] = state_mapping[recommended_package['State']]
elif 'State' in recommended_package:
    recommended_package_decoded['State'] = recommended_package['State']
else:
    recommended_package_decoded['State'] = state_mapping[predicted_state_index]

# Ensure 'Hotel Cost (INR)' is formatted correctly
if 'Hotel Cost (INR)' in recommended_package:
    recommended_package_decoded['Hotel Cost (INR)'] = int(recommended_package['Hotel Cost (INR)'])

# Display the recommendation
st.subheader("🎉 Recommended Travel Package")
st.markdown(f"""
📍 **Destination:** `{recommended_package_decoded['State']}`  
💰 **Budget:** ₹ `{recommended_package_decoded['Budget (INR)']}`  
⏳ **Best Season:** `{recommended_package_decoded['Season']}`  
🎭 **Cultural Highlights:** `{recommended_package_decoded['Cultural Highlights']}`  
🍽 **Food Cost per day:** ₹ `{recommended_package_decoded['Food Cost (INR)']}`  
🏨 **Hotel Cost per night:** ₹ `{recommended_package_decoded['Hotel Cost (INR)']}`  
⭐ **Average Review Rating:** `{recommended_package_decoded['Reviews']} / 5.0`
""")

# Display the dataset for reference
st.subheader("📊 Travel Package Data")
st.dataframe(df[['State', 'Budget (INR)', 'Season', 'Cultural Highlights', 'Food Cost (INR)', 'Hotel Cost (INR)', 'Reviews']].iloc[5:10])

# Store progress in Streamlit session state
if "progress" not in st.session_state:
    st.session_state.progress = {
        "flights_booked": False,
        "hotel_booked": False,
        "activities_planned": False,
        "packing_done": False,
        "trip_completed": False
    }

st.subheader("📊 Your Travel Planning Progress")

flights = st.checkbox("✈️ Flights Booked", value=st.session_state.progress["flights_booked"])
hotel = st.checkbox("🏨 Hotel Booked", value=st.session_state.progress["hotel_booked"])
activities = st.checkbox("🎟 Activities Planned", value=st.session_state.progress["activities_planned"])
packing = st.checkbox("🎒 Packing Done", value=st.session_state.progress["packing_done"])
trip_done = st.checkbox("✅ Trip Completed", value=st.session_state.progress["trip_completed"])

# Update progress
st.session_state.progress["flights_booked"] = flights
st.session_state.progress["hotel_booked"] = hotel
st.session_state.progress["activities_planned"] = activities
st.session_state.progress["packing_done"] = packing
st.session_state.progress["trip_completed"] = trip_done

# Calculate progress
completed_steps = sum(st.session_state.progress.values())
total_steps = 5
progress_percentage = (completed_steps / total_steps) * 100

# Show progress bar
st.progress(progress_percentage / 100)
st.write(f"**Your progress: {progress_percentage:.2f}% completed!**")
