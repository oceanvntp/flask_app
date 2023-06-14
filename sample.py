#必要なモジュール
from flask import Flask

# Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあったときの処理
@app.route('/')
def hello():
    return 'Hello World!'

# エントリーポイント
if __name__ == '__main__': #<- sample.pyが直接実行された場合
    app.run()
