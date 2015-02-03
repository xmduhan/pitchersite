# -*- coding: utf-8 -*-

#%% 设置django项目环境
import sys, os
path = r'E:\pydev\pitchersite'  # 项目位置
#path = r'/home/wx/pitchersite'  # 项目位置
settings = "pitchersite.settings"
sys.path.append(path)
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

from pitcher.tasks import RedoTask

#%%
def main():
    '''
    主过程
    '''
    if len(sys.argv) != 2:
        print 'Use "python refresh.py taskname" To Start This Script. '
        return
    RedoTask(sys.argv[1]).run()

if __name__ == '__main__':
    main()
