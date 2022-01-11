FROM python:3.7-alpine

COPY twitter_bot/oauth_handler.py /twitter_bot/
COPY twitter_bot/retweet_topics.py /twitter_bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /twitter_bot
CMD ["python3", "retweet_topics.py"]