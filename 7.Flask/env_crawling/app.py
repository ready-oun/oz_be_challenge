from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect (
	host = '127.0.0.1',
    user = 'root',
    password = 'robin_robin',
    db='KREAM',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cur = db.cursor()

@app.route('/', methods=('GET',))
def index():    
    category = request.args.get('category_name')
    if category:
        sql = f"SELECT * FROM product WHERE category_name = '{category}'"
    else:
        sql= f"SELECT * FROM product"
    cur.execute(sql)

    kream_data = cur.fetchall()
    # print(kream_data[0])
    kream_data_len = len(kream_data)
    
    return render_template('index.html', kream_data = kream_data, kream_data_len=kream_data_len)
# (1) 검색어, (2) 페이지네이션 !!!! 
if __name__ == '__main__':
	app.debug = True
	app.run()