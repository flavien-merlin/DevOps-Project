from flask import Flask, render_template
import os


def score_server():
    app = Flask(__name__)
    folder = os.path.dirname(__file__)
    app._static_folder = os.path.join(folder, os.path.dirname("static/main.css"))

    @app.route('/')
    def score():
        try:
            with open("Score.txt", "r") as file:
                user_score = file.read()
                print(user_score)
            return render_template('index.html', text=user_score)

        except FileNotFoundError:
            return render_template('Error.html')

    if __name__ == '__main__':
        app.run("0.0.0.0", debug=True)


score_server()
