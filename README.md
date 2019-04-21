# Sentiment-Analysis-of-Story-Headline
It performs sentiment analysis of story headline from http://www.cbc.ca/cmlink/rss-topstories according 2 txt files: positive-word and negative-word.

getStories.py performs the following:
1. Query the xml resource from the web-service endpoint
2. Extract the headline for each story
3. Print the headline to standard output

mapper.py performs the following:
1. Read standard input
2. Print each positive / negative term with count of the term

reducer.py performs the following:
1. Read standard input
2. Compute and output aggregate sentiment score across all terms

These python scripts could be used in Hadoop.
