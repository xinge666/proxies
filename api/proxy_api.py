from flask import Flask, jsonify
from core.db import RedisClient

app = Flask(__name__)
redis_client = RedisClient()

@app.route('/get')
def get_proxy():
    proxy = redis_client.get_random_good_proxy()
    if proxy:
        return jsonify({'proxy': proxy})
    return jsonify({'msg': 'no proxy available'}), 404

@app.route('/count')
def get_counts():
    return jsonify({
        'all': len(redis_client.get_all_proxies()),
        'good': len(redis_client.get_good_proxies()),
        'bad': len(redis_client.get_bad_proxies())
    })

def run_api():
    app.run(host='0.0.0.0', port=5000) 