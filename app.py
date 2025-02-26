import importlib.metadata
from app import create_app

# 获取 Flask 版本（可选）
flask_version = importlib.metadata.version("flask")
print(f"Flask Version: {flask_version}")

# 创建 Flask 应用
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
