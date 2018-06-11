# coding: utf-8

import requests
import xml.etree.ElementTree as ET
from collections import defaultdict
import json
import os
import zipfile
from zipfile import ZipFile
import io
import time
import logging
import datetime

def get_link_info_str(ticker_symbol, base_url):
    url = base_url+ticker_symbol
    response = requests.get(url)
    return response.text

def get_link(tree, namespace):
    yuho_dict = defaultdict(dict)
    for el in tree.findall('.//'+namespace+'entry'):
        title = el.find(namespace+'title').text
        if not is_yuho(title): continue
        _id = el.find(namespace+'id').text
        link = el.find('./'+namespace+'link[@type="application/zip"]')
        url = link.attrib['href']
        yuho_dict[_id] = {'id':_id,'title':title,'url':url}
    return yuho_dict

def is_yuho(title):
    if u'有価証券報告書' in title:
        return True
    else:
        return False

def write_download_info(ofname):
    with open(ofname,'w') as of:
        json.dump(dat_download, of, indent=4)

def download_all_xbrl_files(download_info_dict,directory_path):
    for ticker_symbol, info_dicts in download_info_dict.items():
        save_path = directory_path+ticker_symbol
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        for _id, info_dict in info_dicts.items():
            _download_xbrl_file(info_dict['url'],_id,save_path)

def _download_xbrl_file(url,_id,save_path):

    # 取得対象の絞り込み
    searchString = url.find("ED2018")

    if searchString != -1 :

        try:
            r = requests.get(url)
            if r.ok:
                path = save_path+'/'+_id
                if not os.path.exists(path):
                    os.mkdir(path)
                try:
                    r = requests.get(url)
                    z = ZipFile(io.BytesIO(r.content))
                    z.extractall(path)
                except:
                    txtoutput ("***取得エラー発生："+url)
                    time.sleep(10)
                    _download_xbrl_file(url,_id,save_path)
        except:
            txtoutput ("***接続エラー発生："+url)
            time.sleep(10)
            _download_xbrl_file(url,_id,save_path)
    else:
        txtoutput ("***取得対象外："+url)

def txtoutput(str2):

    f = open('download.log', 'a') # 追記モードで開く
    f.write(str2+"\n") # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる


if __name__=='__main__':

    todaydetail = datetime.datetime.today()
    txtoutput("実行開始："+todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
    # 有報キャッチャー ウェブサービス AtomAPIを利用
    base_url = 'http://resource.ufocatch.com/atom/edinetx/query/'
    namespace = '{http://www.w3.org/2005/Atom}'
    # 証券コードを配列で指定
    t_symbols = ('7203','7267','6178','7201','9432')

    for t_symbol in t_symbols:
        start = time.time()
        txtoutput('実行スタート：'+t_symbol)
        response_string = get_link_info_str(t_symbol, base_url)

        try:

            ET_tree = ET.fromstring( response_string.encode('utf-8') )
            ET.register_namespace('',namespace[1:-1])
            dat_download = defaultdict(dict)
            info_dict = get_link(ET_tree,namespace)
            dat_download[t_symbol] = info_dict

            ofname = os.getcwd()+'/json/dat_download_'+t_symbol+'.json'
            write_download_info(ofname)
            directory_path = os.getcwd()+'/xbrl/'
            download_all_xbrl_files(dat_download,directory_path)

            time.sleep(10)
            txtoutput('実行おわり：'+t_symbol)

            elapsed_time = time.time() - start
            txtoutput ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

        except:
            txtoutput('**APIエラー：'+t_symbol)
