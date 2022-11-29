# Big Data Final Project
## Mental Health Discussion on Twitter

### Todo:
- Sentiment analysis on tweet text
    - already preprocessed
- Make graphs look nice
- filter out non MH related tweets (ie tropical depression)
- GROUP RELATED TERMS


### Observations
- client.persist/compute vs df.persist
    - client seems faster
    - does it not use all cores when df. 
- Computing mean of pol and sub of categories
    - Without persist: 9 mins
    - With persist: < 1min

### Future Improvements
- Translate tweets when they are pulled, or filter by language
    - Couldn't do it with Twitter access level


### Graph Ideas
- Polarity over time
- Subjectivity over time
- polarity vs subjectivity
- avg subjectivity and polarity for each key word