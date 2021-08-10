#!/usr/local/opt/python@3.9/bin/python3.9
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from datetime import timedelta


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"}

for i in range(22, 53):

    # url = f"https://jut.su/narutoo/season-3/episode-{i}.html"
    # url = f"https://jut.su/narutoo/film-{i}.html"
    # url = f"https://jut.su/narutoo/ova-{i}.html"
    url = f"https://jut.su/narutoo/chibi/episode-{i}.html"
    

    session = requests.session()
    response = session.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    link = soup.find('video', class_="video-js vjs-default-skin vjs-16-9").find('source', label='1080p').get('src')
    # link = soup.find('video', class_="video-js vjs-default-skin vjs-16-9").find('source', label='720p').get('src')
    # link = soup.find('video', class_="video-js vjs-default-skin vjs-16-9").find('source', label='480p').get('src')

    start = time.monotonic()
    print(f'Начинаю запись файла №{i}')
    video = session.get(url=link, headers=headers)
    with open(f'Chibi/Naruto_{i}.mp4', 'wb') as f:
        f.write(video.content)
    print(f'Успешно записан файл #{i}! | {timedelta(seconds = (time.monotonic()-start))} секунд затрачено')

    session.close()
