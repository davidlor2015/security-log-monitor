from flask import Flask, jsonify
from parser import parse_auth_log

LOG_PATH = "data/auth.log"

def create_app():
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok"), 200
    
    @app.route("/stats", methods=["GET"])
    def stats():
        results = parse_auth_log(LOG_PATH)

        response = {
            "failed_logins": [
                {"user": user, "ip": ip, "count": count}
                for (user, ip), count in results["failed_logins"].most_common()
            ],
            "accepted_logins": [
                {"user": user, "ip": ip, "count": count}
                for (user, ip), count in results["accepted_logins"].most_common()
            ],
            "sudo_usage": [
                {"user": user, "count":count}
                for user, count in results["sudo_usage"].most_common()
            ],
        }
        
        return jsonify(response), 200
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)