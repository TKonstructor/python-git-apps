from cgitb import text
from os import replace, sep
import random
import tkinter as tk

window = tk.Tk()
window.title("GUI App")
window.geometry("600x600")
color1 = "#333333"
color2 = "#FFFFFF"
color3 = "#000000"
window.configure(bg=color3)

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

name_list = []


def button1_action():
    name_list.append(entry1.get())
    added_name_list = "\n".join(name_list)
    label2.config(text=added_name_list.rstrip())


def button2_action():
    random_name = random.choice(name_list)
    label3.config(text=random_name)


label1 = tk.Label(window, text="名前を入力してください", bg=color1, fg=color2)
label1.pack(pady=10)

entry1 = tk.Entry(window, bg=color2, fg=color1)
entry1.pack(pady=10)

button1 = tk.Button(window, text="追加", bg=color2, fg=color1, command=button1_action)
button1.pack(pady=10)

label2 = tk.Label(window, bg=color1, fg=color2, anchor=tk.NW, justify="left")
label2.pack(pady=10)
label2.config(width=20, height=10)

button2 = tk.Button(
    window, text="ランダム選択", bg=color2, fg=color1, command=button2_action
)
button2.pack(pady=10)

label3 = tk.Label(window, bg=color1, fg=color2, anchor=tk.W)
label3.pack(pady=10)
label3.config(width=20, height=1)

window.mainloop()
