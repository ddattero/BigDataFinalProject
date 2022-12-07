# Big Data Final Project
## Mental Health Discussion on Twitter

### Todo:

- Make graphs look nice
- filter out non MH related tweets (ie tropical depression)
- count pos and neg sentiment among cats
- GROUP RELATED TERMS


### Observations
- client.persist/compute vs df.persist
    - client seems faster
    - does it not use all cores when df. 
- Computing mean of pol and sub of categories
    - Without persist: 9 mins
    - With persist: < 1min
- Time to pre process dataset 6 workers
    - 22m 59.8s

### Future Improvements
- Translate tweets when they are pulled, or filter by language
    - Couldn't do it with Twitter access level


### Graph Ideas
- Polarity over time
- Subjectivity over time
- polarity vs subjectivity
- avg subjectivity and polarity for each key word

### Problems
- Tweets that contain keywords but are not about MH are included (ie tropical depression)
- Sentiment analysis is not very accurate
- Twitter Essential API does not include a language filter

### Questions
- How should I create the diagram?
- Is current code too simplistic?
- Is research presentation format ok, or should I change it to be more of a business presentation?