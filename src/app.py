# MTVのView
# インポート
from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

# app にFlaskをインスタンス化
app = Flask(__name__)

# WTFormsを使い、index.html側で表示させるフォームを構築
class InputForm(Form):
    InputFormTest = StringField('文字を入力してください', [validators.InputRequired()])
    
    # HTMLで表示するsubmitボタンの定義
    submit = SubmitField('送信')
    
# URLにアクセスがあった場合の挙動の設定
@app.route('/', methods=['GET', 'POST'])
def input():
    # WTFormsで構築したフォームをインスタンス化
    form = InputForm(request.form)
    # POST methodの条件の定義
    if request.method == 'POST':
        # 条件に当てはまらない場合
        if form.validate() == False:
            return render_template('index.html', forms=form)
        # 条件に当てはまる場合
        else:
            outputname_ = request.form['InputFormTest']
            return render_template('result.html', outputname=outputname_)
    
    # GET methodの条件の定義
    elif request.method == 'GET':
        return render_template('index.html', forms=form)
    
    # アプリケーション実行の定義
    if __name__ == '__main__':
        app.run(debug=True)
        
#--------------------------------------------------------------
