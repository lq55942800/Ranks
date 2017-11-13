# coding=utf-8

from WindPy import w
import time, sys, random


def get_data(symbol, start_date, end_date):
    w.start()
    resp = w.edb(symbol, start_date, end_date)
    return resp


def get_diff(contract, column):
    w.start()
    # contract = ','.join([contract_one, contract_two, contract_three])
    resp = w.wsq(contract, column)
    return resp


def get_days(resp):
    dates = []
    for i in range(len(resp.Times)):
        date = resp.Times[i].strftime("%Y-%m-%d")
        dates.append(date)
    return dates


def get_single_date(resp, start_date):
    timeArray = time.strptime(start_date, "%Y-%m-%d")
    timestamp = time.mktime(timeArray)
    s_1 = float(timestamp) * 1000, resp.Data[0][0]
    return s_1


def get_day_data(resp, dates):
    get_date_size = len(dates)
    random_dates = []
    for i in range(0, 2):
        random_dates.append(dates[random.randint(0, get_date_size - 1)])
    timeArray_1 = time.strptime(random_dates[0], "%Y-%m-%d")
    timestamp_1 = time.mktime(timeArray_1)
    timeArray_2 = time.strptime(random_dates[1], "%Y-%m-%d")
    timestamp_2 = time.mktime(timeArray_2)
    num_1 = dates.index(random_dates[0])
    num_2 = dates.index(random_dates[1])
    s_1 = float(timestamp_1) * 1000, resp.Data[0][num_1]
    s_2 = float(timestamp_2) * 1000, resp.Data[0][num_2]
    if get_date_size >= 2:
        last_data = resp.Data[0][-2]
        last_day = dates[-2]
        timeArray = time.strptime(last_day, '%Y-%m-%d')
        last_day_timestamp = time.mktime(timeArray)
        s_3 = float(last_day_timestamp) * 1000, last_data
        return s_1, s_2, s_3
    else:
        return s_1, s_2


def get_day_data_with_flag(resp, dates, model1, model2):
    get_date_size = len(dates)
    random_dates = []
    for i in range(0, 2):
        random_dates.append(dates[random.randint(0, get_date_size - 1)])
    timeArray_1 = time.strptime(random_dates[0], "%Y-%m-%d")
    timestamp_1 = time.mktime(timeArray_1)
    timeArray_2 = time.strptime(random_dates[1], "%Y-%m-%d")
    timestamp_2 = time.mktime(timeArray_2)
    num_1 = dates.index(random_dates[0])
    num_2 = dates.index(random_dates[1])
    date_1 = random_dates[0]
    date_2 = random_dates[1]
    last_day = dates[-2]
    last_data = resp.Data[0][-2]
    another_resp = get_data(another_symbol, start_date, end_date)
    another_data_1, another_data_2, another_data_3 = get_ralevant_data(another_resp, date_1, date_2, last_day)
    resp_Data_1 = resp.Data[0][num_1]
    resp_Data_2 = resp.Data[0][num_2]

    if model1 == '1':
        resp_Data_1 = round(resp_Data_1, 2) * 10000
        resp_Data_2 = round(resp_Data_2, 2) * 10000
        resp_Data_3 = round(last_data, 2) * 10000
    else:
        pass

    if model2 == '1':
        another_data_1 = round(another_data_1, 2) * 10000
        another_data_2 = round(another_data_2, 2) * 10000
        another_data_3 = round(another_data_3, 2) * 10000
    else:
        pass

    timeArray = time.strptime(last_day, '%Y-%m-%d')
    last_day_timestamp = time.mktime(timeArray)

    print(date_1, date_2, last_day)
    print(resp_Data_1, resp_Data_2, resp_Data_3)
    print(another_data_1, another_data_2, another_data_3)

    s_1 = float(timestamp_1) * 1000, resp_Data_1 + another_data_1
    s_2 = float(timestamp_2) * 1000, resp_Data_2 + another_data_2
    s_3 = float(last_day_timestamp) * 1000, resp_Data_3 + another_data_3
    return s_1, s_2, s_3


def get_ralevant_data(another_resp, date_1, date_2, last_day):
    another_dates = get_days(another_resp)
    another_resp_datas = another_resp.Data[0]
    if date_1 in another_dates:
        another_data_1 = another_resp_datas[another_dates.index(date_1)]
    else:
        another_data_1 = 0
    if date_2 in another_dates:
        another_data_2 = another_resp_datas[another_dates.index(date_2)]
    else:
        another_data_2 = 0

    if last_day in another_dates:
        another_data_3 = another_resp_datas[another_dates.index(last_day)]
    else:
        another_data_3 = 0
    return another_data_1, another_data_2, another_data_3


if __name__ == '__main__':
    Flag = sys.argv[-1]
    if Flag == '1':
        symbol = sys.argv[1]
        start_date = sys.argv[2]
        resp = get_data(symbol, start_date, start_date)
        list = get_single_date(resp, start_date)
        print(list)
    elif Flag == '2':
        symbol = sys.argv[1]
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        #    timestamp = sys.argv[4]
        resp = get_data(symbol, start_date, end_date)
        dates = get_days(resp)
        list = get_day_data(resp, dates)
        print(list)
    elif Flag == '3':
        contract = sys.argv[1]
        column = sys.argv[2]
        resp = get_diff(contract, column)
        diff_one = resp.Data[0][0] - resp.Data[0][1]
        diff_two = resp.Data[0][0] - resp.Data[0][2]
        diff_three = resp.Data[0][1] - resp.Data[0][2]
        print(diff_one, diff_two, diff_three)
    elif Flag == '4':
        symbol = sys.argv[1]
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        another_symbol = sys.argv[4]
        model1 = sys.argv[5]
        model2 = sys.argv[6]
        resp = get_data(symbol, start_date, end_date)
        dates = get_days(resp)
        list = get_day_data_with_flag(resp, dates, model1, model2)
        print(list)
    else:
        pass
