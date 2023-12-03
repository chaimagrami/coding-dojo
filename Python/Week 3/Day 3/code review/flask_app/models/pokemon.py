from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
class Pokemon :
    def __init__(self,data_dict) :
        self.id=data_dict['id']
        self.name=data_dict['name']
        self.type=data_dict['type']
        self.power=data_dict['power']
        self.hp=data_dict['hp']
        self.image=data_dict['image']
        self.user_id=data_dict['user_id']
        self.created_at=data_dict['created_at']
        self.updated_at=data_dict['updated_at']
    
    @classmethod
    def add (cls,data):
        query='''INSERT INTO pokemons (name,type,power,hp,image,user_id)
            VALUES (%(name)s,%(type)s,%(power)s,%(hp)s,%(image)s,%(user_id)s)'''
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_pokemon_by_user(cls,data):
        query='''
                SELECT * FROM pokemons join users on users.id = pokemons.user_id
                WHERE users.id=%(user_id)s;'''
        results=connectToMySQL(DATABASE).query_db(query,data)
        
        pokemons=[]
        for row in results :
            pokemons.append(cls(row))
        return pokemons
    
    @classmethod
    def get_by_id(cls,data):
        query ="""
        SELECT * FROM pokemons WHERE id = %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def edit(cls,data):
        query="""
        UPDATE pokemons SET name = %(name)s,type  = %(type)s,power  = %(power)s,hp  = %(hp)s,image = %(image)s
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query="DELETE from pokemons Where id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validate(data):
        is_valide = True
        if len(data['name'])< 2:
            flash("Name must be at least 3 ")
            is_valide = False
        if len(data['power'])< 1: 
            flash("You need power!")
            is_valide = False
        if len(data['hp'])< 1: 
            flash("HP too low!")
            is_valide = False
        return is_valide
    