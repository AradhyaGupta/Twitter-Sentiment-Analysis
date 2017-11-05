#for twitter API
import tweepy
#for NLP
import textblob
#visualization
from pylab import *

#get data from twitter using the below API setup
customer_key = 'KIFEFfYGZvopbZtcR3PJrGTVq'
customer_secret = 'Dav48uFsZrylEk3l1LrzJXisxPl841RBc95vHVV1Oups8uDZYO'

access_token = '925084055607001090-RrhT207AbhhFgPl3EDKpSyrQp5oOLDk'
access_token_secret = '144f3SdY1NgQiYAJQJ2JdPaBvO56ApHTZvtZ1Da23UrFq'

auth = tweepy.OAuthHandler(customer_key, customer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

#user input key to search the data from twitter
search = input()
public_tweet = api.search(search)
polarityList = []
subjectivityList = []
for tweet in public_tweet:
	#print (tweet.text)
	analysis = textblob.TextBlob(tweet.text)
	#print (analysis.sentiment)
	polarityList.append(analysis.sentiment.polarity)
	subjectivityList.append(analysis.sentiment.subjectivity)
print (polarityList)
print (subjectivityList)
#to visualize the data using pie chart
countPositive = 0
countNegative = 0
countNeutral = 0
for i in polarityList:
	if i > 0:
		countPositive += 1
	elif i <0:
		countNegative += 1
	else:
		countNeutral += 1
label = ("Positive", "Negative","Neutral")
fracs = (countPositive, countNegative, countNeutral)
pie(fracs, labels = label, startangle = 90, shadow=True)
title('Twitter Sentiment Analysis', bbox={'facecolor':'0.8', 'pad':5})
show()