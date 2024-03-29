# モジュールのインストール
import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():

    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    #   **** ここを実装します（基礎課題） ****
    #     1. はてブのホットエントリーページのHTMLを取得する
    # サイトにアクセスし、htmlを受け取る
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode("utf-8")

    #  2. BeautifulSoupでHTMLを読み込む
    # BeautifulSoupがクラス、htmlが引数、html.parserが第二引数
    soup = BeautifulSoup(html, "html.parser")
    #  3. 記事一覧を取得する
    items = soup.select("item")
    shuffle(items)
    item = items[0]
    print(item)
    return json.dumps({
        "content" : item.find("title").string,
        # "link" : item.find("link").string
        "link": item.get('rdf:about')
    })

    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""
    """
      

       
       
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """

# @app.route("/api/xxxx")
# def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
