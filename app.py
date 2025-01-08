## Main Application File (app.py)

from flask import Flask, render_template, request, send_file, jsonify
from services.twitter_fetcher import fetch_tweets
from services.sentiment_analyzer import analyze_sentiment
from services.visualization import create_visualization
from services.csv_exporter import export_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    keyword = request.form['keyword']
    count = int(request.form['count'])
    tweets = fetch_tweets(keyword, count)
    sentiment_data = analyze_sentiment(tweets)

    img = create_visualization(sentiment_data)
    csv_file = export_to_csv(sentiment_data)

    response = {
        'visualization': f"data:image/png;base64,{img.read().encode('base64').decode()}",
        'csv_file': csv_file
    }

    return jsonify(response)

@app.route('/download_csv')
def download_csv():
    file_path = export_to_csv()
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
