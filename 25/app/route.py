from flask import request
from flask_expects_json import expects_json

from .Exceptions import *
from .db_requests import Drivers, Bases, Clients, Orders

driver_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "car": {"type": "string"}
    },
    "required": ["name", "car"]
}

client_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "is_vip": {"type": "boolean"}
    },
    "required": ["name", "is_vip"]
}

order_schema = {
    "type": "object",
    "properties": {
        "client_id": {"type": "integer"},
        "driver_id": {"type": "integer"},
        "date_created": {"type": "string", "format": "date-time"},
        "status": {"type": "string"},
        "address_from": {"type": "string"},
        "address_to": {"type": "string"},
    },
    "required": ["client_id", "driver_id", "date_created", "status", "address_from", "address_to"]
}


@app.route('/api/v1/drivers', methods=['GET'])
def select_driver():
    result = Bases().search_user('drivers', userid=request.args['driverId'])
    if not result:
        raise Exception_404('ERROR: Нет записи с такими параметрами')
    else:
        for row in result:
            response = make_response(
                jsonify({"id": row.id, "name": row.name, "car": row.car}), 200)
        return response


@app.route('/api/v1/drivers', methods=['POST'])
@expects_json(driver_schema)
def create_driver():
    new_driver = Drivers(name=request.json['name'],
                         car=request.json['car'])
    result = Bases().create_user(new_user=new_driver)
    for row in result:
        response = make_response(
            jsonify({"id": row.id, "name": row.name, "car": row.car}), 201)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/v1/drivers/', methods=['DELETE'])
@app.route('/api/v1/drivers/<int:driverid>', methods=['DELETE'])
def delete_driver(driverid=None):
    if not driverid:
        raise Exception_400
    deleted_driver = Drivers(id=driverid)
    Bases().delete_user(existed_user=deleted_driver)
    response = make_response(
        jsonify({"message": 'Удалено'}), 204)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/v1/clients', methods=['GET'])
def select_client():
    result = Bases().search_user('clients', userid=request.args['clientId'])
    if not result:
        raise Exception_404('ERROR: Нет записи с такими параметрами')
    else:
        for row in result:
            response = make_response(
                jsonify({"id": row.id, "name": row.name, "is_vip": row.is_vip}), 200)
    return response


@app.route('/api/v1/clients', methods=['POST'])
@expects_json(client_schema)
def create_client():
    new_client = Clients(name=request.json['name'],
                         is_vip=request.json['is_vip'])
    result = Bases().create_user(new_user=new_client)

    for row in result:
        response = make_response(
            jsonify({"id": row.id, "name": row.name, "is_vip": row.is_vip}), 201)

    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/v1/clients/', methods=['DELETE'])
@app.route('/api/v1/clients/<int:clientid>', methods=['DELETE'])
def delete_client(clientid=None):
    if not clientid:
        raise Exception_400
    deleted_client = Clients(id=clientid)
    Bases().delete_user(existed_user=deleted_client)
    response = make_response(jsonify({"result": 'Удалено'}), 204)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/v1/orders', methods=['GET'])
def select_order():
    result = Orders().search_order(request.args['orderId'])
    for row in result:
        response = make_response(
            jsonify({"client_id": row.client_id, "driver_id": row.driver_id,
                     "date_created": row.date_created, "status": row.status,
                     "address_from": row.address_from, "address_to": row.address_to}), 200)
    return response


@app.route('/api/v1/orders', methods=['POST'])
@expects_json(order_schema)
def create_order():
    result = Orders().create_order(client_id=request.json['client_id'],
                                   driver_id=request.json['driver_id'],
                                   address_from=request.json['address_from'],
                                   address_to=request.json['address_to'])
    for row in result:
        response = make_response(
            jsonify({"id": row.id, "client_id": row.client_id, "driver_id": row.driver_id,
                     "address_from": row.address_from, "address_to": row.address_to,
                     "status": row.status, "date_created": row.date_created, }), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/v1/orders/', methods=['PUT'])
@app.route('/api/v1/orders/<int:orderId>', methods=['PUT'])
@expects_json(order_schema)
def update_order(orderid=None):
    if not orderid:
        raise Exception_400
    result = Orders().update_order(id_order=request.args['orderid'],
                                   new_client_id=request.json['client_id'],
                                   new_driver_id=request.json['driver_id'],
                                   new_address_from=request.json['address_from'],
                                   new_address_to=request.json['address_to'],
                                   new_status=request.json['status'],
                                   new_date_created=request.json['date_created'],
                                   )

    for row in result:
        response = make_response(
            jsonify({"id": row.id, "client_id": row.client_id, "driver_id": row.driver_id,
                     "address_from": row.address_from, "address_to": row.address_to,
                     "status": row.status, "date_created": row.date_created, }), 200)
    response.headers["Content-Type"] = "application/json"
    return response
