# 第一个flask应用，解决了合并冲突
#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run('192.168.1.1',9000)
