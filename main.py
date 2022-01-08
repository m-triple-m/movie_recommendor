import streamlit as st
from predict import predict

st.title("Movie Recommendation System")
st.image('hero.jpg', use_column_width=True)


# sidebar = st.sidebar

# sidebar.title('User Options')


def introduction():
    st.subheader('Enter 🎥 Movie Name Below 👇')
    movie_name = st.text_input('')
    btn = st.button('Get Movie Recommendations')
    if movie_name and btn:
        with st.spinner():
            st.balloons()
            recommendations=predict(movie_name)
            
            st.markdown(f"""
                #
                #
                ## Movies you should watch if you liked "{movie_name}"
                ---
            """)

            for mov in recommendations:
                st.subheader(mov)

introduction()

# options = ['Project Introduction', 'Execution']

# selOption = sidebar.selectbox("Select an Option", options)

# if selOption == options[0]:
#     introduction()
# elif selOption == options[1]:
#     execute()
