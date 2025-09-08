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
    <title>OnWorks OS Embedded</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0; }
        h1 { color: #333; }
        .os-list { margin-bottom: 20px; }
        button {
            margin-right: 10px; margin-bottom: 10px;
            padding: 8px 16px;
            font-size: 14px;
            cursor: pointer;
            border: none;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
        iframe {
            width: 100%;
            height: 800px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <h1>Launch OS on OnWorks as {{ username }}</h1>

    <div class="os-list">
        {% for name, os_id in os_list.items() %}
            <button onclick="loadOS('{{ os_id }}')">{{ name }}</button>
        {% endfor %}
    </div>

    <iframe id="osframe" src="" allowfullscreen sandbox="allow-scripts allow-same-origin allow-forms allow-popups"></iframe>

    <script>
        function loadOS(os) {
            const iframe = document.getElementById('osframe');
            iframe.src = `https://www.onworks.net/runos/create-os.html?os=${os}&home=init&username={{ username }}`;
        }
        // Load the first OS by default on page load
        window.onload = () => {
            const firstOS = "{{ os_list.values()|list|first }}";
            loadOS(firstOS);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, username=username, os_list=os_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

