from flask import Flask , render_template

app = Flask("meu app")
  
posts =[
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo post",
        "texto": "teste2"
    }
  ]  

@app.route('/')
def exibir_entradas():
    entradas = posts    #Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)
@app.route('/perfil')
def exibir_perfil():
    return render_template('exibir_perfil.html')