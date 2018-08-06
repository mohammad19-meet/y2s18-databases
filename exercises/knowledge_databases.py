from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	article_object = Knowledge(
		name = name,
		topic = topic,
		rating = rating)
	session.add(article_object)
	session.commit()
	

def query_all_articles():
	article = session.query(
		Knowledge).all()
	return article
	

def query_article_by_topic(topic):
	article = session.query(
		Knowledge).filter_by(
			topic = topic).first()
	return article
		
	

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic = topic).delete()
	session.commit()



def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()
	

def edit_article_rating():
	pass


#add_article('wonders',"space", 9)
#print(query_all_articles())