import streamlit as st
import requests
import datetime

# Function to fetch weather data using OpenWeather API
def get_weather(city):
    API_KEY = "f8cb952227a9226d7088520604acec5a"  # Replace with your actual API Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Function to suggest activities based on weather and preferences
def suggest_activities(weather, preferences):
    activities = set()

    if "rain" in weather.lower():
        activities.update([
            "Visit a local museum to learn about the region's heritage",
            "Explore a cultural center showcasing traditional arts",
            "Enjoy local cuisine at a cozy indoor restaurant"
        ])
    else:
        activities.update([
            "Go trekking in the lush green hills",
            "Visit scenic viewpoints and waterfalls",
            "Explore local markets for handicrafts and souvenirs"
        ])

    if "relaxation" in preferences:
        activities.update([
            "Unwind at a scenic lakeside or wellness retreat",
            "Enjoy a spa session with traditional therapies",
            "Visit a serene monastery for peace and quiet"
        ])

    if "food" in preferences:
        activities.update([
            "Embark on a food trail to taste regional delicacies",
            "Take part in a traditional cooking class",
            "Explore vibrant street food markets"
        ])

    if "adventure" in preferences:
        activities.update([
            "Try river rafting in pristine rivers",
            "Go rock climbing or ziplining",
            "Camp under the stars at scenic locations"
        ])

    if "culture" in preferences:
        activities.update([
            "Attend a local cultural festival if timing aligns",
            "Visit historic temples and traditional villages",
            "Interact with local artisans and experience their crafts"
        ])

    if "nature" in preferences:
        activities.update([
            "Explore wildlife sanctuaries and nature parks",
            "Take a boat ride on beautiful lakes",
            "Discover hidden waterfalls and caves"
        ])

    return list(activities)

# Function to generate a daily itinerary
def generate_itinerary(activities, num_days):
    itinerary = {}
    for day in range(1, num_days + 1):
        day_activities = activities[(day - 1) * 3: day * 3]
        if not day_activities:
            day_activities = ["Free exploration day - discover hidden gems!"]
        itinerary[f"Day {day}"] = day_activities
    return itinerary

# App UI
st.title("🌄 Seven Sisters Travel Itinerary Planner")
st.write("Plan your perfect trip to **Northeast India** with a personalized itinerary tailored to your preferences and the local weather.")

# State and city selection
states = ["Arunachal Pradesh", "Assam", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Tripura"]
selected_state = st.selectbox("🗺️ Choose a state", states)
city = st.text_input("🏙️ Enter the name of a city or town")

# Trip dates and timing
col1, col2 = st.columns(2)
with col1:
    arrival_date = st.date_input("📅 Arrival date", datetime.date.today())
    arrival_time = st.time_input("🕒 Arrival time", datetime.time(9, 0))
with col2:
    departure_date = st.date_input("📅 Departure date", datetime.date.today() + datetime.timedelta(days=3))
    departure_time = st.time_input("🕒 Departure time", datetime.time(17, 0))

# Preferences
preferences = st.multiselect(
    "✨ What types of activities do you prefer?",
    ["relaxation", "food", "adventure", "culture", "nature"],
    default=["nature", "culture"]
)

# Calculate number of days
num_days = (departure_date - arrival_date).days + 1

# Generate Itinerary Button
if st.button("🚀 Generate My Itinerary"):
    if not city:
        st.warning("⚠️ Please enter a city name to get started.")
    else:
        with st.spinner("🔎 Gathering weather data and customizing your itinerary..."):
            weather_data = get_weather(city)

            if weather_data:
                weather_desc = weather_data['weather'][0]['description'].capitalize()
                temp = weather_data['main']['temp']

                st.subheader(f"🌦️ Weather Forecast for {city}")
                st.write(f"- **Condition:** {weather_desc}")
                st.write(f"- **Temperature:** {temp}°C")

                # Generate suggested activities based on weather and preferences
                activities = suggest_activities(weather_desc, preferences)

                # Build itinerary
                itinerary = generate_itinerary(activities, num_days)

                # Display itinerary
                st.subheader("📝 Your Personalized Itinerary")
                for day, day_activities in itinerary.items():
                    st.write(f"### {day}")
                    for activity in day_activities:
                        st.write(f"- {activity}")
            else:
                st.error("⚠️ Unable to fetch weather data. Please double-check the city name or try again later.")

# Footer
st.markdown("---")
st.caption("🌏 Crafted with ❤️ for travelers exploring the magic of Northeast India")
