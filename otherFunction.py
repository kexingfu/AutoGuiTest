import os
from logger import log
parentdir=os.path.abspath(os.path.dirname(__file__))

def excuteCase(name):
    log.logger.info('执行'+ name)
    os.system(os.path.join(os.getcwd(),parentdir +'/baseCase/'+ name))