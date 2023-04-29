from flask import Flask , make_response, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec
import psycopg2 

app = Flask(__name__)
spec = FlaskPydanticSpec()
spec.register(app)

conn = psycopg2.connect(database="ecommerce", 
                        user="postgres",
                        password="123456", 
                        host="localhost", port="5432")

@app.route('/listarSecao', methods=['GET'])
def GetSecao():
    cursor =  conn.cursor()
    cursor.execute('SELECT id, nome FROM SECAO Where ativa = true')
    secoes =  cursor.fetchall()
    
    cursor.close()
       
    secoesVO = list()
    for sc in secoes:
        secoesVO.append({
            'id':sc[0],
            'nome':sc[1]    
        })
        
    return make_response(
        jsonify(secoesVO))
    
@app.route('/cadastrarSecao', methods=['POST'])
def PostSecao():
    secao = request.json
    cursor =  conn.cursor()
    sql = f"INSERT INTO SECAO(NOME) VALUES('{secao['nome']}')"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify(secao))

@app.route('/editarSecao', methods=['PUT'])
def PutSecao():
    secao = request.json
    cursor =  conn.cursor()
    sql = f"UPDATE SECAO SET NOME = '{secao['nome']}' WHERE ID = {secao['id']}"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify(secao))    
    
@app.route('/excluirSecao', methods=['DELETE'])
def DeleteSecao():
    secao = request.json
    cursor =  conn.cursor()
    sql = f"DELETE FROM SECAO WHERE ID = {secao['id']}"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify('Excluído com sucesso.'))     
    

@app.route('/cadastrarProduto', methods=['POST'])
def PostProdutos():
    produto = request.json
    cursor =  conn.cursor()
    sql = f"INSERT INTO PRODUTOS(NOME,PRECO, IDSECAO) VALUES('{produto['nome']}', {produto['preco']}, {produto['idSecao']})"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify(produto))
    
@app.route('/listarProdutos', methods=['GET'])
def GetProdutos():
    cursor =  conn.cursor()
    cursor.execute('SELECT id, nome, preco, idSecao FROM PRODUTOS Where ativa = true')
    produtos =  cursor.fetchall()
    
    cursor.close()
       
    produtosVO = list()
    for pd in produtos:
        produtosVO.append({
            'id':pd[0],
            'nome':pd[1],
            'preco':pd[2],
            'Secao':pd[3]    
        })
        
    return make_response(
        jsonify(produtosVO))
    
@app.route('/editarProduto', methods=['PUT'])
def PutProduto():
    produto = request.json
    cursor =  conn.cursor()
    sql = f"UPDATE PRODUTOS SET NOME = '{produto['nome']}', PRECO = {produto['preco']} , IDSECAO = {produto['Secao']} WHERE ID = {produto['id']}"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify(produto)) 
    
@app.route('/excluirProduto', methods=['DELETE'])
def DeleteProduto():
    produto = request.json
    cursor =  conn.cursor()
    sql = f"DELETE FROM PRODUTOS WHERE ID = {produto['id']}"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    return make_response(
        jsonify('Excluído com sucesso.'))  
    
app.run()
conn.close()