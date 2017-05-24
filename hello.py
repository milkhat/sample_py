from bottle import route, run, template
    //routing
    @route('/hello/<name>')
    
    
    def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)
    
    // start server
    run(host='localhost', port=8080)
