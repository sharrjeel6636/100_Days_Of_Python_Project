import streamlit as st
import random

# Hangman ASCII art stages
HANGMAN_PICS = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========''', '''
       +---+
       |   |
      [O]  |
      /|\  |
      / \  |
           |
    ========='''
]

# Word list for the game
WORD_LIST = [
    'python', 'elephant', 'banana', 'guitar', 'mountain', 'sunflower', 'galaxy',
    'ocean', 'adventure', 'technology', 'strawberry', 'jazz', 'library', 'mystery',
    'happiness', 'computer', 'diamond', 'vacation', 'wizard', 'firefly'
]

def init_game():
    """Initializes or resets the game state."""
    secret_word = random.choice(WORD_LIST)
    st.session_state.secret_word = secret_word
    st.session_state.display_word = ['_'] * len(secret_word)
    st.session_state.lives = 7
    st.session_state.guessed_letters = []
    st.session_state.game_status = 'running' # Can be 'running', 'won', or 'lost'
    st.session_state.guess = "" # Clear input field

def handle_guess(guess):
    """Processes a player's guess."""
    # 1. Input Validation
    if len(guess) != 1 or not guess.isalpha():
        st.warning("Please enter a single letter.")
        return

    guess = guess.lower()

    if guess in st.session_state.guessed_letters:
        st.warning(f"You've already guessed the letter '{guess}'. Try another one!")
        return

    # 2. Add guess to the list of guessed letters
    st.session_state.guessed_letters.append(guess)

    # 3. Check if the guess is correct
    if guess in st.session_state.secret_word:
        # Correct guess
        for i, letter in enumerate(st.session_state.secret_word):
            if letter == guess:
                st.session_state.display_word[i] = letter
    else:
        # Incorrect guess
        st.session_state.lives -= 1
        st.error(f"'{guess}' is not in the word. You lose a life! 💔")

    # 4. Check for win/loss conditions
    if '_' not in st.session_state.display_word:
        st.session_state.game_status = 'won'
    elif st.session_state.lives == 0:
        st.session_state.game_status = 'lost'

# --- Main App ---

st.title("🪢 Hangman Game 🪢")
st.markdown("---")

# Initialize the game if it's not already running
if 'game_status' not in st.session_state:
    init_game()

# --- Game Interface ---
if st.session_state.game_status == 'running':
    st.header("Guess the secret word!")

    # Display Hangman ASCII art
    hangman_stage = 7 - st.session_state.lives
    st.code(HANGMAN_PICS[hangman_stage], language='text')

    # Display game info in columns
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Lives Remaining", value=f"{st.session_state.lives} ❤️")
    with col2:
        st.info(f"Guessed Letters: `{'`, `'.join(sorted(st.session_state.guessed_letters))}`")

    # Display the word with blanks
    st.header(f"`{' '.join(st.session_state.display_word)}`")

    # Guess input form
    with st.form(key='guess_form', clear_on_submit=True):
        guess = st.text_input("Enter a single letter", max_chars=1, key="guess_input")
        submit_button = st.form_submit_button(label='Submit Guess')

    if submit_button and guess:
        handle_guess(guess)
        # Rerun to update the UI immediately after processing the guess
        st.rerun()

# --- Game Over Interface ---
elif st.session_state.game_status == 'won':
    st.balloons()
    st.success("🎉 You won! Congratulations! 🎉")
    st.header(f"The word was: `{st.session_state.secret_word}`")
    if st.button("Play Again?"):
        init_game()
        st.rerun()

elif st.session_state.game_status == 'lost':
    st.snow()
    st.error("💀 Game Over! You ran out of lives. 💀")
    st.header(f"The secret word was: `{st.session_state.secret_word}`")
    st.code(HANGMAN_PICS[-1], language='text') # Show final hangman stage
    if st.button("Play Again?"):
        init_game()
        st.rerun()

st.markdown("---")
st.markdown("Made with ❤️ by Sharjeel Code")
