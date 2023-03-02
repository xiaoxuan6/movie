import tkinter as tk

from views import AllFrame, MoreFrame, VipFrame, AbortFrame


class Movie:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.vip_frame = VipFrame(self.root)
        self.all_frame = AllFrame(self.root)
        self.more_frame = MoreFrame(self.root)
        self.abort_frame = AbortFrame(self.root)

        self.root.title('Vip 会员视频解析 v0.0.5')
        self.root.geometry('300x200')
        self.root.resizable(width=False, height=False)

        self.init_menu()
        self.vip_frame.pack()

    def init_menu(self):
        menu = tk.Menu(self.root)
        menu.add_command(label='会员视频', command=self.show_vip)
        menu.add_command(label='全网视频', command=self.show_all)
        menu.add_command(label='更多网站', command=self.show_more)
        menu.add_command(label='关于', command=self.show_abort)

        self.root['menu'] = menu

    def show_vip(self):
        self.vip_frame.pack()
        self.all_frame.pack_forget()
        self.more_frame.pack_forget()
        self.abort_frame.pack_forget()

    def show_all(self):
        self.all_frame.pack()
        self.vip_frame.pack_forget()
        self.more_frame.pack_forget()
        self.abort_frame.pack_forget()

    def show_more(self):
        self.more_frame.pack()
        self.vip_frame.pack_forget()
        self.all_frame.pack_forget()
        self.abort_frame.pack_forget()

    def show_abort(self):
        self.more_frame.pack_forget()
        self.vip_frame.pack_forget()
        self.all_frame.pack_forget()
        self.abort_frame.pack()


if __name__ == '__main__':
    root = tk.Tk()
    Movie(root)
    root.mainloop()
