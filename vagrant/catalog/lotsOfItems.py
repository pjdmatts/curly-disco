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
User1 = User(name="Mr. Warner Himself", email="cwarner@example.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Items for Category1
category1 = Category(name = "Moustache Accessories")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name = "comb", description = "a tiny comb for your moustache", category = category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name = "scissors", description = "to keep the moustache neat and trim", category = category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name = "wax", description = "to shape the moustache", category = category1)

session.add(item3)
session.commit()

#Items for Category2
category2 = Category(name = "Walking Sticks")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name = "gandalf stick", description = "a large stick, possbily with magical properties", category = category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name = "yoda stick", description = "a small stick for bashing things with", category = category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name = "gentlemans spy can", description = "one of those cool canes with a sword hidden inside", category = category2)

session.add(item2)
session.commit()

#Items for Category3
category3 = Category(name = "Telephonice Devices")

session.add(category3)
session.commit()


item1 = Item(user_id=1, name = "The old standby", description = "a megaphone", category = category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name = "The Jefferson 1500", description = "A cool old phone", category = category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name = "The Schoenbach 12", description = "Another cool old phone", category = category3)

session.add(item3)
session.commit()

#Items for Category4
category4 = Category(name = "Things for Exploring")

session.add(category4)
session.commit()


item1 = Item(user_id=1, name = "Jumbo", description = "An Elephant", category = category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name = "Home away from home", description = "A tent", category = category4)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name = "Mr Smith", description = "A Butler", category = category4)

session.add(item3)
session.commit()

#Items for Category5
category5 = Category(name = "Hats")

session.add(category5)
session.commit()


item1 = Item(user_id=1, name = "The Great Detective", description = "A Dearstalker", category = category5)

session.add(item1)
session.commit()


print "added items!"
