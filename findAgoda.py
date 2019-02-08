#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import call
import os
import webbrowser
from datetime import date

def usage(cmd):
    print('-' * 50)
    print('訂飯店利器')
    print('尋找Agoda上指定的飯店與多個指定日期, 比較出最便宜的期間！')
    print('')
    print('usage:')
    print('./%s' % cmd)
    print('-' * 50)

def openFireFox(url):
    webbrowser.get('firefox').open_new_tab(url)

def openChrome(url):
    webbrowser.get('google-chrome').open_new_tab(url)

def openURL(url):
    print(url)
    #openFireFox(url)
    #openChrome(url)
    webbrowser.open(url)

def subDate(date1, date2):
    # return date2 - date1
    date_split_1 = str.split(date1, '-') # 20xx-xx-xx
    date3 = date(int(date_split_1[0]), int(date_split_1[1]), int(date_split_1[2]))
    date_split_2 = str.split(date2, '-') # 20xx-xx-xx
    date4 = date(int(date_split_2[0]), int(date_split_2[1]), int(date_split_2[2]))
    delta = date4 - date3
    return str(delta.days)

def searchAgoda(hotel_url, start_date, end_date, rooms, adults, childs, los):
    # old format
    #url = hotel_url + '?asq=po6ZHZDWWQw%2B%2FNWjtL2wyEIBVzxVr3Usfk%2BlO0TKWNPsgt%2FLx7KfgAWQoa0tSVVAsPUuZxWRo%2BsE8kZJRYTQrn06ACOynX1AJPuHjMmDgFtEa7m4uCVDk%2BwQ64TmXAc%2F4paTD5VHq5sFdVCiCn7snsm4QEc3A1%2FkQoR7ruhEPcHr9u9qwCQVnA3DW6YPDC6lvJqpW%2F81SfForBExjjE3wA%3D%3D' + \
    #    '&hotel=461942' + \
    #    '&cid=-209' + \
    #    '&tick=636362431996' + \
    #    '&pagetypeid=7' + \
    #    '&origin=TW' + \
    #    '&tag=' + \
    #    '&gclid=' + \
    #    '&aid=130589' + \
    #    '&userId=0641beca-ec99-455e-beb1-06c05995bb58' + \
    #    '&languageId=20' + \
    #    '&sessionId=3q1mkzzzfkf4rrlf4jhg5atg' + \
    #    '&storefrontId=3' + \
    #    '&currencyCode=TWD' + \
    #    '&htmlLanguage=zh-tw' + \
    #    '&trafficType=User' + \
    #    '&cultureInfoName=zh-TW' + \
    #    '&checkIn=' + start_date + \
    #    '&checkout=' + end_date + \
    #    '&los=1' + \
    #    '&rooms=' + rooms + \
    #    '&adults=' + adults + \
    #    '&childs=' + childs + \
    #    '&childages=' + \
    #    '&ckuid=0641beca-ec99-455e-beb1-06c05995bb58'

    url = hotel_url + '?asq=nc6qIoJ%2F3eJL%2Bk8xzn0it3prLQCgdyDHMV1Su3d7T8oTXHeCGZlDXl%2FAwV796%2BO0G5NoefbOnJqxH0BVD1V7tyY3KyW%2FItoxQZeH2ITAytMngXd3YDAibbp3O6iERpI49S%2BRlWODTjS142LwtoW1nJgTuYS%2BQExRP9Ffj%2BXOSkLV%2Fi0y0KRQ5wboBBIWaS5iRKFWtxjjadOV3wa9DLH1RCRmNY2uOqW6qq0nRx9KNfVwOMq174WYylNw99FMf2nT' + \
        '&hotel=51918' + \
        '&cid=-209' + \
        '&tick=636852327135' + \
        '&languageId=20' + \
        '&userId=fed40795-9e48-4de6-a1a5-8f5f89309698' + \
        '&sessionId=weqgwbdjgfvhr453uragr5ry' + \
        '&pageTypeId=7' + \
        '&origin=TW' + \
        '&locale=zh-TW' + \
        '&aid=130589' + \
        '&currencyCode=TWD' + \
        '&htmlLanguage=zh-tw' + \
        '&cultureInfoName=zh-TW' + \
        '&ckuid=fed40795-9e48-4de6-a1a5-8f5f89309698' + \
        '&prid=0' + \
        '&checkIn=' + start_date + \
        '&checkOut=' + end_date + \
        '&rooms=' + rooms + \
        '&adults=' + adults + \
        '&childs=' + childs + \
        '&priceCur=TWD' + \
        '&los=' + los + \
        '&textToSearch=' + \
        '&productType=-1' + \
        '&travellerType=1'
    
    openURL(url)

def searchAgodaMultipleDates():
    #hotel_name='toyoko-inn-hakata-guchi-ekimae' # 東橫INN博多口站前 (Toyoko Inn Hakata-guchi Ekimae) agoda 7.9
    #hotel_name='toyoko-inn-hakata-guchi-ekimae-no-2' # 東橫INN博多口站前2 (Toyoko Inn Hakata-guchi Ekimae No.2) agoda 8.2
    #hotel_name='toyoko-inn-hakata-eki-minami' # 東橫INN博多站南 (Toyoko Inn Hakata-eki Minami) agoda 7.7
    #hotel_name='toyoko-inn-hakata-ekimae-gion' # 東橫INN博多站前祇園 (Toyoko Inn Hakata Ekimae Gion) agoda 7.9
    #hotel_name='toyoko-inn-fukuoka-tenjin' # 東橫INN福岡天神 (Toyoko Inn Fukuoka Tenjin) agoda 7.7
    #hotel_name='toyoko-inn-hakata-nishi-nakasu' # 東橫INN博多西中州 (Toyoko Inn Hakata Nishi-nakasu) agoda 6.5
    #hotel_name='super-hotel-hakata' # 博多超級酒店 (Super Hotel Hakata) agoda 7.8
    #hotel_name='sutton-hotel-hakata-city' # 博多城市Sutton飯店 (Sutton Hotel Hakata City) agoda 8.1
    #hotel_name='hotel-areaone-hakata' # AreaOne飯店 - 博多 (Hotel Areaone Hakata) agoda 7.6
    #city='fukuoka-jp' # 福岡

    hotel_name='apa-hotel-nagoya-nishiki-excellent' # APA飯店 - 名古屋錦EXCELLENT (APA Hotel Nagoya-Nishiki Excellent) agoda 7.9
    #hotel_name='dormy-inn-premium-nagoya-sakae-natural-hot-spring' # Dormy Inn高階飯店 - 名古屋榮天然溫泉錦鯱之湯 (Dormy Inn Premium Nagoya Sakae Natural Hot Spring) agoda 8.7
    city='nagoya-jp' # 名古屋

    hotel_url='https://www.agoda.com/zh-tw/' + hotel_name + '/hotel/' + city + '.html'
    
    start_date_array = (
        '2019-02-22',
    )
    end_date_array = (
        '2019-02-24',
    )

    rooms='1'
    adults='2'
    childs='0'

    zipped = zip(start_date_array, end_date_array)
    for i, j in zipped:
        los = subDate(i, j)
        searchAgoda(hotel_url, i, j, rooms, adults, childs, los)
    print('Hotel URL: ' + hotel_url)

def main():
    if len(sys.argv) > 1:
        usage(sys.argv[0])
        sys.exit()
    else:
        searchAgodaMultipleDates()

if __name__ == '__main__':
    main()
