# Sentiment Analysis Tool

## Overview
The Sentiment Analysis Tool is a web-based application that analyzes the sentiment of text data (e.g., tweets, reviews). It provides sentiment trends (positive, negative, neutral) through visualizations and allows users to export the results as a CSV file.

## Features
- Fetch data via APIs (e.g., Twitter API).
- Analyze sentiment using Natural Language Processing (NLP) models.
- Visualize sentiment trends with dynamic charts.
- Export analyzed data to CSV.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (integrated via Flask templates)
- **NLP**: NLTK (VADER Sentiment Analysis)
- **Data Fetching**: Tweepy (Twitter API)
- **Visualization**: Matplotlib, Seaborn
- **Data Export**: Pandas

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/stephenombuya/Sentiment-Analysis-Tool
   cd sentiment-analysis-tool
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Twitter API Keys**
   - Create a Twitter Developer account at [Twitter Developer Platform](https://developer.twitter.com/).
   - Generate API keys and access tokens.
   - Add your keys to the `services/twitter_fetcher.py` file:
     ```python
     API_KEY = "your_api_key"
     API_SECRET = "your_api_secret"
     ACCESS_TOKEN = "your_access_token"
     ACCESS_SECRET = "your_access_secret"
     ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000/`.

## Project Structure
```
.
├── app.py                     # Main application file
├── templates/                 # HTML templates
│   └── index.html
├── static/                    # Static files (CSS, JS, images)
├── services/                  # Modularized services
│   ├── twitter_fetcher.py     # Fetch tweets via Twitter API
│   ├── sentiment_analyzer.py  # Perform sentiment analysis
│   ├── visualization.py       # Generate sentiment visualizations
│   └── csv_exporter.py        # Export data to CSV
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Usage
1. Open the application in a web browser.
2. Enter a keyword and specify the number of tweets to analyze.
3. View sentiment distribution as a bar chart.
4. Download the analyzed data as a CSV file.

## Example
### Input:
- **Keyword**: `climate change`
- **Count**: `100`

### Output:
- **Visualization**: A bar chart showing the number of positive, negative, and neutral tweets.
- **CSV File**: Contains tweets and their corresponding sentiment scores.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature name'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License
This project is licensed under the  GNU GENERAL PUBLIC LICENSE. See the `LICENSE` file for details.

## Acknowledgments
- [NLTK](https://www.nltk.org/) for sentiment analysis.
- [Tweepy](https://www.tweepy.org/) for Twitter API integration.
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for visualizations.
