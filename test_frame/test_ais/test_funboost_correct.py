# -*- coding: utf-8 -*-
"""
Funboost 正确用法示例
严格按照教程推荐：使用 BoosterParams 类传递参数
"""
import time
from funboost import boost, BrokerEnum, BoosterParams, ctrl_c_recv, ConcurrentModeEnum
from funboost.timing_job.timing_push import ApsJobAdder
from funboost.workflow import chain


# 推荐用法：使用 BoosterParams 类传递参数
@boost(BoosterParams(
    queue_name='demo_correct_basic',
    broker_kind=BrokerEnum.REDIS,
    concurrent_num=5,
    log_level=10  # DEBUG
))
def basic_task(name: str, count: int):
    """基础任务"""
    time.sleep(0.5)
    print(f'[基础任务] {name} - 第 {count} 次执行')
    return f'{name}_done_{count}'


@boost(BoosterParams(
    queue_name='demo_correct_rpc',
    broker_kind=BrokerEnum.REDIS,
    concurrent_num=3,
    is_using_rpc_mode=True
))
def rpc_task(x: int, y: int):
    """RPC任务"""
    time.sleep(0.3)
    result = x * y
    print(f'[RPC任务] {x} * {y} = {result}')
    return result


@boost(BoosterParams(
    queue_name='demo_correct_qps',
    broker_kind=BrokerEnum.REDIS,
    concurrent_num=10,
    qps=2
))
def qps_task(data: str):
    """QPS控频任务"""
    print(f'[QPS控频] 处理数据: {data}, 时间: {time.strftime("%H:%M:%S")}')


@boost(BoosterParams(
    queue_name='demo_correct_workflow',
    broker_kind=BrokerEnum.REDIS,
    concurrent_num=3
))
def workflow_step(step_name: str, data: int = 0):
    """工作流步骤"""
    result = data + 10
    print(f'[工作流] {step_name}: 输入={data}, 输出={result}')
    return result


if __name__ == '__main__':
    print('\n' + '#' * 60)
    print('#  Funboost 正确用法示例')
    print('#  严格按照教程：使用 BoosterParams 类传递参数')
    print('#' * 60)
    
    # 启动消费者
    basic_task.consume()
    rpc_task.consume()
    qps_task.consume()
    workflow_step.consume()
    
    # 发布普通任务
    print('\n发布普通任务...')
    for i in range(3):
        basic_task.push(f'任务A', i + 1)
    
    # 发布RPC任务
    print('\n发布RPC任务...')
    result = rpc_task.push(10, 20)
    print(f'RPC结果: 10 * 20 = {result.result}')
    
    # 发布QPS控频任务
    print('\n发布QPS控频任务...')
    for i in range(5):
        qps_task.push(f'data_{i}')
    
    # 工作流
    print('\n发布工作流任务...')
    wf = chain(
        workflow_step.s('步骤1', 0),
        workflow_step.s('步骤2'),
        workflow_step.s('步骤3'),
    )
    wf.apply()
    
    # 定时任务
    print('\n添加定时任务...')
    ApsJobAdder(basic_task, job_store_kind='memory').add_push_job(
        trigger='interval',
        seconds=5,
        args=('定时任务', 999)
    )
    
    print('\n' + '=' * 50)
    print('所有任务已启动，按 Ctrl+C 退出...')
    print('=' * 50)
    ctrl_c_recv()
