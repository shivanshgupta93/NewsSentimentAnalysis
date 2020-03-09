from sqlalchemy import Column, Integer, String, Date, Float
from models.base import Base
import datetime

#### Description class to create Description table
class Description(Base):
    __tablename__ = 'description'

    desc_id = Column(Integer, primary_key=True)
    title_id = Column(Integer)
    news_id = Column(Integer)
    keyword = Column(String)
    keyword_count = Column(Integer)
    insert_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Title (desc_id='%d', title_id='%d', news_id='%d', keyword='%s', keyword_count='%d', inserted_date='%s' )" % (self.desc_id, self.title_id, self.news_id, self.keyword, self.keyword_count, self.inserted_date)
