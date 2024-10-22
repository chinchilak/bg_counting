import streamlit as st
import pandas as pd

CATEGORIES = ["Civilian Buildings (blue cards)", 
              "Scientific Buildings (green cards)", 
              "Commercial Buildings (yellow cards)", 
              "Guilds (purple cards)", 
              "Wonder cards", 
              "Progress Tokens", 
              "Coins",
              "Military Tokens"]

IMG_ID = list(range(1, len(CATEGORIES) + 1))
IMG_PATH = "img_7divu"

SEL_STYLE = ["Number Input", "Slider"]

TITLE = "7 Divů (Duel)"

st.set_page_config(page_title=TITLE, layout="wide")

with st.sidebar:
    st.subheader(TITLE)
    with st.expander("Player Setup", expanded=False):
        num_players = st.number_input("Number of Players", min_value=2, max_value=2, value=2)

        player_names = []
        for i in range(num_players):
            player_name = st.text_input(f"Enter name for Player {i+1}", f"Player {i+1}")
            player_names.append(player_name)

        sel_style = st.radio("Input selector style", SEL_STYLE, 0)

    st.container(height=20, border=False)

columns = st.columns(num_players, gap="large")

scores = {category: [] for category in CATEGORIES}
multipliers = {category: [] for category in CATEGORIES}

for idx, player in enumerate(player_names):
    with columns[idx]:
        st.subheader(f"{player}")
        for index, category in enumerate(CATEGORIES):
            with st.expander(f"{category}", expanded=True):
                col1, col2 = st.columns([0.05, 0.95], gap="small")
                with col1:
                    st.image(f"{IMG_PATH}/{index+1}.png", width=50)
                with col2:
                    if sel_style == SEL_STYLE[0]:
                        score = st.number_input(
                            "Score",
                            min_value=0,
                            max_value=100,
                            value=0,
                            step=1,
                            key=f"{player}_{category}_score",
                            label_visibility="collapsed")
                    else:
                        score = st.slider(
                            "Score",
                            min_value=0,
                            max_value=100,
                            value=0,
                            step=1,
                            key=f"{player}_{category}_score",
                            label_visibility="collapsed")                        
                    scores[category].append(score)

with st.sidebar:
    if st.button("Calculate Total Scores"):
        total_scores = [
            sum(scores[category][i] for category in CATEGORIES)
            for i in range(num_players)
        ]
        results = pd.DataFrame({"Player": player_names, "Total Score": total_scores})
        results = results.sort_values(by="Total Score", ascending=False).reset_index(drop=True)

        st.subheader("Results")
        st.dataframe(results, use_container_width=True, hide_index=True)

        winner = results.iloc[0]["Player"]
        st.success(f"🏆 {winner} !")