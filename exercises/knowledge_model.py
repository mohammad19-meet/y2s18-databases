from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'knowledge'
	knowledge_id = Column(Integer, primary_key = True)
	name = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	def __repr__(self):
		return("Primary Key: {},\n"
				"Name: {},\n"
				"Article: {},\n"
				"Rating: {},\n"
				).format(
					self.knowledge_id, self.name, self.topic, self.rating
				)

x = Knowledge(knowledge_id = 1, name = "weather", topic = "rainbow", rating = 9)

#print(x)

"""if (x.rating < 7):
	print("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be
")
else: print(x)"""