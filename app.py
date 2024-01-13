#UTILIZEI A FERRAMENTA POSTMAN , para rodar e fazer interação consulta e verificacao

#1 objetivo:criação da api que disponibiliza a consulta, criação, edição e exclusao de livros


from flask import Flask, jsonify, request

app = Flask(__name__)

#criação da lista de ivros 
livros =[
    {
        'id': 1,
        'titulo': 'Viagem ao centro da terra',
        'autor':' Junior Verne',
    },
    {
         'id': 3,
        'titulo': 'Harry Potter- Pedra Filosofal',
        'autor':'J.k Howling ',
    },
    {
         'id': 1,
        'titulo': 'James Clear',
        'autor':' Habitos Atômicos',
    },
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livro:
       if  livro.get('id') == id:
           return jsonify(livro)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)



