import csv

import bs4
import pandas as pd;
import numpy as np;
import requests
import sqlite3
from django.http import HttpResponse

# from config.settings import DATA_DIRS

# 갑자기 왜이럴까요 ㅋ 이거 프로젝트 껏다가 ㄷ다시 열어 주실래요 ?
# 아 밥시간 됐네요 .. ㅎㅎ 식사하고 좀있다가 ㄷ다시 하시죠 ~

class Project:

    global cur
    global conn

    # DB 파일 실제 경로 불러오기
    conn = sqlite3.connect('./db.sqlite3',check_same_thread=False)
    cur = conn.cursor()

    # 코인 데이터 가져오기
    def coin(self):

        # DB 조회 조건
        # select replace(replace(replace(sbg.date,'년 ','-'),'월 ','-'),'일','') as date,
        query = cur.execute(''' select replace(replace(replace(sbg.date,'년 ','-'),'월 ','-'),'일','') as date, 
        substr(replace(sbg.open,',',''),-2,-10) as open, 
        substr(replace(sbg.high,',',''),-2,-10) as high,
        substr(replace(sbg.low,',',''),-2,-10) as low,  
        substr(replace(sbg.close,',',''),-2,-10) as close, 
        sbg.volume as volume  
        from sum_bitcoin_gpu sbg  ''')
        cols = [column[0] for column in query.description]
        data = pd.DataFrame.from_records(data=query.fetchall(),columns=cols)
        # print(data)

        dps1 = []
        dps2 = []

        data_list = data.values.tolist()
        dps1_list = {}
        dps2_list = {}

        for i in range(1,int(len(data_list))):

            dps1_list = {
               "date": data_list[i][0],
               "open": data_list[i][1],
               "high": data_list[i][2],
               "low": data_list[i][3],
               "close": data_list[i][4],
               "volume_btc": 0,
               "volume_usd": 0
            }
            dps1.append(dps1_list)

            # dps2_list = {
            #     "date": data_list[i][0],
            #     "close": data_list[i][4]
            #
            # }
            # dps2.append(dps1_list)


        # print(dps1)
        # print(dps2)
        # cur.close()
        # conn.close()

        return HttpResponse(dps1);
        # return dps1;


    # 그래픽 데이터 가져오기
    def graphic(self):
        # DB 조회 조건
        query = cur.execute(''' select
                        sbg.date,
                        sbg.gtx1650,
                        sbg.gtx1650super,
                        sbg.gtx1660,
                        sbg.gtx1660super,
                        sbg.gtx1660ti,
                        sbg.gtx2060,
                        sbg.rtx1660super,
                        sbg.rtx2060,
                        sbg.rtx2060super,
                        sbg.rtx2070super,
                        sbg.rtx2080super,
                        sbg.rtx2080ti,
                        sbg.rtx3060,
                        sbg.rtx3060ti,
                        sbg.rtx3070,
                        sbg.rtx3070ti,
                        sbg.rtx3080,
                        sbg.rtx3080ti,
                        sbg.rtx3090
                        from sum_bitcoin_gpu sbg ''')

        cols = [column[0] for column in query.description]
        data = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        print(data)

        result = ''
        return result;

    # 코인 + 그래픽 데이터 가져오기
    def coin_graphic(self):
        # DB 조회 조건
        query = cur.execute(''' select
                                sbg.date,
                                substr(replace(sbg.close,',',''),-2,-10) as close,
                                sbg.gtx1650,
                                sbg.gtx1650super,
                                sbg.gtx1660,
                                sbg.gtx1660super,
                                sbg.gtx1660ti,
                                sbg.gtx2060,
                                sbg.rtx1660super,
                                sbg.rtx2060,
                                sbg.rtx2060super,
                                sbg.rtx2070super,
                                sbg.rtx2080super,
                                sbg.rtx2080ti,
                                sbg.rtx3060,
                                sbg.rtx3060ti,
                                sbg.rtx3070,
                                sbg.rtx3070ti,
                                sbg.rtx3080,
                                sbg.rtx3080ti,
                                sbg.rtx3090
                                from sum_bitcoin_gpu sbg ''')

        cols = [column[0] for column in query.description]
        data = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        print(data)

        result = ''
        return result;


# if __name__ == '__main__':
#     Project.coin('self');
    # Project.graphic('self');
    # Project.coin_graphic('self');
