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

file_name = 'mental_health_tweets.csv'

with open(file_name, 'a+') as filehandler:
    filehandler.write(f'tweet\ttime')


while True:
    try:
        with open(file_name, 'a+') as filehandler:
            mhsample = twclient.search_recent_tweets(query=query)
            time = datetime.datetime.now()
            for i in mhsample.data:
                i = i.text.replace('\n', ' ')
                filehandler.write(f'\n\"{i}\"\t{time}')
    except:
        print('error')
    sleep(60)

