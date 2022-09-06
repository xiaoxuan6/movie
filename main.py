import json
import os
import sys
import tkinter as tk
import webbrowser
from tkinter import ttk

import requests
import win32api
import win32con
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

root = tk.Tk()
root.geometry('400x300')
root.title('vip电影解析')
root.resizable(False, False)

tk.Label(root).grid(row=0, column=0)
tk.Label(root, text='请输入有效网址，否则解析失败').grid(row=1, column=1)
tk.Label(root, text='方法一、网址', width=20).grid(row=2, column=0)
input1 = tk.Entry(root, text='', width=30)
input1.grid(row=2, column=1)

tk.Label(root).grid(row=3, column=0)
tk.Label(root, text='方法二、剧名').grid(row=4, column=0)
input2 = tk.Entry(root, text='', width=30)
input2.grid(row=4, column=1)

tk.Label(root, text='选集').grid(row=5, column=0)
input3 = tk.Entry(root, text='', width=30)
input3.grid(row=5, column=1)

tk.Label(root).grid(row=6, column=0)
tk.Label(root, text='更多网站').grid(row=7, column=0)


def get_urls():
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        }
        url = os.environ.get('APP_URL')
        content = requests.get(url=url, headers=header).text
        items = json.loads(content.replace('var dh_data = ', ''))[6]['item']

        urls = []
        for item in items:
            urls.append(item['url'])

        return urls
    except Exception as e:
        print(e)
        return []


value = tk.StringVar()
values = get_urls()
combobox = ttk.Combobox(
    master=root,
    height=9,
    width=24,
    state="readonly",
    cursor="arrow",
    font=("", 12),
    textvariable=value,
    values=values,
)
combobox.grid(row=7, column=1)


def openWeb():
    if input1.get():
        import re

        if not re.match(r'^https?:/{2}\w.+$', input1.get()):
            root.destroy()
            win32api.MessageBox(0, '无效的url', '提示', win32con.MB_ICONWARNING)
            sys.exit(0)

        webbrowser.open(os.environ.get('AIDOUER_URL') + input1.get())
        root.destroy()

    elif input2.get() or input3.get():
        import endpoint

        keyword = input2.get()
        num = input3.get()
        if not num:
            webbrowser.open(url=f'{endpoint.hzz.domian}/search?q={keyword}')
            root.destroy()
            sys.exit(0)

        status, response = endpoint.hzz.crawling(keyword, num)
        if not status:
            win32api.MessageBox(0, response, '提示', win32con.MB_ICONWARNING)
            root.destroy()
            sys.exit(0)

        webbrowser.open(response)
        root.destroy()

    else:
        url = combobox.get()
        if not url:
            win32api.MessageBox(0, '无效的链接地址', '提示', win32con.MB_ICONWARNING)
            sys.exit(0)

        webbrowser.open(url)
        root.destroy()
        sys.exit(0)


tk.Label(root).grid(row=9, column=0)

tk.Label(root).grid(row=10, column=0)
tk.Button(root, text='解析', font=12, width=20, command=openWeb).grid(row=10, column=1)

tk.mainloop()
