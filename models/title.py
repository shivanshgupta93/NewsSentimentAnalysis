from sqlalchemy import Column, Integer, String, Date, Float
from models.base import Base
import datetime

#### Title class to create Title table
class Title(Base):
    __tablename__ = 'title'

    id = Column(Integer, primary_key=True)
    title_id = Column(Integer)
    title = Column(String)
    news_id = Column(Integer)
    news_channel = Column(String)
    sentiment_value = Column(Float)
    insert_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Title (title_id='%d', title='%s', news_id='%d', news_channel='%s', sentiment_value='%f', inserted_date='%s' )" % (self.title_id, self.title, self.news_id, self.news_channel, self.sentiment_value, self.inserted_date)
