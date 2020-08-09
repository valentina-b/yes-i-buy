import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wedding-registry'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# @app.route('/')
# def hello():
#     return 'Hello world'

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html',
                            page_title="Welcome to Book My Wedding Wish!")


# on the homepage, enter and submit a wishlist name/description through a form
@app.route('/create_wishlist_name', methods=['POST'])
def create_wishlist_name():
    wishlists = mongo.db.wishlists
    new_wishlist = wishlists.insert_one(request.form.to_dict())
    new_wishlist_id = new_wishlist.inserted_id
    return redirect(url_for('owner_view_dynamic', new_wishlist_id=new_wishlist_id))


# go to created wishlist owner page where owner can add presents
# display all the presents stored with the created wishlist id in the presents collection
@app.route('/<new_wishlist_id>/owner')
def owner_view_dynamic(new_wishlist_id):
    the_wishlist = mongo.db.wishlists.find_one({'_id': ObjectId(new_wishlist_id)})
    presents = mongo.db.present
    displayed_presents = presents.find({'wishlist_id': ObjectId(new_wishlist_id)})
    return render_template('owner_view.html', new_wishlist_id=new_wishlist_id,
                            the_wishlist=the_wishlist,
                            displayed_presents=displayed_presents)


# function that lets you add presents stored with the created wishlist id in the presents collection
# create a link back to the owner's wishlist
@app.route('/<new_wishlist_id>/present_added', methods=['POST'])
def add_new_present(new_wishlist_id):
    presents = mongo.db.present
    new_present = presents.insert_one(request.form.to_dict())
    new_present_id = new_present.inserted_id
    mongo.db.present.update({'_id': ObjectId(new_present_id)},
        {'$set':
            {
                'wishlist_id': ObjectId(new_wishlist_id)
            }
        })
    return render_template('present_added.html', new_wishlist_id=new_wishlist_id)


# delete a present from the present collection
@app.route('/<new_wishlist_id>/present_deleted/<present_id>')
def delete_present(new_wishlist_id, present_id):
    mongo.db.present.remove({'_id': ObjectId(present_id)})
    return render_template('present_deleted.html', new_wishlist_id=new_wishlist_id,
                            present_id=present_id)


# edit a present of a wishlist
@app.route('/<new_wishlist_id>/edit_present/<present_id>')
def edit_present(new_wishlist_id, present_id):
    the_present = mongo.db.present.find_one({"_id": ObjectId(present_id)})
    return render_template('present_editing.html', new_wishlist_id=new_wishlist_id,
                            present_id=present_id, present=the_present)


# update the present in the edit view
@app.route('/<new_wishlist_id>/update_present/<present_id>', methods=["POST"])
def update_present(new_wishlist_id, present_id):
    presents = mongo.db.present
    presents.update({"_id": ObjectId(present_id)},
        {'$set':
            {
                'present_description': request.form.get('present_description'),
                'present_header_image_URL': request.form.get('present_header_image_URL')
            }
        })
    return render_template('present_updated.html', new_wishlist_id=new_wishlist_id,
                            present_id=present_id)


# edit the wishlist
@app.route('/<new_wishlist_id>/owner/edit_wishlist')
def edit_wishlist(new_wishlist_id):
    the_wishlist =  mongo.db.wishlists.find_one({"_id": ObjectId(new_wishlist_id)})
    return render_template('wishlist_editing.html', new_wishlist_id=new_wishlist_id,
                            wishlist=the_wishlist)


# update the wishlist in the edit view
@app.route('/<new_wishlist_id>/owner/update_wishlist', methods=["POST"])
def update_wishlist(new_wishlist_id):
    wishlist = mongo.db.wishlists
    wishlist.update({"_id": ObjectId(new_wishlist_id)},
        {'$set':
            {
                'wishlist_name': request.form.get('wishlist_name'),
                'wishlist_description': request.form.get('wishlist_description'),
                'wishlist_header_image_URL': request.form.get('wishlist_header_image_URL')
            }
        })
    return render_template('wishlist_updated.html', new_wishlist_id=new_wishlist_id)


# delete the wishlist
@app.route('/<new_wishlist_id>/owner/wishlist_deleted')
def delete_wishlist(new_wishlist_id):
    mongo.db.wishlists.remove({'_id': ObjectId(new_wishlist_id)})
    mongo.db.present.remove({"wishlist_id": ObjectId(new_wishlist_id)})
    return render_template('wishlist_deleted.html', new_wishlist_id=new_wishlist_id)


# go to guest page where guests can book presents
# display all the presents stored with the created wishlist id in the presents collection
@app.route('/<new_wishlist_id>/guest')
def guest_view_dynamic(new_wishlist_id):
    the_wishlist = mongo.db.wishlists.find_one({'_id': ObjectId(new_wishlist_id)})
    presents = mongo.db.present
    displayed_presents = presents.find({'wishlist_id': ObjectId(new_wishlist_id)})
    return render_template('guest_view.html', new_wishlist_id=new_wishlist_id,
                            the_wishlist=the_wishlist,
                            displayed_presents=displayed_presents)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
