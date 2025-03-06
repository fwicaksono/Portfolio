from flask import Flask
import redis

app = Flask(__name__)

# Menghubungkan ke Redis
r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    # Menambahkan hitungan jumlah pengunjung
    visits = r.incr('counter')
    return f"Hello! You've visited this page {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
