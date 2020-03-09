from sqlalchemy import func
from models.description import Description
from models.title import Title
from db import DB

db_obj = DB() ### creating a object of DB function in db.py file
db_session = db_obj.get_db() ### getting a session of database

def news_sentiment_data(news_channel, news_title, polarity, keyword_count):
    title = db_session.query(func.max(Title.title_id)).filter(Title.news_channel == news_channel).first()

    if title[0] is None:
        title_id = 1
    
    else:
        title_id = title[0] + 1

    if news_channel.lower() == 'the hill':
        news_id = 1
    elif news_channel.lower() == 'the guardian':
        news_id = 2

    db_session.add_all([Title(title_id=title_id, title=news_title, news_id=news_id, news_channel=news_channel, sentiment_value= float(polarity))])

    for key, value in keyword_count.items():
        db_session.add_all([Description(title_id=title_id, news_id=news_id, keyword=key, keyword_count=value)])

    db_session.commit()
