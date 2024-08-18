import pickle
import streamlit as st 
import numpy as np

st.set_page_config(layout="wide")

background_image = 'https://www.shutterstock.com/image-vector/young-woman-opening-huge-open-600nw-2303965869.jpg'
sidebar_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwtaWAE0i950JcgLL0wuPsNakIAOp3B-kqSQ&s'

st.sidebar.image(background_image, width=350)
st.sidebar.markdown("**<center>This is a 'Collaborative Filtering' based book recommender.**", unsafe_allow_html=True)
st.sidebar.markdown("**<center>Check it out! And you can find all the related files/folders on GitHub.**", unsafe_allow_html=True)
st.sidebar.image(sidebar_image, width=250, use_column_width = True)


st.header("BOOK RECOMMENDATION SYSTEM")
model = pickle.load(open("saved_elements/model.pkl", 'rb'))
book_names = pickle.load(open("saved_elements/book_names.pkl", 'rb'))
final_rating = pickle.load(open("saved_elements/final_rating.pkl", 'rb'))
pivot_table = pickle.load(open("saved_elements/pivot_table.pkl", 'rb'))

selected_books = st.selectbox(
  "Type or select a book name",
  book_names
)

def fetch_poster(suggestion):
    book_name = []
    book_id_index = []
    poster_url = []
    for book_id in suggestion:
        book_name.append(pivot_table.index[book_id])
    for title in book_name[0]:
        id = np.where(final_rating['Book-Title']==title)[0][0]
        book_id_index.append(id)
    for idx in book_id_index:
        url = final_rating.iloc[idx]['Image-URL-L']
        poster_url.append(url)
    return poster_url

def recommender(book_name):
    recom_books = []
    book_id = np.where(pivot_table.index==book_name)[0][0]
    distance, suggestion = model.kneighbors(pivot_table.iloc[book_id,:].values.reshape(1, -1), n_neighbors = 6)
    poster_url = fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books = pivot_table.index[suggestion[i]]
        for j in books:
            recom_books.append(j)
    return recom_books, poster_url

if st.button('Show Recommendations'):
    recommended_books, poster_urls = recommender(selected_books)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_books[1])
        st.image(poster_urls[1])

    with col2:
        st.text(recommended_books[2])
        st.image(poster_urls[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_urls[3])

    with col4:
        st.text(recommended_books[4])
        st.image(poster_urls[4])

    with col5:
        st.text(recommended_books[5])
        st.image(poster_urls[5])
