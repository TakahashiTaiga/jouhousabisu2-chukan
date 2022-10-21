from model import model
from view import view

class controller:
    """
        controller class
        init()  modelとviewクラスのインスタンス化
        ask()   ユーザーを識別する処理
        order() ユーザーのオーダーを聞く処理
        buy()   ユーザーのオーダーがbuyだった時の処理
        show()  ユーザーのオーダーがshowだった時の処理

    """


    def __init__(self):
        # viewとmodelのインスタンス化
        self.view = view()
        self.model = model()
    
    def ask(self):
        # 誰か尋ねる
        self.user = self.view.askWho()
        b = self.model.findUser(self.user)

        # 知らない人だったら終わる
        if b:
            self.order()
        else:
            print("I don't know.")
            print()
            return
    
    def order(self):
        # 購入か購入履歴の閲覧かを聞きそれぞれの処理に行く
        self.order = self.view.askOrder()
        if self.order == 'buy':
            self.buy()
        elif self.order == 'show':
            self.show()

    def buy(self):
        # 買うものを聞く
        self.item = self.view.askItem()
        # 買う個数を聞く
        self.num = self.view.askNum()
        
        # 買うものの価格を持ってくる
        self.price = self.model.getItemPrice(self.item)
        # 小計を出す
        self.subtotal = int(self.price) * int(self.num)

        # 購入履歴を登録する
        self.model.insertPurchaseHistory(self.user, self.item, self.num)

        # レシートを出力する
        self.view.receipt(self.user, self.item, self.num, self.subtotal)

    def show(self):
        # 購入履歴を持ってきて出力する
        purchase_history_list = self.model.getPurchaseHistory(self.user)
        self.view.showPurchaseHistory(purchase_history_list)

