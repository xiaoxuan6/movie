import os
import tkinter as tk
import webbrowser
from tkinter import messagebox


class VipFrame(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.vip_url = tk.StringVar()
        self.show()
        self.root = root

    def show(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='有效的视频地址').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.vip_url).grid(row=1, column=2, pady=10)

        tk.Button(self, text='解析', width=20, command=self.handle).grid(row=2, column=2, pady=10)

    def handle(self):
        import re

        if not re.match(r'^https?:/{2}\w.+$', self.vip_url.get()):
            messagebox.showerror(title='错误', message='无效的链接地址')
            self.vip_url.set('')
        else:
            webbrowser.open(os.environ.get('AIDOUER_URL') + self.vip_url.get())
            self.root.quit()


class AllFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.keyword = tk.StringVar()
        self.num = tk.StringVar()
        self.show()
        self.root = root

    def show(self):
        tk.Label(self, text='剧名越全，解析越准').grid(row=0, column=2, pady=10)
        tk.Label(self, text='剧名').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.keyword).grid(row=1, column=2, pady=10)

        tk.Label(self, text='选集').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.num).grid(row=2, column=2, pady=10)

        tk.Button(self, text='解析', width=20, command=self.handle).grid(row=3, column=2, pady=10)

    def handle(self):
        import endpoint

        keyword = self.keyword.get()
        num = self.num.get()

        if not keyword:
            messagebox.showerror(title='错误', message='无效的剧名')

        elif not num:
            messagebox.showerror(title='错误', message='无效的选集')

        else:
            status, response = endpoint.hzz.crawling(str(keyword), num)
            if not status:
                self.keyword.set('')
                self.num.set('')
                messagebox.showerror(title='错误', message=response)

            else:
                from urllib import parse
                import re

                try:
                    url = parse.unquote(response)
                    url = re.findall('play_url=(.*?)&', url)[0]
                    webbrowser.open(url)
                    self.root.quit()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title='错误', message='解析失败，请重试')


class MoreFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.value = tk.StringVar()
        self.show()

    @staticmethod
    def get_urls():
        import requests
        import json

        try:
            url = os.environ.get('APP_URL')
            content = requests.get(url).text
            items = json.loads(content.replace('var dh_data = ', ''))[6]['item']

            urls = []
            for item in items:
                urls.append(item['url'])

            return urls
        except:
            return []

    def show(self):
        from tkinter import ttk

        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='更多网站').grid(row=1, column=0)
        combobox = ttk.Combobox(
            master=self,
            height=9,
            width=24,
            state="readonly",  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor="arrow",  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=("", 12),
            textvariable=self.value,
            values=self.get_urls(),
        )
        combobox.grid(row=1, column=2)

        tk.Button(self, text='解析', width=20, command=self.handle).grid(row=3, column=2, pady=10)

    def handle(self):
        url = self.value.get()
        if not url:
            messagebox.showerror(title='错误', message='请选择网址')

        else:
            webbrowser.open(url)
            self.root.quit()


class AbortFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self).grid(row=0, column=0)
        # tk.Label(self).grid(row=1, column=0)
        tk.Label(self, text='关于作品:').grid(row=2, column=0)
        tk.Label(self, text='本作品由 tkinter 制作').grid(row=2, column=1, sticky='w')
        tk.Label(self, text='关于作者:').grid(row=3, column=0)
        tk.Label(self, text='xiaoxuan6').grid(row=3, column=1, sticky='w')
        tk.Label(self, text='开源地址:').grid(row=4, column=0)
        tk.Button(self, text='https://github.com/xiaoxuan6/movie', command=self.openUrl).grid(row=4, column=1,
                                                                                              sticky='w')
        tk.Label(self, text='版权所有:').grid(row=5, column=0)
        tk.Label(self, text='晓轩').grid(row=5, column=1, sticky='w')

    @staticmethod
    def openUrl():
        webbrowser.open(url='https://github.com/xiaoxuan6/movie')
