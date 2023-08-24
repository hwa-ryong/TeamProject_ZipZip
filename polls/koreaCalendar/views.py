import aiohttp
import asyncio

from datetime import datetime, timedelta
from django.shortcuts import render

# 이전 달, 현재 연도 당월, 다음달
now = datetime.now()
now_year = now.year
now_month = now.month
next_month = now + timedelta(days=30)

# 이전 달 계산
if now_month == 1:
    previous_month = 12
    previous_year = now_year - 1
else:
    previous_month = now_month - 1
    previous_year = now_year
month = now.strftime('%m')
month2 = next_month.strftime('%m')
previous_month_str = str(previous_month).zfill(2)  # 한 자리 숫자일 경우 0을 추가하여 두 자리로 맞춤

# 비동기 처리 함수
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            return await response.json()

# calendar에 청약 일정 추가하는 함수
async def koreaCalendar(request):
    if request.method == 'GET':

        url1 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
        page = 'page=1&'
        perPage = 'perPage=10000&'
        serviceKey = 'serviceKey=ibEJT6J0bl9WzpzbwJVPg9on2aBStbXKZnT8a7sLOTuEi5LMGvjsPAufQYld%2Br%2FvL6B4VhxXZ5EnI7j1GO%2B8uQ%3D%3D'

        url2 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail?'
        url3 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail?'

        reqUrl1 = url1 + page + perPage + serviceKey
        reqUrl2 = url2 + page + perPage + serviceKey
        reqUrl3 = url3 + page + perPage + serviceKey

        tasks = [
            fetch_data(reqUrl1),
            fetch_data(reqUrl2),
            fetch_data(reqUrl3)
        ]

        # 비동기로 모든 작업 실행
        responses = await asyncio.gather(*tasks)

        json_data1, json_data2, json_data3 = responses

        data_list = []
        # APT 분양정보 청약 접수 시작일
        for data in json_data1['data']:
            if f'{now_year}-{month}' in data['RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['RCEPT_BGNDE']:
                data_list.append(data)

        # 오피스텔/도시형/민간임대 분양정보 청약 접수 시작일
        for data in json_data2['data']:
            if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)

        # APT 무순위/잔여세대 일반 공급 접수 시작일
        for data in json_data3['data']:
            if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)

        results = []

        for data in data_list:
            if 'RCEPT_BGNDE' in data:
                result = {
                    'title': data['HOUSE_NM'],
                    'start': data['RCEPT_BGNDE']
                }
                results.append(result)
            elif 'SUBSCRPT_RCEPT_BGNDE' in data:
                result = {
                    'title': data['HOUSE_NM'],
                    'start': data['SUBSCRPT_RCEPT_BGNDE']
                }
                results.append(result)

        context = {
            'context':results
        }
        return render(request, 'calendar/calendar.html', context)

    return render(request, 'calendar/calendar.html')

# 달력 iframe 출력
async def koreaCalendar_iframe(request, title):
    if request.method == 'GET':

        url1 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
        page = 'page=1&'
        perPage = 'perPage=10000&'
        serviceKey = 'serviceKey=ibEJT6J0bl9WzpzbwJVPg9on2aBStbXKZnT8a7sLOTuEi5LMGvjsPAufQYld%2Br%2FvL6B4VhxXZ5EnI7j1GO%2B8uQ%3D%3D'

        url2 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail?'
        url3 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail?'
        url4 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancMdl?'
        url5 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancMdl?'
        url6 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancMdl?'

        reqUrl1 = url1 + page + perPage + serviceKey
        reqUrl2 = url2 + page + perPage + serviceKey
        reqUrl3 = url3 + page + perPage + serviceKey
        reqUrl4 = url4 + page + perPage + serviceKey
        reqUrl5 = url5 + page + perPage + serviceKey
        reqUrl6 = url6 + page + perPage + serviceKey

        tasks = [
            fetch_data(reqUrl1),
            fetch_data(reqUrl2),
            fetch_data(reqUrl3),
            fetch_data(reqUrl4),
            fetch_data(reqUrl5),
            fetch_data(reqUrl6)
        ]

        # 비동기로 모든 작업 실행
        responses = await asyncio.gather(*tasks)

        json_data1, json_data2, json_data3, json_data4, json_data5, json_data6 = responses

        # 주택관리번호 추출
        data_list = []
        data_list2 = []

        def save_data1(house_manage):
            for data in json_data4['data']:
                if house_manage == data['HOUSE_MANAGE_NO']:
                    data_list2.append(data)

        def save_data2(house_manage):
            for data in json_data5['data']:
                if house_manage == data['HOUSE_MANAGE_NO']:
                    data_list2.append(data)

        def save_data3(house_manage):
            for data in json_data6['data']:
                if house_manage == data['HOUSE_MANAGE_NO']:
                    data_list2.append(data)

        # APT 분양정보 청약 접수 시작일
        for data in json_data1['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{now_year}-{month2}' in data['RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)

        for data in json_data2['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)

        for data in json_data3['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    if data not in data_list:
                        data_list.append(data)

        # 데이터를 저장하는 함수들을 data_list이 채워진 후에 호출합니다.
        for data in data_list:
            house_manage = data['HOUSE_MANAGE_NO']
            save_data1(house_manage)
            save_data2(house_manage)
            save_data3(house_manage)

        rowspan = len(data_list2) + 1

        context = {
            'data_list': data_list,
            'data_list2': data_list2,
            'rowspan': rowspan
        }

        return render(request, 'calendar/calendar_iframe.html', context)

    return render(request, 'calendar/calendar_iframe.html')

