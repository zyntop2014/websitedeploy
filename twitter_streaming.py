# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch, RequestsHttpConnection



# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '838110956660080641-HTzfzOvyVLfMNiMwMaAkn9xMBtQUEVk'
ACCESS_SECRET = 'euVN5HZsIBJttx5JgrxbiBcVKdm4KqdC12FSmEX2GOKSt'
CONSUMER_KEY = 'KMUioXv68EVY2hi4wsjbQhJ7n'
CONSUMER_SECRET = 'euVksyfB0hmm0Xc92GPoq8bH8ZHhYD4SPhh0FpettqCSpGHefi'



oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)


#es = Elasticsearch(['https://search-twittermap-fxwenvc77wcna7ukzghc6lcudm.us-east-1.es.amazonaws.com:9200'])
#es = Elasticsearch(host='search-twittermap-fxwenvc77wcna7ukzghc6lcudm.us-east-1.es.amazonaws.com')

#host = 'search-twitter-idw3atyoomat2q2i5ao3t5nvge.us-east-1.es.amazonaws.com'
host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'
#awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print(es.info())



# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1
for tweet in iterator:
    
    
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #print json.dumps(tweet)  
   
    try:
        
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            #print tweet['id'] # This is the tweet's id
            #print tweet['created_at'] # when the tweet posted
            #print tweet['text'] # content of the tweet
                        
            #print tweet['user']['id'] # id of the user who posted the tweet
            #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
            #print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"
            tweets = api.search(q="place:%s" % place_id, count = 100)
   
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            #print hashtags

            
            es.index(index="tweet", doc_type="tweetmap", id= tweet['id'], body= tweet)
            tweet_count += 1

    except:
        continue

    

    # The command below will do pretty printing for JSON data, try it out
    #print json.dumps(tweet, indent=4)
    #es.index(index = 'twitter', doc_type = 'tweets', id = 'tweet_count' , body = tweet)
    
    if tweet_count > 1000:
       break 

