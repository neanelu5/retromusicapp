#!/usr/bin/env python3

from flask import Flask, redirect, request

def cod_htemeleu(melodii, smecherie=False):

    a=""
    for line in melodii:
        a+="<br>"*bool(a)+line #'<input type = "button" onclick="location.href=\'/\'" value = "sterge cacatul asta />'
        a+=(f'\t<button type="button" onclick="location.href=\'/linksecret/{melodii.index(line)}\'">sterge-o!</button> '*smecherie)
    cod_html=f"""
    <!DOCTYPE html>

    <html>
    <head>
        <meta charset="UTF-8">
        <title>Retro</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" /> 
    </head>
    <body>
        <form action = "#" method = "post">
            {'''<label for="fname">Zi o melodie:</label><br>
            <input type = "text" name = "nm" id="fname"/>
            <input type = "submit" value = "bag-o" /> '''if not smecherie else ""}
            <h4>Melodii in coada:</h4>
            {a}
            
        </form>   
    </body>
    </html>
    """

    return cod_html
lista_melodii=[]


app = Flask(__name__)
#session.permanent = True 
#app.permanent_session_lifetime = timedelta(days=5)


@app.route('/linksecret')
def smecherie():
    
    return cod_htemeleu(lista_melodii, smecherie=True)

@app.route('/linksecret/<nr>',)
def sterge(nr):
    
        lista_melodii.remove(lista_melodii[int(nr)])
        return redirect("/linksecret")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        song = request.form['nm']
        lista_melodii.append(song)
        return redirect("/")
    else:
        return cod_htemeleu(lista_melodii)





if __name__ == "__main__":
    app.run(host="0.0.0.0")