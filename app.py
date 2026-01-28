import requests
import os
from flask import Flask, request, send_file


app = Flask(__name__)


@app.route("/<path:name>")
def route(name):
    try:
        if os.path.exists(f"cache/{name}"):
            return send_file(f"cache/{name}")
    except:
        pass

    response = requests.request(
        url="http://216.9.225.189:9999" + request.path,
        method=request.method,
        data=request.get_data(),
        headers=request.headers
    )
    if response.ok and os.path.splitext(name)[1]:
         dir = os.path.dirname(f"cache/{name}")
         os.makedirs(dir, exist_ok=True)
         with open(f"cache/{name}", "wb") as f:
             f.write(response.content)
    return response.content, response.status_code, {"Content-Type": response.headers.get("Content-Type")}


if __name__ == "__main__":
    app.run()
