from flask import Blueprint, request, jsonify

from controllers.games_controller import (
    create_game,
    get_all_games,
    get_game_by_id,
    update_game,
    delete_game
)

game_bp = Blueprint('game_bp', __name__)


# CREATE
@game_bp.route('/games', methods=['POST'])
def create():
    data = request.get_json()

    response, status = create_game(data)

    return jsonify(response), status


# READ ALL
@game_bp.route('/games', methods=['GET'])
def get_all():
    response, status = get_all_games()

    return jsonify(response), status


# READ BY ID
@game_bp.route('/games/<int:id>', methods=['GET'])
def get_by_id(id):
    response, status = get_game_by_id(id)

    return jsonify(response), status


# UPDATE
@game_bp.route('/games/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()

    response, status = update_game(id, data)

    return jsonify(response), status


# DELETE
@game_bp.route('/games/<int:id>', methods=['DELETE'])
def remove(id):
    response, status = delete_game(id)

    return jsonify(response), status