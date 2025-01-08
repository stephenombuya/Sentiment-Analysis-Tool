import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def create_visualization(sentiment_data):
    df = pd.DataFrame(sentiment_data)
    sentiment_counts = df['sentiment'].value_counts()

    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img
