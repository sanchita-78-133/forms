import streamlit as st
st.title("Commute-Index!")
st.header("A form for checking if you are comfortable with your commute!")

mode_of_com = st.multiselect("What is/are your modes of commuting?", ['Bus', 'Train', 'Cab', 'Walking'])
if mode_of_com:
    st.write(f"So you travel by {", ".join(mode_of_com)}")
   

time_taken = st.text_input("The amount of time you take to get to your destination, in integer in hours")

if st.button("Submit"):
    if int(time_taken)>3:
        st.write(time_taken, "?! that is way too much!")

happiness = st.slider("How happy are you with this?", min_value=0, max_value=10)

if happiness<5:
    st.write("Maybe change your tranport!")
else:
    st.write("Good for you!")