import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_parquet("general_recommendation.parquet")
df_news = pd.read_parquet("news_processed.parquet")

# Function to recommend articles based on popularity
def recommend_popular_articles():
    # Define the weights for the popularity score
    alpha = 0.1  # Weight for clicks
    beta = 0.3   # Weight for time on page
    gamma = 0.4  # Weight for scroll percentage
    delta = 0.2  # Weight for page visits

    # Calculate the popularity score
    df['popularity_score'] = (
        alpha * df['numberOfClicksHistory'] +
        beta * df['timeOnPageHistory'] +
        gamma * df['scrollPercentageHistory'] +
        delta * df['pageVisitsCountHistory']
    )

    # Sort histories by popularity score in descending order
    grouped_sorted = df.sort_values(by='popularity_score', ascending=False)

    # Recommend top N histories
    top_n = 10  # Number of recommendations
    recommendations = grouped_sorted.head(top_n)

    recommendations.rename(columns={"history": "page"}, inplace=True)

    recommendations = recommendations.merge(df_news[['page', 'url']], on="page", how="left")

    recommendations = recommendations.dropna(subset=['url'])

    return recommendations[['page', 'url']].to_dict(orient='records')
