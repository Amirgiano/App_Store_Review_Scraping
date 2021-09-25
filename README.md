# App Store Web Scraping


This case study is composed by 2 parts: <br />


1. Scraping the data with Python 2. Analysing and Visualizing the data in R <br />
For analysis we have retrieved 360 sample observations as a sample data. we are interested in obtaining the general information of what the users think about the application.<br />
```
from app_store_scraper import AppStore
import numpy as np <br />

buddyfit = AppStore(country="it", app_name="buddyfit", app_id=1483572798)
buddyfit.review(how_many=1500)

df = pd.DataFrame(np.array(buddyfit.reviews),columns=['review'])

df2 = df.join(pd.DataFrame(df.pop('review').tolist()))

df2.head()

df2.to_csv('C:/Users/Dell/Desktop/BuddyFit/buddyfit_reviews.csv')


#PlayStore
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all

buddyfit_android = reviews_all(
    'it.tripix.buddyfit',
    sleep_milliseconds=0, # defaults to 0
    lang='it', # defaults to 'en'
    country='it', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

buddyfit_android

buddyfit_android_df = pd.DataFrame(np.array(buddyfit_android),columns=['review'])

buddyfit_android_df_2 = buddyfit_android_df.join(pd.DataFrame(buddyfit_android_df.pop('review').tolist()))

print(buddyfit_android_df_2)

buddyfit_android_df_2.to_csv('C:/Users/Dell/Desktop\BuddyFit/buddyfit_android_reviews.csv')
```

Although I have scarped two datasets my aim is to have a general idea about the application for now so I have randomly choosen one platform (IOS) to go forward with analysis and visualization of the reviews on R <br />
At first glance the application is doing well. As you see  there are much more 5star ratings. <br />

![image](https://user-images.githubusercontent.com/90762709/134775892-2e2fda82-4926-4a73-9f67-3de0ff785d14.png) <br />

I'm interested also in the lenght of the feedbacks that the customers leave. To do so I split my dataset into 2 groups with threshold of 4 stars and call them positive and negative observations <br />
![image](https://user-images.githubusercontent.com/90762709/134775932-8bb61716-9389-4e43-8e49-9167edaec368.png) <br />

I'm loading the next libraries for tokenization and cleaning the words <br />
```
library(tidytext)
library(tm)
tidy_text <- ios %>%
    unnest_tokens(word, text)
library(SnowballC)

tidy_stem <- tidy_text %>%
    mutate(word = wordStem(word))
```
Since I couldn't find Italian  stopwords online. I have created the stopwords on my own and got rid of them <br />
```
#Defining stopwords
stopwords_italian = c("sono","di","per","e", "a", "o","anche","la","il","lo","aver","stato","ho","avevo","del","dal","allora","da","e","chi","che","grazie","grazi","molto","meno","perche","fare","problemi","fantastici","ottimo","wow","super","ottimo","bellissimo")
#Saving the list
lapply(stopwords_italian, write, "stopwords_italian.txt", append=TRUE, ncolumns=1000)

#reading the list
stops = readLines("stopwords_italian.txt")

#Getting rid of the list
tidy_text$word =removeWords(tidy_text$word,stops)
tidy_text = tidy_text %>% 
                  subset(nchar(as.character(word)) > 3)
```
This is the visual distribution of tokens <br />
```
tidy_stem %>%
    count(word) %>%
    slice_max(n, n = 10) %>%
    mutate(word = reorder(word, n)) %>%
    ggplot(aes(word, n, fill = word)) + geom_bar(stat = "identity", 
    fill = "skyblue") + xlab(NULL) + labs(title = "Most common stems in titles", 
    y = "Stems count") + theme(legend.position = "none", plot.title = element_text(color = "steelblue", 
    size = 12, face = "bold")) + coord_flip() + theme_bw()
```
<br />
![image](https://user-images.githubusercontent.com/90762709/134776156-9d563bb1-1cd1-4c36-8aea-23f4857ff73b.png)<br />

Similarly I have also created a word cloud of frquency <br />
![image](https://user-images.githubusercontent.com/90762709/134776236-9ad42a03-d218-4d0a-bd64-8720de9e2cba.png)<br />
We have already splitted our rating variable into two categories.  negative ad positive here is the distribution of the words by categories <br />
![image](https://user-images.githubusercontent.com/90762709/134776272-d207e3a3-962c-4cca-b942-d148623b289e.png)

**We see now what are the most frequent difficulties and happiness that end users are experiencing so we can go further to investigate this topics... Finally there definetely are a lot of improvements could be be done on this project (for instance improving the stopwords)**





