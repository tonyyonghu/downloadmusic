# import pygame
'''
http://music.taihe.com/search?key=%E9%99%88%E7%B2%92

'''

import requests
import re


song_ids=[]


song_id = '1397674264'  # 要下载歌曲的ID
file = "music/"  # 保存音乐的文件路径,最后加斜杠
wurl = "https://link.hhtjim.com/163/"#外链生成地址
wang_url = "https://music.163.com/song?id=" + song_id
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
song_url = wurl + song_id + ".mp3"
# 获取歌曲16进制编码
song = requests.get(url=song_url,headers=headers).content
# 获取歌曲名称
song_names = requests.get(url=wang_url,headers=headers).text



song_name = re.findall('<em class="f-ff2">.*</em>', song_names)[0].lstrip('<em class="f-ff2">').rstrip('</em>')

# 保存文件
with open(file + song_name + '.mp3', 'wb') as f:
    f.write(song)
    print(song_url + ' 歌名：' + song_name)