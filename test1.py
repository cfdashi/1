import tkinter as tk
import datetime as dt
import time


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # 边框大小
        self.geometry("240x120+300+300")
        self.title('下班倒计时！')
        # 两个标签横向排列
        self.lbl_now_time = tk.Label(self, text='')
        self.lbl_now_time.grid(row=0, column=0)
        self.lbl_off_time = tk.Label(self, text='')
        self.lbl_off_time.grid(row=1, column=0)
        self.after(1000, self.refresh_data)
        self.mainloop()

    def refresh_data(self):
        now_time = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(time.time()))
        now_date = time.strftime('%Y:%m:%d', time.localtime(time.time()))
        off_time = now_date + ' 18:00:00'
        # 时间字符串转成时间数组
        off_time = time.strptime(off_time, '%Y:%m:%d %H:%M:%S')
        now_time = time.strptime(now_time, '%Y:%m:%d %H:%M:%S')
        # 时间数组转成时间戳
        off_time = int(time.mktime(off_time))
        now_time = int(time.mktime(now_time))
        # 计算出时间差
        delta = off_time - now_time
        # 时间戳转换成时分秒，并显示两位数
        d_h = '{:0=2}'.format(int(delta / 60 / 60))
        d_m = '{:0=2}'.format(int((delta - int(d_h) * 60 * 60) / 60))
        d_s = '{:0=2}'.format(delta % 60)
        delta_txt = d_h + ':' + d_m + ':' + d_s
        now_time_txt = time.strftime('%H:%M:%S', time.localtime(time.time()))
        self.lbl_now_time = tk.Label(self, text='当前时间：' + now_time_txt, font=24)
        self.lbl_now_time.grid(row=0, column=0, padx=10, pady=10)
        self.lbl_off_time = tk.Label(self, text='剩余时间：' + delta_txt, font=24)
        self.lbl_off_time.grid(row=1, column=0, padx=10, pady=10)
        # 每隔一秒刷新一次
        self.after(1000, self.refresh_data)


if __name__ == '__main__':
    Application = Application()