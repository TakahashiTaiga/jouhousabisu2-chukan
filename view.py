class view:
    """
        view class
        askWho()                ユーザーを尋ねる処理
        askOrder()              オーダーを聞く処理
        askItem()               ユーザーが買う商品を聞く処理
        askNum()                ユーザーが買う個数を聞く処理
        receipt()               レシートを発行する処理
        showPurchaseHistory()   購入履歴を出力する処理
    """

    def askWho(self):
        print('Who are you?')
        self.user = input()
        print()
        return self.user

    def askOrder(self):
        print('Which is your order, "buy" or "show"?')
        self.order = input()
        print()
        return self.order
    
    def askItem(self):
        print('What item would you like?')
        print('ex. "pen"')
        self.item = input()
        print()
        return self.item

    def askNum(self):
        print('How many?')
        self.num = input()
        print()
        return self.num
    
    def receipt(self, user, item, num, subtotal):
        print('receipt {}'.format(user))
        print('     {0}     {1}'.format(item, num))
        print('subtotal {}'.format(subtotal))
        print('Bey.')
        print()

    def showPurchaseHistory(self, purchase_history_list):
        for p in purchase_history_list:
            print(p)
        print()