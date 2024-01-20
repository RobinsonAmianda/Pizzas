""" class Restaurant(db.Model):
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
create_app() """