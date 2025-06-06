from flask import Flask, redirect
import json
import os

app = Flask(__name__)
URL_FILE = "redirect_url.json"

# Initialize the redirect URL if the file doesn't exist
if not os.path.exists(URL_FILE):
    with open(URL_FILE, "w") as f:
        json.dump({"url": "https://scroll-spark-design-site.lovable.app/"}, f)

def get_current_url():
    with open(URL_FILE, "r") as f:
        return json.load(f)["url"]

def set_new_url(new_url):
    with open(URL_FILE, "w") as f:
        json.dump({"url": new_url}, f)

@app.route("/")
def home():
    return redirect(get_current_url(), code=302)

@app.route("/update/<path:new_url>")
def update_url(new_url):
    new_url = f"https://{new_url}"
    set_new_url(new_url)
    return f"Redirect updated to {new_url}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)
