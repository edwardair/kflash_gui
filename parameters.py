import os, sys

appName = "kflash_gui"
author = "Neucrack"
strDataDirName = "kflash_gui_data"
strDataAssetsDirName = "kflash_gui_data/assets"
appIcon = "assets/logo.png"
appLogo = "assets/logo.png"
appLogo2 = "assets/logo2.png"
translationPath = "assets/translation"
configFileName = "kflash_gui.conf"
configFilePath = ""

# 记录最近一次使用的 kflash_gui.conf 的路径
lastConfigName = ".last_kflash_gui"
lastConfigSavePath = ""
if sys.platform.startswith('linux') or sys.platform.startswith('darwin') or sys.platform.startswith('freebsd'):
    configFileDir = os.path.join(os.getenv("HOME"), ".config/kflash_gui")
    try:
        lastConfigSavePath = os.path.join(configFileDir, lastConfigName)
        if not os.path.exists(configFileDir):
            os.makedirs(configFileDir)
    except:
        pass
else:
    lastConfigSavePath = os.path.join(os.getcwd(), lastConfigName)

def getConfigFilePath(path=None, verifyPathExists=True):
    """
    :param path:
    :param verifyPathExists: False: 若path对应文件不存在，也照样返回此路径，用于保存conf时使用
    :return:
    """
    if path is not None and len(path) > 0:
        if os.path.isfile(path) or not verifyPathExists:
            return path
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin') or sys.platform.startswith('freebsd'):
        configFileDir = os.path.join(os.getenv("HOME"), ".config/kflash_gui")
        try:
            path = os.path.join(configFileDir, configFileName)
            if not os.path.exists(configFileDir):
                os.makedirs(configFileDir)
        except:
            pass
    else:
        path = os.path.join(os.getcwd(), configFileName)
    return path

try:
    with open(lastConfigSavePath, 'r', encoding='utf8') as f:
        last_conf_path = f.read()
        if os.path.exists(last_conf_path):
            configFilePath = last_conf_path
        else:
            configFilePath = getConfigFilePath()
except:
    configFilePath = getConfigFilePath()




# get data path
pathDirList = sys.argv[0].replace("\\", "/").split("/")
pathDirList.pop()
dataPath = os.path.abspath("/".join(str(i) for i in pathDirList))
if not os.path.exists(dataPath + "/" + strDataDirName):
    pathDirList.pop()
    dataPath = os.path.abspath("/".join(str(i) for i in pathDirList))
dataPath = getattr(sys, '_MEIPASS', dataPath)
dataPath = (dataPath + "/" + strDataDirName).replace("\\", "/")

translationPathAbs = dataPath + "/" + translationPath
