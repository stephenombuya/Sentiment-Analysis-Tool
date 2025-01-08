import pandas as pd

def export_to_csv(sentiment_data):
    df = pd.DataFrame(sentiment_data)
    csv_file = "sentiment_data.csv"
    df.to_csv(csv_file, index=False)
    return csv_file
