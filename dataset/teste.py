import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
file_path = './files/treino/treino_parte1.csv'  
df = pd.read_csv(file_path)

required_columns = ['history', 'pageVisitsCountHistory', 'scrollPercentageHistory', 'timeOnPageHistory']
df = df.dropna(subset=required_columns)

# Split the 'history' column into individual history IDs
df['history'] = df['history'].str.split(',')  # Split by ','
df_exploded = df.explode('history')  # Create one row per history ID

# Group by 'history' and aggregate metrics
grouped = df_exploded.groupby('history').agg({
    'pageVisitsCountHistory': 'sum',    # Total page visits
    'scrollPercentageHistory': 'mean', # Average scroll percentage
    'timeOnPageHistory': 'mean'        # Average time on page
}).reset_index()

# Normalize the aggregated metrics using MinMaxScaler
scaler = MinMaxScaler()
grouped[['norm_page_visits', 'norm_scroll', 'norm_time']] = scaler.fit_transform(
    grouped[['pageVisitsCountHistory', 'scrollPercentageHistory', 'timeOnPageHistory']]
)

# Define the weights for the popularity score
alpha = 0.5  # Weight for page visits
beta = 0.3   # Weight for scroll percentage
gamma = 0.2  # Weight for time on page

# Calculate the popularity score
grouped['popularity_score'] = (
    alpha * grouped['norm_page_visits'] +
    beta * grouped['norm_scroll'] +
    gamma * grouped['norm_time']
)

# Sort histories by popularity score in descending order
grouped_sorted = grouped.sort_values(by='popularity_score', ascending=False)

# Recommend top N histories
top_n = 10  # Number of recommendations
recommendations = grouped_sorted.head(top_n)

# Display the recommended histories
print("Top Recommended Histories:")
print(recommendations[['history', 'popularity_score']])
