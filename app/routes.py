from flask import render_template
from flask import request, jsonify

# from app.chatbot import load_models, generate_response


def setup_routes(app):
    # load_models()  # 加载模型
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

    @app.route("/projects/ring-web-extractor")
    def ring_web_extractor():
        return render_template("projects/ring-web-extractor.html")

    @app.route("/projects/automatic_testing")
    def automatic_testing():
        return render_template("projects/automatic_testing.html")

    @app.route("/projects/social_science_platform")
    def social_science_platform():
        return render_template("projects/social_science_platform.html")

    @app.route("/projects/data_collection")
    def data_collection_projects():
        return render_template("projects/data_collection.html")

    @app.route("/projects/skill")
    def skill():
        return render_template("projects/skill.html")

    @app.route("/chat", methods=["POST"])
    def chat():
        pass
        # try:
        #     data = request.get_json()
        #     user_input = data.get("message", "").strip()
        #     model_key = data.get("model", "flan")
        #
        #     if not user_input:
        #         return jsonify({"response": "⚠️ 请输入一条消息"}), 400
        #
        #     response = generate_response(model_key, user_input)
        #     if not response.strip():
        #         response = "🤖 抱歉，我暂时无法回答这个问题。"
        #     return jsonify({"response": response})
        #
        # except Exception as e:
        #     return jsonify({"response": f"⚠️ 服务器出错：{str(e)}"}), 500






