'''
Author: allendred
Date: 2022-12-16 23:05:39
LastEditors: allendred
LastEditTime: 2022-12-17 00:55:45
FilePath: /workspace/ops/docker-compose/compose_test/src/app.py
Description: Follow your heart
'''
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello World! I have been seen {count} times.\n'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7700, debug=True)
