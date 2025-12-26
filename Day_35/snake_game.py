import streamlit as st
import time
import random

st.set_page_config(page_title="🐍 Snake Game", layout="centered")

GRID_SIZE = 15
SPEED = 0.25  # Thoda slower start ke liye (bad mein fast kar sakte ho)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize ONLY once
if "snake" not in st.session_state:
    st.session_state.snake = [(7, 7)]  # Center
    st.session_state.direction = RIGHT
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.last_move_time = time.time()
    # Safe food
    while True:
        fx = random.randint(0, GRID_SIZE-1)
        fy = random.randint(0, GRID_SIZE-1)
        if (fx, fy) not in st.session_state.snake:
            st.session_state.food = (fx, fy)
            break

st.title("🐍 Snake Game")
st.markdown("**Buttons se direction badlo – snake khud chalega aur maze lo!**")

st.metric("Score", st.session_state.score)

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("←", use_container_width=True):
        if st.session_state.direction != RIGHT:
            st.session_state.direction = LEFT
            st.rerun()  # Instant change
with col2:
    if st.button("↑", use_container_width=True):
        if st.session_state.direction != DOWN:
            st.session_state.direction = UP
            st.rerun()
    if st.button("↓", use_container_width=True):
        if st.session_state.direction != UP:
            st.session_state.direction = DOWN
            st.rerun()
with col3:
    if st.button("→", use_container_width=True):
        if st.session_state.direction != LEFT:
            st.session_state.direction = RIGHT
            st.rerun()

# Game Over (ab sirf sahi time pe)
if st.session_state.game_over:
    st.error(f"💀 Game Over! Final Score: {st.session_state.score}")
    if st.button("🔄 Restart Game", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.stop()

# Grid draw
grid_html = "<div style='font-size:40px; line-height:1; text-align:center; background:#000; padding:20px; border-radius:15px;'>"
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        if (x, y) == st.session_state.food:
            grid_html += "🍎"
        elif (x, y) in st.session_state.snake:
            grid_html += "🟢" if (x, y) == st.session_state.snake[0] else "🟩"
        else:
            grid_html += "⬜"
    grid_html += "<br>"
grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)

# Auto move (perfect logic)
current_time = time.time()
if current_time - st.session_state.last_move_time >= SPEED:
    head_x, head_y = st.session_state.snake[0]
    dx, dy = st.session_state.direction
    new_head = (head_x + dx, head_y + dy)

    # Collisions BEFORE move
    if not (0 <= new_head[0] < GRID_SIZE and 0 <= new_head[1] < GRID_SIZE):
        st.session_state.game_over = True
    elif new_head in st.session_state.snake:
        st.session_state.game_over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.score += 1
            while True:
                fx = random.randint(0, GRID_SIZE-1)
                fy = random.randint(0, GRID_SIZE-1)
                if (fx, fy) not in st.session_state.snake:
                    st.session_state.food = (fx, fy)
                    break
        else:
            st.session_state.snake.pop()

    st.session_state.last_move_time = current_time

# Always rerun for smooth movement
st.rerun()