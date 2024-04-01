from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Garden :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.image = data['image']
        self.location = data['location']
        self.size = data['size']
        self.created_at = data['updeated_at']