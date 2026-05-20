from models.games import Game, db


# CREATE
def create_game(data):
    titulo = data.get('titulo')
    genero = data.get('genero')
    desenvolvedor = data.get('desenvolvedor')
    plataforma = data.get('plataforma')

    if not all([titulo, genero, desenvolvedor, plataforma]):
        return {"error": "Todos os campos são obrigatórios."}, 400

    novo_game = Game(
        titulo=titulo,
        genero=genero,
        desenvolvedor=desenvolvedor,
        plataforma=plataforma
    )

    db.session.add(novo_game)
    db.session.commit()

    return novo_game.to_dict(), 201


# READ ALL
def get_all_games():
    games = Game.query.all()

    return [game.to_dict() for game in games], 200


# READ BY ID
def get_game_by_id(id):
    game = Game.query.get(id)

    if not game:
        return {"error": "Jogo não encontrado."}, 404

    return game.to_dict(), 200


# UPDATE
def update_game(id, data):
    game = Game.query.get(id)

    if not game:
        return {"error": "Jogo não encontrado."}, 404

    titulo = data.get('titulo')
    genero = data.get('genero')
    desenvolvedor = data.get('desenvolvedor')
    plataforma = data.get('plataforma')

    if not all([titulo, genero, desenvolvedor, plataforma]):
        return {"error": "Todos os campos são obrigatórios."}, 400

    game.titulo = titulo
    game.genero = genero
    game.desenvolvedor = desenvolvedor
    game.plataforma = plataforma

    db.session.commit()

    return game.to_dict(), 200


# DELETE
def delete_game(id):
    game = Game.query.get(id)

    if not game:
        return {"error": "Jogo não encontrado."}, 404

    db.session.delete(game)
    db.session.commit()

    return {"message": "Jogo deletado com sucesso."}, 200