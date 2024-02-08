from flask import Flask

app=Flask(__name__)


@app.route('/')
def hello_pybo():
    app.logger.debug(f"__name__:{__name__}")
    return "<p>Hello, world!</p>"

