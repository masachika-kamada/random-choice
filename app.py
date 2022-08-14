import streamlit as st
import random
import streamlit.components.v1 as stc


def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Fun Community 仲良くなろうの会</h1>",
            unsafe_allow_html=True)
    clicked = st.button("お題を決める")
    with open("data.txt", mode="r", encoding="utf-8") as f:
        themes = f.read().splitlines()

    # css作成
    button_css = """
    <style>
    div.stButton {
        text-align: center;
    }
    div.stButton > button {
        text-align: center;
        width: 400px;a
        height: 60px;
        color: #5f6c7b;
        margin-top: 60px;
        margin-bottom: 40px;
        font-size: 30px;
    }
    </style>
    """
    # css適用
    st.markdown(button_css, unsafe_allow_html=True)

    if clicked:
        idx = random.randrange(len(themes))
        stc.html(f"""
        <h1 class='title'>{themes[idx]}</h1>
        <style>
        .title {{
            text-align: center;
            color: #5f6c7b;
            font-size:60px;
        }}
        </style>
        """)


if __name__ == "__main__":
    main()
