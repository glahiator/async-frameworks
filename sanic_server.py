from sanic import Sanic
from sanic.response import json, text

app = Sanic(name="my-test-app")


@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.route("/greeting")
async def test_path(request):
    return text("Hello, world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
