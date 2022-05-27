import requests
import re
import os
import shutil
from bs4 import BeautifulSoup
import time
from PyQt5.QtCore import QThread, pyqtSignal

cookie = ''  # 可以添加自己的cookies
headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
    'cookie': cookie
}
headers2 = {
    'referer': 'https://www.bilibili.com/bangumi/play/ep402225/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
    'range': 'bytes=0-1000000000000'
}

'''
合并视频和音频，并输出合并后的文件，若文件已存在则替换
'''
def merge(title, output):
    cur_dir = os.getcwd()
    os.system(cur_dir + '/ffmpeg/bin/ffmpeg -i ./cache/"' + title + '.mp3" -i ./cache/"' + title + '.mp4" \
-acodec copy -vcodec copy ' + output + '/"' + title + '.mp4" -y')

'''
下载线程
'''
class DownloadThread(QThread):
    #下载完成信号， 第一个参数为下载进度，0-100表示视频下载进度， 100-200表示音频下载进度， -1表示下载失败
    #第二个参数为
    download_sig = pyqtSignal(int, int)

    #初始化
    def __init__(self, url, row):
        super(DownloadThread, self).__init__()
        self.url = url
        self.row = row
        self.cancel = 0

        # 用空格替换文件名中的非法字符
        correct_file_name(self.url['title'])

    '''
    设置文件保存路径
    '''
    def set_save_path(self, path):
        self.save_path = path


    '''
    取消下载槽函数
    '''
    def cancel_slot(self):
        self.cancel = 1

    '''
    设置Cookie
    '''
    def setCookie(self, c):
        global cookie
        cookie = c

    '''
    启动线程，开始下载
    '''
    def run(self):
        # 创建临时文件夹以便存放音频，视频
        if not os.path.exists('./cache'):
            os.mkdir('./cache')
        # 创建下载目录
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        try:
            # 下载视频
            video = requests.get(self.url['video'], headers=headers2, stream=True)
            if video.status_code == 206:
                chunk_size = 1024
                content_size = int(video.headers['content-length'])
                data_count = 0
                with open('./cache/' + self.url['title'] + '.mp4', 'wb') as f:
                    for data in video.iter_content(chunk_size=chunk_size):
                        f.write(data)
                        data_count += len(data)
                        progress = data_count * 100 / content_size
                        self.download_sig.emit(int(progress), self.row)
                        if self.cancel == 1:
                            raise Exception("Download Cancel")
            # 下载音频
            audio = requests.get(self.url['audio'], headers=headers2, stream=True)
            if audio.status_code == 206:
                chunk_size = 1024
                content_size = int(audio.headers['content-length'])
                data_count = 0
                with open('./cache/' + self.url['title'] + '.mp3', 'wb') as f:
                    for data in audio.iter_content(chunk_size=chunk_size):
                        f.write(data)
                        data_count += len(data)
                        progress = data_count * 100 / content_size
                        self.download_sig.emit(int(progress) + 100, self.row)
                        if self.cancel == 1:
                            raise Exception("Download Cancel")
        except Exception as e:
            # 发送-1表示下载出错, -2表示取消下载
            if e.args[0] == 'Download Cancel':
                self.download_sig.emit(-2, self.row)
            else:
                self.download_sig.emit(-1, self.row)
        else:
            # 合并视频和音频
            merge(self.url['title'], self.save_path)
        finally:
            pass

'''
解析线程
功能：从原始链接中找到所有下载链接
'''
class AnalyThread(QThread):
    # 解析信号，dict为解析得到的下载链接，int为解析进度，-1表示解析失败
    analy_sig = pyqtSignal(dict, int)

    #初始化，url为视频地址
    def __init__(self, url):
        super(AnalyThread, self).__init__()
        self.url = url

    def run(self):
        try:
            type = type_of_video(self.url)
            if len(type) == 0:
                raise Exception

            all_url = get_all_url(self.url, type)
            url_num = len(all_url)
            for i in range(url_num):
                url = all_url[i]
                if type == 'anime' or type == 'tv' or type == 'documentary':
                    url = all_url[i].encode('utf8').decode("unicode_escape")

                download_url = get_downloadurl(url, type)
                if download_url is None:
                    download_url = {'title': '解析失败'}
                elif download_url['video'] == '' or download_url['audio'] == '':
                    download_url['title'] += '（需要大会员）'


                progress = (i+1) * 100 / url_num
                self.analy_sig.emit(download_url, progress)
        except:
            self.analy_sig.emit({}, -1)

'''
将文件名中的非法字符替换成空格
'''
def correct_file_name(file_name):
    reg = re.compile(r'[\\/:*?"<>|\r\n+]')
    vaild_name = reg.findall(file_name)
    if vaild_name:
        for vn in vaild_name:
            file_name = file_name.replace(vn, ' ')

'''
获取视频类型
'''
def type_of_video(url):
    try:
        response = requests.get(url, headers=headers1)
        if response.status_code != 200:
            return ''
        type = BeautifulSoup(response.text, 'lxml').find(attrs={'property': 'og:type'})['content']
    except Exception as e:
        print(e)
        return ''

    if 'movie' in type:
        return 'movie'
    elif 'anime' in type:
        return 'anime'
    elif 'documentary' in type:
        return 'documentary'
    elif 'tv' in type:
        return 'tv'
    else:
        return 'video'

'''
获取原始链接中所有的视频链接
'''
def get_all_url(url, type):
    result = []
    if type == 'anime' or type == 'tv' or type == 'documentary':
        response = requests.get(url, headers=headers1)
        text = response.text
        pattern1 = 'upInfo.*</html>'
        pattern2 = '"share_url":"(http.*?)"'
        a = re.sub(pattern1, '', text)
        result = re.findall(pattern2, a)
    else:
        result.append(url)
    return result


'''
获取视频和音频的下载地址
'''
def get_downloadurl(url, type):
    try:
        response = requests.get(url, headers=headers1)
        if response.status_code == 200:
            text = response.text
            if type == 'movie' or type == 'video':
                pattern_title = '.__INITIAL_STATE__.*?[tT]itle.*?:"(.*?)"'
            else:
                title_of_series = BeautifulSoup(text, 'lxml').find(attrs={'property': 'og:title'})['content']
                pattern_title = '.__INITIAL_STATE__.*?[tT]itle.*?:"' + title_of_series + '.*?：(.*?)"'
            pattern_video = '"video":.+?"baseUrl".*?"(https://.*?.m4s.*?)"'
            pattern_audio = '"audio":.+?"baseUrl".*?"(https://.*?.m4s.*?)"'
            title = re.search(pattern_title, text)[1]
            url_video = re.search(pattern_video, text)[1]
            url_audio = re.search(pattern_audio, text)[1]
            urls = {
                'video': url_video,
                'audio': url_audio,
                'title': title
            }
            return urls
    except ConnectionError as e:
        return None
    except:
        if len(title) != 0:
            urls = {'video': '', 'audio': '', 'title': title}
            return urls
        return None
