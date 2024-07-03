import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

"""

データ型
    変数は決まったデータ型を持つ
    int: 数値型 ex) 1, 2, 3
    str: 文字列型 ex) "Hello", "World", "0", "123", ""
    new(bool): 真偽値型 ex) True, False

条件分岐
    条件によって処理を変える
    if :
        条件が真のときの処理
    elif 条件: (省略可)
        条件が真のときの処理
    else: (省略可)
        それ以外のときの処理

比較演算
    ２つの値を比較して真理値を返す
    条件分岐と合わせて使う
    ( == != < > <= >= )

Paiza -> https://paiza.jp/works/python3/primer/beginner-python2

"""


# 和暦に変換する処理
def convert_to_wareki():  # 関数の定義 ※ボタンが押されたときの動き
    # TODO 和暦の各元号の開始年を調べる
    meiji = 1868  # 明治
    taisho = 1912  # 大正
    showa = 1926  # 昭和
    heisei = 1989  # 平成
    reiwa = 2019  # 令和

    seireki = int(entry1.get())  # TODO 入力値を取得

    # TODO　元号を判定する
    if seireki < taisho:
        gengo = "明治"
        wareki = seireki - meiji + 1
    elif seireki < showa:
        gengo = "大正"
        wareki = seireki - taisho + 1
    elif seireki < heisei:
        gengo = "昭和"
        wareki = seireki - showa + 1
    elif seireki < reiwa:
        gengo = "平成"
        wareki = seireki - heisei + 1
    else:
        gengo = "令和"
        wareki = seireki - reiwa + 1

    # TODO 1年の場合は元年にする
    if wareki == 1:
        wareki = "元"

    label2.config(text=f"西暦 {seireki}年 は {gengo} {wareki}年です。")  # 画面に出力


# TODO 1. ラベル: 西暦を入力してください。と出す
label1 = tk.Label(window, text="西暦を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# TODO 2. エントリー: 西暦を入力するフィールド。
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# TODO 3. ボタン: ボタンを押すとラベルに和暦に変換した結果を表示する。
button1 = tk.Button(window, text="Submit", command=convert_to_wareki)
button1.pack(pady=10)

# TODO 4. ラベル: 和暦に変換した結果を表示する。
label2 = tk.Label(window, text="ここに和暦が出てくる", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
