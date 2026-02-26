# -*- coding: utf-8 -*-
"""Celery 配置文件"""
from celery import Celery
import os

# 设置 Celery 环境变量
os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

# 创建 Celery 实例
celery_app = Celery('demo_celery_app')

# 配置 Celery
celery_app.conf.update(
    broker_url='redis://localhost:6379/0',  # 使用 Redis 作为 Broker
    result_backend='redis://localhost:6379/0',  # 使用 Redis 存储结果
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Asia/Shanghai',
    enable_utc=True,
)

# 注册任务
celery_app.autodiscover_tasks(['test_celery_broker'])

if __name__ == '__main__':
    celery_app.start()
