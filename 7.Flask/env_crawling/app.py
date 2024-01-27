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
    search_q = request.args.get('q')
    if category:
        sql = f"SELECT * FROM product WHERE category_name = '{category}'"
        # AND product_name LIKE '%search_term%' LIMIT 20 OFFSET 0
    else:
        sql= f"SELECT * FROM product"
    cur.execute(sql)

    kream_data = cur.fetchall()
    # print(kream_data[0])
    kream_data_len = len(kream_data)
    
    return render_template('index.html', kream_data = kream_data, kream_data_len=kream_data_len)
# (1) 검색어, (2) 페이지네이션 !!!! 

# def search_result(search_words):

if __name__ == '__main__':
	app.debug = True
	app.run()