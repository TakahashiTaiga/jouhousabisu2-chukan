import sqlite3

"""
    このプログラムはデータベースのテーブルを作成と初期値の入力をするプログラム.

    もしすでにデータベースがある場合は実行しない.
    または値の入力がしたい場合はcreate table文の実行部分をコメントアウトすると良い

    python_chukanを実行するにあたり、初めて実行する場合のみこのファイルを実行する.
    ターミナルで同じディレクトリに入った後、

    python create_tables.py

    を入力し実行する.

"""


# データベースへの接続とカーネルの作成
dbname = 'purchase_manegiment.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# create table文をそれぞれ実行
cur.execute('CREATE TABLE user(user_name STRING PRIMARY KEY)')

cur.execute('CREATE TABLE purchase_history(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name STRING, item_name STRING, num INTEGER)')

cur.execute('CREATE TABLE item(item_name STRING PRIMARY KEY, price INTEGER)')

# 一度コミット
conn.commit()

# ユーザーの初期値の入力
# ユーザーの初期値リスト
users = ['takahashi', 'okazaki', 'suguri']
# ユーザーを登録する
for u in users:
    cur.execute('INSERT INTO user(user_name) VALUES("{}")'.format(u))

# 商品の初期値を入力
# 商品の初期値リスト
items = [('pen', 100), ('eraeser', 150)]
# 商品を登録する
for i in items:
    cur.execute('INSERT INTO item(item_name, price) VALUES("{}", {})'.format(i[0], i[1]))

# コミットして閉じる
conn.commit()
cur.close()
conn.close()