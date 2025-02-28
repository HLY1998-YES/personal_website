from flask import render_template

def setup_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/machine-learning')
    def machine_learning():
        return render_template('machine_learning.html')

    @app.route('/deep-learning')
    def deep_learning():
        return render_template('deep_learning.html')

    @app.route('/nlp')
    def nlp():
        return render_template('nlp.html')

    @app.route('/python')
    def python():
        return render_template('python.html')

    @app.route('/cv')
    def cv():
        return render_template('cv.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/chatbot')
    def chatbot_project():
        return render_template('/chatbot.html')

    @app.route('/emergency')
    def emergency_project():
        return render_template('/healthcare.html')

    @app.route('/leetcode')
    def leetcode_project():
        return render_template('/leetcode.html')

    @app.route('/cv')
    def cv_page():
        return render_template('/cv.html')