import streamlit as st
import pandas as pd
import random
import sqlite3

# Database Functions
def initialize_db():
    conn = sqlite3.connect("Dataset and Database/trivia_scores.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        player_name TEXT,
                        score INTEGER)''')
    conn.commit()
    conn.close()

def add_score(player_name, score):
    conn = sqlite3.connect("Dataset and Database/trivia_scores.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()
    conn.close()

def get_scores():
    conn = sqlite3.connect("Dataset and Database/trivia_scores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10")
    scores = cursor.fetchall()
    conn.close()
    return scores

# Initialize Database
initialize_db()

# Load Questions
def load_questions(file_path):
    return pd.read_csv(file_path).to_dict(orient='records')

def filter_questions_by_category(questions, category):
    if category == "All":
        return random.sample(questions, min(10, len(questions)))
    return [q for q in questions if q["Category"] == category][:10]

st.title("Seven Sisters Trivia Challenge")

# Load data
FILE_PATH = "Dataset and Database/trivia.csv"  # Update with actual path
questions = load_questions(FILE_PATH)

# Player Name Input
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

player_name = st.text_input("Enter your name:", st.session_state.player_name)

if player_name:
    st.session_state.player_name = player_name

# Select Category
categories = ["All"] + list(set(q["Category"] for q in questions))
selected_category = st.selectbox("Which Seven Sister would you like to answer questions about?", categories)

# Initialize session state
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.questions = []
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_answer = None
    st.session_state.answered = False
    st.session_state.shuffled_options = {}

# Start Game
if st.button("Start Game") and player_name:
    st.session_state.game_started = True
    st.session_state.questions = filter_questions_by_category(questions, selected_category)
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_answer = None
    st.session_state.answered = False
    st.session_state.shuffled_options = {}
    st.rerun()

# Game Logic
if st.session_state.game_started:
    if st.session_state.current_question_index < len(st.session_state.questions):
        question_data = st.session_state.questions[st.session_state.current_question_index]
        st.write(f"*Question {st.session_state.current_question_index + 1}:* {question_data['Question']}")

        if st.session_state.current_question_index not in st.session_state.shuffled_options:
            options = [
                ("A", question_data['OptionA']),
                ("B", question_data['OptionB']),
                ("C", question_data['OptionC']),
                ("D", question_data['OptionD'])
            ]
            random.shuffle(options)
            st.session_state.shuffled_options[st.session_state.current_question_index] = options
        else:
            options = st.session_state.shuffled_options[st.session_state.current_question_index]

        correct_option = next(opt[0] for opt in options if opt[0] == question_data['Answer'])

        selected_answer = st.radio("Choose an answer:", [opt[1] for opt in options], 
                                   index=None, key=f"question_{st.session_state.current_question_index}")

        if selected_answer and not st.session_state.answered:
            st.session_state.selected_answer = selected_answer
            st.session_state.answered = True

            chosen_index = [opt[1] for opt in options].index(selected_answer)
            if options[chosen_index][0] == correct_option:
                st.session_state.score += 1
                st.success("Correct! 🎉")
            else:
                st.error(f"Wrong! Correct answer: {options[[opt[0] for opt in options].index(correct_option)][1]}")

        if st.session_state.answered:
            if st.button("Next Question"):
                st.session_state.current_question_index += 1
                st.session_state.selected_answer = None
                st.session_state.answered = False
                st.rerun()

    else:
        final_score = st.session_state.score * 10
        st.write("## Game Over!")
        st.write(f"Your final score: {st.session_state.score}/{len(st.session_state.questions)} ({final_score} points)")

        if player_name:
            add_score(player_name, final_score)

        if st.button("Play Again"):
            st.session_state.game_started = False
            st.rerun()

# Leaderboard
st.write("## Leaderboard")
scores = get_scores()
if scores:
    for rank, (name, score) in enumerate(scores, start=1):
        st.write(f"{rank}. {name} - {score} points**")
else:
    st.write("No scores yet. Play the game to be the first on the leaderboard!")
