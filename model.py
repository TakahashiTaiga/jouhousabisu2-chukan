import re
import sqlite3

class model:
    """
        model class
        init()                  データベースの名前を登録
        findUser()              ユーザーが登録されているかの問い合わせ処理
        getPurchaseHistory()    ユーザーの購買履歴の一覧を取得する処理
        insertPurchaseHistory() ユーザーの購買履歴を登録する処理
        getItemPrice()          商品の価格を取得する処理
        executeQuery()          クエリを実行する際のユーティリティ関数

    """

    def __init__(self):
        # データベースの名前を入力
        self.db_name = 'purchase_manegiment.db'        

    def findUser(self, user):
        # クエリを入力、実行
        query = 'SELECT * FROM user WHERE user_name = "{}"'.format(user)
        result = self.executeQuery(query)

        # 結果の中のuser_nameがuserと同じならTrue、それ以外か例外ならFalseを返す
        try:
            if result[0][0] == user:
                return True
        except:
            return False
        else:
            return False

    def getPurchaseHistory(self, user):
        # クエリを入力、、実行
        query = 'SELECT item_name, num FROM purchase_history WHERE user_name = "{}"'.format(user)
        result = self.executeQuery(query)
        return result
    
    def insertPurchaseHistory(self, user, item, num):
        # クエリを入力、実行
        query = 'INSERT INTO purchase_history(user_name, item_name, num) VALUES("{0}", "{1}", "{2}")'.format(user, item, num)
        result = self.executeQuery(query)
    
    def getItemPrice(self, item_name):
        # クエリを入力、実行
        query = 'SELECT price FROM item WHERE item_name = "{}"'.format(item_name)
        result = self.executeQuery(query)

        # 結果を返す、例外の場合は何も返さない
        try:
            return result[0][0]
        except:
            return

    def executeQuery(self, query):
        # データベースに接続、カーソルの作成
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        
        # クエリの実行、結果の変換
        cur.execute(query)
        result = cur.fetchall()
        
        # データベースへのコミット
        conn.commit()

        # カーソル、クエリの順に閉じる
        cur.close()
        conn.close()
        
        return result
