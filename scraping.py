#importing module
from pytube import YouTube
import pandas as pd
import os

#video elements
videoPrefix = 'http://youtube.com/watch?v='
videoID = 'RDPGg0uRtP4&'
videoObject = YouTube(f'{videoPrefix}{videoID}')

#video object from pytube source
videoMetadata = {
    'id':videoID,
    'title': videoObject.title,
    'description': videoObject.description,
    'length': videoObject.length,
    'publish_date': videoObject.publish_date,
    'views':videoObject.views,
    'keywords': videoObject.keywords,
    'metadata': videoObject.metadata,
    'rating': videoObject.rating
}

#print object values
for key, value in videoMetadata.items():
    print(f'{key} : {value};')

#Check if the data file exists and is not empty
filePath = 'scraping_data.csv'

if os.path.exists(filePath) and os.path.getsize(filePath) > 0:
    #Open scrapping dataset
    scrapingData = pd.read_csv(filePath)
    #Create columns in the dataset if they don't exist
    for key in videoMetadata.keys():
        if key not in scrapingData:
            scrapingData[key] = None
else:
    #Create an empty file with the columns
    scrapingData = pd.DataFrame(columns = videoMetadata.keys())

#Append the videoMetadata in the dataset if doesn't exist yet
if videoMetadata.get('id') not in scrapingData['id'].values:
    scrapingData = scrapingData.append(videoMetadata, ignore_index=True);

print(scrapingData)

#Save/Override file in the path
scrapingData.to_csv(filePath, index=False)







