@app.route('/username')
def home():
    return '<h1>Good morning %s</h1>' %username




if __name__ == '__main__':
    app.run()