from bottle import route, run


@route("/hello")
def hello():
    return "Hello Bottle!"


run(host="192.168.2.150", port=1234, debug=True)
