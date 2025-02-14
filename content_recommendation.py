# content_recommendation.py
import pandas as pd

# Não é mais necessário o uso do argparse
# df_user_acc = pd.read_parquet("recommendation.parquet") 
# df_news = pd.read_parquet("news_processed.parquet")

def recommend_content_based(user_id, users_data, articles_data):
    # Aqui você processa o 'user_id' que foi passado como argumento
    user_row = users_data[users_data['userId'] == user_id]
    if user_row.empty:
        return []

    # Extração de dados do usuário para recomendação
    user_history = set(user_row['history'].iloc[0])  # Artigos já lidos
    user_article_types = set(user_row['article_types'].iloc[0])  # Tipos de artigos de interesse

    # Filtra artigos que o usuário ainda não leu
    potential_articles = articles_data[~articles_data['page'].isin(user_history)]

    # Recomenda artigos com base nos tipos preferidos pelo usuário
    recommendations = potential_articles[potential_articles['article-type'].isin(user_article_types)]
    
    # Ordena por data de modificação (mais recente primeiro)
    recommendations = recommendations.sort_values(by='modified', ascending=False)
    
    return recommendations[['page', 'url']].head(20).to_dict(orient='records')
