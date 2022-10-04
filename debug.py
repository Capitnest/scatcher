from news import news_articles
import datetime 
from datetime import timedelta

# x = datetime.datetime.now() - timedelta(days=1)
# y = x.isoformat()

# # news_articles("bitcoin")

# news_articles("bitcoin", "2022-10-02T23:13:57")

from news import news_articles

news_articles("bitcoin", 2)
