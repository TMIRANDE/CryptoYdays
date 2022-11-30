import requests
from datetime import datetime
import pandas as pd

def main():
    r = requests.get("https://api.alternative.me/fng/?limit=0")
    df = pd.DataFrame.from_dict(r.json()['data'])
    df['date'] = df['timestamp'].apply(lambda x : datetime.fromtimestamp(int(x)))
    df.to_csv('fear_and_greed.csv')

if __name__ == '__main__':
    main()