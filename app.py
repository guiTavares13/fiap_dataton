from flask import Flask, jsonify, request
from content_recommendation import recommend_content_based
from general_popularity import recommend_popular_articles
import pandas as pd

app = Flask(__name__)

df_user_acc = pd.read_parquet("recommendation.parquet")  
df_news = pd.read_parquet("news_processed.parquet")  

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id')  
    
    if user_id:
        recommendations = recommend_content_based(user_id, df_user_acc, df_news)
        if recommendations:
            return jsonify(recommendations), 200
        else:
            return jsonify({"message": "No recommendations found for this user."}), 404
    else:
        # usuario nao logafo
        recommendations = recommend_popular_articles()  
        return jsonify(recommendations), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)  
