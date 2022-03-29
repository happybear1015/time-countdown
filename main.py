import time

from tqdm import tqdm

# 一个可迭代对象，每次请求值时, 都会打印一个动态更新的进度控制条

def time_countdown(minute_num):
    """
    时间倒计时
    :param time: 分钟数
    :return: none
    """
    minute_num=int(minute_num)
    minute_num*=60
    for i in tqdm(range(minute_num)):
        time.sleep(1)
if __name__ == '__main__':
    time_countdown('10')

