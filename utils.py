import os
import glob
import time
from matplotlib import pyplot as plt
import datetime

data_keys = ['date', 'time', 'longitude', 'latitude', 'time_stamp']
data_idxes = {}
for idx, key in enumerate(data_keys):
    data_idxes[key] = idx

def trans_time_stamp(date, h_m_s):
    t = datetime.datetime.strptime(date + ':' + h_m_s, '%Y-%m-%d:%H:%M:%S')
    t = t.timetuple()
    time_stamp = int(time.mktime(t))
    return time_stamp

def read_file(file_name):
    file_format = file_name.split('.')[-1]
    assert file_format == 'txt' or file_format == 'nmea'

    data = []
    with open(file_name, 'r') as f:
        while 1:
            d = f.readline()
            d = d.split('\n')[0]
            if len(d) == 40:
                d = d.split(',')
                time_stamp = trans_time_stamp(d[data_idxes['date']], d[data_idxes['time']])
                d.append(time_stamp)
                # print(d)
                data.append(d)
                
            if d == '':
                break

    return data

def clip_traj(data, start_time = -1, end_time = -1):
    if isinstance(data, str):
        data = read_file(data)

    ##### NULL

    return data.copy()

def show_traj(data, start_time = -1, end_time = -1):
    if isinstance(data, str):
        data = read_file(data)

    clipped_data = clip_traj(data, start_time=start_time, end_time=end_time)
    longitude = [float(d[data_idxes['longitude']]) for d in clipped_data]
    latitude = [float(d[data_idxes['latitude']]) for d in clipped_data]
    # plt.plot(longitude, latitude)
    plt.plot(latitude, longitude)
    plt.show()

    

    


if __name__ == "__main__":
    import glob
    files = glob.glob('data/*')
    # print(read_file(files[1]))
    # show_traj(files[1])
    pass