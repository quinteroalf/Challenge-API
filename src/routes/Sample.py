from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Sample import Sample
# Models
from models.SampleModel import SampleModel

main = Blueprint('Sample_blueprint', __name__)


@main.route('/')
def get_samples():
    try:
        samples = SampleModel.get_Samples()
        return jsonify(samples)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



@main.route('/<id>')
def get_movie(id):
    try:
        movie = SampleModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_sample():
    try:
       
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        company_name = request.json['company_name']
        address = request.json['address']
        city = request.json['city']
        state = request.json['state']
        zip = request.json['zip']
        phone1 = request.json['phone1']
        email = request.json['email']
        department = request.json['department']

        #id = uuid.uuid4()
        sample = Sample( first_name, last_name, company_name,address,city,state, zip, phone1, email, department)

        affected_rows = SampleModel.add_sample(sample)

        if affected_rows == 1:
            return jsonify({'Post': "Value added"})
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message_post': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_sample(id):
    try:
        first_name = id
        last_name = request.json['last_name']
        company_name = request.json['company_name']
        address = request.json['address']
        city = request.json['city']
        state = request.json['state']
        zip = request.json['zip']
        phone1 = request.json['phone1']
        email = request.json['email']
        department = request.json['department']
         
        sample = Sample( first_name, last_name, company_name,address,city,state, zip, phone1, email, department)

        affected_rows = SampleModel.update_sample(sample)

        if affected_rows == 1:
            return jsonify({'message PUT': "sample updated"})
        else:
            return jsonify({'message': "No sample updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Sample(id)

        affected_rows = SampleModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


