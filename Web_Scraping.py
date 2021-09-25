#Appstore
from app_store_scraper import AppStore
import numpy as np

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



