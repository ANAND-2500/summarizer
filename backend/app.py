from flask import Flask, request, jsonify, send_from_directory
import requests
from gnews import GNews
from textblob import TextBlob
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

GNEWS_API_KEY = "f93a963568966228322d6ffddcbfa971"
news_fetcher = GNews(language="en", max_results=5)

if not os.path.exists("static"):
    os.makedirs("static")

def fetch_news(company):
    url = f"https://gnews.io/api/v4/search?q={company}&lang=en&max=5&apikey={GNEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "summary": article["description"],
            "url": article["url"]
        })
    return articles

def analyze_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

def translate_to_hindi(text):
    return GoogleTranslator(source="auto", target="hi").translate(text)

def generate_hindi_audio(text, company, index):
    tts = gTTS(text=text, lang="hi")
    filename = f"{company}_{index}.mp3"
    filepath = os.path.join("static", filename)
    tts.save(filepath)
    return filename

@app.route("/news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    news_articles = fetch_news(company)
    if not news_articles:
        return jsonify({"error": "No news found"}), 404

    results = []
    for index, article in enumerate(news_articles):
        sentiment = analyze_sentiment(article["summary"])
        detailed_summary = f"{article['title']} - {article['summary']} This article discusses recent updates about {company}."

        # Translate to Hindi
        hindi_summary = translate_to_hindi(detailed_summary)

        # Generate Hindi TTS
        audio_file = generate_hindi_audio(hindi_summary, company, index)

        results.append({
            "title": article["title"],
            "summary": detailed_summary,
            "hindi_summary": hindi_summary,
            "sentiment": sentiment,
            "url": article["url"],
            "audio": f"/static/{audio_file}"
        })

    return jsonify({"company": company, "articles": results})

@app.route('/static/<filename>')
def get_audio(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
