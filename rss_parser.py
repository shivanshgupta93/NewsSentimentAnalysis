import feedparser as fp
from article_parser import hill_article, guardian_article
from consts import HILL_RSS_LINK, GUARDIAN_RSS_LINK, KEYWORD
from bs4 import BeautifulSoup

def hill_rss_parse():
    hill_rss = fp.parse(HILL_RSS_LINK)

    for i in range(0, len(hill_rss['entries'])):
        title = hill_rss['entries'][i]['title']

        if KEYWORD.lower() in title.lower():
            link = hill_rss['entries'][i]['link']
            publish_date = hill_rss['entries'][i]['published']
            author = hill_rss['entries'][i]['author']
            if author == '':
                author = 'N/A'
            description = hill_rss['entries'][i]['summary_detail']
            soup = BeautifulSoup(description['value'])

            hill_article(link, publish_date, author, soup.get_text())



def guardian_rss_parse():
    guardian_rss = fp.parse(GUARDIAN_RSS_LINK)

    for i in range(0, len(guardian_rss['entries'])):
        title = guardian_rss['entries'][i]['title']

        if KEYWORD.lower() in title.lower():
            link = guardian_rss['entries'][i]['link']
            publish_date = guardian_rss['entries'][i]['published']
            author = guardian_rss['entries'][i]['author']
            if author == '':
                author = 'N/A'
            description = guardian_rss['entries'][i]['summary_detail']
            soup = BeautifulSoup(description['value'])

            guardian_article(link, publish_date, author, soup.get_text())