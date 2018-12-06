import time
from functools import wraps

def print_use_time(func):
    @wraps(func)
    def _func(*args , **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'函数耗时:{end_time}')
        return result
    return _func

@print_use_time
def send_request(url,method,**kwargs):
    print('发送请求开始')
    time.sleep(2)
    print('发送请求结束')