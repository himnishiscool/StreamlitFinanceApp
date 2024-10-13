import streamlit as st

st.set_page_config(page_title="Finance App", page_icon="💵")

st.sidebar.success("Select a page!")
st.title("Logs")

# Access logs from session state
logs = st.session_state.get("Log", {})

# Display logs with proper formatting
for key, log in logs.items():
    color = "#1DB954" if log["Type"] == "Earned" else "#E74C3C"

    st.markdown(
        f"""
        <div style="
            border: 2px solid {color};
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background-color: #1c1c1c;
        ">
            <p style="font-size:18px; margin:0; color:white;">
                <b>Amount:</b> ${log["Amount"]:.2f}
            </p>
            <p style="font-size:18px; margin:0; color:{color};">
                <b>Type:</b> {log["Type"]}
            </p>
            <p style="font-size:18px; margin:0; color:gray;">
                <b>Description:</b> {log["Description"]}
            </p>
            <p style="font-size:14px; margin:0; color:#aaaaaa;">
                <b>Time:</b> {log["Time"]}
            </p>
        </div>
        """, unsafe_allow_html=True
    )
