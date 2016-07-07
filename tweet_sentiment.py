import sys
import pandas as pn
import json 
import codecs
#reload(sys)  
#sys.setdefaultencoding('utf8')
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readSent():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.    
#    print scores.items()
    return scores

def main():
#    sent_file = open(sys.argv[1])
#    tweet_file = open(sys.argv[2])
    tweetListDict = []    
    sentDict = readSent()
    tweetFile = codecs.open('three_minutes_tweets.json','r', encoding='utf-8')
    for ii,ln in enumerate(tweetFile):
#        print ii, ln
        pp = json.loads(ln)#.encode('utf-8'))
#        print type(pp)
#        print ii
        if pp.has_key('text'):            
            tweet = pp['text']
            print "Tweet: ", tweet
            sentimentValue = 0
            for sentKey,sentVal in sentDict.iteritems():
                try:                
                    if sentKey.upper() in tweet.upper():
                        tweet.upper().replace(sentKey.upper(),'')
                        sentimentValue += sentVal
                except:
                    pass
            print "Line and sentiment: ", ii, sentimentValue
            tweetListDict.append(pp)
#        if ii>2: return pp
    print len(tweetListDict)
    return tweetListDict
#    hw()
#    lines(sent_file)
#    lines(tweet_file)


if __name__ == '__main__':
    tweetListDict = main()
