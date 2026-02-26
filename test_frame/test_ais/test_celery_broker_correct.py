# -*- coding: utf-8 -*-
"""
Funboost 使用 Celery 作为 Broker 的完整正确示例
关键点：
1. funboost 负责定义任务和发布任务
2. 使用 CeleryHelper 启动 Celery Worker 来消费任务
"""
import time
import threading
from funboost import boost, BrokerEnum, BoosterParams, ctrl_c_recv
from funboost.assist.celery_helper import CeleryHelper


# 定义任务 - 使用 Celery 作为 Broker
@boost(BoosterParams(
    queue_name='demo_celery_queue',
    broker_kind=BrokerEnum.CELERY,
    concurrent_num=3
))
def celery_task(task_id: int, data: str):
    """Celery Broker 任务"""
    time.sleep(0.5)
    print(f'[Celery任务执行] 任务 {task_id} 处理数据: {data}')
    return f'task_{task_id}_success'


@boost(BoosterParams(
    queue_name='demo_celery_rpc',
    broker_kind=BrokerEnum.CELERY,
    concurrent_num=3,
    is_using_rpc_mode=True
))
def celery_rpc_task(x: int, y: int):
    """Celery RPC 任务"""
    time.sleep(0.3)
    result = x + y
    print(f'[Celery RPC执行] {x} + {y} = {result}')
    return result


def start_celery_worker():
    """启动 Celery Worker 线程"""
    def worker_thread():
        print('启动 Celery Worker...')
        CeleryHelper.realy_start_celery_worker(
            worker_name='demo_worker',
            loglevel='INFO',
            worker_concurrency=4
        )
    
    t = threading.Thread(target=worker_thread, daemon=True)
    t.start()
    time.sleep(3)  # 等待 Worker 启动


if __name__ == '__main__':
    print('=' * 60)
    print('Funboost 使用 Celery 作为 Broker 完整示例')
    print('=' * 60)
    
    # 1. 启动 Celery Worker（在后台线程中）
    print('\n1. 启动 Celery Worker...')
    start_celery_worker()
    print('Celery Worker 已启动')
    
    # 2. 发布普通任务
    print('\n2. 发布普通任务...')
    for i in range(3):
        task_id = i + 1
        print(f'   发布任务 {task_id}...')
        celery_task.push(task_id, f'data_{task_id}')
    
    # 3. 发布 RPC 任务
    print('\n3. 发布 RPC 任务...')
    print('   发布 RPC 任务 (10 + 20)...')
    result = celery_rpc_task.push(10, 20)
    print(f'   等待 RPC 结果...')
    rpc_result = result.result
    print(f'   RPC 结果: 10 + 20 = {rpc_result}')
    
    print('\n' + '=' * 60)
    print('所有任务已发布')
    print('观察上方 Celery Worker 的执行日志')
    print('按 Ctrl+C 退出...')
    print('=' * 60)
    
    ctrl_c_recv()
