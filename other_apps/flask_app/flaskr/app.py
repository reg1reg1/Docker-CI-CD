import redis
from flask import g
from flask import Flask
app = Flask(__name__)

DB_HOST = 'redis-server'
DB_PORT = 6379
DB_NO = 0
def init_db():
    db = redis.StrictRedis(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NO)
    return db
 
 
@app.before_request
def before_request():
    g.db = init_db()



@app.route('/')
def hello_world():
    g.db.incrby('visit_count')
    visits = g.db.get('visit_count')
    str1="No of page visits are "+str(visits)
    return str1

if __name__ == '__main__':
    print("Flask is up and running")
    app.run(debug=True, host='0.0.0.0')
