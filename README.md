Here's an updated **README.md** including details about `run.bat`:

---

# **News Summarizer & Hindi TTS**

## **Project Overview**

This project is a **web-based News Summarization and Text-to-Speech (TTS) application** that extracts the latest news articles related to a given company, analyzes their sentiment, translates them into Hindi, and generates Hindi audio summaries.

## **Tech Stack**

- **Backend:** Flask (Python)
- **Frontend:** Streamlit (Python)
- **APIs Used:**
  - [GNews API](https://gnews.io/) for fetching news
  - [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis
  - [Google Translator (deep_translator)](https://pypi.org/project/deep-translator/) for translation
  - [gTTS](https://pypi.org/project/gTTS/) for text-to-speech conversion

---

## **Project Structure**

📁 **SUMMARIZER**  
&nbsp;&nbsp;📂 **audio** – Stores generated audio files  
&nbsp;&nbsp;📂 **backend**  
&nbsp;&nbsp;&nbsp;&nbsp;📂 `__pycache__` – Compiled Python files  
&nbsp;&nbsp;&nbsp;&nbsp;📂 **static** – Stores static assets (e.g., MP3 files)  
&nbsp;&nbsp;&nbsp;&nbsp;📄 `app.py` – Flask API backend  
&nbsp;&nbsp;📂 **frontend**  
&nbsp;&nbsp;&nbsp;&nbsp;📂 **assets** – Stores frontend assets (CSS, images, etc.)  
&nbsp;&nbsp;&nbsp;&nbsp;📄 `styles.css` – Custom styles for Streamlit UI  
&nbsp;&nbsp;&nbsp;&nbsp;📄 `main.py` – Streamlit frontend for interacting with the backend  
📄 `requirements.txt` – Dependencies for both backend and frontend  
📄 `README.md` – Project documentation  
📄 `run.bat` – Batch script for running backend & frontend

---

## **Setup & Installation**

### **1️⃣ Install Dependencies**

Ensure you have Python installed (preferably **Python 3.8+**). Then, install required packages:

```bash
pip install -r requirements.txt
```

### **2️⃣ Running the Application Using `run.bat`**

The `run.bat` script automates the process of running both the **backend (Flask API)** and the **frontend (Streamlit UI)** in separate terminal windows.

#### **Steps to Run Using `run.bat`:**

1. **Windows Users:**

   - Simply double-click `run.bat` to start both the backend and frontend.

2. **Alternatively, run manually using Command Prompt:**

   ```cmd
   run.bat
   ```

3. **Linux/Mac Users:**
   - Since `.bat` files are for Windows, you need to run the backend and frontend manually (see next section).

---

## **Manual Execution (Alternative to `run.bat`)**

### **Running the Backend (Flask API)**

Navigate to the `backend` directory and run:

```bash
cd backend
python app.py
```

The Flask server will start at **`http://127.0.0.1:5000`**.

### **Running the Frontend (Streamlit UI)**

In a new terminal, navigate to the `frontend` directory and run:

```bash
cd frontend
streamlit run main.py
```

The frontend will be available in your web browser.

---

## **Features**

### ✅ **News Extraction**

- Fetches latest news articles for a given company using **GNews API**.

### ✅ **Sentiment Analysis**

- Analyzes the sentiment (**Positive, Negative, Neutral**) of news summaries.

### ✅ **Hindi Translation & Audio Generation**

- Translates the summary into **Hindi** using **Google Translator**.
- Generates **Hindi audio (MP3)** using **gTTS**.

### ✅ **User-Friendly UI**

- **Streamlit-powered UI** for easy search and interaction.

---

## **API Endpoints**

### **1️⃣ Fetch News Summary & TTS**

**Endpoint:** `GET /news?company=<company_name>`

**Example:**

```http
GET http://127.0.0.1:5000/news?company=Tesla
```

**Response (JSON Example):**

```json
{
  "company": "Tesla",
  "articles": [
    {
      "title": "Tesla Hits New Record",
      "summary": "Tesla's stock reached an all-time high...",
      "hindi_summary": "टेस्ला का स्टॉक नए उच्चतम स्तर पर पहुँच गया...",
      "sentiment": "Positive",
      "url": "https://example.com/tesla-news",
      "audio": "/static/Tesla_0.mp3"
    }
  ]
}
```

---

## **Troubleshooting**

### ⚠️ **Common Issues & Fixes**

1. **Flask API Not Running?**

   - Ensure you are inside the `backend` directory and run `python app.py`.
   - Check if port **5000** is free or change the port in `app.py`.

2. **Streamlit Not Opening?**

   - Make sure the Flask backend is running before launching the frontend.
   - Run `streamlit run main.py` inside the `frontend` directory.

3. **Audio File Not Playing?**
   - Check if the `static/` folder exists and has write permissions.
   - Restart the Flask server to regenerate missing MP3 files.

---

## **Future Improvements**

🚀 **Enhancements planned for the next version:**

- Add **multi-language support** (e.g., French, Spanish)
- Improve **sentiment analysis** with NLP models
- Enhance **UI with a chatbot feature**

---

## **Contributors**

👨‍💻 **N Anand Raj** - Developer
