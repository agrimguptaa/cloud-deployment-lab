from flask import Flask
app = Flask(__name__)

APP_VERSION = "1.0.0"
STUDENT_NAME = "Agrim Gupta"

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Deployment Lab</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .card {{
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 8px 24px #0002;
                text-align: center;
                max-width: 440px;
                margin: 20px;
            }}
            h1 {{ color: #1769aa; }}
            .version {{
                display: inline-block;
                background: #e1f5e8;
                color: #176b39;
                padding: 8px 16px;
                border-radius: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Cloud Application!</h1>
            <p>Successfully deployed using Docker and AWS EC2.</p>
            <h2>Student: {STUDENT_NAME}</h2>
            <p class="version">Application Version: {APP_VERSION}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
