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
        self.del_files()
        
        self.ful_pt = argv[1] if len(argv)>1 else sys.exit(0)
        self.main_page()

    def set_pos(self):
        screenWidth = self.winfo_screenwidth() 
        screenHeight = self.winfo_screenheight() 
        width = 300 
        height = 100
        left = (screenWidth ) // 2
        top = (screenHeight ) // 2
        self.geometry("%dx%d+%d+%d" % (width, height, left, top))

    def del_files(self):
        for i in os.listdir('.'):
            if i[-3:]=='log':
                os.remove(i)

    def main_page(self):

        self.bar = ctk.CTkProgressBar(self, orientation="horizontal")
        self.bar.grid(row=0, column=0, padx=20, pady=(17.5,0), sticky="ew", columnspan=2)
        self.bar.set(0)

        self.speed = ctk.CTkLabel(self, text="正在解压")
        self.speed.grid(row=1, column=0, padx=20, sticky="w", columnspan=1)

        self.proc = ctk.CTkLabel(self, text="0%")
        self.proc.grid(row=1, column=0, padx=20, sticky="e",columnspan=1)

        self.restart = ctk.CTkButton(self, text="请稍候...", command=lambda:app.destroy(), fg_color="grey", state="disabled")
        self.restart.grid(row=2, column=0, padx=20, pady=0, sticky="ew", columnspan=2)

        begin_dl = threading.Thread(target=self.unzip_proc)
        begin_dl.start()



    def unzip_proc(self):
        ful_pt = self.ful_pt
        dir_pt = os.path.dirname(ful_pt)
        raw_pt = os.path.basename(ful_pt).split('_')[-1]
        bas_pt = raw_pt.split('.')

        if len(bas_pt)>=3:
            for i in os.listdir(dir_pt):
                if bas_pt[0] in i:
                    j = i.split('_')[-1]
                    os.rename(os.path.join(dir_pt, i), os.path.join(dir_pt, j))
                    if 'part1' in j:
                        raw_pt = j
                    elif '001' in j:
                        raw_pt = j


        stamp  = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        sav_pt = os.path.join(dir_pt, stamp)
        os.mkdir(sav_pt)

        v = False
        for idx, pwd in enumerate(pwds):
            log_name = "%s_%d.log"%(stamp, idx)
            unzip_cmd = "7z.exe x %s -p%s -o%s -bsp1 -y >%s 2>&1"%(os.path.join(dir_pt, raw_pt), pwd, sav_pt, log_name)
            print(unzip_cmd)


            subprocess.Popen(unzip_cmd, shell=True)
            vv = False
            while not vv:
                try:
                    f1 = open(log_name, 'r')
                    vv = True
                except FileNotFoundError:
                    time.sleep(0.5)

                
            position = 0
            while not v:
                line = f1.readline().strip()
                if line:
                    if "ERROR" in line:
                        v=False
                        break
                    elif "Everything is Ok" in line:
                        v=True
                        break
                    ret  = re.search("(\d+)\%", line)
                    if ret:
                        self.bar.set(float(ret[1])/100)
                        self.proc.configure(text="%s%%"%ret[1])


                cur_position = f1.tell()
                if cur_position == position:
                    time.sleep(0.2)
                    continue
                else:
                    position = cur_position

                
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




app = App(sys.argv)
app.mainloop()