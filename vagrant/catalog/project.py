from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)

# JSON Endpoints
@app.route('/catalog/JSON')
def catalogJSON():
    return "This is the API endpoint for the whole catalog"

@app.route('/catalog/<int:category_id>/JSON')
def itemsJSON(category_id):
    return "This is the API endpoint for all items under a category"

# Basic Routing
@app.route('/')
@app.route('/catalog')
def defCatalog():
    return "This is the main page for Chumley Warner"

@app.route('/catalog/<int:category_id>/items')
def showItems(category_id):
    return "This is the item list under a category"

@app.route('/catalog/<int:category_id>/<int:item_id>')
def showItem(category_id, item_id):
    return "This is the item page"

@app.route('/catalog/<int:category_id>/add')
def addItem(category_id):
    return "This is the add item page"

@app.route('/catalog/<int:category_id>/<int:item_id>/edit')
def editItem(category_id, item_id):
    return "This is the edit item page"

@app.route('/catalog/<int:category_id>/<int:item_id>/delete')
def deleteItem(category_id, item_id):
    return "This is the delete item page"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
