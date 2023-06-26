#coding: utf-8

from email import message
from flask import Flask, render_template

# appという名前でflaskをインスタンス化
app = Flask(__name__)

# ---View 側の設定---
#　ルートディレクトリにアクセスした場合の挙動
@app.route('/')
def index():
    # DBから以下の変数を読み込んできたと仮定
    title_ = 'ようこそ'
    message_ = 'MTV デザインパターンでwebアプリ作成'
    
    return render_template('index.html', title=title_, message=message_)

# エントリーポイント
if __name__ == '__main__':
    app.run()
    



