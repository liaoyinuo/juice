import re
import os
import sys
import time



pwds = ['宅方社', 'zfshe.com', 'zfshegame',
        '梅子糯米饭团', 'falesti.me'
        'yhsxsx10月',
        ]

bmds = ['存档', '附件']

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

os.popen('msg %username% /TIME:1 "正在解压中, 请稍候..."')
for pwd in pwds:
    unzip_cmd = "7z.exe x %s -p%s -o%s -y"%(raw_pt, pwd, sav_pt)
    r = os.system(unzip_cmd)
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
    os.popen('msg %%username%% /TIME:3 "解压完毕, 输出于%s文件夹中"'%stamp)
else:
    os.popen('msg %%username%% /TIME:3 "解压码错误，请查看下载页密码或者联系站长"')
    os.rmdir(sav_pt)



