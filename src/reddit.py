"""Module reddit. Initialize Reddit instance."""
import os
import praw
from src import configuration as c


USERNAME = c.config.get("RMVIT", "REDDIT_USERNAME", vars=os.environ)
MINIMUM_KARMA = c.config.get("RMVIT", "MINIMUM_KARMA", vars=os.environ)
DELETE_SAVED = c.config.get("RMVIT", "DELETE_SAVED", vars=os.environ)
NUMBER_OF_COMMENTS = c.config.get("RMVIT", "NUMBER_OF_COMMENTS", vars=os.environ)


reddit_instance = praw.Reddit(
    client_id=c.config.get("RMVIT", "REDDIT_CLIENT_ID", vars=os.environ),
    client_secret=c.config.get("RMVIT", "REDDIT_CLIENT_SECRET", vars=os.environ),
    username=USERNAME,
    password=c.config.get("RMVIT", "REDDIT_PASSWORD", vars=os.environ),
    user_agent=c.config.get("RMVIT", "REDDIT_USER_AGENT", vars=os.environ),
    rate_limit=300
    )


read_only_reddit_instance = praw.Reddit(
    client_id=c.config.get("RMVIT", "REDDIT_CLIENT_ID", vars=os.environ),
    client_secret=c.config.get("RMVIT", "REDDIT_CLIENT_SECRET", vars=os.environ),
    user_agent=c.config.get("RMVIT", "REDDIT_USER_AGENT", vars=os.environ),
    rate_limit=300
    )
