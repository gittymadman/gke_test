from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World App!'

@app.route('/new')
def new():
    return 'New World'
# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8080,host='0.0.0.0')
