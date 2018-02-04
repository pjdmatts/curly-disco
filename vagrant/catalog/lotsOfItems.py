from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Items for Category1
category1 = Category(name = "")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name = "", description = "", category = category1)

session.add(item1)
session.commit()

#Items for Category2
category2 = Category(name = "")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name = "", description = "", category = category2)

session.add(item1)
session.commit()

#Items for Category3
category3 = Category(name = "")

session.add(category3)
session.commit()


item1 = Item(user_id=1, name = "", description = "", category = category3)

session.add(item1)
session.commit()

#Items for Category4
category4 = Category(name = "")

session.add(category4)
session.commit()


item1 = Item(user_id=1, name = "", description = "", category = category4)

session.add(item1)
session.commit()

#Items for Category5
category4 = Category(name = "")

session.add(category5)
session.commit()


item1 = Item(user_id=1, name = "", description = "", category = category5)

session.add(item1)
session.commit()


print "added items!"
