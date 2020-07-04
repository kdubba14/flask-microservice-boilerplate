# src/models/MTGModel.py
from . import db
import datetime
import threading
import json
import os
import uuid
# from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class FakeModel(db.Model):
    """
    Fake Model
    """
    __tablename__ = "fake"

    fake_id = db.Column(db.String(128), primary_key=True)
    fake_name = db.Column(db.String(128))
    fake_number_array = db.Column(db.ARRAY(db.Integer))
    fake_boolean = db.Column(db.Boolean)
    fake_json = db.Column(db.JSON)
    fake_number = db.Column(db.Integer)
    fake_string_array = db.Column(db.ARRAY(db.String(128)))              

    def __init__(self, data):
        self.fake_id = data.get('fake_id')
        self.fake_name = data.get('fake_name')
        self.fake_number_array = data.get('fake_number_array')
        self.fake_boolean = data.get('fake_boolean')
        self.fake_json = data.get('fake_json')
        self.fake_number = data.get('fake_number')
        self.fake_string_array = data.get('fake_string_array') 

        # For when creating fields/documents
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def serialize(self):
        # Converting sqlalchemy model to json via marshmallow (imported above)
        fake_schema = FakeSchema()
        dumped_value = fake_schema.dump(self)

        # ================================================================================================
        # ============= The line below indicates that you may need to edit some fields ===================
        # ================================================================================================
        # dumped_value['illustration_id'] = ''.join(dumped_value['illustration_id'])

        return dumped_value

    def save(self):
        db.session.add(self)
        db.session.commit()

    # This is a cleaner way of pulling in the data (better than create function below)
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def create(self, data):
        total_fake = []
        for fake_info in data:
            new_fake = FakeModel({
                'fake_id': str(uuid.uuid4()),
                'fake_name': fake_info.get('fake_name'),
                'fake_number_array': fake_info.get('fake_number_array'),
                'fake_boolean': fake_info.get('fake_boolean'),
                'fake_json': fake_info.get('fake_json'),
                'fake_number': fake_info.get('fake_number'),
                'fake_string_array': fake_info.get('fake_string_array') 
            })
            total_fake.append(new_fake)

        try:
            db.session.add_all(total_fake)
        except:
            print('========AN ERROR OCCURRED======')
            os._exit(1)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_fakes(all_args):
        # =====================================================================
        # ================= IN CASE OF A LIMIT USE: ===========================
        # =====================================================================
        # all_fakes = [z.serialize() for z in FakeModel.query.limit(50).all()]

        all_fakes = [z.serialize() for z in FakeModel.query.all()]
        return all_fakes

    @staticmethod
    def get_one_fake(id):
        return FakeModel.query.get(id)

    def __repr__(self):
        # This is what to show if you printed a FakeModel
        return '{0}'.format(self.fake_name)

    # Making FakeModel iterable
    def __iter__(self):
        return vars(self)

class FakeSchema(SQLAlchemyAutoSchema):
    """
    Fake Schema
    """
    class Meta:
        model = FakeModel
        include_relationships = True
        load_instance = True
