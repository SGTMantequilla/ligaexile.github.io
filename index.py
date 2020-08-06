from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/brackets')
def brackets():
    return render_template('brackets.html')

@app.route('/fechas')
def fechas():
    return render_template('fechas.html')

if __name__ == '__main__':
    app.run(debug=True)
