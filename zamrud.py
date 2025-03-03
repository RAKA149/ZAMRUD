import streamlit as st

# Halaman Login
def login_page():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://source.unsplash.com/1600x900/?love,romantic');
            background-size: cover;
            color: #FF1493;
        }
        .title {
            font-size: 40px;
            text-align: center;
            color: #fff;
            font-weight: bold;
            text-shadow: 2px 2px 5px #FF1493;
        }
        .login-box {
            background: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(255, 20, 147, 0.5);
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<p class="title">Login untuk Kejutan Romantis 💖</p>', unsafe_allow_html=True)
    with st.container():
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", key="login_btn"):
            if username == "NAJMA NUR AINI" and password == "02122023":
                st.session_state.logged_in = True
                st.experimental_rerun()
            else:
                st.error("Username atau Password salah, coba lagi!")

# Halaman Utama setelah Login
def main_page():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFE4E1;
        }
        .big-font {
            font-size: 50px !important;
            color: #FF1493;
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .heart {
            color: #FF1493;
            font-size: 30px;
            text-align: center;
        }
        .container {
            text-align: center;
            padding: 20px;
        }
        .message {
            background: rgba(255, 182, 193, 0.7);
            padding: 20px;
            border-radius: 15px;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #FF1493;
            box-shadow: 2px 2px 15px rgba(255, 20, 147, 0.5);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<p class="big-font">💖 I Love You So Much! 💖</p>', unsafe_allow_html=True)
    st.markdown('<p class="heart">❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️</p>', unsafe_allow_html=True)
    st.markdown('<div class="container"><p class="message">You are the most beautiful person in my life 💖</p></div>', unsafe_allow_html=True)

# Inisialisasi session state untuk login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Tampilkan halaman sesuai dengan status login
if st.session_state.logged_in:
    main_page()
else:
    login_page()