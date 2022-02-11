import requests
from bs4 import BeautifulSoup
import praw

urls = ['https://www.reddit.com/t/coronavirus/']

def top_reddit_posts(num_articles = 8):
    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = [a['href'] for a in soup.findAll("a", {"class": "_3jOxDPIQ0KaOWpzvSQo-1s"}, href=True)]

    data = {}
    reddit = praw.Reddit(
        client_id = '5OrcWSR8nWx_MA',
        client_secret = 'WLGD1sRaP4A8QbLML7R85X7dgEyi2Q',
        user_agent =  'onemincovid'

    )

    for i in range(min(num_articles, len(rows))):
        values = {}
        post = reddit.submission(url=rows[i])
        values['inurl'] = rows[i]
        if len(post.title) > 120:
            values['title'] = post.title[:120] + '...'
        else:
            values['title'] = post.title
        values['upvote'] = round(post.score / 1000, 1) # in k
        values['upvote_ratio'] = round(post.upvote_ratio * 100, 0) # as percent
        values['exurl'] = post.url
        data[i] = values

    return data

def top_youtube_vids(num_articles):
    return