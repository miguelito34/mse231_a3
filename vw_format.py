#########################################################################################################
## Author: Michael Spencer, Andrew (Foster) Docherty, Jorge Nam Song
## Project: MS&E 231 A3
## Script Purpose: Formats tweet data into a readable format for Vowpal Wabbit.
## Notes: Good features may include hour of day, minute of hour, number of capital letters...
#########################################################################################################

# Libraries
import sys
import nltk
from datetime import datetime as dt

# Parameters
INDEX_WHO = 0
INDEX_DATETIME = 1
INDEX_TWEET = 2


def get_label(tweeter):
    if (tweeter == "Trump"):
        return str("1 ")
    else: 
        return str("-1 ")


def get_datetime_features(dt_info):
    dt_object = dt.strptime(dt_info, "%Y-%m-%dT%H:%M:%SZ")
    return "|time hour:" + str(dt_object.hour) + " minute:" + str(dt_object.minute)


# NOTE: Still need to implment tweet length
def get_text_features(text_info):
    
    return ("|text num_caps:" + count_char_type(text_info, "caps") 
            + " num_ats:" + count_char_type(text_info, "ats") 
            + " num_hash:" + count_char_type(text_info, "hash")
            + " " + str("https:" in text_info)
            + " " + str("\"@" in text_info))


def count_char_type(text, char = "caps"):
    count = 0
    
    for letter in text:
        if (char == "caps" and letter.isupper()):
            count += 1
        elif (char == "hash" and letter == "#"):
            count += 1
        elif (char == "at" and letter == "@"):
            count += 1
    
    return str(count)


for line in sys.stdin:
    
    tweet_info = line.split("\t")
    
    if (tweet_info[INDEX_WHO] not in ["Trump", "Staff"]):
        continue
    
    label = get_label(tweet_info[INDEX_WHO])
    time_features = get_datetime_features(tweet_info[INDEX_DATETIME])
    text_features = get_text_features(tweet_info[INDEX_TWEET])
    
    # Print out formatted information, features are below
    
    # label 
    # |time hour:[hour] min_of_hour:[min_of_hour]
    # |text num_caps:[num_caps] num_ats:[num_ats] num_hash:[num_hash] link retweet text_length:[text_length]
    print(label, time_features, text_features)
    
    # use nltk line below if we want to parse out the tweet
    #nltk.tokenize.casual.casual_tokenize(tweet_info[2])