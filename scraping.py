#importing libraries
import os
import googleapiclient.discovery
import googleapiclient.errors
import credentials #credentials.py
import pandas as pd

API_KEY=credentials.api_key

#variables
chartInput='mostPopular'
regionCodeInput = 'US'
videoCategoryIdInput = '10'
maxResultsInput = 50
metadataObject = ['id','title', 'description', 'channelTitle', 'tags', 'categoryId', 'defaultLanguage', 'publishedAt', 'viewCount', 'likeCount', 'favoriteCount', 'commentCount','duration', 'regionCode']

#get metadata from Youtube API
# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = API_KEY

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.videos().list(
        part="snippet, contentDetails, statistics, id",
        chart = chartInput,
        regionCode = regionCodeInput,
        videoCategoryId = videoCategoryIdInput,
        maxResults = maxResultsInput
    )
    response = request.execute()

    return response

if __name__ == "__main__":
    main()

videosList = main()

#function to resolve tags in just meaninfull words
#stringWords = array with strings to resolve
def tagsResolver(stringWords):
    resolvedArray = []
#stopWords from https://medium.com/@yashj302/stopwords-nlp-python-4aa57dc492af
    stopWords = ['call', 'upon', 'still', 'nevertheless', 'down', 'every', 'forty', '‘re', 'always', 'whole', 'side', "n't", 'now', 'however', 'an', 'show', 'least', 'give', 'below', 'did', 'sometimes', 'which', "'s", 'nowhere', 'per', 'hereupon', 'yours', 'she', 'moreover', 'eight', 'somewhere', 'within', 'whereby', 'few', 'has', 'so', 'have', 'for', 'noone', 'top', 'were', 'those', 'thence', 'eleven', 'after', 'no', '’ll', 'others', 'ourselves', 'themselves', 'though', 'that', 'nor', 'just', '’s', 'before', 'had', 'toward', 'another', 'should', 'herself', 'and', 'these', 'such', 'elsewhere', 'further', 'next', 'indeed', 'bottom', 'anyone', 'his', 'each', 'then', 'both', 'became', 'third', 'whom', '‘ve', 'mine', 'take', 'many', 'anywhere', 'to', 'well', 'thereafter', 'besides', 'almost', 'front', 'fifteen', 'towards', 'none', 'be', 'herein', 'two', 'using', 'whatever', 'please', 'perhaps', 'full', 'ca', 'we', 'latterly', 'here', 'therefore', 'us', 'how', 'was', 'made', 'the', 'or', 'may', '’re', 'namely', "'ve", 'anyway', 'amongst', 'used', 'ever', 'of', 'there', 'than', 'why', 'really', 'whither', 'in', 'only', 'wherein', 'last', 'under', 'own', 'therein', 'go', 'seems', '‘m', 'wherever', 'either', 'someone', 'up', 'doing', 'on', 'rather', 'ours', 'again', 'same', 'over', '‘s', 'latter', 'during', 'done', "'re", 'put', "'m", 'much', 'neither', 'among', 'seemed', 'into', 'once', 'my', 'otherwise', 'part', 'everywhere', 'never', 'myself', 'must', 'will', 'am', 'can', 'else', 'although', 'as', 'beyond', 'are', 'too', 'becomes', 'does', 'a', 'everyone', 'but', 'some', 'regarding', '‘ll', 'against', 'throughout', 'yourselves', 'him', "'d", 'it', 'himself', 'whether', 'move', '’m', 'hereafter', 're', 'while', 'whoever', 'your', 'first', 'amount', 'twelve', 'serious', 'other', 'any', 'off', 'seeming', 'four', 'itself', 'nothing', 'beforehand', 'make', 'out', 'very', 'already', 'various', 'until', 'hers', 'they', 'not', 'them', 'where', 'would', 'since', 'everything', 'at', 'together', 'yet', 'more', 'six', 'back', 'with', 'thereupon', 'becoming', 'around', 'due', 'keep', 'somehow', 'n‘t', 'across', 'all', 'when', 'i', 'empty', 'nine', 'five', 'get', 'see', 'been', 'name', 'between', 'hence', 'ten', 'several', 'from', 'whereupon', 'through', 'hereby', "'ll", 'alone', 'something', 'formerly', 'without', 'above', 'onto', 'except', 'enough', 'become', 'behind', '’d', 'its', 'most', 'n’t', 'might', 'whereas', 'anything', 'if', 'her', 'via', 'fifty', 'is', 'thereby', 'twenty', 'often', 'whereafter', 'their', 'also', 'anyhow', 'cannot', 'our', 'could', 'because', 'who', 'beside', 'by', 'whence', 'being', 'meanwhile', 'this', 'afterwards', 'whenever', 'mostly', 'what', 'one', 'nobody', 'seem', 'less', 'do', '‘d', 'say', 'thus', 'unless', 'along', 'yourself', 'former', 'thru', 'he', 'hundred', 'three', 'sixty', 'me', 'sometime', 'whose', 'you', 'quite', '’ve', 'about', 'even']
    for word in stringWords:
    #break strings in single words
        singleWordsArray = word.split(' ')
    #remove stopWords and repeated ones
        for word in singleWordsArray:
            resolvedWord = word.lower()
            if (resolvedWord not in stopWords) & (resolvedWord not in resolvedArray):
                resolvedArray.append(word)
    #return the single word
    return resolvedArray


#create a.csv file to store the data
#check if the data file exists and is not empty
filePath = 'scraping_data.csv'

if os.path.exists(filePath) and os.path.getsize(filePath) > 0:
    #Open scrapping dataset
    scrapingData = pd.read_csv(filePath)
    #Create columns in the dataset if they don't exist
    for key in metadataObject:
        if key not in scrapingData:
            scrapingData[key] = None
else:
    #Create an empty file with the columns
    scrapingData = pd.DataFrame(columns = metadataObject)



for i in range(0, len(videosList['items'])):
#video object from Youtube API (just the desired ones)
    videoMetadata = {
        #id
        'id': videosList['items'][i]['id'],
        #snippet
        'title': videosList['items'][i]['snippet'].get('title'),
        'description': videosList['items'][i]['snippet'].get('description'),
        'channelTitle': videosList['items'][i]['snippet'].get('channelTitle'),
        'tags': videosList['items'][i]['snippet'].get('tags'),
        'categoryId': videosList['items'][i]['snippet'].get('categoryId'),
        'defaultLanguage': videosList['items'][i]['snippet'].get('defaultLanguage'),
        'publishedAt': videosList['items'][i]['snippet'].get('publishedAt'),
        #statistics
        'viewCount':videosList['items'][i]['statistics'].get('viewCount'),
        'likeCount':videosList['items'][i]['statistics'].get('likeCount'),
        'favoriteCount':videosList['items'][i]['statistics'].get('favoriteCount'),
        'commentCount':videosList['items'][i]['statistics'].get('commentCount'),
        #contentDetails
        'duration': videosList['items'][i]['contentDetails'].get('duration'),
        #outsource
        'regionCode':regionCodeInput
    }

    #update videoMetadata.tags with the resolved words
    if videoMetadata['tags'] is not None:
        uniqueWordTags = tagsResolver(videoMetadata.get('tags'))
        videoMetadata.update({'tags':f'{uniqueWordTags}'})
    
    #Append the videoMetadata in the dataset if doesn't exist yet
    if videoMetadata.get('id') not in scrapingData['id'].values:
        scrapingData = pd.concat([scrapingData, pd.DataFrame([videoMetadata])], ignore_index=True);


print(scrapingData)

#Save/Override file in the path
scrapingData.to_csv(filePath, index=False)

