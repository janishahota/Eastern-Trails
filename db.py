import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("Dataset and Database/travel_progress.db")
cursor = conn.cursor()

# Create a table for tracking progress if it doesn’t exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS travel_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        state TEXT,
        budget INTEGER,
        best_season TEXT,
        cultural_highlight TEXT,
        food_cost INTEGER,
        hotel_cost INTEGER,
        review_rating REAL,
        flights_booked INTEGER DEFAULT 0,
        hotel_booked INTEGER DEFAULT 0,
        activities_planned INTEGER DEFAULT 0,
        packing_done INTEGER DEFAULT 0,
        trip_completed INTEGER DEFAULT 0
    )
''')

# Insert the recommended package into the database
cursor.execute('''
    INSERT INTO travel_progress (state, budget, best_season, cultural_highlight, food_cost, hotel_cost, review_rating)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    recommended_package_decoded['State'],
    recommended_package_decoded['Budget (INR)'],
    recommended_package_decoded['Season'],
    recommended_package_decoded['Cultural Highlights'],
    recommended_package_decoded['Food Cost (INR)'],
    recommended_package_decoded['Hotel Cost (INR)'],
    recommended_package_decoded['Reviews']
))

# Commit and close
conn.commit()
conn.close()
