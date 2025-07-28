
import logging
import time
from nb_log import LogManager



from funboost import boost, BrokerEnum, BoosterParams,ctrl_c_recv

from test_frame.my_config import BoosterParamsMy


@boost( boost_params=BoosterParamsMy(queue_name='task_queue_name1c', max_retry_times=4, qps=3,
                                     log_level=10,log_filename='自定义.log'))
def task_fun(x, y):
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 5 次 这个 task_fun 函数的目的。
    return x + y


if __name__ == "__main__":
    pass
    task_fun.consume()  # 消费者启动循环调度并发消费任务
    for i in range(10):
        task_fun.push(i, y=i * 2)  # 发布者发布任务
    # ctrl_c_recv()
    #或者
    while 1:
        time.sleep(100)
      


