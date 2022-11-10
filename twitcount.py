import tweepy

import config

import datetime

from time import sleep


twclient = tweepy.Client(
    #consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET
    bearer_token=config.BEARER
)

search_terms = [
    'mental health', 
    'depression',
    'depressed' 
    'anxiety',
    'anxious' 
    'ADHD', 
    'attention deficit'
    'OCD',
    'obsessive-compulsive disorder',
    'PTSD',
    'posttraumatic stress disorder',
    'trauma',
    'bipolar',
    'autism',
    'schizophrenia',
    'eating disorder',
    'anorexia',
    'bulimia',
    'psychosis',
    'psychologist',
    'psychotherapist',
    'psychiatrist',
    'psychotherapy',
    'depressant'
]

query = '('

for i in range(len(search_terms)):
    query = query + search_terms[i]
    if i < len(search_terms) - 1:
        query = query + ' OR '
    else:
        query = query + ')'

query = query + ' -is:retweet'

file_name = 'mental_health_tweet_count.csv'

with open(file_name, 'a+') as filehandler:
    filehandler.write(f'timestamp\tcount')


while True:
    today = datetime.date.today()
    today = datetime.datetime(year=today.year, month=today.month, day=today.day)
    yesterday = today - datetime.timedelta(1)
    with open(file_name, 'a+') as filehandler:
        counts = twclient.get_recent_tweets_count(query=query, end_time=today, start_time=yesterday, granularity='hour')
        for i in counts.data:
            start = i['start']
            count = i['tweet_count']
            filehandler.write(f'\n\"{start}\"\t{count}')
    sleep(86400)
