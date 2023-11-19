import re
import os
import sys
import time
import threading
import subprocess
import customtkinter as ctk


ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")  


pwds = ['宅方社', 'zfshe.com', 'zfshegame',
        '梅子糯米饭团', 'falesti.me',
        'yhsxsx10月',
        ]

bmds = ['存档', '附件', '补丁']


class App(ctk.CTk):
    def __init__(self, argv):
        super().__init__()
        self.title("Juice")
        self.resizable(False, False)
        self.grid_columnconfigure((0), weight=1)
        self.set_pos()
        
        self.zip_pt = argv[1] if len(argv)>1 else ''
        self.main_page()

    def set_pos(self):
        screenWidth = self.winfo_screenwidth() 
        screenHeight = self.winfo_screenheight() 
        width = 300 
        height = 100
        left = (screenWidth ) // 2
        top = (screenHeight ) // 2
        self.geometry("%dx%d+%d+%d" % (width, height, left, top))


    def main_page(self):

        self.bar = ctk.CTkProgressBar(self, orientation="horizontal")
        self.bar.grid(row=0, column=0, padx=20, pady=(17.5,0), sticky="ew", columnspan=2)
        self.bar.set(0)

        self.speed = ctk.CTkLabel(self, text="正在解压")
        self.speed.grid(row=1, column=0, padx=20, sticky="w", columnspan=1)

        self.proc = ctk.CTkLabel(self, text="0%")
        self.proc.grid(row=1, column=0, padx=20, sticky="e",columnspan=1)

        self.restart = ctk.CTkButton(self, text="请稍候...", command=self.func, fg_color="grey", state="disabled")
        self.restart.grid(row=2, column=0, padx=20, pady=0, sticky="ew", columnspan=2)

        begin_dl = threading.Thread(target=self.unzip_proc)
        begin_dl.start()



    def unzip_proc(self):
        zip_pt = self.zip_pt
        dir_pt = os.path.dirname(zip_pt)
        raw_pt = os.path.basename(zip_pt).split('_')[-1]
        bas_pt = raw_pt.split('.')[0]
        for i in os.listdir(dir_pt):
            if bas_pt in i:
                os.rename(os.path.join(dir_pt, i), os.path.join(dir_pt, i.split('_')[-1]))


        stamp  = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        sav_pt = os.path.join(dir_pt, stamp)
        os.mkdir(sav_pt)

        v = False
        for pwd in pwds:
            unzip_cmd = "7z.exe x %s -p%s -o%s -bsp1 -y"%(os.path.join(dir_pt, raw_pt), pwd, sav_pt)
            print(unzip_cmd)
            proc = subprocess.Popen(unzip_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            for line in iter(proc.stdout.readline, 'b'):
                line = line.strip().decode('gbk', 'ignore')
                if not subprocess.Popen.poll(proc) is None:
                    if line == "":
                        break
                if "ERROR: Wrong password" in line:
                    v=False
                    break
                ret  = re.search("(\d+)\%", line)
                if ret:
                    v=True
                    self.bar.set(float(ret[1])/100)
                    self.proc.configure(text="%s%%"%ret[1])

            if v:
                break            

        self.bar.set(1)
        if not v:
            self.bar.configure(progress_color="red")
            self.speed.configure(text='终止')
            self.restart.configure(text="解压码错误，请联系站长", state="normal", fg_color='#3B8ED0')
            os.rmdir(sav_pt)
        else:
            self.bar.configure(progress_color="green")
            self.proc.configure(text="100%")
            self.speed.configure(text='完毕')
            self.restart.configure(text="解压成功", state="normal", fg_color='#3B8ED0')

            v = False
            for i in os.listdir(sav_pt):
                if re.search(r"[\u4e00-\u9fa5]+", i):
                    for bmd in bmds:
                        if bmd in i:
                            v = True
                    os.rename(os.path.join(sav_pt, i), os.path.join(sav_pt, stamp)) if not v else None


        


    def func(self):
        app.destroy()









'''
if len(sys.argv)<=1:
    os.popen('msg %username% /TIME:3 "没有输入文件"')
    raise SystemExit()

zip_pt = sys.argv[1]
dir_pt = os.path.dirname(zip_pt)
raw_pt = os.path.basename(zip_pt).split('_')[-1]
bas_pt = raw_pt.split('.')[0]
for i in os.listdir(dir_pt):
    if bas_pt in i:
        os.rename(os.path.join(dir_pt, i), os.path.join(dir_pt, i.split('_')[-1]))


stamp  = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
sav_pt = os.path.join(dir_pt, stamp)
os.mkdir(sav_pt)

os.popen('msg %username% /TIME:7 "正在解压中, 时间可能较久，请稍候...\n之后解压完毕还会有一次提示, 在此之前请不要操作"')
for pwd in pwds:
    unzip_cmd = "7zz.exe x %s -p%s -o%s -y"%(raw_pt, pwd, sav_pt)
    r = subprocess.Popen(unzip_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    while r.poll() is None:
        line = r.stdout.readline().strip().decode('gbk', 'ignore')
        print(line)
    print(pwd, r)
    if not r:
        break

v = False
for i in os.listdir(sav_pt):
    if re.search(r"[\u4e00-\u9fa5]+", i):
        for bmd in bmds:
            if bmd in i:
                v = True
        os.rename(os.path.join(sav_pt, i), os.path.join(sav_pt, stamp)) if not v else None
        


if not r:
    os.popen('msg %%username%% /TIME:5 "解压完毕, 输出于%s文件夹中"'%stamp)
else:
    os.popen('msg %%username%% /TIME:5 "解压码错误，请查看下载页密码或者联系站长"')
    os.rmdir(sav_pt)

'''

app = App(sys.argv)
app.mainloop()