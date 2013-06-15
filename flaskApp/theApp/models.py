from theApp import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	ip = db.Column(db.String(64), index = True, unique = True)
	name = db.Column(db.String(64))
	email = db.Column(db.String(120), index = True)
	zip = db.Column(db.String(8), index = True)
	state = db.Column(db.String(2))
	bill = db.relationship('Bill', backref = 'author', lazy = 'dynamic')
	num_in_house = db.Column(db.Integer)
	def __repr__(self):
		return '<User %r>' % (self.ip)    
        
class Bill(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	kwh = db.Column(db.Float)
	month = db.Column(db.Date)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Bill %r>' % (self.kwh)