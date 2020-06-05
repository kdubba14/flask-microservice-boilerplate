#/src/controllers/TodoController.py
from flask import request, g, Blueprint, json, Response
from ..models.FakeModel import FakeModel, FakeSchema
import requests
import threading

fake_api = Blueprint('fake_api', __name__)
fake_schema = FakeSchema()


@fake_api.route('/', methods=['POST'])
def create():
  """
  Create a Fake
  """
  # Getting the request data and converting to the fake schema
  req_data = request.get_json()
  data, error = fake_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  # Taking fake schema and inserting data into model
  fake = FakeModel(data)
  fake.save()
  # Taking model and converting attributes to json
  data = fake_schema.dump(fake).data
  return custom_response(data, 201)

@fake_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Fakes
  """
  all_args = request.args
  # Static method in Fake model
  fakes = FakeModel.get_all_fakes(all_args)
  return custom_response(fakes, 200)

# <{data type}:{variable name}>
@fake_api.route('/<int:fake_id>', methods=['GET'])
def get_one(fake_id):
  """
  Get A Fake
  """
  fake = FakeModel.get_one_fake(fake_id)
  if not fake:
    return custom_response({'error': 'post not found'}, 404)
  # Turning Fake model into json
  data = fake_schema.dump(fake).data
  return custom_response(data, 200)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
