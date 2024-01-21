from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///restaurant.db'
db = SQLAlchemy(app)
CORS(app)

class Restaurant(db.Model):
    __tablename__ = 'restaurants' 
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    pizzas = db.relationship('Pizza',secondary = 'restaurant_pizzas' ,back_populates = 'restaurants')

class Pizza(db.Model):
    __tablename__ = 'pizzas' 
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    restaurants = db.relationship('Restaurant',secondary = 'restaurant_pizzas' ,back_populates = 'pizzas')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id')) 
   
def create_app():
    with app.app_context():
        db.create_all()
create_app()

@app.route('/restaurants',methods = ['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_info = [{'name':restaurants.name,'address':restaurants.address}for restaurant in restaurants]
    return jsonify (restaurant_info) 

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_single_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        restaurant_half_info = {
            'name' : restaurant.name,
            'address' : restaurant.address,
            'pizzas':[]
        }
        for pizza in db.restaurant_pizzas:
            pizza_info = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            restaurant_full_info =restaurant_half_info ['pizzas'].append(pizza_info)
        return jsonify(restaurant_full_info)
    else:
        return jsonify({"error": "Restaurant not found"}),404

@app.route('/pizzas/<int:pizza_id>', methods=['GET'])
def get_single_pizza(pizza_id):
    pizzas = Pizza.query.get(pizza_id)
    if pizzas:
        pizza_making = {
            'name':pizzas.name,
            'ingredients':pizzas.ingredients
        }
        return jsonify(pizza_making)
    else:
        return jsonify({'error':'pizza not found'})

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_single_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({'Restaurant deleted successfully'})
    else:
        return jsonify({ "error": "Restaurant not found"})

@app.route('/pizzas',methods = ['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizzas_info = [{
        'name':pizzas.name,
        'ingredients':pizzas.ingredients
    }
    for pizza in pizzas]
    return jsonify (pizzas_info) 

@app.route('/restaurant_pizzas',methods = ['POST'])
def add_new_pizzas():
    data = request.json 
    price = data.get('price')
    if  not (1<=price<=30):
        return jsonify({'error':'price must be between 1 to 30'})
    new_restaurant_pizzas = RestaurantPizza(price=data['price'],pizza_id=data["pizza_id"],restaurant_id=data["restaurant_id"])
    if new_restaurant_pizzas :
        db.session.add(new_restaurant_pizzas)
        db.session.commit()
        return jsonify({"message":"new_restaurant_pizzas added"})
    else:
        return jsonify({"errors": ["validation errors"]}),400

@app.route('/restaurant_pizzas',methods = ['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    restaurant_pizzas_info = [
                                {
                               'price':restaurant_pizzas.price,
                               'pizza_id':restaurant_pizzas.pizza_id,
                               'restaurant_id':restaurant_pizzas.restaurant_id
                               }
                               for restaurant_pizzas in restaurant_pizzas]
    return jsonify (restaurant_pizzas_info)