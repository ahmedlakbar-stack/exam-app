from flask import Flask, render_template, request
import platform
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    ip_addr = request.remote_addr
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os_info = platform.system()
    os_release = platform.release()

    return render_template(
        "index.html",
        ip=ip_addr,
        time=local_time,
        os=os_info,
        release=os_release
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
