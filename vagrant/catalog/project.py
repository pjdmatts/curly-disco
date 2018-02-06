from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Category, Item
from database_setup import Base, Category, Item, User


app = Flask(__name__)

# Connect to Database and create database session
# engine = create_engine('sqlite:///restaurantmenu.db')
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON Endpoints
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])

@app.route('/catalog/<int:category_id>/items/JSON')
def categoryItemsJSON(category_id):
    category= session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    return jsonify(category=category.serialize, items=[i.serialize for i in items])

# Basic Routing
@app.route('/')
@app.route('/catalog')
def showCatalog():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template("publichome.html", categories=categories)

@app.route('/catalog/<int:category_id>/items')
def showItems(category_id):
    selected_category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template("publiccategory.html", items=items,
                            selected_category=selected_category, categories=categories)

@app.route('/catalog/<int:category_id>/<int:item_id>')
def showItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template("publicitem.html", category=category, item=item)

#CRUDler
@app.route('/catalog/add', methods=['GET', 'POST'])
def addItem():
    categories = session.query(Category).order_by(asc(Category.name))
    if request.method == 'POST':
        category_id = request.form['category_id']
        category = session.query(Category).filter_by(id=category_id).one()
        newItem = Item(name=request.form['name'], description=request.form['description'],
        category_id = category_id, user_id=category.user_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('add.html', categories=categories)

@app.route('/catalog/<int:category_id>/add', methods=['GET', 'POST'])
def addCategoryItem(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'],
                        category_id=category_id, user_id=category.user_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('additem.html', category=category)

@app.route('/catalog/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    editedItem = session.query(Item).filter_by(id=item_id).one()
    categories = session.query(Category).filter(Category.id!=category_id).order_by(asc(Category.name))
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['category_id']:
            category_id = request.form['category_id']
            editedItem.category_id = category_id
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showItem', category_id=category_id, item_id=item_id))
    else:
        return render_template('edit.html', category=category, item=editedItem, categories=categories)

@app.route('/catalog/<int:category_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('delete.html', item=itemToDelete, category=category)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
