import os
from flask import Flask, jsonify, request
from .auth import is_authorized
from .ledger import post_entry

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/approvals/<approval_id>/post")
def post_approval(approval_id):
    user = request.headers.get("X-User", "anonymous")
    if not is_authorized(user, "post_approval"):
        return jsonify(error="forbidden"), 403
    entry = post_entry(approval_id, actor=user)
    return jsonify(entry), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
