import dask.dataframe as dd
from dask.distributed import Client, TimeoutError, LocalCluster

from easynmt import EasyNMT


# df = dd.read_csv(urlpath='mental_health_tweets.csv', sep='\t')

model = EasyNMT('mbart50_m2en')
print(model.translate('ciao come stai', target_lang='en'))

# df['translated'] = df['tweet'].apply(lambda x: model.translate(x, target_lang='en'), meta=('translated', 'object'))

# print(df.head())