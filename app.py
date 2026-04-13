from flask import Flask

app = Flask(__name__)

def my_function(x, y):
    return x * y   # замените на любую простую операцию: x - y, x * y, x / y

@app.route('/')
def home():
    result = my_function(18, 5)
    return f"<h1>Результат: {result}</h1>"

if __name__ == '__main__':
    app.run()
