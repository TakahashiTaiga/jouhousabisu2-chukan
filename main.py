from controller import controller

"""
    このファイルを実行するとプログラムが実行される.

    ターミナルで同じディレクトリに入った後に、

    python main.py

    を入力、実行するとプログラムが実行される.
    
"""

if __name__ == '__main__':
    # コントローラーのインスタンス化、実行を繰り返す
    while True:
        controller = controller()
        controller.ask()
    