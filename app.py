from flask import Flask
#12213
app = Flask(__name__)

def my_function(x, y):
    return x * y   # замените на любую простую операцию: x - y, x * y, x / y

@app.route('/')
def home():
    result = my_function(1200, 5)
    return f"<h1>Результат: {result}</h1>"

if __name__ == '__main__':
    app.run()
