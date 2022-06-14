from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import survey
from flask import flash
# make class, class methods with SQL, and logic


#Create 
class Survey:
    db = 'dojo_survey_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_survey(cls, data):
        query = """
        INSERT INTO dojos(name, location, language, comment, created_at, updated_at)
        VALUES( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW())
        ;"""

        return (connectToMySQL(cls.db).query_db(query, data))

#Read 
    @classmethod
    def read_survey(cls):

        query = """
        SELECT * FROM dojos
        ORDER BY id DESC
        LIMIT 1
        ;"""

        result = connectToMySQL(cls.db).query_db(query)

        return result[0]

#Update 


#Delete 

#Validate 
    @staticmethod
    def validate_survey(survey):
        is_valid = True #always assume is true
        if len(survey['name']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        if  len(survey['location']) < 1:
            flash('Must select a Dojo Location.')
            is_valid = False
        if 'language' not in survey:
            flash('Must select a language.')
            is_valid = False
        return is_valid