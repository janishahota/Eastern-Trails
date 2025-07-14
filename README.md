# Year 2 CRS AI Capstone Project 2024 – 25
# Scenario 1 - AI-Driven Gamified Travel Advisor
# Project Name: - Eastern Trails
# Contributors: - Karan Amol Rajankar, Janisha Hota, Sreelakshmi Rajesh

### Introduction
"Travel makes one modest. You see what a tiny place you occupy in the world." – Gustave Flaubert <br> 
India's northeastern states are a treasure trove of culture, landscapes, and traditions that remain relatively unexplored. With diverse communities, breathtaking scenery, and rich heritage, the Northeast offers travelers an unparalleled experience. However, many tourists hesitate due to a lack of reliable travel information and cultural insights.

### Problem Statement
• **Low Awareness & Misconceptions** – Over 65% of Indian travelers are unaware of the diverse attractions in the Northeast, often associating the region only with hill stations like Shillong or Kaziranga, while missing out on lesser-known cultural gems (India Tourism Survey, 2023). <br>
• **Lack of Reliable Travel Information** – More than 70% of potential visitors struggle to find well-organized itineraries, accommodation recommendations, and cultural insights tailored to the Northeast, making trip planning difficult (TripAdvisor India Report, 2023). <br>
• **Limited Food & Cultural Familiarity** – Over 55% of domestic tourists are hesitant about visiting due to unfamiliarity with local cuisine and customs, fearing they may not find comfortable dining options or cultural guidance (Indian Travel Trends Report, 2023). <br>
• **Seasonal Travel Uncertainty** – The Northeast’s weather varies drastically, and over 60% of travelers find it hard to determine the best time to visit each state, leading to trip cancellations or missed seasonal events like Hornbill Festival or Ziro Music Festival (India Holiday Report, 2022). <br>
• **Transportation Challenges for Tourists** – Around 60% of travelers find it difficult to navigate within the Northeast due to limited public transport options, irregular taxi services, and lack of online booking platforms, making intra-state travel inconvenient (TravelEase India Report, 2023). <br>

### Goal
To bridge this gap, this project aims to create a dedicated travel advisory app for India's northeastern states, offering curated travel recommendations, real-time safety updates, and culturally immersive experiences to promote tourism while ensuring traveler confidence and convenience.

### Objectives
•	Provide authentic, well-researched travel guides for all northeastern states. <br>
•	Integrate real-time safety, weather, and accessibility updates. <br>
•	Highlight the region’s cultural diversity, festivals, and heritage. <br>
•	Offer budget-friendly itinerary planning based on user preferences. <br>

## Requirement Gathering
**Functional requirements** <br>
- Personalised Recommendations:Recommend destinations based on user preferences <br>
- Live Data Integration: Real-time weather <br>
- Trivia: Include fun and engaging trivia related to Northeast India’s history, culture, and landmarks. <br>
- Integrated Chatbot: An AI-driven chatbot to provide instant answers to user queries. The chatbot can recommend destinations, assist with trip planning and suggest trip packages. <br>
- Souvenir Badges: Users receive a souvenir badge as they complete each milestone in their trip.

**Technical requirements**
- Streamlit for deployment. <br>
- Integrate API’s <br>
- Backend development using Python Programming language and its libraries <br>

## Data Exploration
**Datasets**
-We explored various datasets on Kaggle and UNWTO but couldn't find one that perfectly aligns with our requirements.
Thus we generated a dataset using multiple data generators like explo, mockaroo, generatedata.com, ChatGPT etc.

**API keys**
- OpenWeather API: For real-time weather information, forecasts, and historical weather data of various destinations.
- Gemini API: For chatbot integration


## Journey Map
https://www.canva.com/design/DAGW1mX-TTs/X3iOPZVZzdJyepY2yM__LA/edit?utm_content=DAGW1mX-TTs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## User Personas
https://www.canva.com/design/DAGVmqOXij0/1wNJU42RPvoJ3c6nf3iqtQ/edit?utm_content=DAGVmqOXij0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Scamper
https://www.canva.com/design/DAGcRi7_t1w/ZkmcyiZYx3yb4tftTQhUNw/edit?utm_content=DAGcRi7_t1w&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Napkin Pitch
https://www.canva.com/design/DAGbk58W9DY/T9uH6A88__T53x7Kq5tAhg/edit

## Features
- **Travel Itinerary:** Create and customize detailed travel itineraries based on user preferences, travel history, and trip duration. Users can choose from AI-suggested plans or manually add locations, accommodations, and activities. The itinerary dynamically adjusts based on weather conditions, local events, and travel disruptions.
- **Chatbot:** Receive AI-powered travel recommendations and instant answers to common travel-related queries. The chatbot provides real-time assistance for itinerary modifications, language translations, emergency contacts, and booking suggestions, ensuring a seamless travel experience.
- **Trivia:** Engage with interactive quizzes that test and expand your knowledge of NorthEast India. Questions are curated based on history, folklore, geography, and cultural traditions, offering an educational and fun way to explore the region. Earn points, unlock rewards, and challenge friends to see who knows the most!
- **Weather:** Get real-time weather updates for various travel destinations, ensuring that your trip is well-planned. The app integrates live forecasting APIs to provide temperature, precipitation, and climate alerts, helping travelers prepare for different weather conditions before and during their journey.
- **Tourist Guide:** Discover must-visit attractions and hidden gems through curated travel guides. These guides include historical backgrounds, best visiting times, insider tips, and local recommendations. Users can also explore offbeat locations that aren't commonly found in mainstream travel lists.
- **Souvenirs:** Explore and shop for authentic regional souvenirs directly through the app. Discover handcrafted items, cultural artifacts, and specialty products from local artisans across NorthEast India. Users can also earn digital collectibles and virtual travel badges as part of their journey.
- **Group Planning(only Frontend):** Coordinate and plan group trips effortlessly with friends and family. The feature allows shared itinerary creation, collaborative decision-making, and real-time updates on group activities. Users can also split costs, set reminders, and vote on destinations and accommodations.
- **Blog:** Read and share travel stories, tips, and guides from experienced travelers. Whether it’s adventure tales, budget travel hacks, or cultural deep-dives, this feature creates a community-driven platform where users can exchange insights and recommendations.
Game: Enjoy interactive travel games designed to make planning fun and engaging. These games incorporate elements of adventure, exploration, and trivia, encouraging users to learn more about their destinations while competing for rewards.
- **AI-Driven Personalized Recommendations:** Uses collaborative filtering and content-based recommendation algorithms to suggest destinations based on user preferences, travel history, and real-time trends. Features dynamic itinerary generation with adaptive route optimization, considering weather conditions, cultural events, and user interests.
- **Virtual Trekking:** A simple trekking game where players "explore" virtual landscapes of the northeastern states using hand gestures or keyboard keys.

## Technologies Used

1.	Python – The core backend language used to handle logic, data processing, and machine learning models, ensuring efficient computations, API integrations, and database interactions while providing an easy-to-maintain, scalable structure for future improvements in travel recommendations. <br>
2.	Streamlit – Used to create an interactive web application interface, allowing users to input preferences, visualize recommendations, and explore travel packages in a seamless, dynamic, and user-friendly environment without needing complex frontend development knowledge. <br>
3.	SQLite – A lightweight, file-based database system that stores user inputs, travel history, safety preferences, and recommendation logs, ensuring structured data retrieval, efficient storage, and seamless integration with the Python backend. <br>
4.	Pandas – A powerful data manipulation library used for handling and processing travel data, analyzing user preferences, and structuring destination information, ensuring quick retrieval and transformation of data for recommendation calculations. <br>
5.	NumPy – Used for numerical operations, data structuring, and performing array-based computations on travel-related statistics, such as budget calculations, distance metrics, and optimization functions, ensuring fast and memory-efficient processing. <br>
6.	Scikit-learn – A machine learning library used for recommendation models, clustering destinations based on user interests, and optimizing travel package selections by analyzing past user data, ensuring relevant and data-driven suggestions. <br>
7.	Pygame – Used for interactive features like animations, sound effects, or mini-games within the travel application, making user engagement more immersive by simulating travel scenarios or adding gamification elements, such as collecting points or unlocking destinations. <br>
8.	OpenCV (cv2) – Used for computer vision tasks, such as detecting user engagement through facial recognition, capturing live interactions, or enabling gesture-based inputs to navigate the travel system, enhancing accessibility and making interactions more dynamic. <br>
9.	datetime – Used for handling date-based logic, such as travel itinerary scheduling, calculating the best time to visit destinations, and filtering travel recommendations based on seasonal trends or user availability, ensuring well-timed and relevant trip planning. <br>
10.	requests – Used for fetching real-time travel data, such as weather forecasts, flight or hotel prices, and safety updates from external APIs, ensuring users receive up-to-date and relevant information for better trip planning. <br>
11.	PIL (Pillow) – Used for image processing tasks, such as resizing, enhancing, or overlaying travel-related images, allowing dynamic visualization of destinations, user-uploaded photos, and badge icons, ensuring a visually appealing and interactive experience. <br>


## Collaborative Vs. Content-Based Filtering
This system is using content-based filtering.
In content-based filtering, recommendations are based on the features or attributes of the items (in this case, travel packages) and the user's preferences. Here’s why:
**User Input-Based Recommendations:** The system asks the user for their preferences (e.g., weather, budget level, popularity, etc.), and it then uses these preferences to make predictions about the most appropriate travel package.
**Feature Matching:** The system encodes user preferences and matches them with features of travel packages stored in the dataset, such as "Weather", "Budget Level", "Popularity", etc. The package is recommended based on these feature similarities, rather than relying on other users' behavior (which would be typical in collaborative filtering).

## Rewards-System
Badges: Awarded for milestones like visiting landmarks or eco-friendly actions. <br>
Virtual Souvenirs: Collectibles for explored destinations, or points earned based on bookings and interactive features
Points System: Redeem points for discounts, travel coupons, or premium app features.

## Data Preprocessing
- Our Dataset contains entries with information for each on State, Weather, Budget Level, Budget (INR), Transportation Options, Food , Hotels , Famous Places to Visit , Activities, Popularity, Reviews, Season, Language ,Safety ,Family-Friendly, Cultural Highlights
- It has 10,000 total entries.
- Class Imbalance: Applied SMOTE (Synthetic Minority Oversampling Technique) to handle class imbalance effectively.
- Scaling: Standardized numerical features to normalize their range and improve model training stability.
- Encoding: label encoded categorical variables, such as destination type and travel preferences, for machine interpretability.

## Feature Engineering
- **Selected Features:** Focused on weather conditions, budget level, approximate budget, and destination popularity as key factors influencing travel preferences.
- **Feature Importance:** Validated the significance of selected features using a Random Forest Classifier to ensure optimal model performance.

## Model Building
GridSearchCV: It is a powerful tool in machine learning that automates the process of hyperparameter tuning by performing an exhaustive search over a specified parameter grid. It evaluates model performance for each combination of hyperparameters using cross-validation, ensuring that the selected configuration generalizes well to unseen data. By splitting the dataset into training and validation sets multiple times, GridSearchCV systematically assesses how different hyperparameter values affect the model's accuracy, precision, recall, or any other defined metric. This approach not only identifies the best-performing configuration but also helps in mitigating overfitting, ensuring that the model achieves optimal performance on the test set.

Outcome: Enhanced model accuracy and more reliable package recommendations.

### Personalisation 
- To enhance user experience, a dataset of 10,000 entries was created, representing the 7 northeastern states of India. This dataset incorporates multiple factors such as budget, weather, popularity, and tariff to allow for the development of a recommendation model. The model predicts the best travel package based on user preferences and delivers detailed information tailored to their needs, helping users plan their trip effectively.

***Game Engine - Virtual Trekking*** 
- Concept:
A simple trekking game where players "explore" the virtual landscapes of the northeastern states like Sikkim or Meghalaya through computer vision by walking in front of the camera

- Gameplay Features:
Basic Movement: Use hand gestures (e.g., moving hand forward) or walking movements to control the direction of the player’s movement in the game. <br>
Scenic Views: Show static images or simple animations of famous locations in the northeastern states as players "move" through them. <br>
Trivia & Facts: As players explore, display basic facts about the region (e.g., places to visit, local culture, popular trekking routes). <br> <br>

Technology:
Simple Interaction: Basic hand gestures or keyboard controls for movement 
Static Backgrounds/Images: Use simple background images of popular trekking routes or landmarks to simulate the trekking experience.

## Data Visualization, Storytelling, and UI/UX
#### Tableau Link- https://public.tableau.com/app/profile/sreelakshmi.r2798/viz/TRavelAdvisor/Dashboard1
### Prototype Link- https://easterntrails.flutterflow.app


### Usability Testing and Integration
User testing and refinement involve gathering feedback from real users to improve a product’s usability, functionality, and overall experience. This process helps identify issues, enhance features, and ensure the product meets user needs. We conducted user testing by publishing a feedback form, allowing participants to share their experiences, suggestions, and pain points. The collected responses provided valuable insights into areas requiring improvement. Based on the feedback, necessary refinements were made, such as optimizing performance, fixing bugs, and enhancing user interactions. Continuous testing and iteration ensure a well-polished, user-friendly final product that aligns with expectations and requirements. <br> <br>

Forms Link: - [https://docs.google.com/forms/d/e/1FAIpQLSfBc9ofc8t6M0oFv86_kheR2nj0Ue_AFm2sodNSJUMQDGmo7A/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLSfBc9ofc8t6M0oFv86_kheR2nj0Ue_AFm2sodNSJUMQDGmo7A/viewform?usp=header) <br>
Responses Link: - [https://docs.google.com/spreadsheets/d/124XkOoSoNWoxmy9_HeCYjqi2yO2RolQ091qNMw9c8zA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/124XkOoSoNWoxmy9_HeCYjqi2yO2RolQ091qNMw9c8zA/edit?usp=sharing)

### Usage Instructions
Upon launching the app, the home page will display a header with the Eastern Trails logo and title. A subtitle briefly explains the purpose of the app. The main section displays feature cards (such as Travel Itinerary, Chatbot, Trivia, etc.) arranged in a grid. Click any card to navigate to that feature's dedicated page. Each feature page provides detailed information and interactive tools for planning your trip. Enjoy exploring travel options and planning your adventure through NorthEast India!

## Contribution Guidelines

1. Contributions are welcome! To contribute:
2. Fork the Repository.
3. Create a New Branch for your feature or bug fix
4. Commit Your Changes with clear and descriptive commit messages.
5. Push Your Branch to your fork
6. Open a Pull Request on GitHub describing your changes.
7. Please follow the existing code style and structure.

## Acknowledgments

Streamlit: For providing an easy-to-use framework for building interactive web applications.
OpenCV & NumPy: For their powerful image processing and numerical computation capabilities.
Gemini API: For offering an affordable alternative to OpenAI’s API for chatbot functionality.
Community and Documentation: Thanks to the open-source community for tutorials, forums, and resources that helped shape this project.

**Screenshots / Demos**
![image](https://github.com/user-attachments/assets/61ba8cf1-8dec-42d8-8861-eb382056b4c6)
![image](https://github.com/user-attachments/assets/1a791d0d-a5bd-408b-bb32-0cfebee1aeed)
![image](https://github.com/user-attachments/assets/e7efdb82-c490-4b75-b70e-c6c4469c7921)
![image](https://github.com/user-attachments/assets/0c877339-4858-4650-ade1-f8ec079a0aff)
![image](https://github.com/user-attachments/assets/3db9bff1-7903-4878-ab76-f58153525393)
![image](https://github.com/user-attachments/assets/4bcaf66a-fc3a-42a6-919b-32bfcaa574ba)
![image](https://github.com/user-attachments/assets/3a80c3cf-e73c-40a2-a303-d7e233fcf883)
![image](https://github.com/user-attachments/assets/dfd93aa3-8bf0-4297-940e-4ff3a38466e7)
![image](https://github.com/user-attachments/assets/3ce085b7-7177-4231-a1f9-d44ee6144c80)
![image](https://github.com/user-attachments/assets/f07b9574-c91e-402e-aed1-d75c50e923df)
![image](https://github.com/user-attachments/assets/b05da8ce-205f-4d4e-9017-9133553fbb18)

















