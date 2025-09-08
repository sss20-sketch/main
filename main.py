import os
from flask import Flask, render_template_string

app = Flask(__name__)

username = "onworks60"
os_list = {
    "Ubuntu 16.04 Desktop": "ubuntu-16.04.6-desktop-i386",
    "Ubuntu 18.04 Desktop": "ubuntu-18.04.5-desktop-amd64",
    "Fedora Workstation": "fedora-workstation",
    "Kali Linux": "kali-linux-2021"
}

template = """
<!DOCTYPE html>
<html>
<head>
    <title>OnWorks OS Launcher</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0; }
        h1 { color: #333; }
        a { display: block; margin: 10px 0; padding: 10px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; width: 300px; }
        a:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Launch OS on OnWorks as {{ username }}</h1>
    {% for name, os_id in os_list.items() %}
        <a href="https://www.onworks.net/runos/create-os.html?os={{ os_id }}&home=init&username={{ username }}" target="_blank" rel="noopener noreferrer">
            {{ name }}
        </a>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, username=username, os_list=os_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
