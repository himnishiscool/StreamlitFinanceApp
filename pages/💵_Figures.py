import streamlit as st

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Figures")

# Read total spent and earned from session state
amount_spent = st.session_state.get("TSpent", 0)
amount_earned = st.session_state.get("TEarned", 0)

# Display the figures with decoration
st.markdown(
    f"""
    <div style="
        border: 5px solid #1DB954;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 50px;
        background-color: #1c1c1c;
    ">
        <h2 style="color: #1DB954; margin: 0;">💰 Total Earned</h2>
        <p style="font-size: 80px; font-weight: bold; color: #1DB954; margin: 10px 0;">
            ${amount_earned:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        border: 5px solid #E74C3C;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 50px;
        background-color: #1c1c1c;
    ">
        <h2 style="color: #E74C3C; margin: 0;">💸 Total Spent</h2>
        <p style="font-size: 80px; font-weight: bold; color: #E74C3C; margin: 10px 0;">
            ${amount_spent:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True
)
