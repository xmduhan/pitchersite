# -*- coding: utf-8 -*-

#%% 设置django项目环境
import sys, os

path = r'E:\pydev\pitchersite'  # 项目位置
#path = r'/home/wx/pitchersite'  # 项目位置
settings = "pitchersite.settings"
sys.path.append(path)
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

#%%

if __name__ == '__main__':
    from pitcher.tasks import pitcherTask

    pitcherTask()
