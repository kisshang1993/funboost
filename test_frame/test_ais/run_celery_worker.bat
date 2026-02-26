@echo off
echo 启动 Celery Worker...
cd /d d:\codes\funboost\test_frame\test_ais
celery -A celery_config worker --loglevel=info --concurrency=4
echo Celery Worker 已停止
pause