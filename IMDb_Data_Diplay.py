import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# File uploader
st.title("IMDb Movies Data Analysis")

uploaded_file = st.file_uploader("Upload IMDb Movies CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Convert columns to numeric if necessary
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['voting_counts'] = pd.to_numeric(df['voting_counts'], errors='coerce')
    df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

    st.sidebar.header("Filters")
    
    # Filtering Options
    min_rating, max_rating = st.sidebar.slider("Filter by Rating", float(df['Rating'].min()), float(df['Rating'].max()), (float(df['Rating'].min()), float(df['Rating'].max())))
    min_votes, max_votes = st.sidebar.slider("Filter by Voting Counts", int(df['voting_counts'].min()), int(df['voting_counts'].max()), (int(df['voting_counts'].min()), int(df['voting_counts'].max())))
    
    #genre_options = st.sidebar.multiselect("Select Genre", df['Genre'].unique())
    
    filtered_df = df[(df['Rating'].between(min_rating, max_rating)) & (df['voting_counts'].between(min_votes, max_votes))]
    
    #if genre_options:
        #filtered_df = filtered_df[filtered_df['Genre'].isin(genre_options)]

    # Top 10 Movies by Rating & Votes
    st.subheader("Top 10 Movies by Rating")
    top_10_rating = df.nlargest(10, 'Rating')[['Title', 'Rating']]
    st.dataframe(top_10_rating)

    st.subheader("Top 10 Movies by Voting Counts")
    top_10_votes = df.nlargest(10, 'voting_counts')[['Title', 'voting_counts']]
    st.dataframe(top_10_votes)

    # Genre Distribution (Bar Chart)
    #st.subheader("Genre Distribution")
    #genre_counts = df['Genre'].value_counts()
    #fig = px.bar(genre_counts, x=genre_counts.index, y=genre_counts.values, labels={'x': 'Genre', 'y': 'Movie Count'})
    #st.plotly_chart(fig)

    # Average Duration by Genre (Horizontal Bar Chart)
    #st.subheader("Average Duration by Genre")
    #avg_duration = df.groupby('Genre')['Duration'].mean().sort_values()
    #fig, ax = plt.subplots()
    #avg_duration.plot(kind='barh', ax=ax)
    #st.pyplot(fig)

    # Voting Trends by Genre
   # st.subheader("Voting Trends by Genre")
    #avg_votes_by_genre = df.groupby('Genre')['voting_counts'].mean().sort_values()
    #fig, ax = plt.subplots()
    #avg_votes_by_genre.plot(kind='bar', ax=ax, color='orange')
    #st.pyplot(fig)

    # Rating Distribution (Histogram)
    #st.subheader("Rating Distribution")
    #fig, ax = plt.subplots()
    #sns.histplot(df['Rating'], bins=20, kde=True, ax=ax)
    #st.pyplot(fig)

    # Genre-Based Rating Leaders (Table)
    #st.subheader("Top Rated Movies in Each Genre")
    #genre_leaders = df.loc[df.groupby('Genre')['Rating'].idxmax(), ['Genre', 'Title', 'Rating']]
    #st.dataframe(genre_leaders)

    # Most Popular Genres by Voting (Pie Chart)
    #st.subheader("Most Popular Genres by Voting")
    #genre_votes = df.groupby('Genre')['voting_counts'].sum()
    #fig = px.pie(genre_votes, names=genre_votes.index, values=genre_votes.values, title="Genres by Total Votes")
    #st.plotly_chart(fig)

    # Duration Extremes (Table)
    #st.subheader("Movies with Shortest & Longest Duration")
    #shortest_movies = df.nsmallest(5, 'Duration')[['Title', 'Duration']]
    #longest_movies = df.nlargest(5, 'Duration')[['Title', 'Duration']]
    #st.write("### Shortest Movies")
    #st.dataframe(shortest_movies)
    #st.write("### Longest Movies")
    #st.dataframe(longest_movies)

    # Ratings by Genre (Heatmap)
    #st.subheader("Ratings by Genre Heatmap")
    #heatmap_data = df.pivot_table(index='Genre', values='Rating', aggfunc='mean')
    #fig, ax = plt.subplots(figsize=(10, 5))
    #sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", ax=ax)
    #st.pyplot(fig)

    # Correlation Analysis (Scatter Plot)
    st.subheader("Correlation Between Ratings & Voting Counts")
    fig = px.scatter(df, x='Rating', y='voting_counts', title="Ratings vs Voting Counts", labels={'Rating': 'IMDb Rating', 'voting_counts': 'Vote Count'})
    st.plotly_chart(fig)

    # Display filtered dataset
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

else:
    st.warning("Please upload a CSV file to proceed.")