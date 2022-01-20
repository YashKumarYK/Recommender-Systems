#uncomment all the commented code if you want the posters of the  recommended movies along with the names

import streamlit as st
import pickle
import pandas as pd
#import requests


#this function is for the posters of the images if you want the posters of the recommended movies


#def fetch_poster(movie_id):
    #response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=41bfc81f56726a6700c5cfeb97dd6ab1&language=en-US'.format(movie_id))
    #data = response.json()
    #return "https://image.tmdb.org/t/p/w500/" + data['Poster_path']

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster form API
        #recommended_movie_posters.append(fetch_poster(id))
    return recommended_movies #,recommended_movie_posters

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', "rb"))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Type or select a movie from the dropdown',
                                   movies['title'].values)

if st.button("Recommend"):
    # add poster in case you want to return the posters of the image after uncommenting all the comment
    names= recommend(selected_movie_name)
    for i in names:
        st.write(i)


    #row1, row2, row3, row4, row5 = st.columns(5)
    #with row1:
        #st.text(names[0])
        #st.image(posters[0])
    #with row2:
        #st.text(names[1])
        #st.image(posters[1])
    #with row3:
        #st.text(names[2])
        #st.image(posters[2])
    #with row4:
        #st.text(names[3])
        #st.image(posters[3])
    #with row5:
        #st.text(names[4])
        #st.image(posters[4])