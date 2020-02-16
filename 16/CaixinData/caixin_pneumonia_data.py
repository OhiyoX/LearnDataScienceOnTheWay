from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import os
import time


def run():
    url_prefix = "http://datanews.caixin.com/interactive/2020/pneumonia-h5/data/"

    file_list = ['pneumonia.csv', 'data2.csv', 'death2.csv', 'severe.csv', 'heal.csv', 'suspected.csv', 'china.json']

    data_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    for file in file_list:
        while True:
            try:
                file_content = requests.get(url_prefix + file)
                break
            except(TimeoutError, SystemExit, EOFError):
                pass
        current_file_path = 'CaixinData'
        if not os.path.exists(current_file_path):
            os.makedirs(current_file_path)
        with open(current_file_path + '/' + file, 'wb') as file_now:
            # 下载文件
            file_now.write(file_content.content)
            file_now.close()



