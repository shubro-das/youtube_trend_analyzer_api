from flask import Flask, jsonify
from flask_cors import CORS
from database.db_config import connect_db

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Route to fetch trending videos
@app.route('/api/trending_videos', methods=['GET'])
def get_trending_videos():
    conn = connect_db()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM trending_videos ORDER BY views DESC LIMIT 20;")
    videos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(videos)

# Run the Flask app
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=9990)
