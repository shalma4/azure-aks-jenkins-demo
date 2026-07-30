from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Azure AKS + Jenkins CI/CD Project 🚀</h1><p>Successfully deployed to AKS!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)