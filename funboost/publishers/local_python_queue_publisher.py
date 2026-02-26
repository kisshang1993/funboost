# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2022/8/8 0008 13:07
from collections import deque
from concurrent.futures import Future
from queue import Queue, SimpleQueue

from funboost.publishers.base_publisher import AbstractPublisher
from funboost.queues.memory_queues_map import PythonQueues

local_pyhton_queue_name__local_pyhton_queue_obj_map = dict()  # 使local queue和其他中间件完全一样的使用方式，使用映射保存队列的名字，使消费和发布通过队列名字能找到队列对象。


class LocalPythonQueuePublisher(AbstractPublisher):
    """
    使用python内置queue对象作为中间件。方便测试，每个中间件的消费者类是鸭子类，多态可以互相替换。
    """

    # noinspection PyAttributeOutsideInit

    @property
    def local_python_queue(self) -> Queue:
        maxsize = self.publisher_params.broker_exclusive_config['maxsize']
        return PythonQueues.get_queue(self._queue_name, maxsize=maxsize)

    def _publish_impl(self, msg):
        # noinspection PyTypeChecker
        pass
        self.local_python_queue.put(msg)

    def call(self, *func_args, **func_kwargs) -> Future:
        """
        内存队列专用的同步调用方法，发布消息并返回 concurrent.futures.Future 对象，不依赖 Redis 作为 RPC。
        
        利用内存队列不序列化的特性，直接把 Future 对象塞进消息体的 extra 中随消息一起流转，
        消费端执行完函数后，将 FunctionResultStatus 通过 future.set_result() 设置回来。
        完全零外部依赖，纯进程内通信。

        用法:
            future = task_fun.publisher.call(1, y=2)
            function_result_status = future.result(timeout=10)   # 阻塞等待结果
            print(function_result_status.result)    # 获取函数返回值
            print(function_result_status.success)   # 是否成功

        或者通过 booster 的 call 方法:
            future = task_fun.call(1, y=2)
        """
        future = Future()
        # 构造 msg_dict
        msg_dict = dict(func_kwargs)
        for index, arg in enumerate(func_args):
            msg_dict[self.publish_params_checker.all_arg_name_list[index]] = arg
        # 将 Future 对象直接放入消息的 extra 中，内存队列不序列化，Future 对象可以直接传递
        msg_dict['extra'] = {'_memory_call_future': future}
        self.publish(msg_dict)
        return future

    def clear(self):
        # noinspection PyUnresolvedReferences
        self.local_python_queue.queue.clear()
        self.logger.warning(f'清除 本地队列中的消息成功')

    def get_message_count(self):
        return self.local_python_queue.qsize()

    def close(self):
        pass


class LocalPythonQueuePublisherSimpleQueue(AbstractPublisher):
    """
    使用python内置SimpleQueue对象作为中间件。方便测试，每个中间件的消费者类是鸭子类，多态可以互相替换。
    """

    # noinspection PyAttributeOutsideInit
    def custom_init(self):
        if self._queue_name not in local_pyhton_queue_name__local_pyhton_queue_obj_map:
            local_pyhton_queue_name__local_pyhton_queue_obj_map[self._queue_name] = SimpleQueue()
        self.queue = local_pyhton_queue_name__local_pyhton_queue_obj_map[self._queue_name]  # type: SimpleQueue

    def _publish_impl(self, msg):
        # noinspection PyTypeChecker
        self.queue.put(msg)

    def clear(self):
        pass
        # noinspection PyUnresolvedReferences
        # self.queue._queue.clear()
        # self.logger.warning(f'清除 本地队列中的消息成功')

    def get_message_count(self):
        return self.queue.qsize()

    def close(self):
        pass


class LocalPythonQueuePublisherDeque(AbstractPublisher):
    """
    使用python内置 Dequeu 对象作为中间件。方便测试，每个中间件的消费者类是鸭子类，多态可以互相替换。
    """

    # noinspection PyAttributeOutsideInit
    def custom_init(self):
        if self._queue_name not in local_pyhton_queue_name__local_pyhton_queue_obj_map:
            local_pyhton_queue_name__local_pyhton_queue_obj_map[self._queue_name] = deque()
        self.queue = local_pyhton_queue_name__local_pyhton_queue_obj_map[self._queue_name]  # type: deque
        # deque.get = deque.pop
        # # setattr(self.queue,'get',self.queue.pop)

    def _publish_impl(self, msg):
        # noinspection PyTypeChecker
        print(msg)
        self.queue.append(msg)

    def clear(self):
        pass
        # noinspection PyUnresolvedReferences
        self.queue.clear()
        self.logger.warning(f'清除 本地队列中的消息成功')

    def get_message_count(self):
        return len(self.queue)

    def close(self):
        pass
