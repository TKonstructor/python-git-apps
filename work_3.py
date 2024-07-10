from cgitb import text
from os import replace, sep
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
    bool: 真偽値型 ex) True, False
    (new!) リスト: 複数のデータをまとめたもの ex) [1, 2, 3], ["Hello", "World"]    

Paiza 配列 -> https://paiza.jp/works/python3/primer/beginner-python4
Paiza ランダム選択 -> https://paiza.jp/works/python3/primer/beginner-python1/4005
"""

# 名簿リストの作成。ここに名前を追加していく
name_list = []


# TODO 5. ボタンを押すと名前を追加してラベルに表示する関数を作成
# Pythonで改行する文字は→”\n” (“エミリー\nマック\nジョン\n”)
def button1_action():
    name_list.append(entry1.get())
    added_name_list = "\n".join(name_list)
    label2.config(text=added_name_list.rstrip())


# TODO 1. ラベル: 名前を入力してください
label1 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# TODO 2. エントリー: 名前を入力するための入力フィールド
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# TODO 3. ボタン: ボタンを押すと配列に名前が追加される
button1 = tk.Button(
    window, text="追加", bg=fg_color, fg=bg_color, command=button1_action
)
button1.pack(pady=10)
# TODO 4. ラベル: 配列に追加された名前を表示する
label2 = tk.Label(window, bg=fg_color, fg=bg_color, anchor=tk.NW, justify="left")
label2.pack(pady=10)
label2.config(width=20, height=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
