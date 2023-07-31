import streamlit as st
import pickle
import pandas as pd
import requests

# import imdb

button_style = """
    <style>
    .my-button {
        display: inline-block;
        background-color: black;
        color: white;
        padding: 10px 20px;
        border: 2px solid red;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        cursor: pointer;
        border-radius: 4px;
    }
    </style>
"""

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ac57064235fefa00204775dc634edf60&language=en-US'.format(movie_id))
    data = response.json()
    reviews = requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=ac57064235fefa00204775dc634edf60&language=en-US'.format(movie_id))
    reviews = reviews.json()
    key=''
    for i in range(0,len(reviews['results'])):
        if reviews['results'][i]['type'] == 'Trailer':
            key = reviews['results'][i]['key']
            break
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'],data['release_date'],data['imdb_id'],key,data['vote_average']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]

    recommended_movies = []
    recomended_movies_posters = []
    recomended_movies_date = []
    recomended_movies_imdb = []
    recomended_movies_key = []
    recomended_movies_vote = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        poster,date,imdb,key,vote = fetch_poster(movie_id)
        recomended_movies_posters.append(poster)
        recomended_movies_date.append(date)
        recomended_movies_imdb.append(imdb)
        recomended_movies_key.append(key)
        recomended_movies_vote.append(vote)
    return recommended_movies,recomended_movies_posters,recomended_movies_date,recomended_movies_imdb,recomended_movies_key,recomended_movies_vote


movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select the Movie',movies['title'].iloc[:-5].values
)

if st.button('Recommend'):
    names,posters,date,imdb,key,vote = recommend(selected_movie_name)
    col1, col2 = st.columns([2, 1])
    print(vote)
    col1.markdown(
    f"""
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <h3>{names[0]}</h3>
        <img src="{posters[0]}" alt="Movie Poster" style="max-width: 200px;">        
    </div>
    """,
    unsafe_allow_html=True
    )
    col2.markdown("<br>", unsafe_allow_html=True)
    col2.markdown("<br>", unsafe_allow_html=True)
    col2.markdown(f"**Date:** {date[0]}")   

    col2.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[0],2)}/10", unsafe_allow_html=True)
    trailer_text = "Watch Trailer"
    trailer_url = "https://www.youtube.com/watch?v=" + key[0]
    col2.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)

    imdb_text = "Go to IMDb"
    imdb_url = "https://www.imdb.com/title/" + imdb[0]
    button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
    col2.markdown(button_markup, unsafe_allow_html=True)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.markdown(f"**{names[1]}**")
        st.image(posters[1])
        st.text(date[1])
        rating = int(vote[1])
        st.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[1],2)}/10", unsafe_allow_html=True)
        trailer_text = "Watch Trailer"
        trailer_url = "https://www.youtube.com/watch?v="+ key[1]
        st.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)
        imdb_text = "Go to IMDb"
        imdb_url = "https://www.imdb.com/title/"+ imdb[1]
        button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(button_markup, unsafe_allow_html=True)       

    with col2:
        st.markdown(f"**{names[2]}**")
        st.image(posters[2])
        st.text(date[2])
        rating = int(vote[2])
        st.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[2],2)}/10", unsafe_allow_html=True)
        trailer_text = "Watch Trailer"
        trailer_url = "https://www.youtube.com/watch?v="+ key[2]
        st.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)
        imdb_text = "Go to IMDb"
        imdb_url = "https://www.imdb.com/title/"+ imdb[2]
        button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(button_markup, unsafe_allow_html=True)   

    with col3:
        st.markdown(f"**{names[3]}**")
        st.image(posters[3])
        st.text(date[3])
        rating = int(vote[3])
        st.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[3],2)}/10", unsafe_allow_html=True)
        trailer_text = "Watch Trailer"
        trailer_url = "https://www.youtube.com/watch?v="+ key[3]
        st.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)
        imdb_text = "Go to IMDb"
        imdb_url = "https://www.imdb.com/title/"+ imdb[3]
        button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(button_markup, unsafe_allow_html=True)   

    with col4:
        st.markdown(f"**{names[4]}**")
        st.image(posters[4])
        st.text(date[4])
        rating = int(vote[4])
        st.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[4],2)}/10", unsafe_allow_html=True)
        trailer_text = "Watch Trailer"
        trailer_url = "https://www.youtube.com/watch?v="+ key[4]
        st.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)
        imdb_text = "Go to IMDb"
        imdb_url = "https://www.imdb.com/title/"+ imdb[4]
        button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(button_markup, unsafe_allow_html=True)   
        
    with col5:
        st.markdown(f"**{names[5]}**")
        st.image(posters[5])
        st.text(date[5])
        rating = int(vote[5])
        st.markdown(f"**Rating:** \u2B50\uFE0F{round(vote[5],2)}/10", unsafe_allow_html=True)
        trailer_text = "Watch Trailer"
        trailer_url = "https://www.youtube.com/watch?v="+ key[5]
        st.markdown(f'<a href="{trailer_url}">{trailer_text}</a>', unsafe_allow_html=True)
        imdb_text = "Go to IMDb"
        imdb_url = "https://www.imdb.com/title/"+ imdb[5]
        button_markup = f"""<a href="{imdb_url}" class="my-button">{imdb_text}</a>"""
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(button_markup, unsafe_allow_html=True)   

