from flask import Flask, render_template

app = Flask(__name__, template_folder='template') 

@app.route('/')
def task_page():
    dynamic_data = "This is dynamic data from the server!"
    return render_template('task.html', dynamic_data=dynamic_data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
