# -*- coding: utf-8 -*-
"""
Funboost 使用 Celery 作为 Broker 的例子
正确理解：当使用 Celery 作为 Broker 时，
- funboost 只负责发布任务到 Celery 队列
- 实际的消费执行由 Celery Worker 负责
- 不需要启动 funboost 的消费者！
"""
import time
from funboost import boost, BrokerEnum, BoosterParams, ctrl_c_recv


# 推荐用法：使用 BoosterParams 类传递参数
@boost(BoosterParams(
    queue_name='demo_celery_broker',
    broker_kind=BrokerEnum.CELERY,
    concurrent_num=3
))
def celery_broker_task(task_id: int, data: str):
    """使用 Celery 作为 Broker 的任务"""
    time.sleep(0.5)
    print(f'[Celery Broker] 任务 {task_id} 处理数据: {data}')
    return f'task_{task_id}_success'


@boost(BoosterParams(
    queue_name='demo_celery_rpc',
    broker_kind=BrokerEnum.CELERY,
    concurrent_num=3,
    is_using_rpc_mode=True
))
def celery_rpc_task(x: int, y: int):
    """Celery RPC 模式任务"""
    time.sleep(0.3)
    result = x + y
    print(f'[Celery RPC] {x} + {y} = {result}')
    return result


if __name__ == '__main__':
    print('=' * 50)
    print('Funboost 使用 Celery 作为 Broker 演示')
    print('=' * 50)
    print('重要说明：')
    print('- funboost 只负责发布任务到 Celery 队列')
    print('- 实际的消费执行由 Celery Worker 负责')
    print('- 请先启动 Celery Worker！')
    print('=' * 50)
    
    # 注意：当使用 Celery 作为 Broker 时，不需要启动 funboost 的消费者！
    # funboost 只负责将任务发布到 Celery 队列，由 Celery Worker 执行
    
    # 发布普通任务
    print('\n发布普通任务...')
    for i in range(3):
        task_id = i + 1
        print(f'发布任务 {task_id}...')
        celery_broker_task.push(task_id, f'data_{task_id}')
    
    # 发布 RPC 任务
    print('\n发布 RPC 任务...')
    print('发布 RPC 任务 (10 + 20)...')
    result = celery_rpc_task.push(10, 20)
    print(f'等待 RPC 结果...')
    rpc_result = result.result
    print(f'RPC 结果: 10 + 20 = {rpc_result}')
    
    print('\n' + '=' * 50)
    print('任务已发布到 Celery 队列')
    print('请查看 Celery Worker 控制台的执行情况')
    print('按 Ctrl+C 退出...')
    print('=' * 50)
    ctrl_c_recv()
