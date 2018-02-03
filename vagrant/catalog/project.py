from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)


# JSON Endpoints
@app.route('/catalog/JSON')
def catalogJSON():
    return "API-tastic"

@app.route('/catalog/<int:category_id>/JSON')
def itemsJSON(category_id):
    return "This is the API endpoint for all items under a category"


# Basic Routing
@app.route('/')
@app.route('/catalog')
def defCatalog():
    return render_template("publichome.html")

@app.route('/catalog/<int:category_id>/items')
def showItems(category_id):
    return render_template("publiccategory.html")

@app.route('/catalog/<int:category_id>/<int:item_id>')
def showItem(category_id, item_id):
    return render_template("publicitem.html")

@app.route('/catalog/add')
def addItem():
    return render_template("add.html")

@app.route('/catalog/<int:category_id>/add')
def addCategoryItem(category_id):
    return render_template("add.html")

@app.route('/catalog/<int:category_id>/<int:item_id>/edit')
def editItem(category_id, item_id):
    return render_template("edit.html")

@app.route('/catalog/<int:category_id>/<int:item_id>/delete')
def deleteItem(category_id, item_id):
    return render_template("delete.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
