# boost1.python万能分布式函数调度框架简funboost简介

<pre style="color: greenyellow;background-color: #0c1119; font-size: medium;">
pip install funboost ,python全功能分布式函数调度框架。  demo用法例子见文档1.3

funboost的功能是全面性重量级，用户能想得到的功能99%全都有;funboost的使用方式是轻量级，只有@boost一行代码需要写。
funboost的神奇之处在于它同时拥有"轻量级使用方式"和"重量级功能集"，完全颠覆了"功能强大=使用复杂"的传统思维。
它证明了一个框架可以既功能丰富又极其易用，这是对传统Python框架设计的一次巧妙超越。

只需要一行@boost代码即可分布式执行python一切任意函数，99%用过funboost的pythoner 感受是 方便 快速 强大。
支持python所有类型的并发模式,消息队列方面支持全球一切知名消息队列中间件和模拟的实现消息队列，
同时funboost支持celery整个框架作为核心来发布和消费消息，使用funboost的极简api方式来自动化配置和利用celery调度,
也支持huey dramatiq rq等任务队列框架作为funboost的broker。 

python函数加速器，框架包罗万象，一统编程思维，兼容50% python编程业务场景，适用范围广。
python万能分布式函数调度框架，支持5种并发模式，30+种消息队列中间件
(不仅支持几乎所有你能想到的消息队列中间件，还支持本地磁盘队列、数据库队列 (SQLAlchemy, Peewee)、
内存队列、甚至是 HTTP 请求、WebSocket 等作为任务队列，甚至是将 Celery、Dramatiq、Huey 等其他框架整体作为其
Broker。funboost源码高扩展性的设计，造成“万物皆可为Broker”,并不是有30种传统意义上的经典消息队列，
因为世界上总共都没有30种知名的经典消息队列)，
30种任务控制功能。给任意python函数赋能。
用途概念就是常规经典的 生产者 + 消息队列中间件 + 消费者 编程思想。

框架只需要学习@boost这一个装饰器的入参就可以，所有用法几乎和1.3例子一摸一样，非常简化简单。
框架对代码没有入侵,可以加到任意已有项目而对项目python文件目录结构0要求,
不像 celery django scrapy 这样的框架,要从一开始就开始规划好项目目录结构,如果不想用框架了,
或者想改变使用其他框架框架,那么已经所写的代码组织形式就几乎成了废物,需要大改特改. 
但是funboost完全不会这样,不管是加上还是去掉@boost装饰器,对你的项目影响为0,用户照常使用,
所以用户可以对任意项目,任意时候,引入使用funboost或者去掉使用funboost,代码组织形式不需要发生变化.
（即使不想用funboost了，也不需要亲自去掉@boost装饰器，因为函数上面有@boost装饰器对函数自身的直接调用运行没有任何影响，
用户照样可以直接例如 fun(x,y)是直接运行函数 ， fun.push(x,y) 才是发送到消息队列）

通过funboost web manager 管理系统，支持全面 查看 监控 管理 funboost的任务消费。
</pre>

### 框架评价

```
95%的用户在初步使用后，都表示赞不绝口、相见恨晚、两眼放光。认为funboost框架使用简单但功能强大和丰富。

第一次听说此框架的，100%用户会质疑框架性能不行，功能少，表示学习celery的教程文档上的所有功能
已近非常费劲头疼折磨，各种报错不知道如何解决。
一般python用户听到一个新的python框架，脚都软了，学习类似django celery scrapy意味着要学习
几个月文档才只能掌握框架的一小部分用法了，
尤其是celery这种框架，代码在pycharm完全不能自动补全提示，用户连@task装饰的函数有什么方法，
每个方法有什么入参都不知道，配置文件能写哪些配置都不知道，如果不按照博客上的celery目录结构写celery任务
，连celery命令行运行起来都要反复猜测尝试。
正因为如此用户从心理已近十分惧怕学习一种叫python框架的东西了，用户顶多愿意学习一个python包或者模块，
学习一个框架会非常害怕觉得难度高且耗时，所以非常反感尝试新的框架。
用过的99%都说funboost比celery简单方便太多,看都不看的人第一秒就是开始质疑重复造轮子.

funboost只有一个@boost装饰器，@boost入参能自动补全，更重要的是被@boost装饰的函数，
有哪些方法，每个方法入参是什么都能自动补全。funboost的中间件配置文件自当生成在用户当前项目根目录，
用户无需到处找文档，能配置什么东西，框架功能怎么配置。
因为funboost非常注重代码补全提示，所以不存在上面celery的那些复杂高难度缺点。
```

funboost的旧框架名字是function_scheduling_distributed_framework , 关系和兼容性见1.0.3介绍。
旧框架地址： [https://github.com/ydf0509/distributed_framework](https://github.com/ydf0509/distributed_framework)

## 1.0 github地址和文档地址

### 1.0.1 [分布式函数调度框架文档地址 ](https://funboost.readthedocs.io/zh-cn/latest/index.html)

[查看分布式函数调度框架文档 https://funboost.readthedocs.io/zh-cn/latest/index.html](https://funboost.readthedocs.io/zh-cn/latest/index.html)

文档很长，大部分都是讲原理和对比各种框架。但是用户只需要学习1.3这1个例子就能掌握了。因为其他例子只是 @boost的 BoosterParams 里面的控制入参换了一下。

用户只需要专门看 BoosterParams 里面的每个入参的注释就能掌握框架了，因为funboost只有@boost一行代码需要你写。

funboost 框架和一般的框架不一样，因为只有一行代码需要掌握，绝对不是要求用户先精通框架本身才能自由发挥。

#### [1.python万能分布式函数调度框架简funboost简介](https://funboost.readthedocs.io/zh-cn/latest/articles/c1.html)

#### [2. funboost对比celery框架](https://funboost.readthedocs.io/zh-cn/latest/articles/c2.html)

#### [3.funboost框架详细介绍](https://funboost.readthedocs.io/zh-cn/latest/articles/c3.html)

#### [4.funboost使用框架的各种代码示例](https://funboost.readthedocs.io/zh-cn/latest/articles/c4.html)

#### [4b.funboost使用框架的各种代码示例(高级进阶)](https://funboost.readthedocs.io/zh-cn/latest/articles/c4b.html)

#### [5.funboost框架运行时截图](https://funboost.readthedocs.io/zh-cn/latest/articles/c5.html)

#### [6.funboost常见问题回答](https://funboost.readthedocs.io/zh-cn/latest/articles/c6.html)

#### [7.funboost更新记录](https://funboost.readthedocs.io/zh-cn/latest/articles/c7.html)

#### [8.funboost是万能函数调度框架，当然可以爬虫,自由编程 降维打击 框架奴役](https://funboost.readthedocs.io/zh-cn/latest/articles/c8.html)

#### [9.轻松远程服务器部署运行函数](https://funboost.readthedocs.io/zh-cn/latest/articles/c9.html#)

#### [10.python3.6-3.12 安装/使用funboost出错问题反馈](https://funboost.readthedocs.io/zh-cn/latest/articles/c10.html)

#### [11.funboost 使用某些中间件或三方任务队列框架作为broker的例子(包括celery框架)。](https://funboost.readthedocs.io/zh-cn/latest/articles/c11.html)

#### [12.funboost 控制台支持命令行](https://funboost.readthedocs.io/zh-cn/latest/articles/c12.html)

#### [13.启动 funboost web manager,查看消费结果和队列管理](https://funboost.readthedocs.io/zh-cn/latest/articles/c13.html)

#### [funboost依赖的nb_log日志文档 https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id2](https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id2)

```
文档很长，但归根结底只需要学习 1.3 里面的这1个例子就行，主要是修改下@boost的各种参数，
通过不同的入参，实践测试下各种控制功能。
其中文档第四章列举了所有用法举例，

对比 celery 有20种改善，其中之一是无依赖文件夹层级和文件夹名字 文件名字。
首先能把  https://github.com/ydf0509/celery_demo
这个例子的已经写好的不规则目录层级和文件名字的函数用celery框架玩起来，才能说是了解celery，
否则如果项目文件夹层级和文件名字不规矩，后期再用celery，会把celery新手折磨得想死，
很多新手需要小心翼翼模仿网上说的项目目录结构，以为不按照那么规划目录和命名就玩不起来，本身说明celery很坑。
```

### 1.0.2 [分布式函数调度框架github地址](https://github.com/ydf0509/funboost)

[查看分布式函数调度框架github项目](https://github.com/ydf0509/funboost)

### 1.0.3 funboost 框架 和 function_scheduling_distributed_framework 框架 关系说明

```
funboost 是 function_scheduling_distributed_framework的包名更新版本
```

`<span style="font-size:15px">`旧框架地址：`<span><a href="https://github.com/ydf0509/distributed_framework" style="font-size: 15px">`function_scheduling_distributed_framework框架地址链接 `</a>`

## 1.1 安装方式

```
pip install funboost --upgrade

或pip install funboost[all]  一次性安装所有小众三方中间件
```

## 1.2 框架功能介绍

分布式函数调度框架，支持5种并发模式，30+种消息中间件，30种任务控制功能。`<br>`
用途概念就是常规经典的 生产者 + 消息队列中间件 + 消费者 编程思想。

有了这个框架，用户再也无需亲自手写操作进程、线程、协程的并发的代码了。

有了这个框架，用户再也无需亲自手写操作redis rabbitmq socket kafka celery nameko了。

funboost示图：
`<a href="https://imgse.com/i/pkFFghj"><img src="https://s21.ax1x.com/2024/04/29/pkFFghj.png" alt="pkFFghj.png" border="0" />``</a>`

也就是这种非常普通的流程图,一样的意思

`<a href="https://imgse.com/i/pkFFcNQ"><img src="https://s21.ax1x.com/2024/04/29/pkFFcNQ.png" alt="pkFFcNQ.png" border="0" />``</a>`

### 1.2.1 框架支持5种并发模式

<div   style=" font-size: xx-large; font-family: 黑体,serif; "> threading  <span style="font-size: medium">(使用的是可变线程池，可以智能自动缩小和扩大线程数量,也可以运行async def的函数) </span> </div>

<div   style=" font-size: xx-large; font-family: 黑体,serif; "> gevent </div>

<div   style="font-size: xx-large; font-family: 黑体,serif; "> eventlet </div>

<div   style="font-size: xx-large; font-family: 黑体,serif; "> asyncio <span style="font-size: medium">(框架可以直接支持async 定义的携程函数作为任务,celery不支持) </span> </div>

<div   style=" font-size: xx-large; font-family: 黑体,serif; "> single_thread </div>

<br>
<div style=" font-size: 18px; font-family: 黑体,serif; ">除此之外，直接内置方便的支持 多进程multiprocess 叠加 以上5种并发，多进程和以上细粒度并发是叠加的而不是平行的二选一关系。</div>
<br><br>

```
总结一下那就是此框架可以适应所有编程场景，无论是io密集 cpu密集 还是cpu io双密集场景，框架能非常简便的应对任意场景。
框架的 单线程  多线程  gevent eventlet  asyncio 多进程  这些并发模型，囊括了目前python界所有的并发方式。
框架能自动实现 单线程  ，多线程， gevent ， eventlet ，asyncio ，多进程 并发 ，
多进程 + 单线程 ，多进程 + 多线程，多进程 + gevent,  多进程 + eventlet  ，多进程 + asyncio 的组合并发
这么多并发方式能够满足任意编程场景。
```

以下两种方式，都是10线程加python内存queue方式运行f函数，有了此框架，用户无需代码手写手动操作线程 协程 asyncio 进程 来并发。

1)手动开启线程池方式

```python
import time
from concurrent.futures import ThreadPoolExecutor


def f(x):
    time.sleep(3)
    print(x)


pool = ThreadPoolExecutor(10)

if __name__ == '__main__':
    for i in range(100):
        pool.submit(f, i)

```

2)funboost 使用内存队列,设置10线程并发

```python
import time
from funboost import BoosterParams, BrokerEnum


@BoosterParams(queue_name="test_insteda_thread_queue", broker_kind=BrokerEnum.MEMORY_QUEUE, concurrent_num=10, is_auto_start_consuming_message=True)
def f(x):
    time.sleep(3)
    print(x)


if __name__ == '__main__':
    for i in range(100):
        f.push(i)


```

### 1.2.2 框架支持30种中间件或三方框架

框架支持 rabbitmq redis python自带的queue.Queue  sqlite sqlachemy kafka pulsar mongodb 直接socket celery  nameko 等作为消息中间件。

同时此框架也支持操作 kombu 库作为中间件,所以此框架能够支持的中间件类型只会比celery更多。

框架支持的中间件种类大全和选型见文档3.1章节的介绍:

[3.1 各种中间件选择的场景和优势](https://funboost.readthedocs.io/zh-cn/latest/articles/c3.html#id2)

### 1.2.3 框架对任务支持30种控制功能。

<pre>

python通用分布式函数调度框架。适用场景范围广泛， 框架非常适合io密集型(框架支持对函数自动使用 thread gevent eventlet asyncio 并发)
框架非常适合cpu密集型(框架能够在线程 协程基础上 叠加 多进程 multi_process 并发 ，不仅能够多进程执行任务还能多机器执行任务)。
不管是函数需要消耗时io还是消耗cpu，用此框架都很合适，因为任务都是在中间件里面，可以自动分布式分发执行。 此框架是函数的辅助控制倍增器。

框架不适合的场景是 函数极其简单，例如函数只是一行简单的 print hello，函数只需要非常小的cpu和耗时，运行一次函数只消耗了几十hz或者几纳秒，
此时那就采用直接调用函数就好了，因为框架施加了很多控制功能，当框架的运行逻辑耗时耗cpu 远大于函数本身 时候，使用框架反而会使函数执行变慢。

（python框架从全局概念上影响程序的代码组织和运行，包和模块是局部的只影响1个代码文件的几行。）

可以一行代码分布式并发调度起一切任何老代码的旧函数和新项目的新函数，并提供数十种函数控制功能。

还是不懂框架能做什么是什么，就必须先去了解下celery rq。如果连celery rq类似这种的用途概念听都没听说， 那就不可能知道框架的概念和功能用途。

</pre>

20种控制功能包括：

<pre style="color: #A0A000">
     分布式：
        支持数十种最负盛名的消息中间件.(除了常规mq，还包括用不同形式的如 数据库 磁盘文件 redis等来模拟消息队列)

     并发：
        支持threading gevent eventlet asyncio 单线程 5种并发模式 叠加 多进程。
        多进程不是和前面四种模式平行的，是叠加的，例如可以是 多进程 + 协程，多进程 + 多线程。
   
     控频限流：
        例如十分精确的指定1秒钟运行30次函数或者0.02次函数（无论函数需要随机运行多久时间，都能精确控制到指定的消费频率；
   
     分布式控频限流：
        例如一个脚本反复启动多次或者多台机器多个容器在运行，如果要严格控制总的qps，能够支持分布式控频限流。
  
     任务持久化：
        消息队列中间件天然支持
   
     断点接续运行：
        无惧反复重启代码，造成任务丢失。消息队列的持久化 + 消费确认机制 做到不丢失一个消息
        (此框架很重视消息的万无一失，就是执行函数的机器支持在任何时候随时肆无忌惮反复粗暴拉电闸断电，或者强制硬关机，
        或者直接用锄头把执行函数代码的机器砸掉，只要不是暴力破坏安装了消息队列中间件的机器就行，消息就万无一失，
        现在很多人做的简单redis list消息队列，以为就叫做分布式断点接续，那是不正确的，因为这种如果把消息从reidis brpop取出来后，
        如果消息正在被执行，粗暴的kill -9脚本或者直接强制关机，那么正在运行的消息就丢失了，如果是多线程同时并发运行很多消息，粗暴重启
        会丢失几百个大量消息，这种简单的redis list根本就不能叫做安全的断点续传。
        分布式函数调度框架的消费确认机制，保证函数运行完了才确认消费，正在运行突然强制关闭进程不会丢失一个消息，
        下次启动还会消费或者被别的机器消费。
        此框架的消息万无一失特性，不仅支持rabbbitmq因为原生支持，也支持redis，框架对redis的实现机制是因为客户端加了一层保障)。
   
     定时：
        可以按时间间隔、按指定时间执行一次、按指定时间执行多次，使用的是apscheduler包的方式。
   
     延时任务：
         例如规定任务发布后，延迟60秒执行，或者规定18点执行。这个概念和定时任务有一些不同。
    
     指定时间不运行：
        例如，有些任务你不想在白天运行，可以只在晚上的时间段运行
   
     消费确认：
        这是最为重要的一项功能之一，有了这才能肆无忌惮的任性反复重启代码也不会丢失一个任务。
        （常规的手写 redis.lpush + redis.blpop,然后并发的运行取出来的消息，随意关闭重启代码瞬间会丢失大量任务，
        那种有限的 断点接续 完全不可靠，根本不敢随意重启代码）
   
     立即重试指定次数：
        当函数运行出错，会立即重试指定的次数，达到最大次重试数后就确认消费了
   
     重新入队：
        在消费函数内部主动抛出一个特定类型的异常ExceptionForRequeue后，消息重新返回消息队列
   
     超时杀死：
        例如在函数运行时间超过10秒时候，将此运行中的函数kill
   
     计算消费次数速度：
        实时计算单个进程1分钟的消费次数，在日志中显示；当开启函数状态持久化后可在web页面查看消费次数
   
     预估消费时间：
        根据前1分钟的消费次数，按照队列剩余的消息数量来估算剩余的所需时间
   
     函数运行日志记录：
        使用自己设计开发的 控制台五彩日志（根据日志严重级别显示成五种颜色；使用了可跳转点击日志模板）
        + 多进程安全切片的文件日志 + 可选的kafka elastic日志
         
     任务过滤：
        例如求和的add函数，已经计算了1 + 2,再次发布1 + 2的任务到消息中间件，可以让框架跳过执行此任务。
        任务过滤的原理是使用的是函数入参判断是否是已近执行过来进行过滤。
   
     任务过滤有效期缓存：
        例如查询深圳明天的天气，可以设置任务过滤缓存30分钟，30分钟内查询过深圳的天气，则不再查询。
        30分钟以外无论是否查询过深圳明天的天气，则执行查询。
  
     任务过期丢弃：
        例如消息是15秒之前发布的，可以让框架丢弃此消息不执行，防止消息堆积,
        在消息可靠性要求不高但实时性要求高的高并发互联网接口中使用
      
     函数状态和结果持久化：
        可以分别选择函数状态和函数结果持久化到mongodb，使用的是短时间内的离散mongo任务自动聚合成批量
        任务后批量插入，尽可能的减少了插入次数
            
     消费状态实时可视化：
        在页面上按时间倒序实时刷新函数消费状态，包括是否成功 出错的异常类型和异常提示 
        重试运行次数 执行函数的机器名字+进程id+python脚本名字 函数入参 函数结果 函数运行消耗时间等
           
     消费次数和速度生成统计表可视化：
        生成echarts统计图，主要是统计最近60秒每秒的消费次数、最近60分钟每分钟的消费次数
        最近24小时每小时的消费次数、最近10天每天的消费次数
                      
     rpc：
        生产端（或叫发布端）获取消费结果。各个发布端对消费结果进行不同步骤的后续处理更灵活，而不是让消费端对消息的处理一干到底。

     远程服务器部署消费函数：
        代码里面 task_fun.fabric_deploy('192.168.6.133', 22, 'xiaomin', '123456', process_num=2) 只需要这样就可以自动将函数部署在远程机器运行，
        无需任何额外操作，不需要借助阿里云codepipeline发版工具 和 任何运维发版管理工具，就能轻松将函数运行在多台远程机器。task_fun指的是被@boost装饰的函数

     暂停消费：
        支持从python解释器外部/远程机器 ，控制暂停消息消费和继续消费。

     优先级队列：
         支持队列优先级消息。

     远程杀死(取消)任务：
         支持在发布端杀死正在运行的消息，发送杀死命令时候对还未取出的消息则放弃运行消息。
  
     funboost支持命令行操作：
         使用fire实现的命令行，见文档第12章

     可视化查看和操作：
         funboost web manager 可以查看和管理队列和消费运行情况。

</pre>

关于稳定性和性能，一句话概括就是直面百万c端用户（包括app和小程序）， 已经连续超过三个季度稳定高效运行无事故，从没有出现过假死、崩溃、内存泄漏等问题。 windows和linux行为100%一致，不会像celery一样，相同代码前提下，很多功能在win上不能运行或出错。

## 1.3 框架使用例子

使用之前先学习 PYTHONPATH的概念  [https://github.com/ydf0509/pythonpathdemo](https://github.com/ydf0509/pythonpathdemo)

win cmd和linux 运行时候，设置 PYTHONPATH 为项目根目录，是为了自动生成或读取到项目根目录下的 funboost_config.py文件作为配置。

```
以下这只是简单求和例子，实际情况换成任意函数里面写任意逻辑，框架可没有规定只能用于 求和函数 的自动调度并发。
而是根据实际情况函数的参数个数、函数的内部逻辑功能，全部都由用户自定义，函数里面想写什么就写什么，想干什么就干什么，极端自由。
也就是框架很容易学和使用，把下面的task_fun函数的入参和内部逻辑换成你自己想写的函数功能就可以了，框架只需要学习boost这一个函数的参数就行。
测试使用的时候函数里面加上sleep模拟阻塞，从而更好的了解框架的并发和各种控制功能。

有一点要说明的是框架的消息中间件的ip 端口 密码 等配置是在你第一次运行代码时候，在你当前项目的根目录下生成的 funboost_config.py 按需设置。
```

### 1.3.1 funboost最简单例子

```python
import time
from funboost import boost, BrokerEnum,BoosterParams

# BoosterParams 代码自动补全请看文档4.1.3
@boost(BoosterParams(queue_name="task_queue_name1", qps=5, broker_kind=BrokerEnum.SQLITE_QUEUE))  # 入参包括20种，运行控制方式非常多，想得到的控制都会有。
def task_fun(x, y):
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 5 次 这个 task_fun 函数的目的。


if __name__ == "__main__":
    for i in range(100):
        task_fun.push(i, y=i * 2)  # 发布者发布任务
    task_fun.consume()  # 消费者启动循环调度并发消费任务
```

<pre style="background-color: #BA2121;color: yellow">tips: sqlite作为消息队列,如果linux或mac运行报错read-only文件夹权限,需修改SQLLITE_QUEUES_PATH 就好啦,见文档10.3 </pre>

```text
"""
对于消费函数，框架内部会生成发布者(生产者)和消费者。
1.推送。 task_fun.push(1,y=2) 会把 {"x":1,"y":2} (消息也自动包含一些其他辅助信息) 发送到中间件的 task_queue_name1 队列中。
2.消费。 task_fun.consume() 开始自动从中间件拉取消息，并发的调度运行函数，task_fun(**{"x":1,"y":2}),每秒运行5次
整个过程只有这两步，清晰明了，其他的控制方式需要看 boost 的中文入参解释，全都参数都很有用。


这个是单个脚本实现了发布和消费，一般都是分离成两个文件的，任务发布和任务消费无需在同一个进程的解释器内部，
因为是使用了中间件解耦消息和持久化消息，不要被例子误导成了，以为发布和消费必须放在同一个脚本里面


框架使用方式基本上只需要练习这一个例子就行了，其他举得例子只是改了下broker_kind和其他参数而已，
而且装饰器的入参已近解释得非常详细了，框架浓缩到了一个装饰器，并没有用户需要从框架里面要继承什么组合什么的复杂写法。
用户可以修改此函数的sleep大小和@boost的数十种入参来学习 验证 测试框架的功能。
"""
```

控制台运行截图:

`<a href="https://imgse.com/i/pkFkP4H"><img src="https://s21.ax1x.com/2024/04/29/pkFkP4H.png" alt="pkFkP4H.png" border="0" />``</a>`

`<a href="https://imgse.com/i/pkFkCUe"><img src="https://s21.ax1x.com/2024/04/29/pkFkCUe.png" alt="pkFkCUe.png" border="0" />``</a>`

### 1.3.2 funboost集中演示一个功能更多的综合例子

```python


"""
一个展示更全面 funboost 用法的例子
包含了
1.继承BoosterParams，为了每个装饰器少写入参
2.rpc获取结果
3.连续丝滑启动多个消费函数
4.定时任务
"""
from funboost import boost, BrokerEnum,BoosterParams,ctrl_c_recv,ConcurrentModeEnum,ApsJobAdder
import time

class MyBoosterParams(BoosterParams):  # 自定义的参数类，继承BoosterParams，用于减少每个消费函数装饰器的重复相同入参个数
    broker_kind: str = BrokerEnum.REDIS_ACK_ABLE
    max_retry_times: int = 3
    concurrent_mode: str = ConcurrentModeEnum.THREADING 

  
@boost(MyBoosterParams(queue_name='s1_queue', qps=1, 
                    #    do_task_filtering=True, # 可开启任务过滤，防止重复入参消费。
                       is_using_rpc_mode=True, # 开启rpc模式，支持rpc获取结果
                       ))
def step1(a:int,b:int):
    print(f'a={a},b={b}')
    time.sleep(0.7)
    for j in range(10):
        step2.push(c=a+b +j,d=a*b +j,e=a-b +j ) # step1消费函数里面，也可以继续向其他任意队列发布消息。
    return a+b


@boost(MyBoosterParams(queue_name='s2_queue', qps=3, 
                      max_retry_times=5,# 可以在此覆盖MyBoosterParams中的默认值，例如为step2单独设置最大重试次数为5
)) 
def step2(c:int,d:int,e:int=666):
    time.sleep(3)
    print(f'c={c},d={d},e={e}')
    return c* d * e


if __name__ == '__main__':
    step1.clear() # 清空队列
    step2.clear() # 清空队列

    step1.consume() # 调用.consume是非阻塞的启动消费，是在单独的子线程中循环拉取消息的。 
    # 有的人还担心阻塞而手动使用 threading.Thread(target=step1.consume).start() 来启动消费，这是完全多此一举的错误写法。
    step2.consume() # 所以可以在当前主线程连续无阻塞丝滑的启动多个函数消费。
    step2.multi_process_consume(3) # 这是多进程叠加了多线程消费，另外开启了3个进程，叠加了默认的线程并发。

    async_result = step1.push(100,b=200)
    print('step1的rpc结果是：',async_result.result)  # rpc阻塞等待消step1的费结果返回

    for i in range(100):
        step1.push(i,i*2) # 向 step1函数的队列发送消息,入参和手动调用函数那样很相似。
        step1.publish ({'a':i,'b':i*2},task_id=f'task_{i}') # publish 第一个入参是字典，比push能传递更多funboost的辅助参数，类似celery的apply_async和delay的关系。一个简单，一个复杂但强大。
  
  

    """
    1.funboost 使用 ApsJobAdder.add_push_job来添加定时任务，不是add_job。
    2.funboost是轻度封装的知名apscheduler框架，所以定时任务的语法和apscheduler是一样的，没有自己发明语法和入参
    用户需要苦学apscheduler教程，一切定时都是要学apscheduler知识，定时和funboost知识关系很小。
    3.funboost的定时任务目的是定时推送消息到消息队列中，而不是定时直接在当前程序中执行某个消费函数。

    下面是三种方式添加定时任务，这些定时方式都是知名apscheduler包的定时方式，和funboost没关系。
    """

   # ApsJobAdder 类可以多次重复实例化,内部对每一个消费函数使用一个单独的apscheduler对象,避免扫描与当前关心的消费函数不相干的redis jobstore中的定时任务

   # 方式1：指定日期执行一次
    ApsJobAdder(step2, 
               job_store_kind='redis', # 使用reids作为 apscheduler的 jobstrores
               is_auto_start=True,   # 添加任务，并同时顺便启动了定时器 执行了apscheduler对象.start()
    ).add_push_job(
        trigger='date',
        run_date='2025-06-30 16:25:40',
        args=(7, 8,9),
        id='date_job1',
        replace_existing=True,
    )

    # 方式2：固定间隔执行
    ApsJobAdder(step2, job_store_kind='redis').add_push_job(
        trigger='interval',
        seconds=30,
        args=(4, 6,10),
        id='interval_job1',
        replace_existing=True,
    )

    # 方式3：使用cron表达式定时执行
    ApsJobAdder(step2, job_store_kind='redis').add_push_job(
        trigger='cron',
        day_of_week='*',
        hour=23,
        minute=49,
        second=50,
        kwargs={"c": 50, "d": 60,"e":70},
        replace_existing=True,
        id='cron_job1')
  
    ctrl_c_recv()  # 用于阻塞代码，阻止主线程退出，使主线程永久运行。  相当于 你在代码最末尾，加了个 while 1:time.sleep(10)，使主线程永不结束。apscheduler background定时器守护线程需要这样保持定时器不退出。

```

### 1.3.3  funboost的 @BoosterParams(...)  和 @boost(BoosterParams(...)) 等效

通常代码例子是:

```python
@boost(BoosterParams(queue_name="task_queue_consume_any_msg"))
def task_fun(a: int, b: int):
    print(f'a:{a},b:{b}')
    return a + b
```

但如果你追求极致简化,也可以写成如下,不要@boost,直接@BoosterParams

```python
@BoosterParams(queue_name="task_queue_consume_any_msg")
def task_fun(a: int, b: int):
    print(f'a:{a},b:{b}')
    return a + b
```

## funboost web manager 截图：

函数消费结果：可查看和搜索函数实时消费状态和结果
[![pEJCffK.png](https://s21.ax1x.com/2025/03/04/pEJCffK.png)](https://imgse.com/i/pEJCffK)

消费速度图：可查看实时和历史消费速度
[![pEJCWY6.png](https://s21.ax1x.com/2025/03/04/pEJCWY6.png)](https://imgse.com/i/pEJCWY6)

运行中消费者 by ip： 根据ip搜索有哪些消费者
[![pEJCRFx.png](https://s21.ax1x.com/2025/03/04/pEJCRFx.png)](https://imgse.com/i/pEJCRFx)

队列操作：查看和操作队列，包括 清空清空 暂停消费 恢复消费 调整qps和并发

<!-- [![pEJC6m9.png](https://s21.ax1x.com/2025/03/04/pEJC6m9.png)](https://imgse.com/i/pEJC6m9) -->

[![pVSOJcq.png](https://s21.ax1x.com/2025/05/27/pVSOJcq.png)](https://imgse.com/i/pVSOJcq)

队列操作，查看消费者详情：查看队列的所有消费者详情
[![pEJCgT1.png](https://s21.ax1x.com/2025/03/04/pEJCgT1.png)](https://imgse.com/i/pEJCgT1)

队列操作:查看消费曲线图，查看各种消费指标。
[![pVpr7sP.png](https://s21.ax1x.com/2025/05/29/pVpr7sP.png)](https://imgse.com/i/pVpr7sP)

rpc调用：在网页上对30种消息队列发布消息并获取消息的函数执行结；根据taskid获取结果。

<!-- [![pETq8hj.png](https://s21.ax1x.com/2025/04/28/pETq8hj.png)](https://imgse.com/i/pETq8hj) -->

[![pE7y8oT.png](https://s21.ax1x.com/2025/04/29/pE7y8oT.png)](https://imgse.com/i/pE7y8oT)

## 1.4  python分布式函数执行为什么重要？

```text
python比其他语言更需要分布式函数调度框架来执行函数，有两点原因

1 python有gil，
  直接python xx.py启动没有包括multipricsessing的代码，在16核机器上，cpu最多只能达到100%,也就是最高使用率1/16，
  别的语言直接启动代码最高cpu可以达到1600%。如果在python代码里面亲自写多进程将会十分麻烦，对代码需要改造需要很大
  ，多进程之间的通讯，多进程之间的任务共享、任务分配，将会需要耗费大量额外代码，
  而分布式行函数调度框架天生使用中间件解耦的来存储任务，使得单进程的脚本和多进程在写法上
  没有任何区别都不需要亲自导入multiprocessing包，也不需要手动分配任务给每个进程和搞进程间通信，
  因为每个任务都是从中间件里面获取来的。
  
2 python性能很差，不光是gil问题，只要是动态语言无论是否有gil限制，都比静态语言慢很多。
 那么就不光是需要跨进程执行任务了，例如跨pvm解释器启动脚本共享任务(即使是同一个机器，把python xx.py连续启动多次)、
 跨docker容器、跨物理机共享任务。只有让python跑在更多进程的cpu核心 跑在更多的docker容器 跑在更多的物理机上，
 python才能获得与其他语言只需要一台机器就实现的执行速度。分布式函数调度框架来驱动函数执行针对这些不同的场景，
 用代码不需要做任何变化。
 
所以比其他语言来说，python是更需要分布式函数调度框架来执行任务。
  
```

## 1.5 框架学习方式

```
把1.3的求和例子，通过修改boost装饰器额参数和sleep大小反复测试两数求和，
从而体会框架的分布式 并发 控频。

这是最简单的框架，只有@boost 1行代码需要学习。说的是这是最简单框架，这不是最简单的python包。
如果连只有一个重要函数的框架都学不会，那就学不会学习得了更复杂的其他框架了，大部分框架都很复杂比学习一个包难很多。
大部分框架，都要深入使用里面的很多个类，还需要继承组合一顿。
```

## 1.6 funboost支持支持celery框架整体作为funboost的broker (2023.4新增)

```
见11.1章节代码例子，celery框架整体作为funboost的broker，funboost的发布和消费将只作为极简api，
核心的消费调度和发布和定时功能，都是由celery框架来完成，funboost框架的发布和调度代码不实际起作用。
用户操作funboost的api，语法和使用其他消息队列中间件类型一样，funboost自动化操作celery。

用户无需操作celery本身，无需敲击celery难记的命令行启动消费、定时、flower;
用户无需小心翼翼纠结亲自使用celery时候怎么规划目录结构 文件夹命名 需要怎么在配置写include 写task_routes，
完全不存在需要固定的celery目录结构，不需要手动配置懵逼的任务路由，
不需要配置每个函数怎么使用不同的队列名字，funboost自动搞定这些。

用户只需要使用简单的funboost语法就能操控celery框架了。funboost使用celery作为broker_kind,
远远的暴击亲自使用无法ide下代码补全的celery框架的语法。
```

```
funboost通过支持celery作为broker_kind,使celer框架变成了funboost的一个子集
```

[查看分布式函数调度框架完整文档](https://funboost.readthedocs.io/)

![](https://visitor-badge.glitch.me/badge?page_id=distributed_framework)

<div> </div>

[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #

# 2. 对比celery框架

是骡子是马必须拿出来溜溜。

```
此章节对比celery和分布式函数调度框架，是采用最严格的控制变量法精准对比。
例如保持 中间件一致  控制参数一致 并发类型一致 并发数量一致等等，变化的永远只有采用什么框架。 
```

## 2.0,在比较之前，说明一下和celery的关系？

**生产者-broker-消费者 模式是计算机科学中一个非常基础和经典的设计模式，它的历史远比 Celery 悠久得多**
如果认为"只要是使用生产者-消费者模式编程，那么就是抄袭celery"，那所有编程语言中的生产者消费者编程方式，都抄袭celery了，说这话简直是不长脑子。

```
此框架和celery没有关系，没有收到celery启发，也不可能找出与celery连续3行一模一样的代码。
这个是从原来项目代码里面大量重复while 1:redis.blpop()  发散扩展的。

这个和celery唯一有相同点是，都是生产者 消费者 + 消息队列中间件的模式，这种生产消费的编程思想或者叫想法不是celery的专利。
包括我们现在java框架实时处理数据的，其实也就是生产者 消费者加kfaka中间件封装的，难道java人员也是需要模仿python celery源码吗。
任何人都有资格开发封装生产者消费者模式的框架，生产者 消费者模式不是celery专利。生产消费模式很容易想到，不是什么高深的架构思想，不需要受到celery的启发才能开发。

```

**连任何线程池都是 生产者-broker-消费者 编程思想，线程池也抄袭celery了吗**
几乎所有线程池都是下面这样来实现的：

```
1.Broker (中间件/任务通道):
线程池 threadpool 有个 work_queue 属性，work_queue 是个内存队列，  work_queue 就是 broker

2.Producer (生产者):
threadpool有个submit方法，submit方法原理就是把函数和函数入参put丢到这个 threadpool.work_queue里面，submit就是生产者发送消息

3.Consumer (消费者):
线程池里面开启了n个线程， 每个线程里面逻辑是 while True：fun，params = work_queu.get(block=True) ，然后fun(params) 执行函数。
这n个线程就是n个消费者。
```

任何线程池都是这么实现的，那线程池使用 “生产者-broker-消费者“” 编程思想，抄袭了celery吗？
rq dramtiq huery 都抄袭了celery吗？
java中设计线程池的人听都没听说过celery。所以说funboost抄袭celery，简直是不长脑子

## 2.1 celery对目录层级文件名称格式要求很高

celery对目录层级文件名称格式要求太高，只适合规划新的项目，对不规则文件夹套用难度高。

所以新手使用celery很仔细的建立文件夹名字、文件夹层级、python文件名字

所以网上的celery博客教程虽然很多，但是并不能学会使用，因为要运行起来需要以下6个方面都掌握好，博客文字很难表达清楚或者没有写全面以下6个方面。
celery消费任务不执行或者报错NotRegistered，与很多方面有关系，如果要别人排错，至少要发以下6方面的截图，

```
1) 整个项目目录结构,celery的目录结构和任务函数位置，有很大影响
   
2) @task入参 ,用户有没有主动设置装饰器的入参 name,设置了和没设置有很大不同，建议主动设置这个名字对函数名字和所处位置依赖减小
   
3) celery的配置，task_queues(在3.xx叫 CELERY_QUEUES )和task_routes (在3.xx叫 task_routes)

4) celery的配置 include （在3.xx叫 CELERY_INCLUDE）或者 imports (3.xx CELERY_IMPORTS)  或者 app.autodiscover_tasks的入参

5) cmd命令行启动参数 --queues=  的值
   
6) 用户在启动cmd命令行时候，用户所在的文件夹。
   (如果不精通这个demo的，使用cmd命令行启动时候，用户必须cd切换到当前python项目的根目录，
   如果精通主动自己设置PYTHONPATH和精通此demo，可以在任何目录下启动celery命令行或者不使用celery命令行而是调用app.work_main()启动消费
```

在不规范的文件夹路径下，使用celery难度很高，一般教程都没教。
[项目文件夹目录格式不规范下的celery使用演示](https://github.com/ydf0509/celery_demo)

分布式函数调度框架天生没有这些方面的问题，因为此框架实现分布式消费的写法简单很多。

```
如你所见，使用此框架为什么没有配置中间件的 账号 密码 端口号呢。只有运行任何一个导入了框架的脚本文件一次，就会自动生成一个配置文件
然后在配置文件中按需修改需要用到的配置就行。

@boost 和celery的 @app.task 装饰器区别很大，导致写代码方便简化容易很多。没有需要先实例化一个 Celery对象一般叫app变量，
然后任何脚本的消费函数都再需要导入这个app，然后@app.task，一点小区别，但造成的两种框架写法难易程度区别很大。
使用此框架，不需要固定的项目文件夹目录，任意多层级深层级文件夹不规则python文件名字下写函数都行，
celery 实际也可以不规则文件夹和文件名字来写任务函数，但是很难掌握，如果这么写的话，那么在任务注册时候会非常难，
一般demo演示文档都不会和你演示这种不规则文件夹和文件名字下写celery消费函数情况，因为如果演示这种情况会非常容易的劝退绝大部分小白。
但是如果不精通celery的任务注册导入机制同时又没严格按照死板固定的目录格式来写celery任务，
一定会出现令人头疼的 Task of kind 'tasks.add' is not registered, please make sure it's imported. 类似这种错误。
主要原因是celery 需要严格Celery类的实例化对象app变量，然后消费函数所在脚本必须import这个app，这还没完，
你必须在settings配置文件写 include imports 等配置，否则cmd 启动celery 后台命令时候，celery并不知情哪些文件脚本导入了 app这个变量，
当celery框架取出到相关的队列任务时候，就会报错找不到应该用哪个脚本下的哪个函数去运行取出的消息了。
你可能会想，为什么celery app 变量的脚本为什么不可以写导入消费函数的import声明呢，比如from dir1.dir2.pyfilename imprt add 了，
这样celery运行时候就能找到函数了是不是？那要动脑子想想，如果celery app主文件用了 from dir1.dir2.pyfilename import add，
同时消费函数 add 所在的脚本 dir1/dir2/pyfilename.py 又从celery app的猪脚本中导入app，然后把@app.task加到add函数上面 ，
那这就是出现了互相导入，a导入b，b导入a的问题了，脚本一启动就报错，正是因为这个互相导入的问题，
celery才需要从配置中写好 include imports  autodiscover_tasks，从而实现一方延迟导入以解决互相导入。

此框架的装饰器不存在需要一个类似Celery app实例的东西，不会有这个变量将大大减少编程难度，消费函数写在任意深层级不规则文件下都行。
```

例如董伟明的 celery 教程例子的项目目录结构，然后很多练习者需要小心翼翼模仿文件夹层级和py文件名字。

![img_4.png](img_4.png)

```
可以看代码，当文件夹层级不规则和文件名称不规则时候，要使用celery绝非简单事情，如果你只看普通的celery入门文档，是绝对解决不了
这种情况下的celery如何正确使用。
```

![img.png](img.png)

## 2.2 性能远远超过celery10倍以上（使用初中的严格控制变量法）

对比方式使用初中生都知道的严格控制变量法科学精神

任意并发模式，任意中间件类型，发布和消费性能远远超过celery。

funboost比celery的发布性能超过10倍，消费性能超过20倍。

性能跑分代码在下面 2.6 章节

## 2.3 celery的重要方法全部无法ide自动补全提示

函数调度框架为了代码在ide能自动补全做了额外优化，celery全部重要公有方法无法补全提示.

<pre style="color: #00A000;">
1、配置文件方式的代码补全，此框架使用固定的项目根目录下的 funboost_config.py 补全，
   不会造成不知道有哪些配置项可以配置，celery的配置项有100多个，用户不知道能配置什么。
   
2、启动方式补全，celery采用celery -A celeryproj work + 一大串cmd命令行，很容易打错字母，或者不知道
   celery命令行可以接哪些参数。次框架使用 fun.consume()/fun.multi_process_consume()启动消费，
   运行直接 python xx.py方式启动
   
3、发布参数补全，对于简单的只发布函数入参，celery使用delay发布，此框架使用push发布，一般delay5个字母不会敲错。
   对于除了需要发布函数入参还要发布函数任务控制配置的发布，此框架使用publish不仅可以补全函数名本身还能补全函数入参。
   celery使用 add.apply_async 发布，不仅apply_async函数名本身无法补全，最主要是apply_async入参达到20种，不能补全
   的话造成完全无法知道发布任务时候可以传哪些任务控制配置，无法补全时候容易敲错入参字母，导致配置没生效。
   举个其他包的例子是例如 requests.get 函数，由于无法补全如果用户把headers写成header或者haeders,函数不能报错导致请求头设置无效。
   此框架的发布publish方法不仅函数名本身可以补全，发布任务控制的配置也都可以补全。
   

4、消费任务函数装饰器代码补全，celery使用@app.task，源码入参是 def task(self, *args, **opts),那么args和opts到底能传什么参数，
  从方法本身的注释来看无法找到，即使跳转到源码去也没有说明，task能传什么参数，实际上可以传递大约20种参数，主要是任务控制参数。
  此框架的@boost装饰器的 20个函数入参和入参类型全部可以自动补全提示，以及入参意义注释使用ctrl + shift + i 快捷键可以看得很清楚。
  
5、此框架能够在pycharm下自动补全的原因主要是适当的做了一些调整，以及主要的面向用户的公有方法宁愿重复声明入参，也不使用*args **kwargs这种。

  举个例子说明是 @boost这个装饰器(这里假设装饰到fun函数上)，
  此装饰器的入参和get_consumer工厂函数一模一样，但是为了补全方便没有采用*args **kwargs来达到精简源码的目的，
  因为这个装饰器是真个框架最最最重要的，所以这个是重复吧所有入参都声明了一遍。
  
  对于被装饰的消费函数，此装饰器会自动动态的添加很多方法和属性，附着到被装饰的任务函数上面。
  框架对 boost装饰器进行了针对pycharrm解析代码特点进行了专门优化，
  所以类似fun.clear fun.publish fun.consume  fun.multi_process_conusme 这些方法名本身和他的入参都能够很好的自动补全。
  
6、自动补全为什么重要？对于入参丰富动不动高达20种入参，且会被频繁使用的重要函数，如果不能自动补全，用户无法知道有哪些方法名 方法能传什么参数 或
  者敲了错误的方法名和入参。如果自动补全不重要，那为什么不用vim和txt写python代码，说不重要的人，那以后就别用pycharm vscode这些ide写代码。
  
  celery的复杂难用，主要是第一个要求的目录文件夹格式严格，对于新手文件夹层级 名字很严格，必须小心翼翼模仿。
  第二个是列举的1 2 3 4这4个关键节点的代码补全，分别是配置文件可以指定哪些参数、命令行启动方式不知道可以传哪些参数、apply_async可以传哪些参数、
  @app.task的入参代码补全，最重要的则4个流程节点的代码全都无法补全，虽然是框架很强大但是也很难用。
  
</pre>

## 2.4 比celery强的方面的优势大全

### 2.4.1 funboost对win linux mac 都支持

2.4.1 funboost对win linux mac 都支持，celery 4 以后官方放弃对windwos的支持和测试。

```
   celer4 以后官方放弃对windwos的支持和测试，例如celery的默认多进程模式在windwos启动瞬间就会报错，
   虽然生产一般是linux，但开发机器一般是windwos,
   windwos无法运行celery默认的多进程并发，只能运行 solo gevent eventlet threads并发模式。
```

### 2.4.2 funboost万物皆可为broker，支持消息队列种类远超celery

funboost支持所有消息队列和消费框架，万物皆可为broker，不管是内存 文件 数据库 tcp udp,redis 正经消息队列 消费者框架都是funboost的broker。

```
   如5.4所写，新增了python内置 queue队列和 基于本机的持久化消息队列。不需要安装中间件，即可使用。
   只要是celery能支持的中间件，这个全部能支持。因为此框架的 BrokerEnum.KOMBU 中间件模式一次性
   支持了celery所能支持的所有中间件。但celery不支持kafka、nsq、mqtt、zeromq、rocketmq、pulsar等。
   而且由于funboost的强大扩展， celery  dramtiq rq 这些框架只是 funboost的 中间件模式之一。
   funboost支持kombu所以自动支持了google 亚马逊 微软的云消息队列。
   所以只要celery和kombu能支持的中间件，funboost都能支持，不管未来celery kombu新增什么中间件，
   funboost都能自动支持，funboost可以 以逸待劳，以不变应万变。
```

### 2.4.3 funboost性能远超celery几十倍，性能不在一个数量级。

```
这是最重要的，光使用简单还不够，性能是非常重要的指标。发布性能提升1000%以上，消费性能提升2000%以上。
性能不在一个数量级。看下面2.6章节的严格的控制变量法测试对比方法和源码
```

### 2.4.4 使用funboost框架时候，代码在ide自动补全暴击使用celery。

```
   全部公有方法或函数都能在pycharm智能能提示补全参数名称和参数
   一切为了调用时候方便而不是为了实现时候简略，例如get_consumer函数和AbstractConsumer的入参完全重复了，
   本来实现的时候可以使用*args **kwargs来省略入参，
   但这样会造成ide不能补全提示，此框架一切写法只为给调用者带来使用上的方便。不学celery让用户不知道传什么参数。
   如果拼错了参数，pycharm会显红，大大降低了用户调用出错概率。过多的元编程过于动态，不仅会降低性能，
   还会让ide无法补全提示，动态一时爽，重构火葬场不是没原因的。
```

### 2.4.5 funboost 无需使用难记复杂的命令行启动消费。

```
   不使用命令行启动，在cmd打那么长的一串命令，容易打错字母。并且让用户不知道如何正确的使用celery命令，不友好。
    此框架是直接python xx.py 就启动了。
```

### 2.4.6 框架不依赖任何固定的目录结构，无结构100%自由。

```
   框架不依赖任何固定的目录结构，无结构100%自由，想把使用框架写在哪里就写在哪里，写在10层级的深层文件夹下都可以。
   脚本可以四处移动改名。celery想要做到这样，要做额外的处理。
   对于不规则文件夹项目的clery使用时如何的麻烦，可以参考 celery_demo项目 https://github.com/ydf0509/celery_demo。
```

### 2.4.7 funboost框架比celery更简单10倍

```
使用此funoost框架比celery更简单10倍，如例子所示。使用此框架代码绝对比使用celery少几十行。
```

### 2.4.8 funboost的消息格式比celery更容易自己构造

```
由于funboost消息中间件里面没有存放其他与python 和项目配置有关的信息，这是真正的跨语言的函数调度框架。
java人员也可以直接使用java的redis类rabbitmq类，发送json参数到中间件，由python消费。
celery里面的那种参数，高达几十项，和项目配置混合了，java人员绝对拼凑不出来这种格式的消息结构。
```

### 2.4.9 celery目录结构限制严格，不规范目录结果层级使用难度高。

celery目录结构限制严格，不规范目录结果层级使用难度高。见这个项目：
演示复杂深层路径，完全不按照一般套路的目录格式的celery使用
https://github.com/ydf0509/celery_demo

```
celery目录结构限制严格，不规范目录结果层级使用难度高。 celery有1个中心化的celery app实例，函数注册成任务，
 添加装饰器时候先要导入app，然后@app.task，
同时celery启动app时候，调度函数就需要知道函数在哪里，所以celery app所在的py文件也是需要导入消费函数的，否则会
celery.exceptions.NotRegistered报错
这样以来就发生了务必蛋疼的互相导入的情况，a要导入b，b要导入a，这问题太令人窘迫了，通常解决这种情况是让其中一个模块后导入，
这样就能解决互相导入的问题了。celery的做法是，使用imports或者include一个列表，列表的每一项是消费函数所在的模块的字符串表示形式，
例如 如果消费函数f1在项目的a文件夹下的b文件夹下的c.py中，消费函数与f2在项目的d文件夹的e.py文件中，
为了解决互相导入问题，celery app中需要配置 imports = ["a.b.c",'d.e']，这种import在pycharm下容易打错字，
例如scrapy和django的中间件注册方式，也是使用的这种类似的字符串表示导入路径，每添加一个函数，只要不在之前的模块中，就要这么写，
不然不写improt的话，那是调度不了消费函数的。此框架原先没有装饰器方式，来加的装饰器方式与celery的用法大不相同，
因为没有一个叫做app类似概念的东西，不需要相互导入，启动也是任意文件夹下的任意脚本都可以，自然不需要写什么imports = ['a.b.c']
```

### 2.4.10 funboost学习难度远低于celery

```
funboost虽然功能更强大，但使用更简单，不需要看复杂的celery 那样的5000页英文文档，
因为函数调度框架只需要学习@boost一个装饰器，只有一行代码学要学。
别看funboost的文档也很长，但都是讲实现原理和为什么那么设计的，大篇幅讲对比是怎么暴击知名celery scrapy框架的。
实际funboost使用例子只有教程1.3章节不到8行代码需要学习。其他例子只是改了下boost装饰器的入参，
教程长是为了方便懒惰的小白压根不看BoosterParams的入参注释。
```

### 2.4.11 funboost原生支持 asyncio ，支持async def 函数

funboost原生支持 asyncio 原始函数，不用用户额外处理 asyncio loop相关麻烦的问题。

```
此框架原生支持 asyncio 原始函数，不用用户额外处理 asyncio loop相关麻烦的问题。celery不支持async定义的函数，
celery不能把@app.task 加到一个async def 的函数上面。

celery 的 threading 和asyncio 并发模式都支持 async def 函数。 
threading并发模式是所有函数跑在无数个线程中，然后每个线程内部启动一个loop.run_until_complete(fun(1,2))，实际还是多线程运行异步函数。
asyncio 并发模式是真的在一个线程中一个loop中多协程并发运行。
```

### 2.4.12 funboost比celery对函数的辅助运行控制方式更多

```
此框架比celery对函数的辅助运行控制方式更多，支持celery的所有如 并发 控频 超时杀死 重试 消息过期
确认消费 等一切所有功能，同时包括了celery没有支持的功能，例如原生对函数入参的任务过滤 ,分布式qps全局控频。
```

### 2.4.13 funboost能分布式qps全局控频，celery不能

funboost 能支持全局分布式控频，无论多少台机器和进程启动。

```
celery不支持分布式全局控频，celery的rate_limit 基于单work控频，如果把脚本在同一台机器启动好几次，
或者在多个容器里面启动消费，那么总的qps会乘倍数增长。
funboost框架能支持单个消费者控频，同时也支持分布式全局控频。
is_using_distributed_frequency_contro=True 则分布式全局控频
```

### 2.4.14 funboost自带内置一键启动多进程，celery无法。

```
 funboost框架比celery更简单开启 多进程 + 线程或协程。celery的多进程和多线程是互斥的并发模式，funboost框架是叠加的。
很多任务都是需要 多进程并发利用多核 + 细粒度的线程/协程绕过io 叠加并发 ，才能使运行速度更快，消耗cpu大 消耗io也大的场景太多了。
```

### 2.4.15 funboost 限速控频精准度远高于celery

```
此框架精确控频率精确度达到99.9%，celery控频相当不准确，最多到达60%左右，两框架同样是做简单的加法然后sleep0.7秒，都设置500并发100qps。
测试对比代码见qps测试章节,欢迎亲自测试证明。很容易测试，消费函数里面打印下时间和hello，然后启动消费，搜索控制台，看qps是否准确。
```

### 2.4.16 funboost日志的颜色和格式，远超celery。

```
funboost日志的颜色和格式，远超celery。此框架的日志使用nb_log,日志在windwos远超celery，在linux也超过celery很多。
```

### 2.4.17  funboost内置支持python代码级别的一键远程linux机器消费部署

```
funboost支持python代码级别的远程linux机器消费部署,可以方便的部署到测试环境的其他机器测试。
funboost 支持 task_fun.fabric_deploy 一键部署到远程linux机器
```

### 2.4.18 funboost 直接支持类/实例方法作为消费函数，celery只支持静态方法/函数

```
funboost 直接支持 类的实例方法和类方法作为消费函数，celery只能支持 普通函数和静态方法作为消费函数，funboost更为方便。
```

### 2.4.19 funboost支持多进程叠加 多线程或者协程，是叠加的。 celery只能gevent/threading和多进程二选一。

```
funboost 的 fun.multi_process_consume 函数可以叠加多进程 + 多线程/协程，是叠加的。
celery只能gevent/threading和多进程二选一，不是叠加的。
funboost更能同时充分利用io和cpu。
```

### 2.4.20 funboost 队列路由配置直观度和简易度暴击celery，celery的队列路由配置是劝退新手的第一步。

```
@boost(BoosterParams(queue_name='math_queue', broker_kind=BrokerEnum.REDIS))
def fun(x,y)：
     pass
funboost的写法更紧凑队列名和函数在一起，小白一看就知道函数是绑定什么队列。


celery的 task_queues 和 task_routes 配置简直是劝退新手的第一步，连没用过rabitmq，只用过redis kafka的编程老手也是一脸懵逼。
下面这个celery路由队列配置写法太难了，而且容易写错，如果写错了到时候用户不消费也不提示，用户整个心态都崩了。
尤其是task_routes，如果用户改了函数名字，而配置没改写成一致，走了默认队列，用户又懵逼了。
于是队列没跑起来：
为什么我发了消息队列却不消费？
还有：为啥 worker 和我任务跑在不同队列……
就这样一天过去了，都没调出来。
```

```python
# celery的路由配置。
from kombu import Queue, Exchange

# 定义交换机（可复用）
default_exchange = Exchange('default', type='direct')

# 注册队列（要跟 worker 启动时一致）
task_queues = (
    Queue('celery', default_exchange, routing_key='celery'),  # 默认队列
    Queue('queue_sms', default_exchange, routing_key='sms'),
    Queue('queue_pdf', default_exchange, routing_key='pdf'),
)

# 路由配置（按任务名绑定到指定队列）
task_routes = {
    'my_proj.tasks.send_sms': {'queue': 'queue_sms', 'routing_key': 'sms'},
    'my_proj.tasks.gen_pdf': {'queue': 'queue_pdf', 'routing_key': 'pdf'},
    # 其他任务默认走 celery 队列
}
```

**funnboost不强制你懂amqp路由协议**

```
项目中真正利用到rabbitmq这种复杂路由系统的celery python用户不到1%，大部分用户只是想简单用个队列而已，but咋就那么难。
你用celery，celery作者就会告诉你，你连交换机都不懂，你还想用消息队列？

funboost就是为了99%场景来设计api，而不是为1%场景搞得99%用户自闭。
你如果想某个消息发到不同的队列，你就简单的fun1.push 和fun2.push 就好了。

再者说了，funboost也能支持完整的rabbitmq的完整路由系统，你把要特殊的入参从装饰器的broker_exclusive_config字典传过来，然后按照文档4.21实现就好了；
另外funboost也可以使用kombu作为broker_kind来支持rabbitmq复杂路由。
```

### 2.4.21 funboost的配置方式吊打celery

```
celery的配置分散在app和app.task上，而且用户压根不知道能配置什么，因为代码无法在ide补全。

funboost的配置集中在@boost装饰器一处；用户也可以使用继承BoosterParams写一个子类，减少每个装饰器相同的重复入参。pydantic在pycharm安装个pydantic插件，补全提示效果很好。
```

### 2.4.22 funboost 能非常容易的扩展用户自己的任何中间件作为broker，celery无法做到。

funboost 的 consumer的 _shedual_task 非常灵活,所以可以轻松接入万物作为broker.

```
funboost 使用模板模式来开发各种消息队列消费者 发布者子类，所以可以兼容任何东西作为消息队列。
例如 文件夹 文件 sqlite  tcp celery dramtiq 等轻松作为 funboost的broker。
因为funboost暴露的非常好，用户就像做填空题一样填写就好了。
具体看文档4.21 和4.21b 章节，里面自带了 python的list数据结构模拟作为broker，代码很短就能完成扩展。


反观celery，用户几乎不可能完成，您无法像 funboost 这样在应用层简单继承。您必须深入其底层的消息库 Kombu，
去理解和实现它的一整套 Transport 和 Channel 接口。这需要阅读大量源码，理解其内部工作流。
```

```
funboost 的 consumer的 _shedual_task 非常灵活，用户实现把从消息队列取出的消息通过_submit_task方法
丢到并发池，他不是强制用户重写实现怎么取一条消息，例如强制你实现一个 _get_one_message的法，那就不灵活和限制扩展任意东西作为broker了，而是用户完全自己来写灵活代码。
所以无论获取消息是 拉模式 还是推模式 还是轮询模式，是单条获取 还是多条批量多条获取，
不管你的新中间件和rabbitmq api用法差别有多么巨大，都能轻松扩展任意东西作为funboost的中间件。 
所以你能看到funboost源码中能轻松实现任何物质作为funboost的broker。

funboost 的 _shedual_task 哲学是：“我不管你怎么从你的系统里拿到任务，我只要求你拿到任务后，调用 self._submit_task(msg) 方法把它交给我处理就行。”
```

### 2.4.23 funboost 强大的的fct上下文，完胜celery 装饰器的bind=True侵入式设计

```
funboost 强大的的fct上下文，吊打celery 装饰器的bind=True，然后再在函数入场中插入一个入参self

funboost的 fct 智能上下文十分强大，不需要改变函数定义入参。类似flask视图的request这种自动线程/协程隔离级别的上下文。例如任务函数里面想知道自己的task_id 和消息发布时间等。

funboost 的方式：函数签名保持纯净
@boost(BoosterParams(queue_name="add_queue"))
def add(x, y):
    # 需要时，从 fct 上下文获取信息
    print(f"Funboost Task ID: {fct.task_id}")
    return x + y

但celery 如果要获取 道自己的task_id 和消息发布时间等，求两数字之和的函数需要写成如下：
@app.task(bind=True)
def add(self,x,y):
     task_id = self.request.id
     return x + y
好好的add函数，不仅要写@app.task(bind=True)，还要在第一个入参位置加个self，改成3个入参。
celery @app.task(bind=True) + self 没有funboost的fct好用和无入侵。
因为你原来的 调用add的地方如add(1,2)会报错，add现在变成需要3个入参了。   
```

### 2.4.24 funboost全流程支持asyncio生态，celery望尘莫及

```
funboost不仅支持async def的函数消费，
更能支持 await aio_push 和 await aio_publish 和 await AioAsyncResult.result 获取rpc结果， 
也就是说funboost 支持 从发布和消费到获取rpc结果，全流程原生asyncio编程生态。
更容易和现代fastapi这种异步web框架搭配。

celery则压根没有支持这样的全流程 asyncio 生态。
```

### 2.4.25 funboost作者的自定义线程池能自动伸缩，完胜。

funboost作者的自定义线程池能自动伸缩，celery使用原生concurrent.futures.ThreadPoolExecutor

```
funboost的线程并发模式的线程池，能根据任务量智能伸缩线程数量，在保证效率的同时避免资源浪费。
celery使用 concurrent.futures.ThreadPoolExecutor，无法自动缩小线程池。
```

### 2.4.26 funboost死信队列机制更完善：

```
funboost 通过抛出特定异常或配置，可以轻松实现**“重试N次后自动移入死信队列”**，逻辑清晰。
```

### 2.4.27 funboost可以消费一切任意json消息(无论json包含什么keys)，celery无法识别

```
funboost支持消费任意key value 结构的 JSON 消息，灵活性极高。
用户只需要装饰器加个should_check_publish_func_params=False，见文档4b.2章节。

@boost(BoosterParam(queue_name='queue_free_format'，should_check_publish_func_params=False))
def task_fun(**kwargs):
    print(kwargs)

也就是说无论消息是否由funboost框架发布的还是第三方自由随意发布的，都能被funbost消费。
json消息无论是什么键值对名字，同一个队列名字，哪怕是json中的key一直变化， 都能被 funboost 消费。
```



###  2.4.28 更强力灵活的,funboost 可以消费一切任意不规范格式的消息(非json也能消费), celery完全不可行.

见文档 4b.2c 章节: funboost 支持消费一切任意不规范格式的消息,不是json也能消费.

```
即使消息队列中的消息不是从funboost发布的,也不是json,而是一个任意内容的字符串,funboost也能消费.

用户自定义自己的Consumer类,继承重写_user_convert_msg_before_run 把消息格式清洗转化成字典或者json字符串, 
在boost装饰器 设置 consumer_override_cls=这个自定义Consumer类,即可.

celery 无法消费任意字符串消息,funboost 能轻松做得到消费任意字符串消息.
```

### 2.4.29 funboost等待任务完成机制：提供了 wait_for_possible_has_finish_all_tasks() 方法

```
funboost中等待任务完成机制：提供了 wait_for_possible_has_finish_all_tasks() 方法，方便在脚本中等待一个队列的所有任务被消费完毕。

celery无此功能。
```

### 2.4.30 funboost无需 框架专用插件
```
无需框架专用插件：funboost 的自由度使其无需 django-funboost、flask-funboost 这类适配插件，可直接在任何 web 框架中简单直观的使用。
```

### 2.4.31 funboost的定时任务比celery更强，能动态添加删除 和 多点部署。

funboost内置自带动态添加定时任务，celery写死在beat_schedule字典

```
funboost的定时代码内启动，无需额外命令
funboost随时通过代码动态添加、暂停、恢复、删除定时任务，非常自然。

celery 的定时任务是配置式，相对繁琐：需要在配置文件中定义一个 beat_schedule 字典，


动态的好处包括了，可以很容易和任何web框架搭配，在接口中添加删除定时任务。
```

funboost的定时器可以多次启动，多台机器启动不会重复执行定时任务。

```
funboost 继承重写了 apscheduler ，使用redis作为job_store时候，
apscheduler的_process_jobs使用了redis分布式锁，
确保一个任务不会同时被多台机器或进程从redis中扫描取出来运行。所以不怕你多次反复部署定时脚本。
顺便实现高可用，其中一台机器宕机了，不会导致定时任务就不运行了。

celery默认是“单点故障”：原生的 celery beat 无法多实例部署，否则会导致任务被重复发布多次。
所以celery的beat命令害怕你在命令行反复部署。



举个例子：
希望间隔5秒打印hello，但你敢为了定时器高可用，而把celery定时任务启动部署2次吗？
那就实际变成了每隔5秒打印2次hello了。
或者是你意外多部署几次celery定时器，那就悲催了，重复触发定时任务。

但funboost使用redis作为job_store时候，不怕你多次启动定时器导致定时任务执行重复。
```

funboost 使用 最知名的apscheduler 轻度封装，定时语法妇孺皆知。
celery的beat_schedule 字典，容易配置错误，导致定时任务不能执行。

```
funboost的API 简洁直观：ApsJobAdder(task_func, ...).add_push_job(...)，API 清晰，
且复用了 apscheduler 的成熟语法，学习成本低。

celery需要在配置文件中定义一个 beat_schedule 字典，可读性较差，且无静态检查，
容易因字符串拼写错误导致任务不执行且无明显报错，太坑人。
```

### 2.4.32 funboost + REDIS_ACK_ABLE ack能力 吊打celery + redis + ack + visibility_timeout (小细节)

funboost作者凭借深厚功底与精准需求感，一人打造出覆盖面广、机制优越、使用简洁的消息队列框架，是非常了不起的技术创举----用一个人的力量解决了celery数百人团队在某些方面难以突破的结构性痛点。

funboost + REDIS_ACK_ABLE 中间件吊打 celery 的 redis + task_acks_late=True + visibility_timeout=固定时间

celery的redis确认消费 只能和 funboost + REIDS_ACK_USING_TIMEOUT 中间件相提并论

```
celery + redis ，如果worker 进程被强制kill -9，那么待确认消费的孤儿消息，需要在 `visibility_timeout` 时间之后重回队列，默认1小时， 
例如你有10个进程在消费，突然kill一个进程或者宕机了一个进程，这个消息需要在1小时候才被重回队列,被其他进程消费运行，这太不及时了。 
如果你的程序本来就耗时2小时，visibility_timeout 设置1小时，会造成无限懵逼死循环重回队列重复消费.
即使你调大visibility_timeout为10000000秒可以100%避免错误的无限重回队列,但是你把消费者突然强制关闭,他的所有孤儿消息也要10000000秒后才重回工作队列,
所以及时重回孤儿消息和避免误重投,通过visibility_timeout来设置,这2者是矛盾的,这个在celery无解.这里不是配置问题，而是架构机制问题,只有基于心跳检测的主动机制才可解决.

celery的redis+ 确认消费 2大缺点是，1是不能及时让孤儿消息快速重回队列，2是容易把本来就耗时长的消息误认为是孤儿消息进而错误的重回队列。


而funboost 的 broker_kind=BrokerEnum.REDIS_ACK_ABLE 时候，使用的是消费者心跳检测机制，
能及时快速精准的让孤儿消息重回工作队列，并且不会把本来就执行慢的消息，误认为是宕机了的孤儿消息错误的重回工作队列。

celery 的 redis + task_acks_late=True + visibility_timeout=固定时间 只能和 funboost的 
REIDS_ACK_USING_TIMEOUT 中间件相提并论,和 funboost的REDIS_ACK_ABLE中间件相比落后太多

```

这不是污蔑celery,而是celery官方文档也承认的,详见:
(celery官方文档的Caveats的Visibility timeout章节 https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html?utm_source=chatgpt.com)[https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html?utm_source=chatgpt.com]

### 2.4.40 （王炸）funboost 支持celery作为broker_kind

有些人一直很质疑担心funboost不稳定，运行时候程序突然崩溃退出，认为celery运行了十几年肯定稳定，现在celery旧王作为funboost新皇的马前卒，
可以使用funboost的极简api来定义消费函数，但是内部使用celery核心来驱动运行消费函数，你还有什么好说的。

```
funboost 不仅支持各种常规消息队列，还支持celery dramtic  rq 等流行的python异步消费框架，作为broker_kind，

funboost支持clery作为broker_kind,@boost('celery_q1', broker_kind=BrokerEnum.CELERY, qps=5) 就能使用celery的核心来调度函数的运行了，
即使你不愿意对比funboost和celery性能，不相信celery的性能比funboost差差多，迷信美国人写的celery，funboost能支持celery作为中间件模式，
通过funboost的极简api来操作celery核心，
用户无需操作Celery实例对象，通过broker_kind=BrokerEnum.CELERY，可以使celery框架成为实际的调度运行。
你说funboost的api只是简单，但是担心funboost长期消费运行不稳定，funboost现在可以支持celery整体作为funboost的中间件模式，还有什么好质疑的，
不喜欢funboost实现的并发消费，可以一键从funboost实现的消费调度代码切换到celery框架作为消费调度，还有什么理由质疑担心不稳定。
通过 @boost(broker_kind=BrokerEnum.CELERY) 就可以让celery变成funboost子集，celery有的funboost都有，celery没的，funboost也有。
```

## 2.4b 讨Celery檄：Funboost十胜定乾坤，函数王朝开天命

**夫任务调度之道，贵在通达！队列纵横之术，胜在易用！**
昔Celery恃RabbitMQ Redis之威，窃踞调度王座十数载，然其架构臃肿如裹足老象，兼容性似残破牢笼！今观其势：**弃Windows如敝履，控频精度若醉汉；困目录结构作茧，性能吞吐成笑谈**——开发者叩首于五千页文档，匍匐于晦涩命令行，此诚天下苦秦久矣！
今有Funboost，承函数调度天命，执 `@boost`神器，以**性能裂苍穹之威，兼容纳百川之量**，革旧弊，立新规，伐无道！十胜锋芒所指，Celery十败如山崩！

---

#### 十胜十败·定鼎九州

**一胜曰：疆域之胜**
Celery弃Windows疆土，多进程启动即崩，开发寸步难行，此谓**金瓯残缺失半壁**！
Funboost跨三界称尊，进程线程协程任选，开发生产皆驰骋，此谓**寰宇纵横掌天门**！

**二胜曰：器量之胜**
Celery闭中间件之门，Kafka/MQTT皆拒，新潮队列成陌路，此谓**夜郎闭户终自绝**！
Funboost纳廿四路诸侯，内建队列立乾坤，更兼**兼容Celery全系器**，此谓**海纳百川容星汉**！

**三胜曰：神速之胜**
Celery吞吐若老牛破车，性能瓶颈成痼疾，此谓**老牛破车困泥潭**！
Funboost疾如雷霆裂空，**发布快1000%惊鬼神，消费疾2000%贯九霄**，此谓**追风逐电荡八荒**！

**四胜曰：明道之胜**
Celery动态元编程蔽日，参数传递如盲人摸象，此谓**雾锁重楼失北斗**！
Funboost智能补全烛幽冥，类型声明破迷障，IDE红线斩谬误，此谓**日月当空照坦途**！

**五胜曰：简政之胜**
Celery命令行如天书符咒，路径错漏频生，此谓**蜀道悬梯困苍生**！
Funboost执**python xx.py**开太平，老幼皆宜无障碍，此谓**大道至简定江山**！

**六胜曰：自由之胜**
Celery目录囚笼锁蛟龙，imports镣铐缚云翼，此谓**金丝雀困雕花笼"**！
Funboost十层深阁任穿梭，脚本四海可为家，此谓**鲲鹏振翅九万里**！

**七胜曰：包容之胜**
Celery消息混杂Python痕，跨语言协作成天堑，此谓**孤岛闭门终自绝**！
Funboost**纯净JSON通万邦**，Python/Java共交响，此谓**丝绸新路连寰宇**！

**八胜曰：天时之胜**
Celery拒async浪潮于门外，协程革命空嗟叹，此谓**刻舟求剑失沧海**！
Funboost纳asyncio入经脉，**异步同步皆如意**，此谓**弄潮敢缚蛟龙归**！

**九胜曰：王道之胜**
Celery控频单机尚粗疏，分布式更成镜花月，此谓**谓乌合之众溃荒原**！
Funboost执**令牌桶算法掌乾坤**，分布式控频**精度99.9%镇山河**，此谓**虎符一出千军肃**！

**十胜曰：革新之胜**
Celery拒类方法于高墙，面向对象成虚妄，此谓**孤芳自赏终取祸**！
Funboost纳**万物入调度**，实例方法皆可Boost，此谓**开宗立派写新章**！

---

#### 弑王绝刃·乾坤倒转：

**更备诛神兵符：**
Funboost竟容Celery为子集！`@boost(broker_kind=BrokerEnum.CELERY)`一出,
旧王纵有疑心，亦成新朝马前卒！此谓**乾坤倒转收降将**，古今未闻之奇策！

**今Funboost携十胜之威：**
东收Redis为粮仓，西纳RabbitMQ作辕门；
南降Kafka为前哨，北抚ZeroMq成轻骑！
**三军并发：**
多进程裂地，多线程碎空，协程织天网！

**开发者当顺天命：**破Celery之枷锁，入函数调度新纪元！何须啃五千页腐简？不必忍性能之憋屈！此乃**任务调度之工业革命，函数王朝之开国大典**！

> **剑指苍穹宣言：**
> "旧王Celery骸骨已寒，新皇Funboost旭日灼天！
> 以@boost为传国玉玺，以分布式为定鼎九器——
> **万物皆可调度，四海终归一统！**"

**Funboost太祖·敕令四海:**
**天命昭昭，神器更易**
**顺之者昌，逆之者绝**
**天命元年·布告寰宇**

---

## 2.5 funboost能支持celery整体框架作为broker_kind

funboost能自动化配置celery和使用celery的核心调度功能,funboost的api + celery的核心调度,爽!

实现了funboost的极简api写代码 + celery的核心调度引擎来运行你的函数 。有的小白觉得funboost api简单，但又不愿意花时间亲自验证测试稳定性和性能，导致内心很犹豫疑虑，现在这种方式结合了两者的优点：funboost提供简洁直观的API接口让开发变得轻松，而celery提供稳定可靠的底层调度引擎。相当于用简单的方式获得了强大的功能，这是很多开发者梦寐以求的组合。

见文档4.28章节 ,funboost 支持celery框架整体作为funboost的broker (2023.4新增)

```
funboost的api来操作celery，完爆用户亲自操作celery框架。

boost装饰器只需要指定 broker_kind=BrokerEnum.CELERY

@boost('celery_q1', broker_kind=BrokerEnum.CELERY, qps=5)


那么funboost就能自动使用celery的核心来执行用户的函数,而不是funboost的调度核心来运行用户的函数.
```

```
因为有的人不信 funboost执行速度暴击celery,那么可以使用funboost的api来自动化操作celery核心,
这样既用法写法简单,又能使用用户认为celery性能好的celery执行核心
```

## 2.6 funboost 和 celery 性能比较源码（控制变量法）

用户不信的可以直接运行里面的代码

对比源代码在：
https://github.com/ydf0509/funboost/tree/master/test_frame/funboost_vs_celery_benchmark

**funboost vs celery 性能对比测试结论**

### 2.6.1 funboost vs celery 控制变量法说明

使用经典的控制变量法测试

共同点是：

在win11 + python3.9 +  本机redis 中间件 + amd r7 5800h cpu 环境下测试 + 选择单线程并发模式 + 相同逻辑消费函数

区别点是：

funboost 和 celery5

### 2.6.2 funboost vs celery 发布性能对比

funboost: 发布10万条消息耗时9秒，每隔0.08秒发布1000条，平均每秒发布11000条

celery: 发布10万条消息耗时110秒，每隔1.1秒发布1000条，平均每秒发布900条

对比结果: funboost发布性能约为celery的12倍

### 2.6.3 funboost vs celery 消费性能对比

funboost: 平均每隔0.15秒消费1000条消息，每秒消费约7000条

celery: 平均每隔3.6秒消费1000条消息，每秒消费约300条

对比结果: funboost消费性能约为celery的23倍

### 2.6.4 funboost vs celery 总体性能对比

funboost在同样的硬件环境和测试条件下（win11 + python3.9 + 本机redis中间件 + AMD R7 5800H CPU + 单线程并发模式 + 相同消费函数），

无论是在消息发布还是消费方面都大幅优于celery，都超过1000% ，所以 celery性能比funboost性能差了一个数量级，funboost性能是绝对断崖式遥遥领先。

<div> </div>

# 3.框架详细介绍


## 3.1 各种中间件选择的场景和优势

```python
class BrokerEnum:

    """
    在funboost中万物皆可为消息队列broker,funboost内置了所有 知名的正经经典消息队列作为broker, 
    也支持了基于 内存 各种数据库 文件系统 tcp/udp/http这些socket 模拟作为broker.
    funboost也内置支持了各种python三方包和消费框架作为broker,例如 sqlachemy kombu celery rq dramtiq huey nameko 等等

    用户也可以按照文档4.21章节,轻松扩展任何物质概念作为funboost的broker.
    """
    
    # funboost框架能轻松兼容消息队列各种工作模式, 拉模式/推模式/轮询模式，单条获取 批量获取
    """
    funboost 的 consumer的 _shedual_task 非常灵活，用户实现把从消息队列取出的消息通过_submit_task方法
    丢到并发池，他不是强制用户重写实现怎么取一条消息，例如强制你实现一个 _get_one_message的法，
    那就不灵活和限制扩展任意东西作为broker了，而是用户完全自己来写灵活代码。
    所以无论获取消息是 拉模式 还是推模式 还是轮询模式，是单条获取 还是多条批量获取，
    不管你的新中间件和rabbitmq api用法差别有多么巨大，都能轻松扩展任意东西作为funboost的中间件。 
    所以你能看到funboost源码中能轻松实现任物质概念作为funboost的broker。
    """

    EMPTY = 'empty'  # 空的实现，需要搭配 boost入参的 consumer_override_cls 和 publisher_override_cls使用，或者被继承。

    RABBITMQ_AMQPSTORM = 'RABBITMQ_AMQPSTORM'  # 使用 amqpstorm 包操作rabbitmq  作为 分布式消息队列，支持消费确认.强烈推荐这个作为funboost中间件。
    RABBITMQ = RABBITMQ_AMQPSTORM

    RABBITMQ_RABBITPY = 'RABBITMQ_RABBITPY'  # 使用 rabbitpy 包操作rabbitmq  作为 分布式消息队列，支持消费确认，不建议使用

     """
    以下是各种redis数据结构和各种方式来实现作为消息队列的,redis简直被作者玩出花来了.
    因为redis本身是缓存数据库,不是消息队列,redis没有实现经典AMQP协议,所以redis是模拟消息队列不是真消息队列.
    例如要实现消费确认,随意重启但消息万无一失,你搞个简单的 redis.blpop 弹出删除消息,那就压根不行.重启就丢失了,但消息可能还没开始运行或者正在运行中.

    redis做ack挑战难点不是怎么实现确认消费本身,而是何时应该把关闭或宕机进程的消费者的待确认消费的孤儿消息重回队列.  
    在 Redis 上实现 ACK 的真正难点，根本不在于“确认”这个动作本身，而在于建立一套可靠的、能够准确判断“何时可以安全地及时地进行任务恢复”的分布式故障检测机制。
    所以你以为只要使用 brpoplpush 或者 REDIS_STREAM 就能自动轻易解决ack问题,那就太天真了,因为redis服务端不能像rabbitmq服务端那样天生自带自动重回宕机消费者的消息机制,需要你在redis客户端来维护实现这套机制.
    """
    REDIS = 'REDIS'  # 使用 redis 的 list结构，brpop 作为分布式消息队列。随意重启和关闭会丢失大量消息，不支持消费确认。注重性能不在乎丢失消息可以选这个redis方案。
    REDIS_ACK_ABLE = 'REDIS_ACK_ABLE'  # 基于redis的 list + 临时unack的set队列，采用了 lua脚本操持了取任务和加到pengding为原子性，,基于进程心跳消失判断消息是否为掉线进程的，随意重启和掉线不会丢失任务。
    REIDS_ACK_USING_TIMEOUT = 'reids_ack_using_timeout'  # 基于redis的 list + 临时unack的set队列，使用超时多少秒没确认消费就自动重回队列，请注意 ack_timeout的设置值和函数耗时大小，否则会发生反复重回队列的后果,boost可以设置ack超时，broker_exclusive_config={'ack_timeout': 1800}.缺点是无法区分执行太慢还是真宕机
    REDIS_PRIORITY = 'REDIS_PRIORITY'  # # 基于redis的多 list + 临时unack的set队列，blpop监听多个key，和rabbitmq的x-max-priority属性一样，支持任务优先级。看文档4.29优先级队列说明。
    REDIS_STREAM = 'REDIS_STREAM'  # 基于redis 5.0 版本以后，使用 stream 数据结构作为分布式消息队列，支持消费确认和持久化和分组消费，是redis官方推荐的消息队列形式，比list结构更适合。
    RedisBrpopLpush = 'RedisBrpopLpush'  # 基于redis的list结构但是采用brpoplpush 双队列形式，和 redis_ack_able的实现差不多，实现上采用了原生命令就不需要lua脚本来实现取出和加入unack了。
    REDIS_PUBSUB = 'REDIS_PUBSUB'  # 基于redis 发布订阅的，发布一个消息多个消费者都能收到同一条消息，但不支持持久化

    MEMORY_QUEUE = 'MEMORY_QUEUE'  # 使用python queue.Queue实现的基于当前python进程的消息队列，不支持跨进程 跨脚本 跨机器共享任务，不支持持久化，适合一次性短期简单任务。
    LOCAL_PYTHON_QUEUE = MEMORY_QUEUE  # 别名，python本地queue就是基于python自带的语言的queue.Queue，消息存在python程序的内存中，不支持重启断点接续。

    RABBITMQ_PIKA = 'RABBITMQ_PIKA'  # 使用pika包操作rabbitmq  作为 分布式消息队列。，不建议使用

    MONGOMQ = 'MONGOMQ'  # 使用mongo的表中的行模拟的 作为分布式消息队列，支持消费确认。

    SQLITE_QUEUE = 'sqlite3'  # 使用基于sqlite3模拟消息队列，支持消费确认和持久化，但不支持跨机器共享任务，可以基于本机单机跨脚本和跨进程共享任务，好处是不需要安装中间件。
    PERSISTQUEUE = SQLITE_QUEUE  # PERSISTQUEUE的别名

    NSQ = 'NSQ'  # 基于nsq作为分布式消息队列，支持消费确认。

    KAFKA = 'KAFKA'  # 基于kafka作为分布式消息队列，如果随意重启会丢失消息，建议使用BrokerEnum.CONFLUENT_KAFKA。

    """基于confluent-kafka包，包的性能比kafka-python提升10倍。同时应对反复随意重启部署消费代码的场景，此消费者实现至少消费一次，第8种BrokerEnum.KAFKA是最多消费一次。"""
    KAFKA_CONFLUENT = 'KAFKA_CONFLUENT'
    CONFLUENT_KAFKA = KAFKA_CONFLUENT

    KAFKA_CONFLUENT_SASlPlAIN = 'KAFKA_CONFLUENT_SASlPlAIN'  # 可以设置账号密码的kafka

    SQLACHEMY = 'SQLACHEMY'  # 基于SQLACHEMY 的连接作为分布式消息队列中间件支持持久化和消费确认。支持mysql oracle sqlserver等5种数据库。

    ROCKETMQ = 'ROCKETMQ'  # 基于 rocketmq 作为分布式消息队列，这个中间件必须在linux下运行，win不支持。

    ZEROMQ = 'ZEROMQ'  # 基于zeromq作为分布式消息队列，不需要安装中间件，可以支持跨机器但不支持持久化。

    """
    kombu 和 celery 都是 funboost中的神级别broker_kind。
    使得funboost以逸待劳，支持kombu的所有现有和未来的消息队列。
    通过直接支持 kombu，funboost 相当于一瞬间就继承了 `kombu` 支持的所有现有和未来的消息队列能力。
    无论 kombu 社区未来增加了对哪种新的云消息服务（如 Google Pub/Sub、Azure Service Bus）或小众 MQ 
    的支持，funboost 无需修改自身代码，就能自动获得这种能力。这是一种“以逸待劳”的策略，极大地扩展了 funboost 的适用范围。


    kombu 包可以作为funboost的broker，这个包也是celery的中间件依赖包，这个包可以操作10种中间件(例如rabbitmq redis)，但没包括分布式函数调度框架的kafka nsq zeromq 等。
    同时 kombu 包的性能非常差，可以用原生redis的lpush和kombu的publish测试发布，使用brpop 和 kombu 的 drain_events测试消费，对比差距相差了5到10倍。
    由于性能差，除非是分布式函数调度框架没实现的中间件才选kombu方式(例如kombu支持亚马逊队列  qpid pyro 队列)，否则强烈建议使用此框架的操作中间件方式而不是使用kombu。
    """
    KOMBU = 'KOMBU'

    """ 基于emq作为中间件的。这个和上面的中间件有很大不同，服务端不存储消息。所以不能先发布几十万个消息，然后再启动消费。mqtt优点是web前后端能交互，
    前端不能操作redis rabbitmq kafka，但很方便操作mqtt。这种使用场景是高实时的互联网接口。
    """
    MQTT = 'MQTT'

    HTTPSQS = 'HTTPSQS'  # httpsqs中间件实现的，基于http协议操作，dcoker安装此中间件简单。

    PULSAR = 'PULSAR'  # 最有潜力的下一代分布式消息系统。5年后会同时取代rabbitmq和kafka。

    UDP = 'UDP'  # 基于socket udp 实现的，需要先启动消费端再启动发布，支持分布式但不支持持久化，好处是不需要安装消息队列中间件软件。

    TCP = 'TCP'  # 基于socket tcp 实现的，需要先启动消费端再启动发布，支持分布式但不支持持久化，好处是不需要安装消息队列中间件软件。

    HTTP = 'HTTP'  # 基于http实现的，发布使用的urllib3，消费服务端使用的aiohttp.server实现的，支持分布式但不支持持久化，好处是不需要安装消息队列中间件软件。

    NATS = 'NATS'  # 高性能中间件nats,中间件服务端性能很好,。

    TXT_FILE = 'TXT_FILE'  # 磁盘txt文件作为消息队列，支持单机持久化，不支持多机分布式。不建议这个，用sqlite。

    PEEWEE = 'PEEWEE'  # peewee包操作mysql，使用表模拟消息队列

    CELERY = 'CELERY'  # funboost支持celery框架来发布和消费任务，由celery框架来调度执行任务，但是写法简单远远暴击用户亲自使用celery的麻烦程度，
    # 用户永无无需关心和操作Celery对象实例,无需关心celery的task_routes和include配置,funboost来自动化设置这些celery配置。
    # funboost将Celery本身纳入了自己的Broker体系。能“吞下”另一个大型框架，简直太妙了。本身就证明了funboost架构的包容性和精妙性和复杂性。

    DRAMATIQ = 'DRAMATIQ'  # funboost使用 dramatiq 框架作为消息队列，dramatiq类似celery也是任务队列框架。用户使用funboost api来操作dramatiq核心调度。

    HUEY = 'HUEY'  # huey任务队列框架作为funboost调度核心

    RQ = 'RQ'  # rq任务队列框架作为funboost调度核心

    NAMEKO = 'NAMEKO'  # funboost支持python微服务框架nameko，用户无需掌握nameko api语法，就玩转python nameko微服务

```

```
你项目根目录下自动生成的 funboost_config.py 文件中修改配置，会被自动读取到。

此文件按需修改，例如你使用redis中间件作为消息队列，可以不用管rabbitmq mongodb kafka啥的配置。
但有3个功能例外，如果你需要使用rpc模式或者分布式控频或者任务过滤功能，无论设置使用何种消息队列中间件都需要把redis连接配置好，
如果@boost装饰器设置is_using_rpc_mode为True或者 is_using_distributed_frequency_control为True或do_task_filtering=True则需要把redis连接配置好，默认是False。

```
## 3.2 框架支持的函数调度并发模式种类详细介绍
<pre style="font-size: smaller">
1、threading 多线程，使用自定义的可缩小、节制开启新线程的自定义线程池，不是直接用官方内置concurrent.futures.ThreadpoolExecutor
   此线程池非常智能，配合qps参数，任何场景可以无脑开500线程，真正的做到智能扩张，智能自动缩小。
   这线程池是智能线程池，由于非常好用，为这个线程池做了独立的pypi包，可以单独用于没有使用此框架的项目。

2、gevent    需要在运行起点的脚本首行打 gevent 猴子补丁。

3、eventlet  需要在运行起点的脚本首行打 eventlet 猴子补丁。

4、asyncio  async异步，主要是针对消费函数已经定义成了   async def fun(x)  这种情况，这种情况不能直接使用多线程，
   因为执行  fun(1)  后得到的并不是所想象的函数最终结果，而是得到的一个协程对象，所以针对已经定义成异步函数了的，需要使用此种并发模式。
   框架不鼓励用户定义异步函数，你就用同步的直观方式思维定义函数就行了，其余的并发调度交给框架就行了。

5、开启多进程启动多个consumer，此模式是 多进程  + 上面4种的其中一种并发方式，充分利用多核和充分利用io，用法如下。可以实现 多进程 叠加 协程并发。
# 这种是多进程方式，一次编写能够兼容win和linux的运行。

from funboost import boost, BrokerEnum, ConcurrentModeEnum
import os

@boost('test_multi_process_queue',broker_kind=BrokerEnum.REDIS_ACK_ABLE,
           concurrent_mode=ConcurrentModeEnum.THREADING,)
def fff(x):
    print(x * 10,os.getpid())

if __name__ == '__main__':
    fff.multi_process_consume(6)  # 一次性启动6进程叠加多线程。

</pre>

## 3.3 框架最最重要的boost装饰器的BoosterParams参数入参大全

```python
class BoosterParams(BaseJsonAbleModel):
    """
    pydatinc pycharm编程代码补全,请安装 pydantic插件, 在pycharm的  file -> settings -> Plugins -> 输入 pydantic 搜索,点击安装 pydantic 插件.

    @boost的传参必须是此类或者继承此类,如果你不想每个装饰器入参都很多,你可以写一个子类继承BoosterParams, 传参这个子类,例如下面的 BoosterParamsComplete
    """

    queue_name: str  # 队列名字,必传项,每个函数要使用不同的队列名字.
    broker_kind: str = BrokerEnum.SQLITE_QUEUE  # 中间件选型见3.1章节 https://funboost.readthedocs.io/zh-cn/latest/articles/c3.html

    """如果设置了qps，并且cocurrent_num是默认的50，会自动开了500并发，由于是采用的智能线程池任务少时候不会真开那么多线程而且会自动缩小线程数量。具体看ThreadPoolExecutorShrinkAble的说明
    由于有很好用的qps控制运行频率和智能扩大缩小的线程池，此框架建议不需要理会和设置并发数量只需要关心qps就行了，框架的并发是自适应并发数量，这一点很强很好用。"""
    concurrent_mode: str = ConcurrentModeEnum.THREADING  # 并发模式,支持THREADING,GEVENT,EVENTLET,ASYNC,SINGLE_THREAD并发,multi_process_consume 支持协程/线程 叠加多进程并发,性能炸裂.
    concurrent_num: int = 50  # 并发数量，并发种类由concurrent_mode决定
    specify_concurrent_pool: typing.Optional[FunboostBaseConcurrentPool] = None  # 使用指定的线程池/携程池，可以多个消费者共使用一个线程池,节约线程.不为None时候。threads_num失效
    specify_async_loop: typing.Optional[asyncio.AbstractEventLoop] = None  # 指定的async的loop循环，设置并发模式为async才能起作用。 有些包例如aiohttp,发送请求和httpclient的实例化不能处在两个不同的loop中,可以传过来.

    """qps:
    强悍的控制功能,指定1秒内的函数执行次数，例如可以是小数0.01代表每100秒执行一次，也可以是50代表1秒执行50次.为None则不控频。 设置qps时候,不需要指定并发数量,funboost的能够自适应智能动态调节并发池大小."""
    qps: typing.Union[float, int, None] = None
    """is_using_distributed_frequency_control:
    是否使用分布式空频（依赖redis统计消费者数量，然后频率平分），默认只对当前实例化的消费者空频有效。假如实例化了2个qps为10的使用同一队列名的消费者，并且都启动，则每秒运行次数会达到20。
    如果使用分布式空频则所有消费者加起来的总运行次数是10。"""
    is_using_distributed_frequency_control: bool = False

    is_send_consumer_hearbeat_to_redis: bool = False  # 是否将发布者的心跳发送到redis，有些功能的实现需要统计活跃消费者。因为有的中间件不是真mq。这个功能,需要安装redis.

    """max_retry_times:
    最大自动重试次数，当函数发生错误，立即自动重试运行n次，对一些特殊不稳定情况会有效果。
    可以在函数中主动抛出重试的异常ExceptionForRetry，框架也会立即自动重试。
    主动抛出ExceptionForRequeue异常，则当前 消息会重返中间件，
    主动抛出 ExceptionForPushToDlxqueue  异常，可以使消息发送到单独的死信队列中，死信队列的名字是 队列名字 + _dlx。"""
    max_retry_times: int = 3
    retry_interval: typing.Union[float, int] = 0  # 函数出错后间隔多少秒再重试.
    is_push_to_dlx_queue_when_retry_max_times: bool = False  # 函数达到最大重试次数仍然没成功，是否发送到死信队列,死信队列的名字是 队列名字 + _dlx。


    consumin_function_decorator: typing.Optional[typing.Callable] = None  # 函数的装饰器。因为此框架做参数自动转指点，需要获取精准的入参名称，不支持在消费函数上叠加 @ *args  **kwargs的装饰器，如果想用装饰器可以这里指定。
    function_timeout: typing.Union[int, float,None] = None  # 超时秒数，函数运行超过这个时间，则自动杀死函数。为0是不限制。 谨慎使用,非必要别去设置超时时间,设置后性能会降低(因为需要把用户函数包装到另一个线单独的程中去运行),而且突然强制超时杀死运行中函数,可能会造成死锁.(例如用户函数在获得线程锁后突然杀死函数,别的线程再也无法获得锁了)

    """
    log_level:
        logger_name 对应的 日志级别
        消费者和发布者的日志级别,建议设置DEBUG级别,不然无法知道正在运行什么消息.
        这个是funboost每个队列的单独命名空间的日志级别,不会影响改变用户其他日志以及root命名空间的日志级别,所以DEBUG级别就好,
        用户不要不懂什么是python logger 的name,还去手痒调高级别. 
        不懂python日志命名空间的小白去看nb_log文档,或者直接问ai python logger name的作用是什么.
    """
    log_level: int = logging.DEBUG  
    logger_prefix: str = ''  # 日志名字前缀,可以设置前缀
    create_logger_file: bool = True  # 发布者和消费者是否创建文件文件日志,为False则只打印控制台不写文件.
    logger_name: str = ''  # 队列消费者发布者的日志命名空间.
    log_filename: typing.Union[str, None] = None  # 消费者发布者的文件日志名字.如果为None,则自动使用 funboost.队列 名字作为文件日志名字.  日志文件夹是在nb_log_config.py的 LOG_PATH中决定的.
    is_show_message_get_from_broker: bool = False  # 运行时候,是否记录从消息队列获取出来的消息内容
    is_print_detail_exception: bool = True  # 消费函数出错时候,是否打印详细的报错堆栈,为False则只打印简略的报错信息不包含堆栈.

    msg_expire_senconds: typing.Union[float, int,None] = None  # 消息过期时间,可以设置消息是多久之前发布的就丢弃这条消息,不运行. 为None则永不丢弃

    do_task_filtering: bool = False  # 是否对函数入参进行过滤去重.
    task_filtering_expire_seconds: int = 0  # 任务过滤的失效期，为0则永久性过滤任务。例如设置过滤过期时间是1800秒 ， 30分钟前发布过1 + 2 的任务，现在仍然执行，如果是30分钟以内执行过这个任务，则不执行1 + 2

    function_result_status_persistance_conf: FunctionResultStatusPersistanceConfig = FunctionResultStatusPersistanceConfig(
        is_save_result=False, is_save_status=False, expire_seconds=7 * 24 * 3600, is_use_bulk_insert=False)  # 是否保存函数的入参，运行结果和运行状态到mongodb。这一步用于后续的参数追溯，任务统计和web展示，需要安装mongo。

    user_custom_record_process_info_func: typing.Optional[typing.Callable] = None  # 提供一个用户自定义的保存消息处理记录到某个地方例如mysql数据库的函数，函数仅仅接受一个入参，入参类型是 FunctionResultStatus，用户可以打印参数

    is_using_rpc_mode: bool = False  # 是否使用rpc模式，可以在发布端获取消费端的结果回调，但消耗一定性能，使用async_result.result时候会等待阻塞住当前线程。
    rpc_result_expire_seconds: int = 600  # 保存rpc结果的过期时间.

    delay_task_apscheduler_jobstores_kind :Literal[ 'redis', 'memory'] = 'redis'  # 延时任务的aspcheduler对象使用哪种jobstores ，可以为 redis memory 两种作为jobstore

    is_support_remote_kill_task: bool = False  # 是否支持远程任务杀死功能，如果任务数量少，单个任务耗时长，确实需要远程发送命令来杀死正在运行的函数，才设置为true，否则不建议开启此功能。(是把函数放在单独的线程中实现的,随时准备线程被远程命令杀死,所以性能会降低)

    is_do_not_run_by_specify_time_effect: bool = False  # 是否使不运行的时间段生效
    do_not_run_by_specify_time: tuple = ('10:00:00', '22:00:00')  # 不运行的时间段,在这个时间段自动不运行函数.

    schedule_tasks_on_main_thread: bool = False  # 直接在主线程调度任务，意味着不能直接在当前主线程同时开启两个消费者。

    is_auto_start_consuming_message: bool = False  # 是否在定义后就自动启动消费，无需用户手动写 .consume() 来启动消息消费。

    consuming_function: typing.Optional[typing.Callable] = None  # 消费函数,在@boost时候不用指定,因为装饰器知道下面的函数.
    consuming_function_raw: typing.Optional[typing.Callable] = None  # 不需要传递，自动生成
    consuming_function_name: str = '' # 不需要传递，自动生成

    

    broker_exclusive_config: dict = {}  # 加上一个不同种类中间件非通用的配置,不同中间件自身独有的配置，不是所有中间件都兼容的配置，因为框架支持30种消息队列，消息队列不仅仅是一般的先进先出queue这么简单的概念，
    # 例如kafka支持消费者组，rabbitmq也支持各种独特概念例如各种ack机制 复杂路由机制，有的中间件原生能支持消息优先级有的中间件不支持,每一种消息队列都有独特的配置参数意义，可以通过这里传递。每种中间件能传递的键值对可以看consumer类的 BROKER_EXCLUSIVE_CONFIG_DEFAULT

    should_check_publish_func_params: bool = True  # 消息发布时候是否校验消息发布内容,比如有的人发布消息,函数只接受a,b两个入参,他去传2个入参,或者传参不存在的参数名字; 如果消费函数加了装饰器 ，你非要写*args,**kwargs,那就需要关掉发布消息时候的函数入参检查
    publish_msg_log_use_full_msg: bool = False # 发布到消息队列的消息内容的日志，是否显示消息的完整体，还是只显示函数入参。

    consumer_override_cls: typing.Optional[typing.Type] = None  # 使用 consumer_override_cls 和 publisher_override_cls 来自定义重写或新增消费者 发布者,见文档4.21b介绍，
    publisher_override_cls: typing.Optional[typing.Type] = None

    # func_params_is_pydantic_model: bool = False  # funboost 兼容支持 函数娼还是 pydantic model类型，funboost在发布之前和取出来时候自己转化。

    consuming_function_kind: typing.Optional[str] = None  # 自动生成的信息,不需要用户主动传参,如果自动判断失误就传递。是判断消费函数是函数还是实例方法还是类方法。如果传递了，就不自动获取函数类型。
    """ consuming_function_kind 可以为以下类型，
    class FunctionKind:
        CLASS_METHOD = 'CLASS_METHOD'
        INSTANCE_METHOD = 'INSTANCE_METHOD'
        STATIC_METHOD = 'STATIC_METHOD'
        COMMON_FUNCTION = 'COMMON_FUNCTION'
    """

    auto_generate_info: dict = {}  # 自动生成的信息,不需要用户主动传参.

   
```
 
关于boost参数太多的说明：

```
有人会抱怨入参超多很复杂，是因为要实现一切控制方式，实现的运行控制手段非常丰富，所以参数就会多。

看这个里面的参数解释非常重要，几乎能想到的控制功能全部都有。比如有人说日志太多，不想看那么详细的提示日志
，早就通过参数提供实现了，自己抱怨参数多又以为没提供这个功能，简直是自相矛盾。

想入参参数少那就看新增的那个10行代码的函数的最精简乞丐版实现的分布式函数执行框架，演示最本质实现原理。“ 
这个例子的框架啥控制手段都没有，参数自然就很少。

乞丐版分布式函数调度框架的代码在 

funboost/beggar_version_implementation/beggar_redis_consumer.py
```



## 3.3.2 funboost 重要公有方法大全介绍

仔细看以下代码注释，函数的功能
```python
import json
import time

from funboost import boost, BrokerEnum,PriorityConsumingControlConfig,BoosterParams


@boost(BoosterParams(queue_name='queue1', broker_kind=BrokerEnum.REDIS, qps=0.2))
def f(x, y):
    return x + y


@boost(BoosterParams(queue_name='queue2', broker_kind=BrokerEnum.REDIS, qps=7))
def f2(a, b):
    return a - b


if __name__ == '__main__':
    f.clear()  # 清空f函数对应的queue1所有消息
    for i in range(10):
        f.push(i, i * 2)  # 使用push发布消息到queue1，push的入参和正常调用函数一样
        f2.publish({'a': i, 'b': i * 2},priority_control_config=PriorityConsumingControlConfig(msg_expire_senconds=30))  # # 使用publish发布消息到queue2，publish的入参第一个参数是一个字典，把所有参数组成一个字典，还可以传入其他参数。publish更强大。

    print(f.get_message_count())  # 获取消息队列中的消息数量
    f.consume()  # 在当前进程启动多线程/协程消费
    f2.multi_process_consume(3)  # 启动3个进程，每个进程内部都启动多线程/协程消费，性能炸裂。

```

```
重要方法就是 @boost装饰器的入参，被@boost装饰的消费函数自动有funboost框架的功能
其中最常见的是：
push，推送消息到消息队列
consume， 在当前进程启动多线程/协程消费
multi_process_consume(n) ，启动多个进程，每个进程内部叠加多线程/协程，性能更强.

```

冷门方法
```
除以上方法外，还有其他的不常用的方法，在第四章有介绍，
在pycharm中可以代码补全有哪些方法，自己按照方法名字就能猜出是什么意思了。也可以点进去boost装饰器里面去，里面有每个方法的注释说明。
例如 f.pause_consume() 可以从python解释器的外部远程，让已经启动queue1的消费函数停止消费，f.continue_consume() 继续消费。
```



## 3.3.3 boost装饰器 的 concurrent_num 和 qps 之间的关系。

```
 concurrent_num:并发数量。
    qps qps是有个很有趣的参数，能精确控制函数每秒运行多少次。
    concurrent_num和qps存在着一定的关系。
    
    例如对于下面这个函数
    
    def func(x):
           time.sleep(2)
           print(x）

    1）如果设置 concurrent_num = 1000(或100万)  qps = 10
    那么一秒钟会执行10次func函数。如果不指定qps的值，则不进行控频，消费框架会平均每秒钟会执行50次函数func。

    如果设置concurrent_num = 1000  qps = 5   
    那么一秒钟会执行5次func函数。所以可以看到，当你不知道要开多少并发合适的时候，可以粗暴开1000个线程，但要设置一个qps。
   
    那为什么次框架，可以让你粗暴的设置1000设置100万线程呢，并不是做了数字截取，判断线程设置大于多少就自动调小了，此消费框架并没有这样去实现。
    而是次框架使用的非concurrent.tutures.ThreadpoolExecutor，是使用的自定义的  ThreadPoolExecutorShrinkAble 线程池，
    此线程池其中之一的功能就是节制开更多的线程，因为对于上面的休眠2秒的func函数，如果设置concurrent_num = 1000000  qps = 5，
    正常来说开10个线程足够实现每秒执行5次了，此框架在调节线程新增线程时候进行了更多的判断，所以原生线程池不可以设置100万大小，
    而ThreadPoolExecutorShrinkAble可以设置为100万大小。

    此外ThreadPoolExecutorShrinkAble 实现了线程池自动缩小的功能，这也是原生concurrent.tutures.ThreadpoolExecutor没有的功能。
    自动缩小是什么意思呢，比如一段时间任务非常密集1秒钟来了几百个任务，所以当时开启了很多线程来应付，但一段时间后每分钟只来了个把任务，
    此时 ThreadPoolExecutorShrinkAble 能够自动缩小线程池，
    ThreadPoolExecutorShrinkAble实现了java ThreadpoolExecutor的KeepAliveTime参数的功能，
    原生concurrent.tutures.ThreadpoolExecutor线程池即使以后永久不来新任务，之前开的线程数量一致保持这。

    关于 ThreadPoolExecutorShrinkAble 的厉害之处，可以参考 https://github.com/ydf0509/threadpool_executor_shrink_able
    
    最终关于 concurrent_num 大小设置为多少，看自己需求，上面说的100万是举个例子，
    实际这个参数还被用作为线程池的任务队列的有界队列的大小，所以一定要设置为1000以下，否则如果设置为100万，
    从消息中间件预取出的消息过多，造成python内存大、单个消费者掏空消息队列中间件造成别的新启动的消费者无任务可消费、
    对于不支持消费确认类型的中间件的随意重启会丢失大量正在运行的任务 等不利影响。

    2）上面的func函数，设置 concurrent_num = 1  qps = 100，那会如何呢？
       由于你设置的并发是1,对于一个需要2秒运行完成的函数，显然平均每2秒才能执行1次，就是框架真正的只能达到0.5个qps。
       所以 concurrent_num 和 qps，既有关系，也不是绝对的关系。
    
    在对一个随机消耗时间的函数进行并发控制时候，如果函数的运行时间是0.5到20秒任意时间不确定的徘徊，你可以设置 concurrent_num = 100,
    如果合作方要求了只能1秒钟能让你使用多少次，例如需要精确控频10次，可以设置qps =10，concurrent_num随便搞个 一两百 两三百就行了,
    因为是智能的克制的调节线程池大小的，所以不会真的达到concurrent_num的值。

    3）qps是个小数可以小于1，如果要设置10秒执行一次函数，则设置qps=0.1

    这主要是介绍了 concurrent_num 和qps的关系和设置值,qps是优先，但受到concurrent_num的约束。
```

## 3.4 框架的乞丐精简版实现方式

由于框架的功能十分多，如果没学习36种设计模式，就很难看懂源码，现在演示精简实现原理

此精简例子十分之简单明了，就是死循环从中间件取任务然后丢到线程池里面执行。

此代码在 funboost/beggar_version_implementation/beggar_redis_consumer.py

这样简单明了，演示了基本原理，但是这个缺少消费确认(随意重启代码会造成大量任务丢失) qps恒定等20种功能。

```python
def start_consuming_message(queue_name, consume_function, threads_num=50):
    pool = ThreadPoolExecutor(threads_num)
    while True:
        try:
            redis_task = redis.brpop(queue_name, timeout=60)
            if redis_task:
                task_str = redis_task[1].decode()
                print(f'从redis的 {queue_name} 队列中 取出的消息是： {task_str}')
                pool.submit(consume_function, **json.loads(task_str))
            else:
                print(f'redis的 {queue_name} 队列中没有任务')
        except redis.RedisError as e:
            print(e)


if __name__ == '__main__':
    import time


    def add(x, y):
        time.sleep(5)
        print(f'{x} + {y} 的结果是 {x + y}')

    # 推送任务
    for i in range(100):
        print(i)
        redis.lpush('test_beggar_redis_consumer_queue', json.dumps(dict(x=i, y=i * 2)))


    start_consuming_message('test_beggar_redis_consumer_queue', consume_function=add, threads_num=10)
```

## 3.5 框架的任务消费确认

<pre>
此框架可以确保客户端任何时候 随意断电 粗暴重启代码 随意关机，任务万无一失。

3.4演示的精简版框架，实现redis的list的push和pop来模拟消息队列，很明显不靠谱，kill 9 重启代码或者重启电脑很容易会丢失大量任务。

分布式一致性消息传递、事件处理等场景中十分重要，分为3种情况：
At most Onece：最多一次，如果算子处理事件失败，算子将不再尝试该事件。
At Least Onece：至少一次，如果算子处理事件失败，算子会再次尝试该处理事件，直到有一次成功。
Exactly-Once：严格地，有且仅处理一次，通常有两种方法实现。

3.4实现的是最多一次，框架在多种中间件使用消费确认实现了万无一失 ，达到了Exactly-Once。
Exactly-Once是最好的也是实现难度最复杂的；At most Onece通常是最差的方式，也是最简单的实现方式。

框架在使用rabbitmq，内置默认了确认消费。

框架在使用redis作为中间件时候，有很多种实现方式，REDIS 是最不靠谱的会丢失消息。
REDIS_ACK_ABLE 、 REDIS_STREAM、 RedisBrpopLpush BrokerKind 这三种都是实现了确认消费。

</pre>


## 3.6 框架的设计规范原则

因为使用了oop编程和良好的设计模式，所以 funboost 很容易新增任意消息队列类型以及任何消费框架 作为 funboost的 broker_kind。
目前没遇到集成不到funboost的消息队列类型和消费框架。

```
源码实现思路基本90%遵守了oop的6个设计原则，很容易扩展中间件。
1、单一职责原则——SRP
2、开闭原则——OCP
3、里式替换原则——LSP
4、依赖倒置原则——DIP
5、接口隔离原则——ISP
6、迪米特原则——LOD

最主要是大量使用了模板模式、工厂模式、策略模式、鸭子类。
可以仿照源码中实现中间件的例子，只需要继承发布者、消费者基类后实现几个抽象方法即可添加新的中间件。
```

<div> </div>
# 4.使用框架的各种代码示例

框架极其简单并且自由，只有一个boost装饰器的参数学习， 实际上这个章节所有的例子都是调整了一下boost的参数而已。

有一点要说明的是框架的消息中间件的ip 端口 密码 等配置是在你第一次随意运行代码时候，在你当前项目的根目录下生成的 funboost_config.py 按需设置。

所有例子的发布和消费都没必须写在同一个py文件，(除了使用python 自带语言queue)，因为是使用中间件解耦的消息，好多人误以为发布和消费必须在同一个python文件。

## 4.0 框架最重要的@boost装饰器的入参格式说明

### 4.0.1 老的 @booost 直接传入多个参数方式

以下是老的入参方式:
@boost(queue_test_f01', qps=0.2,broker_kind=BrokerEnum.REDIS_ACK_ABLE,)

40.0版本之前是老的入参方式,直接在@booost传很多个参数,40.0版本之后你仍然可以这么传参,但是不太推荐,因为不能代码补全函数入参了.

### 4.0.2 新的@ boost 只传入一个 pydantic Model BoostParams 类型或子类 的入参

新的@ boost 只传入一个 BoostParams 类型或子类 的入参 ,入参类型是 非常流行的 pydantic包的 model类型.

@boost(BoosterParams(queue_name='queue_test_f01', qps=0.2,broker_kind=BrokerEnum.REDIS_ACK_ABLE,))

因为采用pydantic,可以在框架开发时候,减少很多一大推重复入参声明,因为作者很注重代码补全,
作者不想直接 *args **kwargs暴露给用户,这种会导致用户不知道应该传参什么,pycharm也无法补全,所以需要大量重复的声明,每次加入参,都需要很多地方去修改,
所以改为使用流行的 pydantic 包来实现入参,fastapi的入参声明就是使用pydantic,非常棒.

### 4.0.3 pydantic model 的 BoosterParams 的入参pycharm下自动补全

```
因为BoosterParams这个pydantic model 类没有 __init__(self,一堆参数) ,而是把类变量,转化成实例变量,
所以直接对BoostParams传参是无法代码补全的,需要用户在pycharm的Plugins安装一个pydantic的插件,这样就能敲击入参自动补全入参名字了.

pydatinc pycharm编程代码补全,请安装 pydantic插件, 在pycharm的  file -> settings -> Plugins -> 输入 pydantic 搜索,
点击安装 pydantic 插件.
```

![pydantic_install.png](pydantic_install.png)

### 4.0.4 关于很多funboost 例子的@boost 使用直接入参,没有使用 pydantic Model类型的BoostParams

因为是兼容老的写法的,老的直接入参仍然可以正常运行,所以例子中没有修改成 @boost(BoosterParams(...)) 入参方式,
用户知道就行.

### 4.0.5 自定义子类继承 BoosterParams,使得每次少传参

```python
import logging
import time
from funboost import boost, BrokerEnum, BoosterParams


class BoosterParamsMy(BoosterParams): # 传这个类就可以少每次都亲自指定使用rabbitmq作为消息队列，和重试改为4次,和消费发布日志写入自定义.log文件。
    broker_kind : str = BrokerEnum.RABBITMQ  
    max_retry_times : int =4
    log_level :int = logging.DEBUG
    log_filename : str ='自定义.log'

@boost(boost_params=BoosterParamsMy(queue_name='task_queue_name1d',  qps=3,))
def task_fun(x, y):
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 3 次 这个 task_fun 函数的目的。
  

@boost(boost_params=BoosterParamsMy(queue_name='task_queue_name1d', qps=10,))
def task_fun2(x, y):
    print(f'{x} - {y} = {x - y}')
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 10 次 这个 task_fun 函数的目的。


if __name__ == "__main__":
    task_fun.consume()  # 消费者启动循环调度并发消费任务
    task_fun2.consume()
    for i in range(10):
        task_fun.push(i, y=i * 2)  # 发布者发布任务
        task_fun2.push(i,i*10)
```

## 4.1 装饰器方式调度函数

```python
from funboost import boost, BrokerEnum,BoosterParams


# qps可以指定每秒运行多少次，可以设置0.001到10000随意。
# broker_kind 指定使用什么中间件，如果用redis，就需要在 funboost_config.py 设置redis相关的配置。
@boost(BoosterParams(queue_name='queue_test_f01', qps=0.2,
       broker_kind=BrokerEnum.REDIS_ACK_ABLE,))  # qps 0.2表示每5秒运行一次函数，broker_kind=2表示使用redis作中间件。
def add(a, b):
    print(a + b)


if __name__ == '__main__':
    for i in range(10, 20):
        add.publish(dict(a=i, b=i * 2))  # 使用add.publish 发布任务
        add.push(i, b=i * 2)  # 使用add.push 发布任务
    add.consume()  # 使用add.consume 消费任务
    # add.multi_process_consume(4)  # 这是开启4进程 叠加 细粒度(协程/线程)并发，速度更强。
```

## 4.2a 非装饰器调度函数,方式一，(现在非常不推荐直接用get_consumer写代码,这样跳过了一些步骤,应该推荐用4.2c方式)

#### 如果你不想使用@boost装饰器，最推荐的是4.2.c的  BoostersManager.build_booster 方式

```
有的人动态生成消费者，queue_name或者其他装饰器入参是动态的，无法在代码里面提前写死。可以这样。

最开始框架就没有装饰器，一开始是这么使用的get_consumer，利用工厂模式生成不同中间件类型的消费者。这个更接近本质使用。
boost装饰器使用方式是在后来时候才设计加上的。
```

```python
from funboost import get_consumer, BrokerEnum,BoosterParams


def add(a, b):
    print(a + b)


# 非装饰器方式，多了一个入参，需要手动指定consuming_function入参的值。
consumer = get_consumer(BoosterParams(queue_name='queue_test_f01', consuming_function=add, qps=0.2, broker_kind=BrokerEnum.REDIS_ACK_ABLE))

if __name__ == '__main__':
    for i in range(10, 20):
        consumer.publisher_of_same_queue.publish(dict(a=i, b=i * 2))  # consumer.publisher_of_same_queue.publish 发布任务
    consumer.start_consuming_message()  # 使用consumer.start_consuming_message 消费任务
```

## 4.2b 非装饰器调度函数,方式二，(非装饰器使用,这是装饰器的本质用法)

```
只要python装饰器基础知识本质 掌握得好，这种就能想得出来。
这种不是框架实现的方式，是装饰器本质就是这样的。
建议这样做写，这样和装饰器方式的文档演示的 使用方式更加的一致。
```

```python
from funboost import boost,Booster,ConcurrentModeEnum,BoosterParams


def add(a, b):
    print(a + b)

# deco(a=100)(f)(x=1,y=2)的结果  和f被deco(100)装饰 然后f(x=1,y=2)效果是一样的，这是装饰器基本本质，这里不展开啰嗦了。
add_boost = boost(BoosterParams(queue_name='queue_test_f01b',  qps=0.2,concurrent_mode= ConcurrentModeEnum.THREADING))(add)   # type: Booster


if __name__ == '__main__':
    for i in range(10, 20):
        add_boost.push(a=i, b=i * 2)  # consumer.publisher_of_same_queue.publish 发布任务
    add_boost.consume()  # 当前进程内启动消费,多线程消费
    add_boost.multi_process_consume(2) #  启动单独的2个进程叠加多线程并发
```

## 4.2c 在函数内部无限次按照队列名动态生成booster(消费者、生产者) (非装饰器)

BoostersManager.build_booster 方法。

用法:
booster = BoostersManager.build_booster(BoosterParams(queue_name=queue_name, qps=0.2, consuming_function=add))

1）如果是在函数内部按照不同的queue_name无限次动态生成booster，不能按照以下写代码

```python
from funboost import boost,Booster,ConcurrentModeEnum,BoosterParams


def add(a, b):
    print(a + b)

def my_push(quue_name,a,b):
    booster = boost(BoosterParams(queue_name=quue_name,  qps=0.2,concurrent_mode= ConcurrentModeEnum.THREADING))(add)   # type: Booster
    # 上面这行代码太惨了，在push函数里面无数次创建生产者、消费者和消息队列连接，造成cpu 内存和消息队列服务端压力巨大。
    booster.push(a,b)

for i in range(1000000):
    queue_namx = f'queue_{i%10}'
    my_push(queue_namx,i,i*2)
```

```
看到有的人这样写代码，这样太惨了，会使python内存和cpu高，会对消息队列服务器产生巨大压力。调用100万次push函数，生成100万次消费者 生产者，对消息队列中间件创建100万次连接。
这样写代码太惨了，会发生悲剧。
4.2b的代码例子是在全局变量里面只生成了一次booster，性能没问题。而上面这个代码是在push函数里面实例化100万次 Consumer和Publisher，太悲催了。

如果你需要动态按照队列名生成生产者消费者，根据入参发布到不同的队列名中，可以自己写个字典判断队列名对应的booster有没有创建过，也可以使用框架提供的 build_booster 函数。
```

2）如果是在函数内部无限次动态生成booster，应该使用 BoostersManager.build_booster

```
build_booster 是创建或者直接从全局变量字典中获取booster对象。

如果当前进程没有这个queue_name对应的booster对象就创建，有则直接使用已创建的booster对象。

下面假设动态生成10个队列名的booster对象，发布100万次消息不需要对消息队列中间件创建100万次连接。
```

```python
from funboost import Booster, BoostersManager,BoosterParams


def add(a, b):
    print(a + b)


def my_push(queue_name, a, b):
    booster = BoostersManager.build_booster(BoosterParams(queue_name=queue_name, qps=0.2, consuming_function=add))  # type: Booster
    # build_booster 这种就不会无数次去创建 消息队列连接了。有则直接使用，没有则创建。
    booster.push(a, b)


if __name__ == '__main__':
    for i in range(1000000):
        queue_namex = f'queue_{i % 10}'  # 动态的发布消息到 queue_0 queue_1 queue_2 queue_3 .... queue_9 队列中。
        my_push(queue_namex, i, i * 2)

    for j in range(10):  # 启动  queue_0 queue_1 queue_2 queue_3 .... queue_9 队列的消费者进行消费。
        booster = BoostersManager.build_booster(BoosterParams(queue_name=f'queue_{j}', qps=0.2,
                                                consuming_function=add))  # type: Booster
        booster.consume()

```

## 4.2d 框架的 BoostersManager boosters管理介绍

虽然funboost没有显式的需要你实例化一个app对象,但背后有BoostersManager来登记了所有booster
例如用户可以通过 BoostersManager 来知道你声明了哪些队列名.

```
所有@boost的或者 BoostersManager.build_booster 创建的booster都会登记到 BoostersManager.pid_queue_name__booster_map这里来
用户可以看到声明了哪些队列名

BoosterDiscovery(project_root_path: typing.Union[PathLike, str],
                 booster_dirs: typing.List[typing.Union[PathLike, str]],
                 max_depth=1, py_file_re_str: str = None).auto_discovery()   
可以扫描python文件夹自动导入模块,找到@boost函数


BoostersManager.get_or_create_booster_by_queue_name 可以根据队列名创建或者获得booster
```

### 4.2d.2 使用 BoostersManager 一次性启动所有队列消费,

(无需亲自 fun1.consume()  fun2.consume() fun100.consume())

假设:

代码文件夹结构如下:
![img_59.png](img_59.png)

具体完整代码可见:
[https://github.com/ydf0509/funboost/tree/master/test_frame/test_boosters_manager](https://github.com/ydf0509/funboost/tree/master/test_frame/test_boosters_manager)

mod1.py和mod2.py 文件一共有3个消费函数,如果用户不想亲自使用如下方式按需一个个函数的亲自启动消费,而是想粗暴的启动所有消费函数.那么可以使用 BoostersManager的 consume_all 或者 BoostersManager.m_consume_all(3) 这样启动.

```python
mod1.fun1.consume()
mod2.fun2a.consume()
mod2.fun2b.consume()
```

```python
from pathlib import Path

import queue_names
from funboost import BoostersManager, BoosterDiscovery

# import mod1, mod2  # 这个是必须导入的,可以不用,但必须导入,这样BoostersManager才能知道相关模块中的@boost装饰器,或者用下面的 BoosterDiscovery.auto_discovery()来自动导入m1和m2模块.


if __name__ == '__main__':
    """ 有的人不想这样写代码,一个个的函数亲自 .consume() 来启动消费,可以使用BoostersManager相关的方法来启动某些队列或者启动所有队列.
    mod1.fun1.consume()
    mod2.fun2a.consume()
    mod2.fun2b.consume()
    """
    BoosterDiscovery(project_root_path=Path(__file__).parent.parent.parent, booster_dirs=[Path(__file__).parent]).auto_discovery()  # 这个放在main里面运行,防止无限懵逼死循环

    # 选择启动哪些队列名消费
    # BoostersManager.consume(queue_names.q_test_queue_manager1,queue_names.q_test_queue_manager2a)

    # 选择启动哪些队列名消费,每个队列设置不同的消费进程数量
    # BoostersManager.m_consume(**{queue_names.q_test_queue_manager1: 2, queue_names.q_test_queue_manager2a: 3})

    # 启动所有队列名消费,在同一个进程内消费
    BoostersManager.consume_all()

    # 启动所有队列名消费,每个队列启动单独的n个进程消费
    # BoostersManager.m_consume_all(2)

```

### 4.2d.3 使用 BoostersManager ,通过queue_name 得到 booster对象

BoostersManager.get_booster(queue_name) 通过queue_name 获取 booster(被@boost装饰的函数)

## 4.2e funboost 支持实例方法、类方法、静态方法、普通函数 4种类型，作为消费函数的例子

funboost 在 2024年6月新增支持了实例方法、类方法作为消费函数 ，见文档4.32章节

## 4.3a 演示如何解决多个步骤的消费函数

看这个例子，step1函数中不仅可以给step2发布任务，也可以给step1自身发布任务。

qps规定了step1每2秒执行一次，step2每秒执行3次。

```python
import time

from funboost import boost, BrokerEnum,BoosterParams


@boost(BoosterParams(queue_name='queue_test_step1', qps=0.5, broker_kind=BrokerEnum.LOCAL_PYTHON_QUEUE))
def step1(x):
    print(f'x 的值是 {x}')
    if x == 0:
        for i in range(1, 300):
            step1.pub(dict(x=x + i))
    for j in range(10):
        step2.push(x * 100 + j)  # push是直接发送多个参数，pub是发布一个字典
    time.sleep(10)


@boost(BoosterParams(queue_name='queue_test_step2', qps=3, broker_kind=BrokerEnum.LOCAL_PYTHON_QUEUE))
def step2(y):
    print(f'y 的值是 {y}')
    time.sleep(10)


if __name__ == '__main__':
    # step1.clear()
    step1.push(0)  # 给step1的队列推送任务。

    step1.consume()  # 可以连续启动两个消费者，因为conusme是启动独立线程里面while 1调度的，不会阻塞主线程，所以可以连续运行多个启动消费。
    step2.consume()

```

## 4.3.b 演示多个函数消费者使用同一个线程池

```python
from funboost import boost,BoosterParams
from funboost.concurrent_pool.flexible_thread_pool import FlexibleThreadPool


"""
这个是演示多个不同的函数消费者，使用同一个全局的并发池。
如果一次性启动的函数过多，使用这种方式避免每个消费者创建各自的并发池，减少线程/协程资源浪费。
"""

# 总共那个有5种并发池，用户随便选。
pool = FlexibleThreadPool(300)  # 指定多个消费者使用同一个线程池，




# @boost('test_f1_queue', specify_concurrent_pool=pool, qps=3)  # 旧写法，直接在@boost传各种参数
@boost(BoosterParams(queue_name='test_f1_queue', specify_concurrent_pool=pool, qps=3)) # 新写法在BoosterParams传各种参数
def f1(x):
    print(f'x : {x}')


@boost(BoosterParams(queue_name='test_f2_queue', specify_concurrent_pool=pool, qps=2))
def f2(y):
    print(f'y : {y}')


@boost(BoosterParams(queue_name='test_f3_queue', specify_concurrent_pool=pool))
def f3(m, n):
    print(f'm : {m} , n : {n}')


if __name__ == '__main__':
    for i in range(1000):
        f1.push(i)
        f2.push(i)
        f3.push(i, 1 * 2)
    f1.consume()
    f2.consume()
    f3.consume()



```

## 4.3c 演示清空消息队列和获取消息队列中的消息数量

```
f2.clear()  清空消息队列

f2.get_message_count() 获取消息队中的消息数量，
不能使用 f2.get_message_count() =0 来判断消息队列没任务了以为该函数的所有消息被消费完成了，本地内存队列存储了
一部分消息和正在执行的也有一部分消息，如果要判断消费完成了，应该使用4.17章节的 判断函数运行完所有任务，再执行后续操作。
```

```python

@boost(BoosterParams(queue_name='test_queue77g', log_level=10, broker_kind=BrokerEnum.REDIS_ACK_ABLE, qps=5,
       create_logger_file=False, is_show_message_get_from_broker=True, concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD
       # specify_concurrent_pool= pool2,
       # concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD, concurrent_num=3,is_send_consumer_hearbeat_to_redis=True,function_timeout=10,
       # function_result_status_persistance_conf=FunctionResultStatusPersistanceConfig(True,True)
       ))
def f2(a, b):
    time.sleep(10)
    print(a, b)
    return a - b


if __name__ == '__main__':

    f2.clear()
    for i in range(8):
        f2.push(i, i * 5)
    print(f2.get_message_count())

    f2.clear()
    for i in range(20):
        f2.push(i, i * 2)
    print(f2.get_message_count())
```

## 4.4 演示funboost定时运行例子

ApsJobAdder(消费函数, job_store_kind='redis').add_push_job(....) 来添加定时任务.

ApsJobAdder实例化时候,会默认自动启动定时器,用户可以设置实例化时候是否 顺便 is_auto_paused 暂停执行  定时任务.

<pre class="warn">
警告!!!
ApsJobAdder(消费函数, job_store_kind='redis').add_push_job(....) 实际上是做了2件事情,
分别是 启动定时器 aps_obj.start() 和 添加定时任务 aps_obj.add_job(). 不要以为只是添加定时任务

所以如果是 添加定时任务和启动消费是分开部署的, 一定记得要在消费脚本中加上启动定时器
启动消费中加上  ApsJobAdder(消费函数, job_store_kind='redis') 这样实例化就顺便启动了定时器.
如果你不启动定时器,那么即使你之前已经加到redis job_store的定时任务,也没有定时器来触发.
</pre>

定时运行消费演示，定时方式入参用法可以百度 apscheduler 定时包。

定时的语法和入参与本框架无关系，不是本框架发明的定时语法，具体的需要刻苦学习 最知名的 apscheduler 定时包 ,所有对定时使用或报错感到疑惑的都是因为用户不愿意刻苦学习 apscheduler 官方文档造成的，
和funboost框架毫无关系。

要想玩好定时请务必苦学 apscheduler 3.x 官方文档：
[https://apscheduler.readthedocs.io/en/3.x/](https://apscheduler.readthedocs.io/en/3.x/)



### 4.4.0 funboost定时任务最基本原理说明

**funboost中的定时任务原理是:自动定时发布消息到消息队列，而非直接执行函数本身**

```
定时执行funboost发送函数入参到消息队列，然后funboost框架持续消费消息队列中的任务,从而达到执行消费函数的目的。
而不是在当前程序定时执行消费函数本身。

例如funboost中  add_push_job 添加一个每隔3秒运行fun消费函数的， 本质是每隔3秒自动运行 fun.push() , 而不是每隔3秒运行 fun() 本身，
理解这点至关重要。
如果你理解了这个原理，那么funboost的定时任务就非常简单，你可以自己使用apscheudler原生包来添加定时任务，
而不是非得使用funboost框架的ApsJobAdder的add_push_job来添加定时任务。


如果你直接使用官方的 apscheduler对象，
假设 fun是@boost装饰的消费函数，
apscheduler对象.add_job(fun,args=(1,2)) 你这是错误写法，除非你期望就是在当前程序执行add_job函数本身，

你应该写的是，要多加一个发送函数
def fun_push_msg(x,y):
    fun.push(x,y)
apscheduler对象.add_job(fun_push_msg,args=(1,2)) 


所以如果你用 apscheduler原生，那就要自己写一个发布消息的函数，add_job调用你定义的发布消息的函数。
有人认为为什么不能写成 apscheduler对象.add_job(fun.push,args=(1,2)) ，那就可以少写一个fun_push_msg函数， 你太年轻了，没实践采坑过就不知道。
要说明的是 fun.push 他是一个实例方法，他不是一个函数，方法是和对象绑定的，对象上面是有属性的不一定可序列化，所以apscheduler.add_job 是函数定时，没给你说是实例方法能定时啊。
所以apscheduler对象.add_job第一个入参必须是函数或者静态方法，不能是实例方法啊。
所以apscheduler对象.add_job(fun.push,args=(1,2))这种写法当然不行了。

而使用 funboost封装的 ApsJobAdder().add_push_job 就是为了帮你自动节约少写一个 fun_push_msg 这种函数。

```

### 4.4.1 funboost定时任务代码演示：

```python


"""
2025年后定时任务现在推荐使用 ApsJobAdder 写法 ，用户不需要亲自选择使用 apscheduler对象来添加定时任务。

使用对apscheduler封装的ApsJobAdder比 直接使用 apscheduler 包的好处如下：

1、ApsJobAdder.add_push_job 来添加定时发布到消息队列的任务，
  可以让用户少写一个 push_xx_fun_to_broker 的函数，用户不需要 apscheduler.add_job(push_xx_fun_to_broker,args=(1,)) ，
  而是 ApsJobAdder.add_push_job(xx_fun,args=(1,))
  
2.ApsJobAdder在redis作为job_store时候，每个消费函数使用单独的 jobs_key ，每个消费函数使用独立的 apscheduler对象，
避免扫描定时任务互相干扰。 
例如你只想启动fun1的定时任务，而不像启动fun2的定时任务，更能单独控制。
  
3. ApsJobAdder在redis作为job_store时候 ，_process_jobs 使用了 redis分布式锁， 解决经典头疼的 apschduler实例建议
只在一个进程启动一次，
现在可以在多机器多进程随意反复启动多次 apscheduler对象，不会造成定时任务执行重复。
"""

from funboost import boost, BrokerEnum,ctrl_c_recv,BoosterParams,ApsJobAdder



# 定义任务处理函数
@boost(BoosterParams(queue_name='sum_queue5', broker_kind=BrokerEnum.REDIS))
def sum_two_numbers(x, y):  
    result = x + y 
    print(f'The sum of {x} and {y} is {result}')  


@boost(BoosterParams(queue_name='data_queue5', broker_kind=BrokerEnum.REDIS))
def show_msg(data):
    print(f'data: {data}')

if __name__ == '__main__':
 
    # 启动消费者
    sum_two_numbers.consume()
    show_msg.consume()
  
    # 发布任务
    sum_two_numbers.push(3, 5)
    sum_two_numbers.push(10, 20)

    show_msg.push('hello world')
  
    # 使用ApsJobAdder添加定时任务， 里面的定时语法，和apscheduler是一样的，用户需要自己熟悉知名框架apscheduler的add_job定时入参
    # ApsJobAdder 类可以多次重复实例化,内部对每一个消费函数使用一个单独的apscheduler对象,避免扫描与当前关心的消费函数不相干的redis jobstore中的定时任务

    # 方式1：指定日期执行一次, 
    # ApsJobAdder(sum_two_numbers, job_store_kind='redis').aps_obj.start(paused=False)
    ApsJobAdder(sum_two_numbers, job_store_kind='redis').add_push_job(
        trigger='date',
        run_date='2025-01-17 23:25:40',
        args=(7, 8),
        replace_existing=True, # 如果写个id，就不能重复添加相同id的定时任务了，要使用replace_existing来替换之前的定时任务id
        id='date_job1'
    )

    # 方式2：固定间隔执行,使用内存作为apscheduler的 job_store
    ApsJobAdder(sum_two_numbers, job_store_kind='redis').add_push_job(
        trigger='interval',
        seconds=5,
        args=(4, 6),
        id='interval_job1',
        replace_existing=True
    )

    # 方式3：使用cron表达式定时执行
    ApsJobAdder(sum_two_numbers, job_store_kind='redis').add_push_job(
        trigger='cron',
        day_of_week='*',
        hour=23,
        minute=49,
        second=50,
        kwargs={"x":50,"y":60},
        replace_existing=True,
        id='cron_job1')

    # 延时使用内存作为apscheduler的 job_store ，因为是内存，这种定时任务计划就不能持久化。
    ApsJobAdder(show_msg, job_store_kind='memory').add_push_job(
        trigger='interval',
        seconds=20,
        args=('hi python',)
    )

    ctrl_c_recv() # 这个是阻止代码主线程结束，这在background类型的apscheduler很重要，否则会报错提示主线程已退出。 当然，你也可以在末尾加 time.sleep 来阻止主线结束。
```

funboost 定时语法说明：

```
funboost中定时任务用法是：
ApsJobAdder(消费函数,).add_push_job(trigger='interval',.....)

原生 apscheduler 添加定时任务用法例子是：
scheduler.add_job(my_job, 'interval', seconds=3, id='my_interval_job')

相比较而言，funboost中定时推荐你使用 ApsJobAdder(消费函数,).add_push_job ，
注意是 add_push_job 而非 add_job ， 并且add_push_job去掉了第一个入参func ，
add_push_job 其他入参和 apscheduler的add_job一模一样。

用户有兴趣可以看 ApsJobAdder 源码，他只是基于 apscheduler 的一个非常简单易懂的包装而已。
```

<pre style="background-color:yellow;color:red">

python3.9及以上 定时任务报错 RuntimeError: cannot schedule new futures after interpreter shutdown

我们是需要使得主线程其他任务不结束， 看10.2章节文档，在你脚本的最后一行加个 while 1: time.sleep(100) , 阻止主线程退出就好了。
或者结尾加个 ctrl_c_recv()   （先from funboost import  ctrl_c_recv）

</pre>

### 4.4.2 ApsJobAdder对象.aps_obj 核心对象说明

ApsJobAdder对象.aps_obj 是官方 apscheduler.BackgroundScheduler类型对象

你可以亲自使用 ApsJobAdder(sum_two_numbers, job_store_kind='redis',is_auto_start=False,).aps_obj 来精细化操作这个对象。

**例如删除一个定时任务：**   
ApsJobAdder(sum_two_numbers, job_store_kind='redis',is_auto_start=False,).aps_obj.remove_job('你指定的job_id')

**删除所有定时任务：**
ApsJobAdder(sum_two_numbers, job_store_kind='redis',is_auto_start=False,).aps_obj.remove_all_jobs()

**例如查看所有定时计划**
ApsJobAdder(sum_two_numbers, job_store_kind='redis',is_auto_start=False,).aps_obj.get_jobs()

**aps_obj的其他方法我不再啰嗦了，都是知名三方包apscheduler的Scheduler类型的方法，本质原因是你不愿意苦学apscheduler，这些用法功能和funboost自身源码毫无关系。**

funboost的对apscheduler包的轻度二次包装，是为了简化添加 “push到消息队列” 的定时任务，用户完全可以直接使用原生 apscheduler。   
但你要把”发布消息到消息队列“作为定时任务，而不是把“执行函数本身逻辑”作为定时任务。   

### 4.4.3 演示在python web中定时任务的添加 （添加和执行定时任务分在不同的py脚本中）

web中去添加和修改定时任务，web单独部署一次。
funboost后台异步任务单独部署一次,建议定时器需要随着消费一起启动。


**在web接口代码中添加定时任务计划，但可以不执行定时任务,设置is_auto_paused=True**

**在启动消费的脚本中,要明确启动定时器,ApsJobAdder(fun_sum,job_store_kind='redis',) ,ApsJobAdder类默认就是  is_auto_start=True is_auto_paused=False** 

web中添加定时任务demo连接：

[https://github.com/ydf0509/funboost/tree/master/test_frame/funboost_aps_web_demo](https://github.com/ydf0509/funboost/tree/master/test_frame/funboost_aps_web_demo)

```
演示在python web中定时任务的添加，添加定时任务的脚本和启动消费的脚本不在同一个py文件中,一定要注意务必要启动定时任务apschduler对象，这是最关键的。

web中需要启动定时器,is_auto_start=True,但你可以选择暂停执行定时任务is_auto_paused=True,在启动消费的那里去写启动和执行定时任务.
ApsJobAdder(消费函数, job_store_kind='redis', is_auto_start=True,is_auto_paused=True)

(ps:当然可以多个地方都 is_auto_start=True,is_auto_paused=True 这样启动定时器,
因为funboost已经继承优化了原生apscheduler类,不怕你多次重复部署apscheduler定时器造成重复执行相同的定时任务
有兴趣的用户可以看 https://github.com/ydf0509/funboost/blob/master/funboost/timing_job/apscheduler_use_redis_store.py 的 FunboostBackgroundSchedulerProcessJobsWithinRedisLock 的 _process_jobs 方法, 这个是防止apscheduler多次部署导致重复执行定时任务的根本核心解决.
)
```

###### 4.4.3.2 web_app.py 是web应用，负责添加定时任务到redis中。此处使用flask框架演示， django  fastapi同理，不需要我一一举例子。

```
因为funboost是自由无拘无束的，不需要 django-funboost  flask-funboost fastapi-funboost 插件。

只有坑爹难用的celery才需要django-celery  flask-celery fastapi-celery 三方插件来帮助用户简化适配各种web框架使用，
funboost压根不需要这种适配各种web框架的插件。
```

###### 4.4.3.3 run_consume.py 是启动消费 和 启动apschduler定时器的脚本

```python
ApsJobAdder(fun_sum,job_store_kind='redis',) #负责启动apschduler对象，apschduler对象会扫描redis中的定时任务，并执行定时任务，定时任务的功能就是定时push消息到消息队列中。

fun_sum.consume()  # 启动消费消息队列中的消息
```

<pre style="background-color:yellow;color:red;font-weight:bold">
警告！！！你不要只启动fun_sum.consume()  而不启动apschduler对象，
否则apschduler对象不会扫描redis中已添加好的定时任务，就不会自动定时的push消息到消息队列中。
</pre>

## 4.5 多进程并发 + 多线程/协程，代码例子。

ff.multi_process_start(2)  就是代表启动2个独立进程并发 + 叠加 asyncio、gevent、eventlet、threding 、single_thread 细粒度并发，<br>
例如fun函数加上@boost(BoosterParams(queue_name='queue_name', concurrent_num=200)),fun.multi_process_start(16) ,这样16进程叠加每个进程内部开200线程/协程，运行性能炸裂。

多进程消费

```python
import time
from funboost import boost, BrokerEnum, PriorityConsumingControlConfig, BoosterParams

"""
演示多进程启动消费，多进程和 asyncio/threading/gevnt/evntlet是叠加关系，不是平行的关系。
"""

# qps=5，is_using_distributed_frequency_control=True 分布式控频每秒执行5次。
# 如果is_using_distributed_frequency_control不设置为True,默认每个进程都会每秒执行5次。
@boost(BoosterParams(queue_name='test_queue', broker_kind=BrokerEnum.REDIS, qps=5, is_using_distributed_frequency_control=True))
def ff(x, y):
    import os
    time.sleep(2)
    print(os.getpid(), x, y)


if __name__ == '__main__':
    ff.clear() # 清除
    # ff.publish()
    for i in range(1000):
        ff.push(i, y=i * 2)

        # 这个与push相比是复杂的发布，第一个参数是函数本身的入参字典，后面的参数为任务控制参数，例如可以设置task_id，设置延时任务，设置是否使用rpc模式等。
        ff.publish({'x': i * 10, 'y': i * 2}, priority_control_config=PriorityConsumingControlConfig(countdown=1, misfire_grace_time=15))

    ff(666, 888)  # 直接运行函数
    ff.start()  # 和 conusme()等效
    ff.consume()  # 和 start()等效
    ff.multi_process_start(2)  # 启动两个进程，

```

## 4.6 演示rpc模式，即客户端调用远程函数并及时得到结果。

```
如果在发布端要获取消费端的执行结果，有两种方式
1、需要在@boost设置is_using_rpc_mode=True，默认是False不会得到结果。
2、如果@boost没有指定，也可以在发布任务的时候，用publish方法并写上
  priority_control_config=PriorityConsumingControlConfig(is_using_rpc_mode=True)
  
用这个功能必须在funboost_config.py配置文件中配置好redis链接，
无论你使用 redis kafka rabbitmq 还是 sqlite 等 作为中间件，想用rpc功能就必须配置好redis连接。
```

### 4.6.1 rpc 消费端执行两数求

远程服务端脚本，执行求和逻辑。 test_frame\test_rpc\test_consume.py

```python
import time
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_rpc_queue', is_using_rpc_mode=True, broker_kind=BrokerEnum.REDIS_ACK_ABLE, concurrent_num=200))
def add(a, b):
    time.sleep(3)
    return a + b


if __name__ == '__main__':
    add.consume()
```

### 4.6.2 发布端获取求和的结果

客户端调用脚本，单线程发布阻塞获取两书之和的结果，执行求和过程是在服务端。 test_frame\test_rpc\test_publish.py

这种方式如果在主线程单线程for循环运行100次，因为为了获取结果，导致需要300秒才能完成100次求和。

客户端获取服务端执行结果脚本

```python
from funboost import PriorityConsumingControlConfig
from test_frame.test_rpc.test_consume import add

for i in range(100):
    async_result = add.push(i, i * 2)
    print(async_result.result)  # 执行 .result是获取函数的运行结果，会阻塞当前发布消息的线程直到函数运行完成。

    # 如果add函数的@boost装饰器参数没有设置 is_using_rpc_mode=True，则在发布时候也可以指定使用rpc模式。
    async_result = add.publish(dict(a=i * 10, b=i * 20), priority_control_config=
    PriorityConsumingControlConfig(is_using_rpc_mode=True))
    print(async_result.status_and_result)

```

### 4.6.2b 发布端获取求和的结果，在线程池中进一步处理结果

上面方式中是在单线程环境下阻塞的一个接一个打印结果。如果想快速并发处理结果，可以自己手动在多线程或线程池处理结果。 框架也提供一个设置回调函数，自动在线程池中处理回调结果，回调函数有且只有一个入参，表示函数运行结果及状态。

如下脚本则不需要300秒运行完成只需要3秒即可，会自动在并发池中处理结果。

```python
from funboost import PriorityConsumingControlConfig
from test_frame.test_rpc.test_consume import add


def show_result(status_and_result: dict):
    """
    :param status_and_result: 一个字典包括了函数入参、函数结果、函数是否运行成功、函数运行异常类型
    """
    print(status_and_result)


for i in range(100):
    async_result = add.push(i, i * 2)
    # print(async_result.result)   # 执行 .result是获取函数的运行结果，会阻塞当前发布消息的线程直到函数运行完成。
    async_result.set_callback(show_result)  # 使用回调函数在线程池中并发的运行函数结果
```

### 4.6.3 手动设置rpc结果最大等待时间

手动设置rpc结果最大等待时间，不使用默认的120秒等待时间。

```
上面的求和例子是耗时3秒，所以只要任务不在消息队列积压，120秒内可以获取到结果。如果上面的求和函数耗时600秒，120秒内就获取不到结果了。
可以手动设置异步结果最大的等待时间，.set_timeout(3600) 就是最大等待1小时了。

async_result = add.push(i, i * 2)
async_result.set_timeout(3600)

这样设置后，就是为了获得消费结果，最大等待3600秒。
默认是最大等待120秒返回结果，如果消费函数本身耗时就需要消耗很长的时间，可以适当扩大这个时间。
```

### 4.6.4 为什么获取不到执行结果？

1) 首先要检查 有没有设置 is_using_rpc_mode=True ，默认是不使用这个模式的，没有设置为True就不可能得到执行结果。
2) 默认为等待结果最大120秒，如果你的函数耗时本来就很大或者消息队列有大量积压，需要按4.6.3 调大最大等等时间

### 4.6.5 asyncio 语法生态下rpc获取执行结果。

<p style="color: #00A000">完整的除了asyncio并发，包括 aio_push 和 asyncio 来等待获取结果，请看4b.3 章节</p>p> [ funboost + 全asyncio 编程生态演示](https://funboost.readthedocs.io/zh-cn/latest/articles/c4b.html#b-3-funboost-asyncio)

```
因为 async_result= fun.push() ，默认返回的是 AsyncResult 类型对象,里面的方法都是同步语法。
async_result.result 是一个耗时的函数， 解释一下result， 是property装饰的所以不用 async_result.result()
有的人直接在async def 的异步函数里面 print (async_result.result)，如果消费函数消费需要耗时5秒，
那么意味rpc获取结果至少需要5秒才能返回，你这样写代码会发生灭顶之灾，asyncio生态流程里面一旦异步需要处处异步。
所以新增了 AioAsyncResult 类，和用户本来的asyncio编程生态更好的搭配。
```

服务端求和脚本还是4.6.1 两数求和不变，这里演示asyncio生态下的获取rpc结果脚本

```python
import asyncio

from funboost import AioAsyncResult
from test_frame.test_rpc.test_consume import add


async def process_result(status_and_result: dict):
    """
    :param status_and_result: 一个字典包括了函数入参、函数结果、函数是否运行成功、函数运行异常类型
    """
    await asyncio.sleep(1)
    print(status_and_result)


async def test_get_result(i):
    async_result = add.push(i, i * 2)
    aio_async_result = AioAsyncResult(task_id=async_result.task_id) # 这里要使用asyncio语法的类，更方便的配合asyncio异步编程生态
    print(await aio_async_result.result) # 注意这里有个await，如果不await就是打印一个协程对象，不会得到结果。这是asyncio的基本语法，需要用户精通asyncio。
    print(await aio_async_result.status_and_result)
    await aio_async_result.set_callback(process_result)  #  你也可以编排任务到loop中


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for j in range(100):
        loop.create_task(test_get_result(j))
    loop.run_forever()

```

```text
async_result = add.push(i, i * 2)   
async_result 的类型是AsyncResult，是同步场景下的类。这个Async不是指的asyncio语法异步，是生产者消费者模式整体大的概念上的异步，不是指的python asyncio语法异步。

aio_async_result = AioAsyncResult(task_id=async_result.task_id) ，这个是asyncio语法类AioAsyncResult，这个类里面的耗时io的方法全都是async def的，
这种更好的配合用户当前已经是 asyncio 编程生态。因为在asyncio编程生态中，在一个loop里面，要全部异步，只要一个是同步阻塞的方法，整个loop中其他协程任务完了个蛋，
也就是常说的一旦异步要处处异步，不要在一串流程中一会儿调用asyncio的耗时函数，一会调用同步耗时函数，这样是个悲剧，懂的都懂这句话。
```

### 4.6.7 从mongo中获取函数执行结果

首先 boost装饰器中设置函数状态结果持久化后，会保存函数的状态和结果到mongodb中。

function_result_status_persistance_conf=FunctionResultStatusPersistanceConfig(is_save_status=True,is_save_result=True,expire_seconds=500000)

使用 ResultFromMongo 类获取函数结果

```python
# 以非等待方式获取mongo中函数的结果。
import time
from funboost import ResultFromMongo

async_result = add.push(10, 20)
task_id = async_result.task_id
time.sleep(2)
print(ResultFromMongo(task_id).get_status_and_result())

print(ResultFromMongo('test_queue77h6_result:764a1ba2-14eb-49e2-9209-ac83fc5db1e8').get_status_and_result())
print(ResultFromMongo('test_queue77h6_result:5cdb4386-44cc-452f-97f4-9e5d2882a7c1').get_result())
```

## 4.7 演示qps控频

演示框架的qps控频功能

此框架对函数耗时随机波动很大的控频精确度达到96%以上

此框架对耗时恒定的函数控频精确度达到99.9%

在指定rate_limit 超过 20/s 时候，celery对耗时恒定的函数控频精确度60%左右，下面的代码会演示这两个框架的控频精准度对比。

<pre style="color: #00A000">
此框架针对不同指定不同qps频次大小的时候做了不同的三种处理方式。
框架的控频是直接基于代码计数，而非使用redis 的incr计数，因为python操作一次redis指令要消耗800行代码左右，
如果所有任务都高频率incr很消耗python脚本的cpu也对redis服务端产生灾难压力。
例如假设有50个不同的函数，分别都要做好几千qps的控频，如果采用incr计数，光是incr指令每秒就要操作10万次redis，
所以如果用redis的incr计数控频就是个灾难，redis incr的计数只适合 1到10大小的qps，不适合 0.01 qps 和 1000 qps这样的任务。

同时此框架也能很方便的达到 5万 qps的目的，装饰器设置qps=50000 和 is_using_distributed_frequency_control=True,
然后只需要部署很多个进程 + 多台机器，框架通过redis统计活跃消费者数量，来自动调节每台机器的qps，框架的分布式控频开销非常十分低，
因为分布式控频使用的仍然不是redis的incr计数，而是基于每个消费者的心跳来统计活跃消费者数量，然后给每个进程分配qps的，依然基于本地代码计数。

例如部署100个进程(如果机器是128核的，一台机器足以，或者20台8核机器也可以)
以20台8核机器为例子，如果把机器减少到15台或增加机器到30台，随便减少部署的机器数量或者随便增加机器的数量，
代码都不需要做任何改动和重新部署，框架能够自动调节来保持持续5万次每秒来执行函数，不用担心部署多了30台机器，实际运行qps就变成了10几万。
(前提是不要把机器减少到10台以下，因为这里假设这个函数是一个稍微耗cpu耗时的函数，要保证所有资源硬件加起来有实力支撑5万次每秒执行函数)

每台机器都运行 test_fun.multi_process_conusme(8)，只要10台以上1000台以下随意随时随地增大减小运行机器数量，
代码不需要做任何修改变化，就能很方便的达到每秒运行5万次函数的目的。
</pre>

### 4.7.1 演示qps控频和自适应扩大和减小并发数量。

```
通过不同的时间观察控制台，可以发现无论f2这个函数需要耗时多久（无论是函数耗时需要远小于1秒还是远大于1秒），框架都能精确控制每秒刚好运行2次。
当函数耗时很小的时候，只需要很少的线程就能自动控制函数每秒运行2次。
当函数突然需要耗时很大的时候，智能线程池会自动启动更多的线程来达到每秒运行2次的目的。
当函数耗时从需要耗时很大变成只需要耗时很小的时候，智能线程池会自动缩小线程数量。
总之是围绕qps恒定，会自动变幻线程数量，做到既不多开浪费cpu切换，也不少开造成执行速度慢。
```

```python
import time
import threading
from funboost import boost, BrokerEnum, ConcurrentModeEnum, BoosterParams

t_start = time.time()


@boost(BoosterParams(queue_name='queue_test2_qps', qps=2, broker_kind=BrokerEnum.PERSISTQUEUE, concurrent_mode=ConcurrentModeEnum.THREADING,
       concurrent_num=600))
def f2(a, b):
    """
    这个例子是测试函数耗时是动态变化的，这样就不可能通过提前设置参数预估函数固定耗时和搞鬼了。看看能不能实现qps稳定和线程池自动扩大自动缩小
    要说明的是打印的线程数量也包含了框架启动时候几个其他的线程，所以数量不是刚好和所需的线程计算一样的。
    """
    result = a + b
    sleep_time = 0.01
    if time.time() - t_start > 60:  # 先测试函数耗时慢慢变大了，框架能不能按需自动增大线程数量
        sleep_time = 7
    if time.time() - t_start > 120:
        sleep_time = 30
    if time.time() - t_start > 240:  # 最后把函数耗时又减小，看看框架能不能自动缩小线程数量。
        sleep_time = 0.8
    if time.time() - t_start > 300:
        sleep_time = None
    print(
        f'{time.strftime("%H:%M:%S")}  ，当前线程数量是 {threading.active_count()},   {a} + {b} 的结果是 {result}， sleep {sleep_time} 秒')
    if sleep_time is not None:
        time.sleep(sleep_time)  # 模拟做某事需要阻塞n秒种，必须用并发绕过此阻塞。
    return result


if __name__ == '__main__':
    f2.clear()
    for i in range(1000):
        f2.push(i, i * 2)
    f2.consume()
```

### 4.7.2 此框架对固定耗时的任务，持续控频精确度高于99.9%

4.7.2 此框架对固定耗时的任务，持续控频精确度高于99.9%，远超celery的rate_limit 60%控频的精确度。

```
对于耗时恒定的函数，此框架精确控频率精确度达到99.9%，celery控频相当不准确，最多到达60%左右，两框架同样是做简单的加法然后sleep0.7秒，都设置500并发100qps。
```

```python
@boost(BoosterParams(queue_name='test_queue66', broker_kind=BrokerEnum.REDIS, qps=100))
def f(x, y):
    print(f''' {int(time.time())} 计算  {x} + {y} = {x + y}''')
    time.sleep(0.7)
    return x + y


@celery_app.task(name='求和啊', rate_limit='100/s')
def add(a, b):
    print(f'{int(time.time())} 计算 {a} + {b} 得到的结果是  {a + b}')
    time.sleep(0.7)
    return a + b

```

```text
# 在pycahrm控制台搜索 某一秒的时间戳 + 计算 作为关键字查询，分布式函数调度框架启动5秒后，以后持续每一秒都是100次，未出现过99和101的现象。
在pycahrm控制台搜索 某一秒的时间戳 + 计算 作为关键字查询，celery框架，每一秒求和次数都是飘忽不定的，而且是六十几徘徊，
如果celery能控制到95至105次每秒徘徊波动还能接受，类似现象还有celery设置rate_limit=50/s，实际32次每秒徘徊，
设置rate_limit=30/s，实际18-22次每秒徘徊，可见celery的控频相当差。
设置rate_limit=10/s，实际7-10次每秒徘徊，大部分时候是9次，当rate_limit大于20时候就越来越相差大了，可见celery的控频相当差。
```

### 4.7.3 对函数耗时随机性大的控频功能证明

对函数耗时随机性大的控频功能证明，使用外网连接远程broker,持续qps控频。

```
设置函数的qps为100，来调度需要消耗任意随机时长的函数，能够做到持续精确控频，频率误差小。
如果设置每秒精确运行超过500000次以上的固定频率，前提是cpu够强机器数量多，
设置qps=50000，并指定is_using_distributed_frequency_control=True(只有这样才是分布式全局控频，默认是基于单个进程的控频),。

如果任务不是很重型很耗cpu，此框架单个消费进程可以控制每秒运行次数的qps 从0.01到1000很容易。
当设置qps为0.01时候，指定的是每100秒运行1次，qps为100指的是每一秒运行100次。

```

```python
import time
import random
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_rabbit_queue7', broker_kind=BrokerEnum.RABBITMQ_AMQPSTORM, qps=100, log_level=20))
def test_fun(x):
    # time.sleep(2.9)
    # sleep时间随机从0.1毫秒到5秒任意徘徊。传统的恒定并发数量的线程池对未知的耗时任务，持续100次每秒的精确控频无能为力。
    # 但此框架只要简单设置一个qps就自动达到了这个目的。
    random_sleep = random.randrange(1, 50000) / 10000
    time.sleep(random_sleep)
    print(x, random_sleep)


if __name__ == '__main__':
    test_fun.consume()
    # test_fun.multi_process_consume(3)
```

分布式函数调度框架对耗时波动大的函数持续控频曲线
![img_3.png](img_3.png)

### 4.7.4 分布式全局控频和单个消费者控频区别

```
@boost中指定 is_using_distributed_frequency_control=True 则启用分布式全局控频，是跨进程跨python解释器跨服务器的全局控频。
否则是基于当前消费者的控频。

例如 你设置的qps是100，如果你不设置全局控频，run_consume.py 脚本中启动 fun.consume() ，如果你反复启动5次这个 run_consume.py，
如果不设置分布式控频，那么5个独立的脚本运行，频率总共会达到 500次每秒，因为你部署了5个脚本。
同理你如果用 fun.multi_process_consume(4)启动了4个进程消费，那么就是4个消费者，总qps也会达到400次每秒。
这个控频方式是看你需求了。


如果设置了 is_using_distributed_frequency_control=True，那就会使用每个消费者发送到redis的心跳来统计总消费者个数。
如果你部署了2次，那么每个消费者会平分qps，每个消费者是变成50qps，总共100qps。
如果你部署了5次，那么每个消费者会平分qps，每个消费者是变成20qps，总共100qps。
如果你中途关闭2个消费者，变成了3个消费者，每个消费者是变成 33.33qps，总共100qps。(框架qps支持小数，0.1qps表示每10秒执行1次)

```

## 4.8 再次说明qps能做什么，qps为什么流弊？常规并发方式无法完成的需求是什么？

以模拟请求一个flask接口为例子，我要求每一秒都持续精确完成8次请求，即控制台每1秒都持续得到8次flask接口返回的hello world结果。

### 4.8.1 下面讲讲常规并发手段为什么对8qps控频需求无能为力？

不用框架也可以实现8并发， 例如Threadpool设置8线程很容易，但不用框架实现8qps不仅难而且烦

```
虽然
框架能自动实现 单线程  ，多线程， gevent ， eventlet ，asyncio ，多进程 并发 ，
多进程 + 单线程 ，多进程 + 多线程，多进程 + gevent,  多进程 + eventlet  ，多进程 + asyncio 的组合并发
可以说囊括了python界的一切知名的并发模型，能做到这一点就很方便强大了
但是
此框架还额外能实现qps控频，能够实现函数每秒运行次数的精确控制，我觉得这个功能也很实用，甚至比上面的那些并发用起来还实用。
```

```
这个代码是模拟常规并发手段无法达到每秒持续精确运行8次函数(请求flask接口8次)的目的。

下面的代码使用8个线程并发运行 request_flask_api 函数，
当flask_veiw_mock 接口耗时0.1秒时候,在python输出控制台可以看到，10秒钟就运行结束了，控制台每秒打印了80次hello world，严重超频10倍了不符合需求
当flask_veiw_mock 接口耗时刚好精确等于1秒时候,在python输出控制台可以看到，100秒钟运行结束了，控制台每秒打印了8次hello world，只有当接口耗时刚好精确等于1秒时候，并发数量才符合qps需求
当flask_veiw_mock 接口耗时10秒时候,在python输出控制台可以看到，需要1000秒钟运行结束，控制台每隔10秒打印8次hello world，严重不符合持续每秒打印8次的目的。
由此可见，用设置并发数量来达到每秒请求8次flask的目的非常困难，99.99%的情况下服务端没那么巧刚好耗时1秒。
```

天真的人会说根据函数耗时大小，来设置并发数量，这可行吗？

```
有人会说，为了达到8qps目的，当函数里面sleep 0.1 时候他开1线程，那你这样仍然超频啊，你是每1秒钟打印10次了超过了8次。
当sleep 0.01 时候，为了达到8qps目的，就算你开1线程，那不是每1秒钟打印100次hello？你不会想到开0.08个线程个线程来实现控频吧？
当sleep 10秒时候，为了8qps目的，你开80线程，那这样是控制台每隔10秒打印80次hello，我要求的是控制台每一秒都打印8次hello，没告诉你是每隔10秒打印80次hello吧？还是没达到目的。
如果函数里面是sleep 0.005 0.07 0.09 1.3 2.7 7 11 13这些不规则无法整除的数字？请问你是如何一一计算精确开多少线程来达到8qps的？
如果flask网站接口昨天是3秒的响应时间，今天变成了0.1秒的响应时间，你的线程池数量不做变化，代码不进行重启，请问你如何做到自适应无视请求耗时，一直持续8qps的目的？
固定并发数量大小就是定速巡航不够智能前车减速会撞车，qps自适应控频那就是acc自适应巡航了，自动调整极端智能，压根无需提前测算预估函数需要耗时多久(接口响应耗时多久)。
所以综上所述,如果你有控频需求，你想用并发数量来达到控频目的，那是不可能的。
```

有些人到现在还没明白并发数量和qps(每秒执行多少次)之间的区别，并发数量只有在函数耗时刚好精确等于1秒时候才等于qps。

```

```python
import time
from concurrent.futures import ThreadPoolExecutor


def flask_veiw_mock(x):
    # time.sleep(0.1)  # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    # time.sleep(1)   # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    time.sleep(10)  # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    return f"hello world {x}"


def request_flask_api(x):
    response = flask_veiw_mock(x)
    print(time.strftime("%H:%M:%S"), '   ', response)


if __name__ == '__main__':
    with ThreadPoolExecutor(8) as pool:
        for i in range(800):
            pool.submit(request_flask_api,i)

```

截图是当 flask_veiw_mock 耗时为10秒时候，控制台是每隔10秒打印8次 hello world，没达到每一秒都打印8次的目的<br>
当 flask_veiw_mock 耗时为0.1 秒时候，控制台是每隔1秒打印80次 hello world，没达到每一秒都打印8次的目的<br>

![img_16.png](img_16.png)

### 4.8.2 使用分布式函数调度框架，无论接口耗时多少，轻松达到8qps的例子

```
这个代码是模拟常规并发手段无法达到每秒持续精确运行8次函数(请求flask接口8次)的目的。
但是使用分布式函数调度框架能轻松达到这个目的。

下面的代码使用分部署函数调度框架来调度运行 request_flask_api 函数，

flask_veiw_mock 接口耗时0.1秒时候，控制台每秒打印8次 hello world，非常精确的符合控频目标
flask_veiw_mock 接口耗时1秒时候，控制台每秒打印8次 hello world，非常精确的符合控频目标
flask_veiw_mock 接口耗时10秒时候控，控制台每秒打印8次 hello world，非常精确的符合控频目标
flask_veiw_mock 接口耗时0.001秒时候，控制台每秒打印8次 hello world，非常精确的符合控频目标
flask_veiw_mock 接口耗时50 秒时候，控制台每秒打印8次 hello world，非常精确的符合控频目标
可以发现分布式函数调度框架无视函数耗时大小，都能做到精确控频，常规的线程池 asyncio什么的，面对这种不确定的接口耗时，简直毫无办法。

有些人到现在还没明白并发数量和qps(每秒执行多少次)之间的区别，并发数量只有在函数耗时刚好精确等于1秒时候才等于qps。
```

```python
import time
from funboost import boost, BrokerEnum, BoosterParams


def flask_veiw_mock(x):
    time.sleep(0.1)  # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    # time.sleep(1)   # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    # time.sleep(10)  # 通过不同的sleep大小来模拟服务端响应需要消耗的时间
    return f"hello world {x}"


@boost(BoosterParams(queue_name="test_qps", broker_kind=BrokerEnum.MEMORY_QUEUE, qps=8))
def request_flask_api(x):
    response = flask_veiw_mock(x)
    print(time.strftime("%H:%M:%S"), '   ', response)


if __name__ == '__main__':
    for i in range(800):
        request_flask_api.push(i)
    request_flask_api.consume()
```

从截图可以看出，分布式函数调度框架，控频稳如狗，完全无视flask_veiw_mock耗时是多少。
![img_17.png](img_17.png)

### 4.8.3  并发数量和qps(每秒执行多少次)之间的区别

有些人到现在还没明白并发数量和qps(每秒执行多少次)之间的区别，并发数量只有在函数耗时刚好精确等于1秒时候才等于qps。

拿10并发(线程/协程)和10qps 运行10000次函数 举例子，

```
如果函数耗时 0.1秒，10并发运行10000次，那么是 100秒运行完成 
如果函数耗时 1 秒，10并发运行10000次，那么是 1000秒运行完成
如果函数耗时 10 秒，10并发运行10000次，那么是 10000秒运行完成


如果函数耗时 0.1秒，10qps运行10000次，那么是 1000秒运行完成 
如果函数耗时 1 秒，10qps运行10000次，那么是 1000秒运行完成 
如果函数耗时 10 秒，10qps运行10000次，那么是 1000秒运行完成 

并发是恒定同时有多少个线程/协程 在运行函数，不能达到消费速率恒定，除非函数耗时是1秒并且稳定
qps是无视函数耗时多少，总是能在固定的时间内完成所有任务。
qps恒定，前提是电脑cpu能力范围之内，防止有杠精会说他要指定 qps为1千亿，在函数里面每次做一个很大数字的斐波那契数列，与求和1到1万亿，
然后框架达不到这个速度，杠精说qps不准。

```

## 4.9 演示延时运行任务

4.4章节的定时任务一般指的是周期性重复触发执行某个参数任务，4.9的演示任务是说对一个消息规定在什么时候去运行。

4.4是重复周期性的触发执行任务，4.9是对一个消息规定延时多长时间来执行它。一个有周期性重复触发的含义，一个是一次性的含义。

```
因为有很多人有这样的需求，希望发布后不是马上运行，而是延迟60秒或者现在发布晚上18点运行。
然来是希望用户自己亲自在消费函数内部写个sleep(60)秒再执行业务逻辑，来达到延时执行的目的，
但这样会被sleep占据大量的并发线程/协程,如果是用户消费函数内部写sleep7200秒这么长的时间，那
sleep等待会占据99.9%的并发工作线程/协程的时间，导致真正的执行函数的速度大幅度下降，所以框架
现在从框架层面新增这个延时任务的功能。

之前已做的功能是定时任务，现在新增延时任务，这两个概念有一些不同。

定时任务一般情况下是配置为周期重复性任务，延时任务是一次性任务。
1）框架实现定时任务原理是代码本身自动定时发布，自然而然就能达到定时消费的目的。
2）框架实现延时任务的原理是马上立即发布，当消费者取出消息后，并不是立刻去运行，
   而是使用定时运行一次的方式延迟这个任务的运行。

在需求开发过程中，我们经常会遇到一些类似下面的场景：
1）外卖订单超过15分钟未支付，自动取消
2）使用抢票软件订到车票后，1小时内未支付，自动取消
3）待处理申请超时1天，通知审核人员经理，超时2天通知审核人员总监
4）客户预定自如房子后，24小时内未支付，房源自动释放


分布式函数调度框架的延时任务概念类似celery的countdown和eta入参，  add.apply_async(args=(1, 2),countdown=20)  # 规定取出后20秒再运行
此框架的入参名称那就也叫 countdown和eta。
countdown 传一个数字，表示多少秒后运行。
eta传一个datetime对象表示，精确的运行时间运行一次。

```

消费，消费代码没有任何变化

```python
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_delay', broker_kind=BrokerEnum.REDIS_ACK_ABLE))
def f(x):
    print(x)


if __name__ == '__main__':
    f.consume()
```

发布延时任务

```python
# 需要用publish，而不是push，这个前面已经说明了，如果要传函数入参本身以外的参数到中间件，需要用publish。
# 不然框架分不清哪些是函数入参，哪些是控制参数。如果无法理解就，就好好想想琢磨下celery的 apply_async 和 delay的关系。

from test_frame.test_delay_task.test_delay_consume import f
import datetime
import time
from funboost import PriorityConsumingControlConfig

"""
测试发布延时任务，不是发布后马上就执行函数。

countdown 和 eta 只能设置一个。
countdown 指的是 离发布多少秒后执行，
eta是指定的精确时间运行一次。

misfire_grace_time 是指定消息轮到被消费时候，如果已经超过了应该运行的时间多少秒之内，仍然执行。
misfire_grace_time 如果设置为None，则消息一定会被运行，不会由于大连消息积压导致消费时候已近太晚了而取消运行。
misfire_grace_time 如果不为None，必须是大于等于1的整数，此值表示消息轮到消费时候超过本应该运行的时间的多少秒内仍然执行。
此值的数字设置越小，如果由于消费慢的原因，就有越大概率导致消息被丢弃不运行。如果此值设置为1亿，则几乎不会导致放弃运行(1亿的作用接近于None了)
如果还是不懂这个值的作用，可以百度 apscheduler 包的 misfire_grace_time 概念

"""
for i in range(1, 20):
    time.sleep(1)

    # 消息发布10秒后再执行。如果消费慢导致任务积压，misfire_grace_time为None，即使轮到消息消费时候离发布超过10秒了仍然执行。
    f.publish({'x': i}, priority_control_config=PriorityConsumingControlConfig(countdown=10))

    # 规定消息在17点56分30秒运行，如果消费慢导致任务积压，misfire_grace_time为None，即使轮到消息消费时候已经过了17点56分30秒仍然执行。
    f.publish({'x': i * 10}, priority_control_config=PriorityConsumingControlConfig(
        eta=datetime.datetime(2021, 5, 19, 17, 56, 30) + datetime.timedelta(seconds=i)))

    # 消息发布10秒后再执行。如果消费慢导致任务积压，misfire_grace_time为30，如果轮到消息消费时候离发布超过40 (10+30) 秒了则放弃执行，
    # 如果轮到消息消费时候离发布时间是20秒，由于 20 < (10 + 30)，则仍然执行
    f.publish({'x': i * 100}, priority_control_config=PriorityConsumingControlConfig(
        countdown=10, misfire_grace_time=30))

    # 规定消息在17点56分30秒运行，如果消费慢导致任务积压，如果轮到消息消费时候已经过了17点57分00秒，
    # misfire_grace_time为30，如果轮到消息消费时候超过了17点57分0秒 则放弃执行，
    # 如果如果轮到消息消费时候是17点56分50秒则执行。
    f.publish({'x': i * 1000}, priority_control_config=PriorityConsumingControlConfig(
        eta=datetime.datetime(2021, 5, 19, 17, 56, 30) + datetime.timedelta(seconds=i),
        misfire_grace_time=30))

    # 这个设置了消息由于推挤导致运行的时候比本应该运行的时间如果小于1亿秒，就仍然会被执行，所以几乎肯定不会被放弃运行
    f.publish({'x': i * 10000}, priority_control_config=PriorityConsumingControlConfig(
        eta=datetime.datetime(2021, 5, 19, 17, 56, 30) + datetime.timedelta(seconds=i),
        misfire_grace_time=100000000))
```

## 4.10 在web中如flask fastapi django 如何搭配使用消费框架的例子。

```
在web中推送任务，后台进程消费任务，很多人问怎么在web使用，用法和不与web框架搭配并没有什么不同之处。


因为发布和消费是使用中间件解耦的，一般可以分成web接口启动一次，后台消费启动一次，需要独立部署两次。

演示了flask 使用app应用上下文。

web接口中发布任务到消息队列，独立启动异步消费。
```

flask + 分布式函数调度框架演示例子在：

[https://github.com/ydf0509/distributed_framework/blob/master/test_frame/use_in_flask_tonardo_fastapi](https://github.com/ydf0509/distributed_framework/blob/master/test_frame/use_in_flask_tonardo_fastapi)

fastapi + 分布式函数调度框架演示例子在：

[https://github.com/ydf0509/fastapi_use_distributed_framework_demo](https://github.com/ydf0509/fastapi_use_distributed_framework_demo)

django + 分布式函数调度框架演示例子在：

[https://github.com/ydf0509/django_use_funboost](https://github.com/ydf0509/django_use_funboost)

dajngo + funboost + 函数中操作了django orm的例子在:

[https://github.com/ydf0509/funboost_django_orm_demo](https://github.com/ydf0509/funboost_django_orm_demo)

uwsgi + flask + funboost 演示例子在：

[https://github.com/ydf0509/uwsgi_flask_funboost](https://github.com/ydf0509/uwsgi_flask_funboost)

这三个web框架demo + funboost 框架，几乎是一模一样的，有的人不能举一反三，非要我单独增加demo例子。

部署方式都是web部署一次，后台消费部署一次，web接口中发布消息到消息队列，funboost没有与任何web框架有任何绑定关系，都是一样的用法。

如果前端在乎任务的结果：

```
非常适合使用mqtt， 前端订阅唯一uuid的topic 然后表单中带上这个topic名字请求python接口 -> 接口中发布任务到rabbitmq或redis消息队列 ->
后台消费进程执行任务消费,并将结果发布到mqtt的那个唯一uuid的topic -> mqtt 把结果推送到前端。
使用ajax轮训或者后台导入websocket相关的包来做和前端的长耗时任务的交互 是伪命题。
```

使用 web + funboost +mqtt的流程图

![img_43.png](img_43.png)

## 4.11 保存消费状态和结果包mongo，开启消费状态结果的web页面

### 4.11.1 保存消费状态和结果到mongodb

需要配置好mongodb连接，并且设置 function_result_status_persistance_conf 持久化配置。

（1）需要安装mongodb，并且设置 MONGO_URL 的值

```
如果需要使用这个页面，那么无论选择何种中间件，即使不是使用mongo作为消息队列，也需要安装mongodb，因为因为是从这里读取数据的。
需要在 funboost_config.py 中设置MONGO_URL的值，mongo url的格式如下，这是通用的可以百度mongo url连接形式。
有密码 MONGO_CONNECT_URL = f'mongodb://yourname:yourpassword@127.0.01:27017/admin'
没密码 MONGO_CONNECT_URL = f'mongodb://192.168.6.132:27017/'
```

（2） 装饰器上需要设置持久化的配置参数,代码例子

```
框架默认不会保存消息状态和结果到mongo的，因为大部分人并没有安装mongo，且这个web显示并不是框架代码运行的必须部分，还有会降低一丝丝运行性能。


如果需要页面显示消费状态和结果，需要设置 @boost装饰器的 function_result_status_persistance_conf 的参数
FunctionResultStatusPersistanceConfig的如参是 (is_save_status: bool, is_save_result: bool, expire_seconds: int)
is_save_status 指的是是否保存消费状态，这个只有设置为True,才会保存消费状态到mongodb，从而使web页面能显示该队列任务的消费信息
is_save_result 指的是是否保存消费结果，如果函数的结果超大字符串或者对函数结果不关心或者函数没有返回值，可以设置为False。
expire_seconds 指的是多久以后，这些保存的数据自动从mongodb里面消失删除，避免爆磁盘。
```

```python
from funboost import boost, FunctionResultStatusPersistanceConfig, BoosterParams


@boost(BoosterParams(queue_name='queue_test_f01', qps=2,
       function_result_status_persistance_conf=FunctionResultStatusPersistanceConfig(
           is_save_status=True, is_save_result=True, expire_seconds=7 * 24 * 3600)))
def f(a, b):
    return a + b

if __name__ == '__main__':
    f(5, 6)  # 可以直接调用
  
    for i in range(0, 200):
        f.push(i, b=i * 2)
  
    f.consume()

```

(3) 消费结果状态保存到mongo什么库什么表了？

是固定保存到名为 task_status 的库，表的名字就是队列名字。每个函数都会使用一个单独的表来保存消费状态结果。
有的人企图在 MONGO_CONNECT_URL 中指定db来决定消费结果保存到什么db

如下图所示,每次函数运行后，一共保存了37个字段到数据库中。

mongo保存结果截图
![img_39.png](img_39.png)

### 4.11.2 框架是可以自动保存消费状态/结果到mongo，你想保存到MySQL?

需要看 4.19 用户自定义记录函数消费 状态/结果 钩子函数 章节，设置一个记录函数运行状态的钩子函数，
你想在函数里面做啥都可以，把状态/结果插入到elastic orcale都没人管得了你。

因为mysql需要运维建立数据库和建立表，funboost操作mongo可以代码中建立数据库和多个不同的队列名的表来保存消费状态。
用户想保存到mysql自己自定义 user_custom_record_process_info_func 钩子函数就好了,因为FunctionResultStatus对象上包含了所有必要信息。

#### 4.11.2.b  作者自己贡献一个吧函数消费状态保存到mysql的函数,(2024.02新增)

实现代码见文件:
[https://github.com/ydf0509/funboost/blob/master/funboost/contrib/save_result_status_to_sqldb.py](https://github.com/ydf0509/funboost/blob/master/funboost/contrib/save_result_status_to_sqldb.py)

```python

from funboost import boost, FunctionResultStatus, BoosterParams
import json
from funboost.contrib.save_result_status_to_sqldb import save_result_status_to_sqlalchemy # 不是框架必要部分的就通过 contrib 中增加代码.

"""
测试用户自定义记录函数消息处理的结果和状态到mysql

"""

# user_custom_record_process_info_func=my_save_process_info_fun 设置记录函数消费状态的钩子
@boost(BoosterParams(queue_name='test_user_custom', user_custom_record_process_info_func=save_result_status_to_sqlalchemy))
def f(x):
    print(x * 10)
    return x*10


if __name__ == '__main__':
    for i in range(3):
        f.push(i)
    print(f.publisher.get_message_count())
    f.consume()

```

```
作者自己实现的 save_result_status_to_sqlalchemy 记录函数,
1. 用户按照 funboost.contrib.save_result_status_to_sqldb 文件中的建表语句先建表,
2. 配置好 BrokerConnConfig.SQLACHEMY_ENGINE_URL 参数,
3. boost装饰器指定 user_custom_record_process_info_func=save_result_status_to_sqlalchemy
这样就能自动吧函数消费状态保存到mysql了.

用户自己也可以按需增加索引和增加字段和修改字段长度的,自己也可以改下建表语句或save_result_status_to_sqlalchemy函数就好了.
例如你可以增加消费函数的入参作为mysql表字段.
```

再一次附上funboost.contrib.save_result_status_to_sqldb 文件中的建表语句:

```sql
CREATE TABLE funboost_consume_results
(
    _id              VARCHAR(255),
    `function`         VARCHAR(255),
    host_name        VARCHAR(255),
    host_process     VARCHAR(255),
    insert_minutes   VARCHAR(255),
    insert_time      datetime,
    insert_time_str  VARCHAR(255),
    msg_dict         JSON,
    params           JSON,
    params_str       VARCHAR(255),
    process_id       BIGINT(20),
    publish_time     FLOAT,
    publish_time_str VARCHAR(255),
    queue_name       VARCHAR(255),
    result           VARCHAR(255),
    run_times        INT,
    script_name      VARCHAR(255),
    script_name_long VARCHAR(255),
    success          BOOLEAN,
    task_id          VARCHAR(255),
    thread_id        BIGINT(20),
    time_cost        FLOAT,
    time_end         FLOAT,
    time_start       FLOAT,
    total_thread     INT,
    utime            VARCHAR(255),
    `exception`       MEDIUMTEXT ,
    rpc_result_expire_seconds BIGINT(20),
    primary key (_id),
    key idx_insert_time(insert_time),
    key idx_queue_name_insert_time(queue_name,insert_time),
    key idx_params_str(params_str)
)

```

保存到mysql中的消费状态和结果截图:

![img_57.png](img_57.png)
![img_58.png](img_58.png)

### 4.11.3 可视化，启动python分布式函数调度框架之函数运行结果状态web

见第13章文档， 启动 funboost web,查看消费结果和队列管理

## 4.12 框架 asyncio 方式运行协程

<p style="color: #00A000">完整的除了asyncio并发，包括 aio_push 和 asyncio 来等待获取结果，请看4b.3 章节</p>p> [ funboost + 全asyncio 编程生态演示](https://funboost.readthedocs.io/zh-cn/latest/articles/c4b.html#b-3-funboost-asyncio)

### 4.12.1 concurrent_mode=ConcurrentModeEnum.ASYNC 运行协程

concurrent_mode=ConcurrentModeEnum.ASYNC是一个loop中真异步运行协程

见7.8的demo介绍，

```python
import asyncio
from funboost import boost, ConcurrentModeEnum, BoosterParams
@boost(BoosterParams(queue_name='async_queue', concurrent_mode=ConcurrentModeEnum.ASYNC))
async def f():
    await asyncio.sleep(2)
```

这种方式是@boost装饰在async def定义的函数上面。

celery不支持直接调度执行async def定义的函数，但此框架是直接支持asyncio并发的。

### 4.12.2 concurrent_mode=ConcurrentModeEnum.THREADING 运行asyncio协程

concurrent_mode=ConcurrentModeEnum.THREADING  在每个线程都创建独立的loop，每个协程运行在不同的loop中

见7.38的demo介绍，

```python
import asyncio
from funboost import boost, ConcurrentModeEnum, BoosterParams
@boost(BoosterParams(queue_name='threading_async_queue', concurrent_mode=ConcurrentModeEnum.THREADING))
async def f():
    await asyncio.sleep(2)
```

这种方式就是临时为每一个协程创建一个 loop,loop是一次性的。

```
funboot的asyncio 并发模式是真asyncio , 是在同一个loop中并发的运行多个协程对象。

伪 async 并发是多线程中每个线程临时 loop = asyncio.new_event_loop() ，然后 loop.run_until_complete() ， 
这种就是假的，每隔协程都运行在不同的loop中。
```

ConcurrentModeEnum.THREADING 照样可以运行async def的函数。

这种当然是伪asyncio的，是临时 创建一个 loop。 看你咋想的喜欢真asyncio还是假的，这种也可以单进程1秒钟运行2000次asyncio的函数

## 4.13 跨项目怎么发布任务或者获取函数执行结果(即不定义@boost消费函数就发送消息)？

别的语言项目或者别的python项目手动发布消息到中间件，让分布式函数调度框架消费任务，<br>
例如项目b中有add函数，项目a里面无法 import 导入这个add 函数。

##### 1)第一种方式，使用能操作消息中间件的python包，手动发布任务到消息队列中间件<br>

如果是别的语言发布任务，或者python项目a发布任务但是让python项目b的函数去执行，可以直接发布消息到中间件里面。<br>
手动发布时候需要注意 中间件类型 中间件地址 队列名 @boost和funboost_config.py指定的配置要保持一致。<br>
需要发布的消息内容是 入参字典转成json字符串，然后发布到消息队列中间件。<br>
以下以redis中间件为例子。演示手动发布任务到中间件。<br>

```python
@boost(BoosterParams(queue_name='test_queue668', broker_kind=BrokerEnum.REDIS))
def add(x, y):
    print(f'''  计算  {x} + {y} = {x + y}''')
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    r = Redis(db=7, host='127.0.0.1')
    for i in range(10):
        add.push(i, i * 2)  # 正常同一个python项目是这么发布消息,使用函数.push或者publish方法
        r.lpush('test_queue668', json.dumps({'x': i, 'y': i * 2}))  # 不同的项目交互，可以直接手动发布消息到中间件
```

```
这个很容易黑盒测试出来，自己观察下中间件里面的内容格式就能很容易手动模仿构造出消息内容了。

需要说明的是 消息内容不仅包括 入参本身，也包括其他控制功能的辅助参数，可以用框架的自动发布功能发布消息，然后观察中间件里面的字段内容，模拟构造。

举个例子之一，例如如果要使用消息过期丢弃这个功能，那么就需要发布消息当时的时间戳了。
```

##### 2)第二种方式，使用伪函数来作为任务,只写函数声明不写函数体。<br>

此方式是一名网友的很机智的建议，我觉得可行。<br>
例如还是以上面的求和函数任务为例，在项目a里面可以定义一个假函数声明,并且将b项目的求和add函数装饰器复制过去，但函数体不需要具体内容

```python
@boost(BoosterParams(queue_name='test_queue668', broker_kind=BrokerEnum.REDIS))  # a项目里面的这行和b项目里面的add函数装饰器保持一致。
def add(x, y):  # 方法名可以一样，也可以不一样，但函数入参个数 位置 名称需要保持不变。
    pass  # 方法体，没有具体的求和逻辑代码，只需要写个pass就行了。

add.push(1,y=2)
```

之后通过这个假的add函数就可以享受到与在同一个项目中如何正常发布和获取求和函数的执行结果 一模一样的写法方式了。<br>
例如add.clear() 清空消息队列，add.push发布,add.publish发布，async_result.get获取结果，都可以正常使用，
但不要使用add.consume启动消费，因为这个是假的函数体，不能真正的执行求和.<br>

##### 3)第三种方式(推荐),使用BoostersManager.get_cross_project_publisher来获取发布者,然后使用publish来发布函数的入参字典。

```python
from funboost import BoostersManager, PublisherParams, BrokerEnum

publisher = BoostersManager.get_cross_project_publisher(PublisherParams(queue_name='test_cross_qeueu1', broker_kind=BrokerEnum.REDIS, publish_msg_log_use_full_msg=True))
publisher.publish({"a": 1, "b": 2})  # 远程函数入参是 def f(a,b)

# 如果还包含其他消息控制字段，其他的extra中的参数，可以查看并模仿消息队列中的消息，自行构造。

'''send_msg 是发送原始消息到消息队列，就是不会给消费加上extra， taskid 等额外字段。
publish会自动添加extra taskid publish_time等字段到消息中，send_msg则不会 '''
publisher.send_msg({"c": 5, "d": 6}) 

```

##### 4)第四种方式,在消费函数所在项目里面用 fastapi flask啥的写一个接口用于接受请求并把接收到的消息发送到消息队列(框架自带了一个fastapi 发布消息接口).

例如项目a是java,项目b是你的python消费函数所在项目.

你在b项目里面用falsk fastapi 框架开个接口,接口中根据队列名和消息体,在python项目的web接口中发布消息到消息队列.

<p style="color: red">funboost.contrib.api_publish_msg 贡献了一个fastapi的接口,可以用于发布消息和获取消息执行结果.</p>

运行web前,用户需要手动import导入 @boost所在模块,或者BoosterDiscovery自动导入模块,以便能找到队列对应的函数.

```python
from pathlib import Path

from funboost.contrib.api_publish_msg import app, BoosterDiscovery

"""
# 如果用户不使用 BoosterDiscovery,那么需要导入一下boost相关的函数所在的模块,不然无法根据队列名找到队列相关的函数定义.
需要
import test_frame.test_api_publish_msg.tasks.boost1
import test_frame.test_api_publish_msg.tasks.boost2
"""

BoosterDiscovery(project_root_path=Path(__file__).absolute().parent.parent.parent,
                 booster_dirs=[Path(__file__).absolute().parent / Path('tasks')]).auto_discovery()

if __name__ == '__main__':
    '''
    uvicorn test_frame.test_api_publish_msg.test_api_publish_server:app --workers 4 --port 16667
    '''
    import uvicorn

    uvicorn.run('funboost.contrib.api_publish_msg:app', host="0.0.0.0", port=16667, workers=4)


```

## 4.14 获取消费进程信息的方法(用于排查查看正在运行的消费者)

```python3
from funboost import ActiveCousumerProcessInfoGetter

'''
获取分布式环境中的消费进程信息。
使用这里面的4个方法需要相应函数的@boost装饰器设置 is_send_consumer_hearbeat_to_redis=True，这样会自动发送活跃心跳到redis。否则查询不到该函数的消费者进程信息。
要想使用消费者进程信息统计功能，用户无论使用何种消息队列中间件类型，用户都必须安装redis，并在 funboost_config.py 中配置好redis链接信息
'''

# 获取分布式环境中 test_queue 队列的所有消费者信息
print(ActiveCousumerProcessInfoGetter().get_all_hearbeat_info_by_queue_name('test_queue'))

# 获取分布式环境中 当前列机器的所有消费者信息
print(ActiveCousumerProcessInfoGetter().get_all_hearbeat_info_by_ip())

# 获取分布式环境中 指定ip的所有消费者信息
print(ActiveCousumerProcessInfoGetter().get_all_hearbeat_info_by_ip('10.0.195.220'))

# 获取分布式环境中 所有 队列的所有消费者信息，按队列划分
print(ActiveCousumerProcessInfoGetter().get_all_hearbeat_info_partition_by_queue_name())

# 获取分布式环境中 所有 机器的所有消费者信息，按ip划分
print(ActiveCousumerProcessInfoGetter().get_all_hearbeat_info_partition_by_ip())
```

获取消费进程信息的方法的用途，用于排查查看正在运行的消费者

```
1、有的人老是说自己已经把消费进程关了，但是消息队列中的消费还在消费，用get_all_hearbeat_info_by_queue_name方法就能查出来还有哪些机器在消费这个队列了
2、有的人老是说发送消息，消息队列的任务，没被消费，也可以使用get_all_hearbeat_info_by_queue_name方法
3、get_all_hearbeat_info_by_ip 方法用于查看一台机器在运行哪些消息队列。
4、get_all_hearbeat_info_partition_by_queue_name和get_all_hearbeat_info_partition_by_ip分别按队列和机器分组显示
```

## 4.16 文件日志所在的地方

框架使用的是nb_log,控制台五彩日志 + 多进程安全切割文件的 nb_log

你项目根目录下的 nb_log_config.py 中的 LOG_PATH 决定了默认日志文件夹的位置，win默认在磁盘根目录下的/pythonlogs文件夹。
具体看 nb_log_config.py

nb_log 介绍见: [https://github.com/ydf0509/nb_log](https://github.com/ydf0509/nb_log)

tips:

嫌弃日志提示详细(啰嗦)的问题见:文档6.17  https://funboost.readthedocs.io/zh-cn/latest/articles/c6.html#b-2-logmanager-preset-log-level

### 4.16.1 没亲自指定 日志文件名

代码:

![img_50.png](img_50.png)

文件日志截图:
![img_49.png](img_49.png)

如上图，如果你不在boost装饰器亲自指定log_filename,那么每个队列的都有单独的日志文件，就是不同的消费函数写在不同的日志文件中，很方便查看问题。

### 4.16.2 亲自指定日志文件名,log_filename的值

如果你指定了log_filename,那么就会写入到你指定的文件中,而不是使用队列名自动生成文件名.

代码:

```python
import logging
import time
from funboost import boost, BrokerEnum, BoosterParams
from nb_log import get_logger

LOG_FILENAME = '自定义日志文件名.log'


class BoosterParamsMy(BoosterParams):  # 传这个类就可以少每次都亲自指定使用rabbitmq作为消息队列，和使用rpc模式。
    """
    定义子类时候，字段也要注意带上类型注释
    """
    broker_kind: str = BrokerEnum.RABBITMQ
    max_retry_times: int = 4
    log_level: int = logging.DEBUG
    log_filename: str = LOG_FILENAME


my_file_logger = get_logger('my_business', log_filename=LOG_FILENAME)


@boost(boost_params=BoosterParamsMy(queue_name='task_queue_name1111', qps=3, ))
def task_fun(x, y):
    print(f'{x} + {y} = {x + y}')
    my_file_logger.debug(f"1111 这条日志会写到 {LOG_FILENAME} 日志文件中  {x} + {y} = {x + y}")
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 3 次 这个 task_fun 函数的目的。


@boost(boost_params=BoosterParamsMy(queue_name='task_queue_name2222', qps=10, ))
def task_fun2(x, y):
    print(f'{x} - {y} = {x - y}')
    my_file_logger.debug(f"2222 这条日志会写到 {LOG_FILENAME} 日志文件中 {x} - {y} = {x - y} ")
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 10 次 这个 task_fun 函数的目的。


if __name__ == "__main__":
    task_fun.consume()  # 消费者启动循环调度并发消费任务
    task_fun2.consume()
    for i in range(10):
        task_fun.push(i, y=i * 2)  # 发布者发布任务
        task_fun2.push(i, i * 10)


```

日志文件截图,可以发现所有消费发布都写到 自定义日志文件名.log里面了,my_file_logger 的get_logger 入参 log_filename 也是指定写到 这个文件,
所以你的业务日志和框架日志可以是在同一个文件中

![img_51.png](img_51.png)

### 4.16.3 把用户自己的业务日志和funboost框架日志写到同一个文件

```
from nb_log import get_logger
如上 4.16.2, my_file_logger = get_logger('my_business', log_filename=LOG_FILENAME),
你用这个实例化的 my_file_logger 去记录日志,
在boost装饰器的log_filename 和get_logger 的 log_filename 指定为相同的文件名字,那就可以写入同一个文件了.
```

## 4.16.4 funboost 日志由 nb_log 提供。

关于funboost的日志和日志级别过滤，看nb_log 9.5 章节文档

[https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id6](https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id6)

## 4.17 判断函数运行完所有任务，再执行后续操作

```text
框架是消息队列执行任务，理论上永不停止，消息源源不断的进入消息队列然后被消费，
不会有明显的结束含义，即使消息队列已经空了，代码也会待命拉取消费未来的下一条消息，
因为代码无法知道用户会不会将来又push消息到消息队列中。

但有的人脚本是一次性运行的或者他需要当前批次的消息消费完后执行某个操作，
可以使用 wait_for_possible_has_finish_all_tasks来判断函数的消息队列是否已经运行完了。
原理是消费者近n分钟内没有执行任务并且消息队列中间件中的消息数量持续n分钟是0，就判断为可能运行完了。
wait_for_possible_has_finish_all_tasks的入参是判断n分钟内消息数量，那么这个n最好是消费函数最大运行时间的3倍。
例如函数最大耗时120秒，那么可以设置入参为6分钟，如果设置过小，可能会出现实际还有余量任务正在执行中，导致判断失误。

wait_for_possible_has_finish_all_tasks是一个阻塞函数，只有判断疑似消息队列所有任务完成了，代码才会运行到下一行。
然后执行某些操作，例如可以发个邮件通知下，例如 os._exit()可以退出脚本，非常的灵活。

```

此功能可以用于，例如

```
爬取猫眼 淘票票 糯米全中国所有城市的电影院的放映场次，然后对电影场次进行全网匹配和统计分析，一个电影场次在每个app的价格，统计全中国每个城市播放多少场次电影。
那么这种后续的操作就必须先等每一个电影播放场次的详情页爬虫函数运行完了，再进行匹配和统计分析。如果都没爬取完成还在运行，就开始执行全量电影场次的统计分析那无疑是漏数据不准确。
```

```python
import time
import os

from funboost import boost, BoosterParams


@boost(BoosterParams(queue_name='test_f1_queue', qps=0.5))
def f1(x):
    time.sleep(3)
    print(f'x: {x}')
    for j in range(1, 5):
        f2.push(x * j)


@boost(BoosterParams(queue_name='test_f2_queue', qps=2))
def f2(y):
    time.sleep(5)
    print(f'y: {y}')


if __name__ == '__main__':
    f1.clear()
    f2.clear()
    for i in range(30):
        f1.push(i)
    f1.consume()
    f1.wait_for_possible_has_finish_all_tasks(4)
    print('f1函数的队列中4分钟内没有需要执行的任务,f1运行完了，现在启动f2的消费')
    f2.consume()
    f2.wait_for_possible_has_finish_all_tasks(3)
    print('f2函数的队列中3分钟内没有需要执行的任务，发个邮件通知一下')
    print('f1 和f2任务都运行完了，。。。')
    print('马上 os._exit(444) 结束脚本')
    os._exit(444)  # 结束脚本
```

## 4.18 暂停消费

框架支持暂停消费功能和继续消费功能，boost装饰器需要设置is_send_consumer_hearbeat_to_redis=True

```python
from funboost import boost, BoosterParams

@boost(BoosterParams(queue_name='test_queue73ac', is_send_consumer_hearbeat_to_redis=True))
def f2(a, b):
    return a - b


if __name__ == '__main__':
    for i in range(1000):
        # f.push(i, i * 2)
        f2.push(i, i * 2)
    f2.consume()
  
    while 1:
        f2.pause_consume()
        time.sleep(300)
        f2.continue_consume()
        time.sleep(300)

```

```
f.continue_consume 意思是继续消费，这个设置redis对应键 f'funboost_pause_flag:{self.queue_name}' 的状态为1了，
f.pause_consume 意思是暂停消费，这个设置redis对应键 f'funboost_pause_flag:{self.queue_name}' 的状态为0了，
框架中有专门的线程每隔10秒扫描redis中设置的暂停状态判断是否需要暂停和继续消费，所以设置暂停和接续后最多需要10秒就能暂停或启动消费生效了。
```

![img_26.png](img_26.png)

上图片为上面例子的代码消费5分钟然后暂停5分钟，一直循环

```
有的人问怎么在其他地方设置暂停消费，说我这例子是函数和设置暂停消费在同一个脚本，
这个从redis获取暂停状态本来就是为了支持从python解释器外部或者远程机器设置暂停，怎么可能只能在函数所在脚本设置暂停消费。

例如在脚本 control_pause.py中写

from xx import f2

f2.pause_consume()

这不就完了吗。如果是别的java项目代码中控制暂停消费，可以设置redis的 funboost_pause_flag:{queue_name} 这个键的值为 1，
这样就能使消费暂停了。在python web接口中设置暂停状态就用 f2.pause_consume() 就行了。

```

## 4.19 用户自定义记录函数消费 状态/结果 钩子函数

```
可以通过设置 user_custom_record_process_info_func 的值指向你的函数，来记录函数的消费结果，这种比较灵活。
用户定义一个函数，函数的入参只有一个 function_result_status ，这个变量是 FunctionResultStatus 类型的对象，有很多属性可供使用，
例如函数 入参 结果 耗时 发布时间 处理线程id 处理机器等等，可以更好的和用户自己的系统对接。
```

```python
from funboost import boost, FunctionResultStatus, BoosterParams

"""
测试用户自定义记录函数消息处理的结果和状态到mysql

"""


def my_save_process_info_fun(function_result_status: FunctionResultStatus):
    """ function_result_status变量上有各种丰富的信息 ,用户可以使用其中的信息
    用户自定义记录函数消费信息的钩子函数
    """
    print('function_result_status变量上有各种丰富的信息: ',
          function_result_status.publish_time, function_result_status.publish_time_str,
          function_result_status.params, function_result_status.msg_dict,
          function_result_status.time_cost, function_result_status.result,
          function_result_status.process_id, function_result_status.thread_id,
          function_result_status.host_process, )
    print('保存到数据库', function_result_status.get_status_dict())

# user_custom_record_process_info_func=my_save_process_info_fun 设置记录函数消费状态的钩子
@boost(BoosterParams(queue_name='test_user_custom', user_custom_record_process_info_func=my_save_process_info_fun))
def f(x):
    print(x * 10)


if __name__ == '__main__':
    for i in range(50):
        f.push(i)
    print(f.publisher.get_message_count())
    f.consume()

```

### 4.19.b 自定义保存函数消费状态结果到mysql/sqlite/pgsql请看4.11.2.b的章节

## 4.20 通过 broker_exclusive_config 参数 设置不同中间件能使用到的差异化独特配置

```
加上一个不同种类中间件非通用的配置,不同中间件自身独有的配置，不是所有中间件都兼容的配置，因为框架支持30种消息队列，消息队列不仅仅是一般的先进先出queue这么简单的概念，
例如kafka支持消费者组，rabbitmq也支持各种独特概念例如各种ack机制 复杂路由机制，每一种消息队列都有独特的配置参数意义，可以通过这里传递。

之前的做法是为了简化难度和兼容各种消息队列中间件用法，有的地方写死了不利于精细化控制使用，例如kafka消费其实有很多配置的高达30多项，不是光有个 bootstrap_servers 设置kafka的地址，
例如 group_id  max_in_flight_requests_per_connection auto_offset_reset 等。以后会逐步精细化针对各种消息队列的独特概念用途放开更多的差异化独特配置。

使用方式例如设置
@boost(BoosterParams(queue_name='test_queue70ac', broker_kind=BrokerEnum.KAFKA_CONFLUENT, broker_exclusive_config={'group_id':"my_kafka_group_id_xx"}))
def f(x):
    pass
  
具体的每种消息队列能支持哪些参数配置，必须是对应Consumer类的 BROKER_EXCLUSIVE_CONFIG_KEYS 指定的配置名字的范围之类才能起作用，
例如你使用redis的list结构做消息队列，你去设置消费者组那是没什么卵用的。

打个比喻消费是看书，redis的list和rabbitmq消费消息，是看一页就把书本的那一页撕下来，下次继续看书本中剩下的页就好了。不可多组重复回拨消费，不需要存在啥消费者组这种概念。
kafka消费消息，是小明和小红分别看这本书，小明每看完几页后，会夹一个小明的书签到最新看到的地方，下次小明继续看就先找到小明的书签，继续读之后的页数。
小红和小明分别使用不同的书签标记他们各自读到哪一页了，kafka不是看完一页就把那张撕下来，所以kafka存在消费者组概念，
所以funboost提供broker_exclusive_config入参来支持不同消息队列独有特性。

以后将增加更多的差异化设置参数，能更深入灵活使用不同中间件的独特概念和功能
```

## 4.21 【完全自由定制扩展（方式1）】 使用 register_custom_broker 完全彻底自由灵活自定义扩展和定制修改中间件(消费者和发布者)

4.21和4.21b 都可以实现普通用户自由增加新中间件；

也可以用于不重头增加新的中间件，而是覆盖修改父类逻辑，例如funboost某个地方有bug或者你想按你的逻辑来运行，都可以用户高度自定义，用户压根不需要修改funboost的源码。       
有些人很冲动不看教程，老想硬改site_packages pip安装目录下的funboost安装包源码，压根不需要的，因为框架已经提供了用户级别高度自定义扩展，用户的方法可以覆盖任何AbstractConsumer的方法以及他的子类方法。

**方式1，使用register_custom_broker**
继承框架的消费者和发布者抽象类或抽象类的子孙类，注册到框架种。消费和发布逻辑细节可以完全由用户自定义。


<pre style="font-size: large;color: greenyellow;background-color: black">
这个是增加的一种很强大的功能,用户可以自定义发布者和消费者，注册到框架中。boost装饰器就能自动使用你的消费者类和发布者类了。
这个功能很好很强，能彻底解决框架的流程逻辑不符合你的期望时候，用户能够自定义一些细节。需要用户有一定的python语法基础和面向对象 设计模式才能用这个功能。
为什么增加这个功能，是由于总是有不符合用户期望的细节，用户如果要定制就要修改源码这样不方便，现在有了这就可以自由定制扩展了
</pre>

<pre style=" font-size: large; font-family: 黑体,serif; color: brown">
用户自定义的类可以继承 AbstractConsumer ，这种方式适合扩展支持新的中间件种类。<br>

也可以继承自框架中已有的 AbstractConsumer 的子类，这种适合对逻辑进行调整，或者增加打印什么的 。
test_frame/test_custom_broker/test_custom_redis_consume_latest_publish_msg_broker.py 就是继承自 AbstractConsumer 的子类。

</pre>

```
register_custom_broker有两个用途
1 是给用户提供一种方式新增消息队列中间件种类，(funboost框架支持了所有知名类型消息队列中间件或模拟中间件，这个用途的可能性比较少)
2 可以对已有中间件类型的消费者 发布者类继承重写符合自己意愿的，这样就不需要修改项目的源代码了，这种用法非常的强大自由，可以满足一切用户的特殊定制想法。
  因为用户可以使用到self成员变量和通过重写使用其中的函数内部局部变量，能够做到更精细化的特殊定制。这个用途很强大自由灵活定制。

用法例如 register_custom_broker(BROKER_KIND_LIST, ListPublisher, ListConsumer)  # 核心，这就是将自己写的类注册到框架中，框架可以自动使用用户的类，这样用户无需修改框架的源代码了。

```

以下为4个扩展或定制的代码例子：

[继承AbstractConsumer基类 ，自定义扩展使用list作为消息队列](https://github.com/ydf0509/funboost/tree/master/test_frame/test_custom_broker/test_custom_list_as_broker.py)

[继承AbstractConsumer基类 ，自定义扩展使用deque作为消息队列](https://github.com/ydf0509/funboost/tree/master/test_frame/test_custom_broker/test_custom_deque_as_broker.py)

[继承AbstractConsumer的子类 ，自定义扩展使用redis实现先进后出 后进先出，总是优先消费最晚发布的消息的例子](https://github.com/ydf0509/funboost/tree/master/test_frame/test_custom_broker/test_custom_redis_consume_latest_publish_msg_broker.py)

[继承AbstractConsumer的子类 ，自定义扩展重写消费者最核心控制运行函数的 _run方法的逻辑的例子](https://github.com/ydf0509/funboost/tree/master/test_frame/test_custom_broker/rewrite_run.py)

## 4.21b 【完全自由定制扩展(方式2)】,使用 consumer_override_cls 和 publisher_override_cls 来自定义消费者 发布者。

**方式2，使用装饰器的入参 consumer_override_cls 和 publisher_override_cls**

### 4.21b.1 重写某些方法的例子

下面的例子是自定义一个MyConsumer，传给 consumer_override_cls，MyConsumer可以继承自AbstractConsumer或者他的子类。
这个代码会让用户自定义记录函数的消费结果，可以重写AbstractConsumer的任意所有方法和属性，所以用户完全可以自由定义重写。

同理，通过指定 publisher_override_cls 一个自定义的 Publisher类，用户可以重写或自定义发布者。

下面例子是重写实现记录函数消费状态方法，所以只需要重写 user_custom_record_process_info_func ，
你就能实现 celery的类似 on_sucess 和 on_failure

```python
import time

from funboost import boost, BrokerEnum, BoosterParams, AbstractConsumer, FunctionResultStatus


import random
import time

from funboost import boost, BrokerEnum, FunctionResultStatusPersistanceConfig, BoosterParams, ConcurrentModeEnum, AbstractConsumer, FunctionResultStatus


class MyConsumer(AbstractConsumer):
    def user_custom_record_process_info_func(self, current_function_result_status: FunctionResultStatus):
        print('使用指定的consumer_override_cls来自定义或重写方法')
        if current_function_result_status.success is True:
            print(f'入参 {current_function_result_status.params} 成功了，结果是： {current_function_result_status.result}，模拟发个微信通知')
        else:
            print(f'入参 {current_function_result_status.params} 失败了，原因是： {current_function_result_status.exception},模拟发个邮件')
        self.logger.debug(current_function_result_status.get_status_dict()) # 给用户打印下current_function_result_status有哪些字段信息。


@boost(BoosterParams(queue_name='test_redis_ack_use_timeout_queue', broker_kind=BrokerEnum.REDIS,
                     concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD,
                     log_level=10,  consumer_override_cls=MyConsumer,
                     is_show_message_get_from_broker=True))
def cost_long_time_fun(x):
    print(f'start {x}')
    time.sleep(2)
    if random.random()>0.5:
        raise ValueError('模拟函数运行出错')
    print(f'end {x}')
    return x*2


if __name__ == '__main__':
    for i in range(100):
        cost_long_time_fun.push(i)
    cost_long_time_fun.consume()

```

上面例子是重写了父类方法,轻度的自定义某个方法.
也可以重量级自定义用于新增消息队列中间件种类,例如下面的代码,使用 list 模拟消息队列.

### 4.21b.2 完全实现新增中间件类型.

使用 list 列表作为 消息队列的中间件 实现, 通过指定 consumer_override_cls 和 publisher_override_cls 为用户自定义的类来实现新增消息队列种类。

这里只是用例子演示怎么使用  consumer_override_cls 和 publisher_override_cls 来开发新的消息队列种类,增加到 funboost,
不是真的推荐用户在生产大规模使用 list 结构作为消息队列中间件.

```python
import threading

import json

import time
from collections import defaultdict
from funboost import boost, BrokerEnum, BoosterParams, EmptyConsumer, EmptyPublisher

queue_name__list_map = defaultdict(list)
list_lock = threading.Lock()

'''
使用 list 列表作为 消息队列的中间件 实现, 通过指定 consumer_override_cls 和 publisher_override_cls 为用户自定义的类来实现新增消息队列种类。
这里只是用例子演示怎么使用  consumer_override_cls 和 publisher_override_cls 来开发新的消息队列种类,增加到 funboost, 
不是真的推荐用户在生产大规模使用 list 结构作为消息队列中间件.
'''
class MyListConsumer(EmptyConsumer):
    def custom_init(self):
        self.list: list = queue_name__list_map[self.queue_name]

    def _shedual_task(self):
        while True:
            try:
                with list_lock:
                    msg = self.list.pop()
                self._submit_task({'body': msg})
            except IndexError:
                time.sleep(0.1)

    def _confirm_consume(self, kw):
        """ 这里是演示,所以搞简单一点,不实现确认消费 """
        pass

    def _requeue(self, kw):
        with list_lock:
            self.list.append(kw['body'])


class MyListPublisher(EmptyPublisher):
    def custom_init(self):
        self.list: list = queue_name__list_map[self.queue_name]

    def concrete_realization_of_publish(self, msg: str):
        with list_lock:
            self.list.append(msg)

    def clear(self):
        with list_lock:
            self.list.clear()

    def get_message_count(self):
        with list_lock:
            return len(self.list)

    def close(self):
        pass


'''
完全重新自定义增加中间件时候,broker_kind 建议指定为 BrokerEnum.EMPTY
'''


@boost(BoosterParams(queue_name='test_define_list_queue',
                     broker_kind=BrokerEnum.EMPTY,  # 完全重新自定义新增中间件时候,broker_kind 请指定 BrokerEnum.EMPTY
                     concurrent_num=10, consumer_override_cls=MyListConsumer, publisher_override_cls=MyListPublisher,
                     is_show_message_get_from_broker=True))
def cost_long_time_fun(x):
    print(f'start {x}')
    time.sleep(20)
    print(f'end {x}')


if __name__ == '__main__':

    for i in range(100):
        cost_long_time_fun.push(i)
    cost_long_time_fun.consume()

```


**在文档4b.2c章节,也演示了通过指定 consumer_override_cls 来消费任意格式的消息,用户可以和4.21章节一起阅读**

## 4.23 演示funboost框架是如何代替用户手写调用线程池的

为什么框架介绍中说有了funboost，再也无需用户手动操作线程和线程池ThradPoolExecutor以及multiprossing.Process()了。

手动使用线程池写法

```python
import time
from concurrent.futures import ThreadPoolExecutor


def f(x, y):
    print(f'{x} + {y} = {x + y}')
    time.sleep(10)


if __name__ == '__main__':

    pool = ThreadPoolExecutor(5)

    for i in range(100):
        pool.submit(f, i, i * 2)
```

funboost取代手写调用线程池

```python
import time
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test1', broker_kind=BrokerEnum.MEMORY_QUEUE, concurrent_num=5))
def f(x, y):
    print(f'{x} + {y} = {x + y}')
    time.sleep(10)


if __name__ == '__main__':
    f.consume()
    for i in range(100):
        f.push(i, i * 2)

```

```text
这两个的效果是一样的，都是使用内存queue来保存待运行的任务，都是使用5线程并发运行f函数的。

funboost还能开启多进程，取代用户手写 Process(target=fx),所以有了funboost，用户无需手写开启线程 进程。

如果用户希望任务保存到redis中先，而不是保存在python内存queue中，那就使用funboost比调用ThreadPoolExecutor方便多了。
再比如用户希望每秒运行完成10次f函数(控制台每秒都打印10次求和结果)，而不是开启10线程来运行f函数，funboost则远方便于ThreadPoolExecutor
```

## 4.24 设置消费函数重试次数

```python
import random
import time
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_queue9', broker_kind=BrokerEnum.REDIS_ACK_ABLE, max_retry_times=5))
def add(a, b):
    time.sleep(2)
    if random.random() >0.5:
        raise ValueError('模拟消费函数可能出错')
    return a + b


if __name__ == '__main__':
    for i in range(1,1000):
        add.push(i,i*2)
    add.consume()
```

```
通过设置 max_retry_times 的值，可以设置最大重试次数，函数如果出错了，立即将参数重试max_retry_times次，如果重试次数达到指定的max_retry_times，就执行确认消费了。
```

### 4.24.b 抛出ExceptionForRequeue类型错误，消息立即重回消息队列

```python
@boost(BoosterParams(queue_name='test_rpc_queue', is_using_rpc_mode=True, broker_kind=BrokerEnum.REDIS_ACK_ABLE, qps=100, max_retry_times=5))
def add(a, b):
    time.sleep(2)
    if random.random() >0.5:
        raise ExceptionForRequeue('模拟消费函数可能出错,抛出ExceptionForRequeue类型的错误可以使消息立即重回消息队列')
    return a + b


if __name__ == '__main__':
    add.consume()
```

```
消费函数中 raise ExceptionForRequeue ，会使消息立即重回消息队列的尾部。  如果函数运行该消息的出错概率使100%，就要慎重了，
避免函数运行这个消息一直出错一直重回消息队列，无限蒙蔽死循环消费这个入参。
```

### 4.24.c 抛出 ExceptionForPushToDlxqueue 类型错误，消息发送到单独另外的死信队列中

```python
@boost(BoosterParams(queue_name='test_rpc_queue', is_using_rpc_mode=True, broker_kind=BrokerEnum.REDIS_ACK_ABLE, qps=100, max_retry_times=5))
def add(a, b):
    time.sleep(2)
    if random.random() >0.5:
        raise ExceptionForPushToDlxqueue('模拟消费函数可能出错,抛出ExceptionForPushToDlxqueue类型的错误，可以使消息发送到单独的死信队列中')
    return a + b


if __name__ == '__main__':
    add.consume()
```

```
消费函数中 raise ExceptionForPushToDlxqueue ，可以使消息发送到单独的死信队列中，死信队列的名字是正常队列的名字 + _dlx
```

### 4.24.d  设置is_push_to_dlx_queue_when_retry_max_times,重试到max_retry_times最大次数没成功发送到死信队列

```
@boost 装饰器 设置 is_push_to_dlx_queue_when_retry_max_times = True，
则函数运行消息出错达到max_retry_times最大重试次数后仍没成功，确认消费，同时发送到死信队列中。
```

### 4.24.e (内置辅助)将一个消息队列中的消息转移到另一个队列

```
可以用于死信队列转移到正常队列。
```

```python
from funboost.contrib.queue2queue import consume_and_push_to_another_queue,multi_prcocess_queue2queue

if __name__ == '__main__':
    # 一次转移一个队列，使用单进程
    # consume_and_push_to_another_queue('test_queue77h3', BrokerEnum.RABBITMQ_AMQPSTORM,
    #                                   'test_queue77h3_dlx', BrokerEnum.RABBITMQ_AMQPSTORM,
    #                                   log_level_int=logging.INFO, exit_script_when_finish=True)

    # 转移多个队列，并使用多进程。
    multi_prcocess_queue2queue([['test_queue77h5', BrokerEnum.RABBITMQ_AMQPSTORM, 'test_queue77h4', BrokerEnum.RABBITMQ_AMQPSTORM]],
                               log_level_int=logging.INFO, exit_script_when_finish=True, n=6)
```

## 4.25 push和publish发布消息区别

```
funboost的push和publish 就像celery的delay和apply_async关系一样。
一个简单方便，一个复杂强大。前者的入参和函数本身入参类似，后者除了函数入参本身，还可以单独指定改任务的控制属性。
```

```python
from funboost import boost, BoosterParams
@boost(BoosterParams(queue_name='test_queue_pub'))
def add(a, b):
    return a + b

if __name__ == '__main__':
    # push的入参就和正常调用函数一样的入参方式，框架会自动把多个入参组合成一个字典，字典再转化成json发布到消息队列。
    add.push(1,2)
    add.push(1,b=2)
    add.push(a=1,b=2)
  
    # publish 意思是把所有入参参数作为一个字典，框架会把字典转化成json发布到消息队列，publish除了发布函数入场本身外，还可以设置一些其他任务属性。
    # 所以publish是比push更强大的存在，push是简单，publish是更可以发布任务控制参数。
    add.publish({"a":1,"b":2})  
    # publish 除了可以发布函数入参本身以外，还能发布任务控制参数，例如可以手动的指定id而非有框架自动生成任务id，还能设置其他控制参数。
    # 例如 在 priority_control_config的PriorityConsumingControlConfig中设置   msg_expire_senconds =5，可以使得发布消息离消费超过5秒，丢弃消息不消费。
    # 例如设置is_using_rpc_mode = True ，则可以单独使该任务参数支持rpc获得结果。
    add.publish({"a":1,"b":2},task_id=100005,priority_control_config=PriorityConsumingControlConfig(is_using_rpc_mode=True))
```

## 4.26 性能调优演示

要看4.5章节的说明，有的人不看文档，不知道怎么性能达到最好，不知道怎么开多进程,只知道简单demo的 fun.consume()方式启动消费

有的人不看4.5章节文档，需要重新说明

```python
import time
from funboost import boost, ConcurrentModeEnum, BoosterParams

@boost(BoosterParams(queue_name='test_queue_add'))
def add(a, b):
    time.sleep(2) # 模拟io或cpu耗时
    return a + b

@boost(BoosterParams(queue_name='test_queue_sub', concurrent_num=200, concurrent_mode=ConcurrentModeEnum.THREADING))
def sub(x, y):
    time.sleep(5) # 模拟io或cpu耗时
    return x - y
```

对于上面这两个消费函数，启动消费说明

### 4.26.1 在一个进程中启动多个函数的消费，适合轻型任务

常规启动方式是这样，直接在当前进程里面启动两个函数的consume

```
add.consume()
sub.consume()

这种是一个进程内部启动多个消费函数，每个函数是默认使用多线程运行或协程（有5种细粒度并发模式，默认是线程，详细看4.5章节的介绍）
如果这个python进程的任务较重，python进程的cpu已经明显很高了，则应该使用多进程叠加线程（协程）并发
```

### 4.26.2 在多个进程中启动函数的消费，适合一次启动大量函数的消费或重型任务

假如add和sub是很费cpu的函数，或者一次性启动30个函数的消费，4.26.1的在一个进程中启动多个函数的消费的方式就不合适了。

应该在独立进程中运行函数，这样性能好，突破单进程 无法使用多核心 gil限制，充分使用多核。

```
add.multi_process_consume(1) # 独立开1个进程，每个进程内部使用多线程运行或协程 来运行求和函数
sub.multi_process_consume(3) # 独立开3个进程来运行求差函数，每个进程内部使用多线程运行或协程 来运行求和函数.
sub函数是开3个进程，每个进程使用多线程并发方式，每个进程内部按照boost装饰器指定的，开了200线程。也就是总共600线程运行sub函数。
3进程，每个进程内部开200线程，比单进程设置600线程岁强很多的。尤其是cpu密集型，多进程优势明显。

```

要看4.5章节的说明，有的人不看文档，不知道怎么性能达到最好，不知道怎么开多进程,只知道简单demo的 fun.consume()方式启动消费

## 4.28 funboost 支持celery框架整体作为funboost的broker (2023.4新增)

funboost的api来操作celery，完爆用户亲自操作celery框架。

害怕celery框架用法pythoner的福音。

```
见11.1章节代码例子，celery框架整体作为funboost的broker，funboost的发布和消费将只作为极简api，核心的消费调度和发布和定时功能，都是由celery框架来完成，funboost框架的发布和调度代码不实际起作用。
用户操作funboost的api，语法和使用其他消息队列中间件类型一样，funboost自动化操作celery。

用户无需操作celery本身，无需敲击celery难记的命令行启动消费、定时、flower;
用户无需小心翼翼纠结亲自使用celery时候怎么规划目录结构 文件夹命名 需要怎么在配置写include 写task_routes，
完全不存在需要固定的celery目录结构，不需要手动配置懵逼的任务路由，不需要配置每个函数怎么使用不同的队列名字，funboost自动搞定这些。
celery框架的一大堆需要用户使用的重要的高频公有核心方法入参声明都是 *agrs,**kwargs，代码无法在ide补全，
并且点击到celery源码方法里面取也没有明确的说明*agrs **kwargs能传递哪些几十个参数，网上的简单demoi例子也不会列举出来各种细节入参，导致一般用户不知道celery能传什么，
 比如@app.task的入参、task_fun.apply_async的入参、app.send_task、celery的配置大全 能传哪些，用户无法知道，这种不能再pycharm ide下代码补全的框架可以说是极端的操蛋，
 不能代码补全的框架，就算是功能强大也没用，不好使用。还有celery启动work 启动定时 启动flower都需要手敲 cmd 命令行，用户连入参能传哪些控制命令大全都不知道，
所以celery框架对不非常熟练python的人是极端的操蛋。

用户只需要使用简单的funboost语法就能操控celery框架了。funboost使用celery作为broker_kind,远远的暴击亲自使用无法ide下代码补全的celery框架的语法。
```

```
funboost通过支持celery作为broker_kind,使celer框架变成了funboost的一个子集
```

funboost使用broker_kind=BrokerEnum.CELERY作为中间件的代码。

```python
import time

from funboost import boost, BrokerEnum, BoosterParams
from funboost.consumers.celery_consumer import CeleryHelper


@boost(BoosterParams(queue_name='celery_q1', broker_kind=BrokerEnum.CELERY, qps=5))
def f1(x, y):
    time.sleep(3)
    print('哈哈哈', x, y)
    return x + y


@boost(BoosterParams(queue_name='celery_q2', broker_kind=BrokerEnum.CELERY, qps=1))
def f2(a, b):
    time.sleep(2)
    print('嘻嘻', a, b)
    return a - b


if __name__ == '__main__':
    for i in range(200):
        f1.push(i, i * 2)
        f2.push(a=i, b=i * 10)

    f1.consume()  # 登记celery worker命令需要启动的--queues
    f2.consume()  # 登记celery worker命令需要启动的--queues
    CeleryHelper.realy_start_celery_worker(worker_name='测试celery worker2') # 正正的启动celery worker


```

funboost 以celery中间件模式运行的github项目代码：

[https://github.com/ydf0509/funboost_run_celery_mode/tree/main](https://github.com/ydf0509/funboost_run_celery_mode/tree/main)

11.1章节有更多的funboost 操作celery代码说明，包括原生的celery定时和flower。

## 4.29 funboost支持任务优先级队列

目前只有 BrokerEnum.REDIS_PRIORITY 和 BrokerEnum.RABBITMQ_AMQPSTORM 两个broker支持队列优先级，选择其他的broker_kind不支持优先级队列。

### 4.29.1 队列支持优先级的说明：

```
 注意：        rabbitmq、celery队列优先级都指的是同一个队列中的每个消息具有不同的优先级，消息可以不遵守先进先出，而是优先级越高的消息越先取出来。
              队列优先级其实是某个队列中的消息的优先级，这是队列的 x-max-priority 的原生概念。

              队列优先级有的人错误的以为是 queuexx 和queueyy两个队列，以为是优先消费queuexx的消息，这是大错特错的想法。
              队列优先级是指某个队列中的每个消息可以具有不同的优先级，不是在不同队列名之间来比较哪个队列名具有更高的优先级。
```

### 4.29.2 优先级通俗理解，用食堂打饭比喻：

```
校食堂有两个打饭窗口a和b。a窗口的排队是声明了支持优先级队列，b窗口的排队是没有声明支持优先级的队列。

声明了支持优先级的打饭窗口a排队可以允许插队，例如校领导优先级是3，老师优先级是2，学生优先级是1。就算是学生先去排队，但校长优先级高，
就算排了100个学生排队长龙打饭，校长在这个a窗口来打饭时候可以插队，优先给校长打饭，只要校领导和老师的饭没打完，学生是不能打饭的。

b打饭窗口由于没有声明支持优先级，任何人来这个b窗口打饭必须老老实实排队，谁先来排队就先给谁打饭，天王老子来了都不可以插队优先打饭。


a窗口和b窗口排队的人是互不影响的，优先级是针对各自的队列。
并不是有的人以为的，a窗口优先级高，b窗口优先级低，只要a窗口有人排队，就不给b窗口的人打饭了，你这样那就是想错了。自己好好搜索rabbitmq的 x-max-priority 概念先。
```

### 4.29.3 队列支持任务优先级的代码主要有三点：

```
   第一，如果使用redis做支持优先级的消息队列， @boost中要选择 broker_kind = BrokerEnum.REDIS_PRIORITY，
       如果是使用rabbitmq写 BrokerEnum.RABBITMQ_AMQPSTORM。
    
   第二，broker_exclusive_config={'x-max-priority':5} 意思是声明这个队列中的任务消息支持多少种优先级，一般写5就完全够用了，不要写太大了，不需要那么多种级别。
   
   第三，发布消息时候要使用publish而非push,发布要加入参  priority_control_config=PriorityConsumingControlConfig(other_extra_params={'priroty': priority})，
        其中 priority 必须是整数，要大于等于0且小于队列声明的x-max-priority。x-max-priority这个概念是rabbitmq的原生概念，celery中也是这样的参数名字。

        发布的消息priroty 越大，那么该消息就越先被取出来，这样就达到了打破了先进先出的规律。比如优先级高的消息可以给vip用户来运行函数实时，优先级低的消息可以离线跑批。
```

### 4.29.4 队列支持任务优先级的代码如下：

```python
import random
import time

from funboost import boost, PriorityConsumingControlConfig, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_redis_priority_queue4', broker_kind=BrokerEnum.REDIS_PRIORITY, qps=100, concurrent_num=50, broker_exclusive_config={'x-max-priority':4}))
def f(x):
    time.sleep(60)
    print(x)


if __name__ == '__main__':
    f.clear()
    print(f.get_message_count())

    for i in range(1000):
        randx = random.randint(1, 4)
        f.publish({'x': randx}, priority_control_config=PriorityConsumingControlConfig(other_extra_params={'priroty': randx}))
    print(f.get_message_count())

    f.consume()
```

从控制台打印可以看到先print的都是4，最后print的是1，无视了消息的发布顺序，而是以消息的优先级来决定谁先被消费。

### 4.29.5 消息队列优先级是针对一个queue内消息的，那么怎样才能实现不同函数之间的按优先级运行？

很简单，既然优先级队列指的是一个队列中不同的消息可以具有不同的优先级。那么只要用一个队列就好了。一个总的函数消费消息队列，然后分发调用不同的函数,就可以实现优先运行哪个函数了。

下面例子就是，交替发布1000次 f1 f2 f3函数的消息到 test_priority_between_funs 队列中，但消费时候优先运行f3函数，最后才运行f1函数。通过控制台的打印可以看到。

```python
"""
演示不同的函数，怎么优先消费某个函数。
比如爬虫你想深度优先，那就优先运行爬详情页的函数，发布消息时候把爬详情页函数的优先级设置的priroty更大。
你想广度优先就优先运行爬列表页的函数，发布消息时候把爬列表页函数的优先级设置的priroty更大。

如下代码就是把f3函数的优先级设置成了3，f2的优先级设置成了2，f1的优先级设置成了1，所以先交替发布3000个消息到消息队列中，会优先运行f3函数，最后才运行f1函数。
虽然优先级是针对某一个队列而言，不是针对不同队列的优先级，但只要懂得变通，在下面代码的例子中的 dispatch_fun 函数这样分发调用不同的函数，就可以实现多个函数之间的优先级了。

运行可以发现控制台先打印的都是f3，最后还是f1.
"""
"""
演示不同的函数，怎么优先消费某个函数。
比如爬虫你想深度优先，那就优先运行爬详情页的函数，把爬详情页函数的优先级调大。
你想广度优先就优先运行爬列表页的函数，把爬列表页页函数的优先级调大。

如下代码就是把f3函数的优先级设置成了3，f2的优先级设置成了2，f1的优先级设置成了1，所以先发布3000个消息到消息队列中，会优先运行f3函数，最后才运行f1函数。
优先级是针对某一个队列而言，不是针对不同队列的优先级，但只要懂得变通，在下面代码的例子中的boost_fun函数这样分发调用不同的函数，就可以实现多个函数之间的优先级了。

运行可以发现控制台先打印的都是f3，最后还是f1.
"""
from funboost import boost, PriorityConsumingControlConfig, BrokerEnum, BoosterParams


def f1(x, y):
    print(f'f1  x:{x},y:{y}')


def f2(a):
    print(f'f2  a:{a}')


def f3(b):
    print(f'f3  b:{b}')


@boost(BoosterParams(queue_name='test_priority_between_funs', broker_kind=BrokerEnum.RABBITMQ_AMQPSTORM, qps=100, broker_exclusive_config={'x-max-priority': 5}))
def dispatch_fun(fun_name: str, fun_kwargs: dict, ):
    function = globals()[fun_name]
    return function(**fun_kwargs)


if __name__ == '__main__':
    dispatch_fun.clear()
    for i in range(1000):
        dispatch_fun.publish({'fun_name': 'f1', 'fun_kwargs': {'x': i, 'y': i}, },
                             priority_control_config=PriorityConsumingControlConfig(other_extra_params={'priroty': 1}))
        dispatch_fun.publish({'fun_name': 'f2', 'fun_kwargs': {'a': i, }, },
                             priority_control_config=PriorityConsumingControlConfig(other_extra_params={'priroty': 2}))
        dispatch_fun.publish({'fun_name': 'f3', 'fun_kwargs': {'b': i, }, },
                             priority_control_config=PriorityConsumingControlConfig(other_extra_params={'priroty': 3}))

    print(dispatch_fun.get_message_count())
    dispatch_fun.consume()


```

## 4.30 funboost 远程杀死(取消)任务

之前有的人想远程杀死一个正在运行的任务，或者刚发布消息后后悔了，不想运行那个消息了，现在支持这种功能。
用户无论选择哪种消息队列中间件，想使用远程杀死就必须在funboost_config.py配置好redis连接。

远程杀死任务分两种情况：

```
1）对于发布后，还没从消息队列中取出来运行的消息，funboost会放弃运行这个消息。
2）对于正在执行中的消息，funboost会杀死正在运行的这个函数消息。
```

```
celery如果选择threading并发模式，celery不支持terminate杀死，celery的消费端在收到terminate命令时候会报错，celery多线程并发池没有实现杀死功能。

funboost支持杀死正在运行中的函数消息。
```

### 4.30.1 funboost远程杀死函数的代码例子

注意要设置 is_support_remote_kill_task=True，如果不需要远程杀死函数消息的功能，就别设置为True，浪费性能；
因为函数要支持杀死，必须把函数单独运行在一个线程中，杀死这个线程来达到杀死函数的目的。所以非必要别设置 is_support_remote_kill_task=True。

开启 is_support_remote_kill_task=True  适合任务数量少，函数运行耗时非常大的情况；
因为如果函数只需要10秒能运行完，你还没来得及开始写发送远程杀死命令的代码，函数就已经执行完了，杀死了个寂寞。

下面代码是让funboost结束执行求和 3+4。

消费端代码求和：

```python
import time

from funboost import boost, BoosterParams


@boost(BoosterParams(queue_name='test_kill_fun_queue', is_support_remote_kill_task=True)) #  is_support_remote_kill_task=True 要设置为True
def test_kill_add(x, y):
    print(f'start {x} + {y} ....')
    time.sleep(120)
    print(f'over {x} + {y} = {x + y}')


if __name__ == '__main__':
    test_kill_add.consume()
```

发布端代码：

```python
import time
from test_funboost_kill_consume import test_kill_add
from funboost import RemoteTaskKiller

if __name__ == '__main__':
    async_result = test_kill_add.push(3,4)
    # time.sleep(10)
    RemoteTaskKiller(test_kill_add.queue_name,async_result.task_id).send_kill_remote_task_comd() #  RemoteTaskKiller 传入要杀死的队列名和消息的taskid
```

超时杀死控制台截图：
![img_42.png](img_42.png)

### 4.30.2 远程强制杀死函数、超时自动杀死(function_timeout设置不为0)， 这两个功能要注意死锁：

```
funboost的多线程并发模式的 function_timeout超时自动杀死 和远程命令来杀死函数都需要注意杀死函数后的锁不释放问题。

1）在消费函数中 with 推荐

with lock:
    长耗时代码
  
在执行长耗时代码块时候，这种函数被强制杀死，不会发生死锁。


2）在消费函数中，lock.acquire() 和 release() 不推荐，

lock.acquire():
长耗时代码
lock.release()

在执行长耗时代码块时候，这种函数被强制杀死，会发生死锁,杀死函数后，消费会一直卡住，所以消费会一直等待这个锁，导致消费无法继续运行。


对于使用锁的建议：
大家尽量使用with语法使用锁，或者锁别加在长耗时代码块上，减少死锁概率。
或使用可过期锁expire_lock。

```

### 4.30.2.b 如果想启用funboost函数超时自动杀死功能或者 远程杀死函数功能，推荐消费函数中使用可过期锁 expire_lock

pip install expire_lock

或者 from funboost.utils import expire_lock

expire_lock 使用文档：
[https://pypi.org/project/expire-lock/](https://pypi.org/project/expire-lock/)

expire_lock 规定了一个锁的最大占用时间，如果达到了最大的expire时间一直没有释放这个锁，会自动过期释放。

## 4.31 神级别 fct (funboost_current_task) 上下文获取当前消息和任务状态

fct 就是 funboost_current_task 简写，就是当前任务的意思。

通过fct这个线程/协程 精妙的上下文全局变量，可以获取消息的完全体。

可以去ai大模型提问flask视图函数中的 request 对象的设计！

funboost的fct 和 flask的request就是类似用途，不需要从函数入参显式传递，但在函数内部可以精准得到当前请求的入参。

这个线程/协程上下文 可以在多个函数中自动传递，而不需要手动把这个对象作为函数在一条链路上的多个函数中作为函数入参传来传去的。

例如django就没有flask这种神奇的request对象，django需要明显的把request定义为视图函数的入参。

没有fct时候，之前无法在用户的消费函数内部去获取消息的完全体,只能知道函数的入参,无法知道消息的发布时间 taskid等.

```
用户在任意消费函数中 
fct 就能获取当前的任务消息了。

这个功能使得用户在用户函数中就能知道消息的完全体、 当前是哪台机器 、哪个进程、 第几次重试运行函数
消息的发布时间  消息的task_id 等等。

原来用户在消费函数中是无法获取这些信息的。
```

```python

import random
import time

from funboost import boost, BoosterParams, fct


@boost(BoosterParams(queue_name='queue_test_fct', qps=2, concurrent_num=5, ))
def f(a, b):
    print(fct.task_id)  # 获取消息的任务id
    print(fct.function_result_status.run_times)  # 获取消息是第几次重试运行
    print(fct.full_msg)  # 获取消息的完全体。出了a和b的值意外，还有发布时间 task_id等。
    print(fct.function_result_status.publish_time)  # 获取消息的发布时间
    print(fct.function_result_status.get_status_dict())  # 获取任务的信息，可以转成字典看。

    time.sleep(20)
    if random.random() > 0.5:
        raise Exception(f'{a} {b} 模拟出错啦')
    print(a + b)
    common_fun() # 这里不要手动把消息taskid和消息内容告诉 common_fun ，common_fun 能自动通过fct上下文知道。
    return a + b


def common_fun():
    """ common_fun 函数中也能自动通过上下文知道当前是在消费什么消息内容，无需让f函数调用 common_fun 时候吧taskid full_msg作为入参传过来 """
    print(f'common_fun函数也能自动知道消息的taskid，无需在f消费函数中把taskid作为common_fun函数的入参传过来,taskid: {fct.task_id}, full_msg: {fct.full_msg}')


if __name__ == '__main__':
    # f(5, 6)  # 可以直接调用

    for i in range(0, 200):
        f.push(i, b=i * 2)

    f.consume()

```

```
代码中无论是 f 消费函数，还是 common_fun 普通函数， 都能通过fct获取当前任务
```

![img_61.png](img_61.png)

## 4.32 重磅更新！！！ funboost 独家新增支持实例方法和类方法作为消费函数

funboost 之前一直是只支持 普通函数或者静态方法作为消费函数，celery也是不能支持实例方法和类方法作为消费函数。

这个问题之前还专门写个常见问题答疑里面，见第 6.5 章节 ,为什么强调是函数调度框架不是类调度框架，不是方法调度框架？ [https://funboost.readthedocs.io/zh-cn/latest/articles/c6.html#id5](https://funboost.readthedocs.io/zh-cn/latest/articles/c6.html#id5)
,通过里面的介绍就知道，如果支持要实例方法和类方法作为消费函数有多么困难。
对于 实例方法和类方法作为消费函数，funboost 是做了判断和专门适配的。

### 4.32.1 funboost 支持实例方法和类方法作为消费函数的原理

funboost 适配 实例方法和类方法的实现原理讲一下：

假设类如下：

```python
class Myclass:
    m = 1

    def __init__(self, x):
        self.obj_init_params: dict = ClsHelper.get_obj_init_params_for_funboost(copy.copy(locals())) # 这行重要，如果实例方法作为消费函数，那么必须定义obj_init_params_for_funboost保存对象的 __init__ 入参，用于还原生成对象。
        # self.obj_init_params_for_funboost= {'x':x}  # 上面这行相当于这行，如果__init__入参太多，一个个的写到字典麻烦，可以使用上面的方式获取__init__入参字典。
        self.x = x

    @boost(BoosterParams(queue_name='instance_method_queue', is_show_message_get_from_broker=True, ))
    def instance_method(self, y):
        print(self.x + y) # 这个求和用到了实例属性和方法入参求和，证明为什么发布消息时候要传递self。

    #
    @classmethod
    @BoosterParams(queue_name='class_method_queue', is_show_message_get_from_broker=True, )
    def class_method(cls, y):
        print(cls.m + y)
```

```
对于类方法：
通过方法所属的类名和模块名，反射得到类，但不能直接把类本身作为消息的函数入参，发布到消息队列，
因为采用的是json序列化消息，所以入参不能包括在定义类型和在定义类型的对象， funboost发布消息时候使用字典代替了类方法的第一个入参 cls，
funboost在消费消息时候，把消息的第一个入参cls，替换成类本身，这样就是生成真正的函数入参，然后再去调用类方法。
发布消息： Myclass.class_method.push(Myclass,2)



对于实例方法：
funboost发布消息时候使用字典代替了实例方法的第一个入参 self，把 对象的实例化时候的入参字典就是对象的 obj_init_params 属性，放到这个字典里面去了。
消费时候，从消息队列获取入参后，使用 obj_init_params 这个字典作为对象实例化的入参，重新生成一个对象，然后把这个对象替换实例方法的第一个入参self，再去调用实例方法。
对象必须定义 obj_init_params 属性，保存对象 __init__ 时候的入参字典，供消费时候重新生成对象。
因为 1+2=3,是不仅和instance_method的入参y有关系，还和对象本身的x属性也有关系。
发布消息： Myclass.instance_method(Myclass(1),2) 


！！！特别需要注意的是实例方法作为消费函数的时候，对象必须定义 obj_init_params 属性保存初始化入参，并且 __init__ 的入参同样必须是基础类型，能被json序列化的，
不能是自定义类型和对象。

```

### 4.32.2 funboost 支持实例方法、类方法、静态方法、普通函数 4种类型，作为消费函数的例子

下面代码完整的演示了 实例方法、类方法、静态方法、普通函数 4种类型，作为消费函数的例子，请务必注意看代码和注释说明。

```python3
import copy
from funboost import BoosterParams, boost
from funboost.constant import FunctionKind
from funboost.utils.class_utils import ClsHelper


class Myclass:
    m = 1

    def __init__(self, x):
        # 这行重要，如果实例方法作为消费函数，那么必须定义obj_init_params_for_funboost保存对象的 __init__ 入参，用于还原生成对象。
        self.obj_init_params: dict = ClsHelper.get_obj_init_params_for_funboost(copy.copy(locals()))
        # self.obj_init_params = {'x':x}  # 上面这行相当于这行，如果__init__入参太多，一个个的写到字典麻烦，可以使用上面的方式获取__init__入参字典。
        self.x = x

    @boost(BoosterParams(queue_name='instance_method_queue', is_show_message_get_from_broker=True, ))
    def instance_method(self, y):
        print(self.x + y)  # 这个求和用到了实例属性和方法入参求和，证明为什么发布消息时候要传递self。

    #
    @classmethod
    @BoosterParams(queue_name='class_method_queue', is_show_message_get_from_broker=True, )
    def class_method(cls, y):
        print(cls.m + y)

    @staticmethod
    @BoosterParams(queue_name='static_method_queue', is_show_message_get_from_broker=True)
    def static_method(y):
        print(y)


@BoosterParams(queue_name='common_fun_queue', is_show_message_get_from_broker=True)
def common_f(y):
    print(y)


if __name__ == '__main__':

    for i in range(6, 10):
        Myclass.instance_method.push(Myclass(i), i * 2)  # 注意发布形式，实例方法发布消息不能写成 Myclass(i).push(i * 2) 只发布self之后的入参, self也必须传递。
    Myclass.instance_method.consume()

    for i in range(6, 10):
        Myclass.class_method.push(Myclass,i * 2)  # 注意发布形式，不是 Myclass.class_method.push(i * 2) ， 而是应该写 Myclass.class_method.push(Myclass,i * 2)，cls也要传
    Myclass.class_method.consume()

    for i in range(10):
        Myclass.static_method.push(i * 2)  # 不需要注意发布形式，和 普通函数的发布一样
    Myclass.static_method.consume()

    for i in range(10):
        common_f.push(i * 2)
    common_f.consume()



```

请注意看下面运行截图中的消息，self 在消息队列中间件中使用 json来表达了。消费运行时候重新根据obj_init_params和类名、文件名，生成Myclass类型的对象。

```
 向instance_method_queue 队列，推送消息 耗时0.001秒  {'self': {'first_param_name': 'self', 'obj_init_params': {'x': 6}, 'cls_name': 'Myclass', 'cls_file': 'D:/codes/funboost/test_frame/test_instancemothed_funboost/test_method_consume.py'}, 'y': 12}
```

![img_80.png](img_80.png)

## 4.33  @boost设置is_auto_start_consuming_message，自动启动消费。

```
@BoosterParams(queue_name="q1",  is_auto_start_consuming_message=True)
def f(x):
这样写后，自动启动消费，不需要 用户手动的写  f.consume() 来启动消费。
```

```python
import time
from funboost import BoosterParams, BrokerEnum


@BoosterParams(queue_name="test_instead_thread_queue", broker_kind=BrokerEnum.MEMORY_QUEUE, concurrent_num=10,
               is_auto_start_consuming_message=True)  # is_auto_start_consuming_message 这里设置为了True
def f(x):
    time.sleep(3)
    print(x)


if __name__ == '__main__':
    for i in range(100):
        f.push(i)
    #### f.conusme() #is_auto_start_consuming_message=True后， 这一行代码不需要，不需要手动 f.consume() 来启动消费。

```

## 4.34 pyinstaller 打包 funboost项目为exe 的说明

见独立demo项目 https://github.com/ydf0509/funboost_pyinstaller

里面有报错解决说明，funboost打包很容易。

## 4.35 演示 funboost 的函数入参过滤功能

```python
@BoosterParams(queue_name='queue_test2', qps=6, broker_kind=BrokerEnum.REDIS,
               do_task_filtering=True, # 这个是设置是否开启任务入参过滤
               task_filtering_expire_seconds=3600, # 这个是可以设置任务入参过滤过期时间，例如1小时内查询了深圳天气，在1小时内再查会被过滤，因为1小时内已经查询过了，而1小时后查询的深圳天气，则不会被过滤。
               concurrent_num=1)
def f2(a, b):
    sleep_time = 1
    result = a + b
    print(f'消费此消息 {a} + {b} 中。。。。。,此次需要消耗 {sleep_time} 秒')
    time.sleep(sleep_time)  # 模拟做某事需要阻塞n秒种，必须用并发绕过此阻塞。
    print(f'{a} + {b} 的结果是 {result}')
    return result


@BoosterParams(queue_name='queue_test3', qps=6, broker_kind=BrokerEnum.REDIS,
                do_task_filtering=True, # 设置开启消息过滤
               concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD)
def f3(a, b):
    sleep_time = 1
    result = a + b
    print(f'消费此消息 {a} + {b} 中。。。。。,此次需要消耗 {sleep_time} 秒')
    time.sleep(sleep_time)  # 模拟做某事需要阻塞n秒种，必须用并发绕过此阻塞。
    print(f'{a} + {b} 的结果是 {result}')
    return result

if __name__ == '__main__':
    pass
    # print(f2.__name__)
    # f2.clear()
    f2.consume()
    f3.consume()
    for i in range(200):
        f2.push(i, i * 2) # 如果不传递filter_str， 默认是 把 所有入参 a和b，排序后作为json都加入到过滤中
        f3.publish(msg={'a':i,'b':i*2},priority_control_config=PriorityConsumingControlConfig(filter_str=str(i))) # 这个是仅仅把 a 作为过滤条件，例如函数入参 userid username sex ，通常按照userid 过滤足以， 不需要username sex也一起过滤，可以节约redis内存。
    time.sleep(5)  # 因为 funboost 是确认消费完成后才加入过滤。如果消息耗时很长，且并发很大，且两个相同入参的消息连续挨着，第二个还会执行，所以这里演示sleep一下。
    for i in range(200):
        f2.push(i, i * 2)
        f3.publish(msg={'a':i,'b':i*2},priority_control_config=PriorityConsumingControlConfig(filter_str=str(i)))
    ctrl_c_recv()
```

## 4.35 演示 funboost 使用 tcp/udp/http 作为broker

**这再次印证了在funboost中万物皆可为broker**

```
funboost 使用 tcp/udp/http 作为broker 的好处是不需要安装任何消息队列服务,
使用操作系统自带的 socket 实现跨机器消息通信, 用于不需要高可靠但需要跨机器通信的场景.
```

```python
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(
    queue_name='test_socket_queue', broker_kind=BrokerEnum.UDP, # BrokerEnum.UDP就是设置udp socket作为broker
    broker_exclusive_config={'host': '127.0.0.1', 'port': 7102}, # 需要在broker_exclusive_config中设置socket的 ip和端口
))
def f(x):
    print(x)


if __name__ == '__main__':
    f.consume() # 启动消费.从socket 获取消息消费
    for i in range(2000):
        f.push(i) # 给ip 端口发消息
```

## 4.36 演示`funboost`入参可以是自定义类型(不可json序列化的类型)(2025-07新增支持)

以前作者不愿意支持消费函数入参是自定义类型,2025-07 之后支持了.

就是现在消费函数的入参可以是 字符串 数字 列表 字典 以外的自定义类型,    
def func1(a:MyClass,b:str,c:MyPydanticModel)  现在可以.

原理:
```
消息整体还是一个json,但是对于不可序列化的那些入参字段key对应的value,
会用pickle序列化成字符串(非bytes)替代.
str(pickle.dumps(obj_x))


当运行函数之前,会对不可json序列化的那些入参的value,使用
pickle.loads(ast.literal_eval(para_pickle_str)) 转成对象
```


```python
"""
此demo演示funboost新增支持了pickle序列化,
当用户的消费函数入参不是基本类型,而是自定义类型时候,funboost能自动识别,并将相关字段使用pickle序列化成字符串.
当消费函数运行时,funboost能自动将 不可json序列化的那些字段的pickle字符串反序列化成对象,并赋值给消费函数入参.
"""

from pydantic import BaseModel
from funboost import (boost, BoosterParams, BrokerEnum, ctrl_c_recv, fct)


class MyClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def change(self,n):
        self.x +=n
        self.y +=n
    def __str__(self):
        return f'<MyClass(x={self.x},y={self.y})>'

class MyPydanticModel(BaseModel):
    str1:str
    num1:int

@boost(BoosterParams(queue_name='queue_pickle',concurrent_num=10,is_using_rpc_mode=True,
                     broker_kind=BrokerEnum.REDIS_ACK_ABLE))
def func1(a:MyClass,b:str,c:MyPydanticModel):
    # print(fct.full_msg) # 可以查看原始消息
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
    print(f'a.x:{a.x},a.y:{a.y}')


if __name__ == '__main__':

    obj1 = MyClass(1,2)
    func1.push(obj1,'hello',MyPydanticModel(str1='hello',num1=1)) # 入参包括自定义类型和pydantic模型

    obj1.change(10)
    func1.push(obj1,'hello',MyPydanticModel(str1='world',num1=100)) # 入参包括自定义类型和pydantic模型

    func1.consume()
    ctrl_c_recv()
```

## 4.100 使用funboost时候对框架的疑问和猜测，使用控制变量法

就是要把自己的疑问和猜测，使用控制变量法精简成一个 time.sleep() print('hello')的demo。
只有这样你才好验证你的想法，不然放在业务代码中去验证，你又难以模拟控制业务函数期望发生的情况。

```
比如你怀疑funboost重试次数不生效，你说你的mysql插入数据时候网络连接报错了但是funboost没给你重试，你现在又不方便模拟mysql网络断开极小概率事件，
那你就写个 raise Exception('模拟出错') 的函数，看funboost会不会重试运行就好了。
因为funboost是执行函数，不会改变用户函数内部的代码逻辑。

有的人极端笨脑筋，不知道使用控制变量法写个精简demo验证，仅需不到10行代码而已。连初中生都知道的控制变量法做实验猜测，缺到现在这样思维都忘了。
```

```
有的人老是一开始学习funboost就用复杂业务函数逻辑来运行，不好调试,不方便表示自己的用法。
应该把自己的想法抽象成 1个简单的 包含 time.sleep 的函数，用简单demo才比较方便表示自己的疑惑和验证自己的猜测。

用户修改boost装饰器的参数 和 函数的sleep 大小 来 测试你想要验证你对框架功能的猜测。

例如你要测试确认消费，框架的broker_kind 为 redis_ack_able是否能做到消息确认消费不丢失消息，那你就可以发布20个任务，并启动消费，
消费函数里面time.sleep(200)，然后你在第100秒时候突然把正在运行的消费脚本强行关闭，你就能看到消息被其他消费进程或机器拿运行了。
或者你只有一个脚本在运行，当你下次重新启动脚本时候这些消息也会被消费。

例如你要测试框架是不是能并发运行，那么运行下面的f函数，你设置10线程，那应该每50秒能打印求和10次，设置并发模式为single_thread那么每50秒能打印求和1次。
```

```python
from funboost import boost, BoosterParams

@boost(BoosterParams(queue_name='test_queue'))  # 用户修改boost的参数测试你想要的破欸子效果
def f(x,y):
    time.sleep(50)     # 用户修改sleep大小测试因函数耗时造成的猜测
    print(f'{x} + {y} = {x + y}')
    return x +y

if __name__ == '__main__':
    for i in range(1000):
        time.sleep(0.2)
        f.push(i,i*2)
    f.consume()
```

### 4.100.b 举个例子，验证测试框架的超时杀死 function_timeout参数的作用

```textmate
有的人老是问超时杀死是不是杀死进程，杀死python脚本。

问的太不用大脑了，默认的 task_fun.consume() 是单进程多线程启动的，如果是杀进程和脚本，那部署脚本相当于自杀结束了，这可能吗？
把脚本杀死了，那就永远无法再消费了，框架怎么可能这么设计为，因为一个函数入参超时而退出程序。
做出这种猜测就不应该了，而且用户自己测试验证这个想法很难吗。

例如下面的求和函数，里面写个sleep,然后设置 function_timeout=20，
框架的各个控制功能都太容易通过写一个简单的sleep 求和函数demo来测试了。
```

测试脚本：

```python
import random
import time

from funboost import boost, BoosterParams

@boost(BoosterParams(queue_name='test_timeout', concurrent_num=5, function_timeout=20, max_retry_times=4))
def add(x,y):
    t_sleep = random.randint(10, 30)
    print(f'计算 {x} + {y} 中。。。。,需要耗费 {t_sleep} 秒时间')
    time.sleep(t_sleep)
    print(f'执行 {x} + {y} 的结果是 {x+y}  ')
    return x+y


if __name__ == '__main__':
    for i in range(100):
        add.push(i,i*2)
    add.consume()

```

超时运行的截图

![img_30.png](img_30.png)

从运行来看就知道了，funboost的function_timeout超时杀死功能，是针对一个正在运行的函数执行参数，是杀死运行中的函数，使函数运行中断结束，
不继续往下运行函数了，不会把自身脚本整个杀死。所以对funboost提供的功能不用猜测，只需要写demo测试就可以了。

### 4.100.c

## 4.200 [分布式函数调度框架qq群]

现在新建一个qq群 189603256

<div> </div>

[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
[//]: #
# 4b.使用框架的各种代码示例(高级进阶)

## 4b.1 日志模板中自动显示task_id

### 4b.1.1 日志模板中显示task_id

在 funboost_config.py 中设置如下 (43.0版本以后的配置默认就是待task_id的模板了)

如果用户的 funboost_config.py 是旧的日志模板,升级到43.0以后版本,需要修改 NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER 为新的带task_id的日志模板,日志中才能自动显示task_id

```python
import logging
from nb_log import nb_log_config_default
class FunboostCommonConfig(DataClassBase):
    # nb_log包的第几个日志模板，内置了7个模板，可以在你当前项目根目录下的nb_log_config.py文件扩展模板。
    # NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER = 11  # 7是简短的不可跳转，5是可点击跳转的，11是可显示ip 进程 线程的模板,也可以亲自设置日志模板不传递数字。
    NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER = logging.Formatter(
        f'%(asctime)s-({nb_log_config_default.computer_ip},{nb_log_config_default.computer_name})-[p%(process)d_t%(thread)d] - %(name)s - "%(filename)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(task_id)s - %(message)s',
        "%Y-%m-%d %H:%M:%S",)   # 这个是带task_id的日志模板,日志可以显示task_id,方便用户串联起来排查某一个人物消息的所有日志.
```

待task_id的日志模板如下图

![img_62.png](img_62.png)

### 4b.1.2 用户在消费函数中想自动显示task_id,方便搜索task_id的关键字来排查某条消息的所有日志.

用户使用 logger = LogManager('namexx',logger_cls=TaskIdLogger).get_logger_and_add_handlers(......) 的方式来创建logger,

关键是用户需要设置 logger_cls=TaskIdLogger

代码连接:
[https://github.com/ydf0509/funboost/blob/master/test_frame/test_funboost_current_task/test_current_task.py](https://github.com/ydf0509/funboost/blob/master/test_frame/test_funboost_current_task/test_current_task.py)

代码如下:

```python

import random
import time

from funboost import boost, FunctionResultStatusPersistanceConfig, BoosterParams,fct

from funboost.core.task_id_logger import TaskIdLogger
import nb_log
from funboost.funboost_config_deafult import FunboostCommonConfig
from nb_log import LogManager

LOG_FILENAME_QUEUE_FCT = 'queue_fct.log'
# 使用TaskIdLogger创建的日志配合带task_id的日志模板，每条日志会自动带上task_id，方便用户搜索日志，定位某一个任务id的所有日志。
task_id_logger = LogManager('namexx', logger_cls=TaskIdLogger).get_logger_and_add_handlers(
    log_filename='queue_fct.log',
    error_log_filename=nb_log.generate_error_file_name(LOG_FILENAME_QUEUE_FCT),
    formatter_template=FunboostCommonConfig.NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER, )

# 如果不使用TaskIdLogger来创建logger还想使用task_id的日志模板,需要用户在打印日志时候手动传 extra={'task_id': fct.task_id}
common_logger = nb_log.get_logger('namexx2',formatter_template=FunboostCommonConfig.NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER)



@boost(BoosterParams(queue_name='queue_test_fct', qps=2, concurrent_num=5, log_filename=LOG_FILENAME_QUEUE_FCT))
def f(a, b):


    # 以下的每一条日志都会自带task_id显示，方便用户串联起来排查问题。
    fct.logger.warning('如果不想亲自创建logger对象，可以使用fct.logger来记录日志，fct.logger是当前队列的消费者logger对象')
    task_id_logger.info(fct.function_result_status.task_id)  # 获取消息的任务id
    task_id_logger.debug(fct.function_result_status.run_times)  # 获取消息是第几次重试运行
    task_id_logger.info(fct.full_msg)  # 获取消息的完全体。出了a和b的值意外，还有发布时间 task_id等。
    task_id_logger.debug(fct.function_result_status.publish_time_str)  # 获取消息的发布时间
    task_id_logger.debug(fct.function_result_status.get_status_dict())  # 获取任务的信息，可以转成字典看。

    # 如果 用户不是使用TaskIdLogger插件的logger对象,那么要在模板中显示task_id,
    common_logger.debug('假设logger不是TaskIdLogger类型的,想使用带task_id的日志模板,那么需要使用extra={"task_id":fct.task_id}', extra={'task_id': fct.task_id})

    time.sleep(2)
    task_id_logger.debug(f'哈哈 a: {a}')
    task_id_logger.debug(f'哈哈 b: {b}')
    task_id_logger.info(a + b)
    if random.random() > 0.99:
        raise Exception(f'{a} {b} 模拟出错啦')

    return a + b


if __name__ == '__main__':
    # f(5, 6)  # 可以直接调用

    for i in range(0, 200):
        f.push(i, b=i * 2)

    f.consume()
```

运行如图:

![img_63.png](img_63.png)

可以看到每条日志自动就显示了task_id, 这样的好处是可以通过搜索 task_id,来排查用户的某条消息的整条链路情况.

### 4b.1.3 一键全局使用 TaskIdLogger 代替 logging.Logger 的方式

```python
import logging
logging.setLoggerClass(TaskIdLogger)  # 越早运行越好，这样就不需要每次都设置TaskIdLogger来实例化logger了。

```

### 4b.1.4 能在消费函数的整个链路里面的调用的任意函数获取task_id的原理

fct 因为是线程 /协程 级别隔离的,就是线程/协程上下文.


## 4b.2  支持消费函数定义入参 **kwargs ,用于消费包含随机不确定keys(或者keys太多了)的json消息

相比Celery等工具，在4b.2和4b.2c 章节 ,funboost展现出极强的异构兼容性.

###  4b.2.0 funboost函数执行一条消息的最根本原理是 fun(**消息字典)

**funboost push的背后**
```
假设消费函数签名是 def task_fun(a,b,c,d,e):pass ,
那么funboost框架的 task_fun.push(1,2,3,4,5) ,会把 {"a":1,"b":2,"c":3,"d":4,"e":5} 这个字典转成json
发到消息队列. (当然funboost框架也会生成包含其他辅助字段,放到extra字段中,例如task_id,发布时间等等)
```

**掌握funboost push背后原理,就可以知道怎么消费任意非funboost发布的已存在的json消息了**

```
例如别的部门手动发布了 {"a":1,"b":2,"c":3,"d":4,"e":5} 这个json到消息队列,
那么用户消费函数定义成 def task_fun(a,b,c,d,e):pass ,  
那么就可以消费到这个消息.  

如果字段太多了或者或json的keys会发生变化,
那么可以按照两种方式:
4b.2.3 方式一 :消费函数定义成 def task_fun(**kwargs):pass ,来接受不定项的json keys
               或者 def task_fun(**message) 也可以,此时 kwargs/message 就是这个json字典.
               这是基本通用的python语法问题,用户可以问ai, fun(**字典) 是什么意思

4b.2.4 方式二 :消费函数定义成 def task_fun(my_msg):pass ,但 使用 _user_convert_msg_before_run,
              生成一个新的字典/json, 把原始消息作为 my_msg 这个key的value 
              相当于是funboost识别到的消息是 {"my_msg":{"a":1,"b":2,"c":3,"d":4,"e":5}}
              你用 task_fun(my_msg={"a":1,"b":2,"c":3,"d":4,"e":5}) 来调用 task_fun(my_msg) 签名的函数肯定合法
             
              
```


### 4b.2.1 演示错误的消费已存在json消息的例子,企图使用 def task_fun(message) 的函数签名来消费

```
例如别的部门手动发布了 {"a":1,"b":2,"c":3,"d":4,"e":5} 这个json到消息队列,
用户不是正确的定义一个 def task_fun(a,b,c,d,e):pass 的函数来消费,
而是错误的定义成了一个  def task_fun(message):pass 的函数,
用户错误的以为 message 会代表 {"a":1,"b":2,"c":3,"d":4,"e":5}
def task_fun(message) 这样肯定会报错啊 , 
框架相当于是使用 task_fun(a=1,b=2,c=3,d=4,e=5) 来调用 task_fun(message) 签名的函数,
肯定不行.函数入参个数和名字都不一样,咋能不报错.
```

**小结:**    

面对已存在的 json消息 {"a":1,"b":2,"c":3,"d":4,"e":5}

<pre class="warn">
1)这样写消费函数正确 def task_fun(a,b,c,d,e):pass  ,json的一级keys和消费函数入参名字一一对应可以.

2)这样写消费函数正确 def task_fun(**message):pass ,  **message 可以接受不定项的函数入参,
   此时message就是消息字典,可以用 message["a"] 来获取a的值.

3)这样写消费函数不正确  def task_fun(message):pass ,json的一级keys和消费函数入参个数和名字压根不同,
肯定报错, 除非使用 _user_convert_msg_before_run 转化,把原始消息移到 message 这个一级key中.
</pre>




### 4b.2.3 方式一: 使用 **kwargs 方式 消费随机keys (或者json的一级keys太多不想逐个定义消费函数入参的情况)

```
例如消息是json格式,但是消息一会儿是 {"a":1,"b":2},一会是 {"c":3,"d":4,"e":5}, 如果要消费这个消息,消费函数不能固定写死成 def task_fun(a,b):
那么可以定义成 def task_fun(**kwargs):
```

有时候,消息是已存在的,而且别的部门没有使用funboost,且消息中字段达到几十上百个,用户不希望一个个字段的来定义消费函数入参.


如果是funboost来发布不定项的入参（json键名字随机不确定）,通过设置 should_check_publish_func_params=False,让 publisher 不再校验发布入参


代码如下:

```python

"""
Funboost 消费任意 JSON 消息格式完整示例（兼容非 Funboost 发布）

Funboost 天然支持消费任意 JSON 消息，且不要求任务必须通过 Funboost 发布，具备极强的异构兼容性与消息格式容忍度，
这在实际系统中大大降低了对接成本与协作门槛。
相比之下，Celery 的格式封闭、消息结构复杂，使得跨语言对接几乎不可能，这一点 Funboost 完胜。
"""

import time
import redis
import json
from funboost import boost, BrokerEnum, BoosterParams, fct,ctrl_c_recv

@boost(boost_params=BoosterParams(queue_name="task_queue_name2c", qps=5,
                                   broker_kind=BrokerEnum.REDIS, 
                                  log_level=10, should_check_publish_func_params=False
                                  ))  # 入参包括20种，运行控制方式非常多，想得到的控制都会有。
def task_fun(**kwargs):
    print(kwargs)
    print(fct.full_msg)
    time.sleep(3)  # 框架会自动并发绕开这个阻塞，无论函数内部随机耗时多久都能自动调节并发达到每秒运行 5 次 这个 task_fun 函数的目的。


if __name__ == "__main__":
    redis_conn = redis.Redis(db=7) # 使用原生redis来发布消息，funboost照样能消费。
    for i in range(10):
        task_fun.publish(dict(x=i, y=i * 2, x3=6, x4=8, x5={'k1': i, 'k2': i * 2, 'k3': i * 3}))  # 发布者发布任务
        task_fun.publisher.send_msg(dict(y1=i, y2=i * 2, y3=6, y4=8, y5={'k1': i, 'k2': i * 2, 'k3': i * 3})) # send_msg是发送原始消息

        # 用户和其他部门的java golang员工发送的自由格式任意消息，也能被funboost消费，也即是说无视是否使用funboost来发消息，funboost都能消费。
        # funboost消费兼容性太强了，这一点完爆celery。
        redis_conn.lpush('task_queue_name2c',json.dumps({"m":666,"n":777})) 

    task_fun.consume()
   
    ctrl_c_recv()


```

运行如图:
![img_66.png](img_66.png)

假设 task_queue_name2c 队列是别的部门发布的,或者你希望向 task_queue_name2c 队列中发布任意消息,那么可以使用send_msg

或者通过设置 should_check_publish_func_params=False 后使用 push或者publish来发布消息.

这样task_fun 支持消息任意消息,只要消息是json就行了.



### 4b.2.4 方式二: 使用 下面的 4b.2c 中章节的 强力灵活的 _user_convert_msg_before_run 方式,来消费随机keys或者keys太多的json

```
假如已存在的消息json是 {"a":1,"b":2,"c":3,""d":4,"e":5  ..........} ,有100多个keys.

如果funboost正常能消费情况下,需要
@boost(BoosterParams(....))
def task_fun(a,b,c,d,e .......): # 消费函数入参需要定义100多个,这太恐怖了.
```

方式一: 上面的消费函数入参定义成 `**kwargs` 来解决问题   
方式二: 可以使用下面代码方式,将json重新放到一个函数入参中,函数只需要定义一个入参:  
```python
class MyTooManyKeysJsonConvetConsumer(AbstractConsumer):
    def _user_convert_msg_before_run(self, msg)
        # 这是核心关键,把整个很长的json放到一个my_msg字段中,因为消费函数签名是 task_fun(my_msg)
        return {"my_msg":json.loads(msg)} 

@BoosterParams(...,consumer_override_cls=MyTooManyKeysJsonConvetConsumer) # 指定你的自定义类
def task_fun(my_msg):  # 函数只定义一个入参,例如 my_msg
    print(my_msg) # 会打印出   {"a":1,"b":2,"c":3,""d":4,"e":5  ..........}
```

**核心说明:**
```
如果 task_fun(**{"a":1,"b":2,"c":3,""d":4,"e":5  ..........}) 来调用 task_fun(my_msg)的函数,
肯定会报错,函数名和个数都不正确,肯定报错,

所以使用 _user_convert_msg_before_run 把 这个超长的json放到 my_msg中,相当于是把消息清洗转化成了
{"my_msg":{"a":1,"b":2,"c":3,""d":4,"e":5  ..........}}

此时使用 task_fun(**{"my_msg":{"a":1,"b":2,"c":3,""d":4,"e":5  ..........}}) , 那就完全ok,
因为转化后的json消息一级keys只有一个 my_msg字段,task_fun(**{"my_msg":$任意东西}) 完全符合python语法.
```


## 4b.2c 更强力灵活的,funboost支持消费地球上一切任意格式的不规范消息(非json格式也能消费)

`funboost` 默认要求消息是JSON格式，因为内部需要通过 `task_fun(**json.loads(json_str))` 的方式来调用消费函数。

```
即使消息队列中的消息不是从funboost发布的,也不是json,而是一个任意不规范内容的字符串,funboost也能消费.

celery 无法消费任意格式消息,funboost 能轻松做得到.
```

**实现方式是:**

- 继承并自定义 Consumer 类 (实际上也可以不继承,因为是mixin混入生成新类,继承是为了更好的ide中代码补全基类方法和属性)
- **重写 `_user_convert_msg_before_run` 方法**
- **使用 `consumer_override_cls` 参数**

关于 `consumer_override_cls` 参数,用户可以看文档4.21章节详细介绍


### 4b.2c.1 例如funboost消费消息队列中已存在的消息 'a=1,b=2' 这种.


例如需求如下:
```
消费函数是  def task_fun(a: int, b: int)      
但消息队列中消息是 'a=1,b=2' , 用户在函数运行前自定义转化消息格式,转换成字典或者json字符串.    
因为funboost中实际需要使用 task_fun(**{"a":1,"b":2}) 来调用消费函数.
```


demo代码例子如下:
```python

"""
此代码演示 funboost 强大的 消息格式兼容能力, 能消费一切任意队列中已存在的不规范格式的消息(消息格式不是json也能消费),
无论你是否使用funboost来发布消息,无视你的消息是不是json格式,funboost一样能消费.
通过用户自定义 _user_convert_msg_before_run 清洗转化消息成字典或者json字符串,funboost就能消费任意消息.
这是个小奇葩需求,但是funboost在消费任意消息的简单程度这方面能吊打celery
"""

import typing
import redis
from funboost import BrokerEnum, BoosterParams, AbstractConsumer


class MyAnyMsgConvetConsumer(AbstractConsumer):
    def _user_convert_msg_before_run(self, msg) -> typing.Union[dict,str]:
        # 'a=1,b=2' 例如从这个字符串,提取出键值对,返回新字典或者json字符串,以适配funboost消费函数的入参签名
        new_msg = {}
        msg_split_list = msg.split(',')
        for item in msg_split_list:
            key, value = item.split('=')
            new_msg[key] = int(value)
        self.logger.debug(f'原来消息是:{msg},转换成的新消息是:{new_msg}')  # 例如 实际会打印 原来消息是:a=3,b=4,转换成的新消息是:{'a': 3, 'b': 4}
        return new_msg


@BoosterParams(queue_name="task_queue_consume_any_msg", broker_kind=BrokerEnum.REDIS,
               consumer_override_cls=MyAnyMsgConvetConsumer  # 这行是关键,MyAnyMsgConvetConsumer类自定义了_user_convert_msg_before_run,这个方法里面,用户可以自由发挥清洗转化消息
               )
def task_fun(a: int, b: int):
    print(f'a:{a},b:{b}')
    return a + b


if __name__ == "__main__":
    redis_conn = redis.Redis(db=7)  # 使用原生redis来发布消息，funboost照样能消费。

    redis_conn.lpush('task_queue_consume_any_msg', 'a=1,b=2')  # 模拟别的部门员工,手动发送了funboost框架无法识别的消息格式,原本funboost需要消息是json,但别的部门直接发字符串到消息队列中了.,
    task_fun.publisher.send_msg('a=3,b=4')  # 使用send_msg 而非push和publish方法,是故意发送不规范消息, 就是发送原始消息到消息队列里面,funboost不会去处理添加任何辅助字段发到消息队列里面,例如task_id 发布时间这些东西.

    task_fun.consume()  # funboost 现在可以消费消息队列里面的不规范消息了,因为用户在_user_convert_msg_before_run清洗了消息

```


### 4b.2c.2 例如,funboost消费队列中已存在的 "1000123"(假设是纯粹的用户id) 这种非json消息

`funboost` 默认要求消息是JSON格式，因为内部需要通过 `task_fun(**json.loads(json_str))` 的方式来调用消费函数。但如果消息队列中已存在大量非JSON的简单字符串消息（例如，仅包含一个用户ID），`funboost` 同样可以轻松消费。

**场景**：


处理方式和 4b.2c.1 章节一样,用户可以自定义 _user_convert_msg_before_run 来清洗转化消息成字典或者json字符串,funboost就能消费这些消息.
```python


class MyUserIDMsgConvetConsumer(AbstractConsumer):
    def _user_convert_msg_before_run(self, msg)
        """返回新字典或者json字符串,以适配funboost消费函数的入参签名"""
        # 这是关键核心,因为消费函数签名是 task_fun(user_id)  
        return {"user_id":int(msg)}

@BoosterParams(...,consumer_override_cls=MyUserIDMsgConvetConsumer) # 指定你的自定义类
def task_fun(user_id:int):
    pass
```

这个例子清晰地展示了如何通过一小段定制代码，让 `funboost` 具备消费任意格式消息的能力，这在集成遗留系统或与第三方跨部门系统对接时尤其有用。



## 4b.3 funboost + 全asyncio 编程生态演示

funboost 对 asyncio 编程生态的直接性支持远超 celery.

全套的asyncio生态，不仅包括了消费支持async def函数，也包括发布消息支持asyncio生态，获取rpc结果支持asyncio生态。

为了与asyncio编程生态更搭配,新介绍 aio_push/aio_publish 和 AioAsyncResult 这些方法和类型.

此代码例子在 :
[https://github.com/ydf0509/funboost/tree/master/test_frame/full_asyncio_demo](https://github.com/ydf0509/funboost/tree/master/test_frame/full_asyncio_demo)

### 4b.3.1 funboost 天然支持 async def 的消费函数,和支持 aio_push 来异步发布消息.

下面funboost代码包含了同步函数和异步函数的消费的演示,包含了同步发布和异步发布的演示

ps: funboost的 concurrent_mode=ConcurrentModeEnum.THREADING 和 ConcurrentModeEnum.ASYNC 都支持 async def 函数。

注意对asyncio编程生态更友好的 aio_push 用法

```python
import asyncio
import time
from funboost import boost,BrokerEnum,ConcurrentModeEnum,BoosterParams

# funboost 直接方便性支持 async def 函数逇消费,远超 celery对async 函数的支持
@boost(BoosterParams(queue_name='aio_long_time_fun_queue',is_using_rpc_mode=True,concurrent_mode))
async def aio_long_time_fun(x):
    await asyncio.sleep(10)
    print(f'aio_long_time_fun {x}')
    return f'aio_long_time_fun {x}'

@boost(BoosterParams(queue_name='long_time_fun_queue',is_using_rpc_mode=True))
def long_time_fun(x):
    time.sleep(5)
    print(f'long_time_fun {x}')
    return f'long_time_fun {x}'


if __name__ == '__main__':
    async def aio_push_msg():
        for i in range(10):
            await aio_long_time_fun.aio_push(i)
    asyncio.run(aio_push_msg()) # asyncio 发布消息到中间件演示

    for j in range(10):     # 同步发布消息到中间件演示
        long_time_fun.push(j)


    aio_long_time_fun.consume() # 启动消费,funboost 能直接性支持async def 的函数作为消费函数,这点上的方便性完爆celery对asycn def的支持.
    long_time_fun.consume()  # 启动消费
```

### 4b.3.2 演示fastapi 中aio_push来发布消息,和 AioAsyncResult asyncio方式 等待获取结果.

下面fastapi web代码是在 流行的 fastapi 中,演示aio_push发布和rpc

注意 AioAsyncResult 类的使用

千万别在fastapi接口中使用同步的AsyncResult.result,异步函数中调用同步且耗时大的函数,整个程序会阻塞产生灭顶之灾.

```python
from fastapi import FastAPI
from funboost import AioAsyncResult

from consume_fun import aio_long_time_fun, long_time_fun

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


# 演示push同步发布, 并且aio rpc获取消费结果
@app.get("/url1/{name}")
async def api1(name: str):
    async_result = long_time_fun.push(name)  # 通常发布消息时间比较小,局域网内一般少于0.3毫秒,所以在asyncio的异步方法中调用同步io方法一般不会产生过于严重的灾难
    return {"result": await AioAsyncResult(async_result.task_id).status_and_result}   # 一般情况下不需要请求时候立即使用rpc模式获取消费结果,直接吧消息发到中间件后就不用管了.前端使用ajx轮训或者mqtt
    # return {"result": async_result.result}  # 如果你直接这样写代码,会产生所有协程全局阻塞灭顶之灾.

# 演示aio_push 异步发布, 并且aio rpc获取消费结果
@app.get("/url2/{name}")
async def api2(name: str):
    asio_async_result = await aio_long_time_fun.aio_push(name)  # 如果你用的是asyncio编程生态,那还是建议这种,尤其是对外网发布消息会耗时大的情况下.
    return {"result": await asio_async_result.result}  # 一般情况下不需要请求时候立即使用rpc模式获取消费结果,直接吧消息发到中间件后就不用管了.前端使用ajx轮训或者mqtt


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

```

```
运行web服务,浏览器中输入 http://127.0.0.1:8000/url1/name_xxx1
就能请求接口并发布消息,并获得消费结果.
```

### 4b.3.3 关于funboost的asyncio生态支持实现原理的答疑

<p style="background-color: #2cc36b;color:white">消费是怎么支持async def 函数并发的？</p>

```
funboost的 concurrent_mode=ConcurrentModeEnum.THREADING 和 ConcurrentModeEnum.ASYNC 都支持 async def 函数。

ConcurrentModeEnum.THREADING 相当于在线程池的每个线程内部，每个线程有一个单独loop，每个线程里面 loop.run_until_complete 来运行协程的。
使用的并发池是 funboost/concurrent_pool/flexible_thread_pool.py 的FlexibleThreadPool， 这个线程池不仅能支持同步函数，还能顺带兼容支持运行异步函数。
这是作者亲自开发的可变线程池(可自动缩小)

ConcurrentModeEnum.ASYNC 并发模式，是真正的让每个消费队列的函数协程任务运行在同一个单独的 loop 中。
使用的并发池是 funboost/concurrent_pool/async_pool_executor.py 的 AsyncPoolExecutor ，这个是 专用的asyncio并发池，
这个并发池只能用于执行async 异步函数，不支持运行同步函数。
这是作者开发的准用asyncio协程池。
```

<p style="background-color: #2cc36b;color:white">从消息队列中间件获取消息是io的，为什么源码的各种消息队列三方包都是同步的包？</p>

```
因为获取消息，是每个队列在一个进程里面，有且只有一个单独的独立的线程中去消息队列中间件获取消息，所以不存在并发的去拉取消息，在单个进程同个队列名，拉取消息不存在并发。
所以这个无需异步包。
```

<p style="background-color: #2cc36b;color:white">await funxx.aio_push 发布消息是咋实现的？为什么源码的各种消息队列三方包都是同步的包？</p>

```
一般内网中发布一个消息少于1毫秒，即使在你的asyncio项目生态中使用同步的funxx.push来发布消息，也不会造成长时间严重的阻塞，
但是funboost仍然开发了独立的 funxx.aio_push 来更好的搭配asyncio生态，这样你就不用担心发布消息耗时大阻塞loop了。

funboost没有使用各种异步消息队列包，咋搞定异步发布消息的？
funboost使用万能的同步函数转异步函数的loop.run_in_executor实现，大大节约了使用各种异步包来重新开发一遍。这个用户看async def aio_push()方法源码即可。
```

<p style="background-color: #2cc36b;color:white">AioAsyncResult 异步生态中获取rpc，避免使用同步方式来获取结果阻塞loop，如何实现的？</p>

```
因为funboost 的不管任何中间件，如果用户要使用rpc获取结果功能，就需要用到redis，所以作者工作量不大，实现时候使用 redis5.asyncio.Redis 这个异步redis操作类就可以了。

async_result = add.push(i, i * 2)
aio_async_result = AioAsyncResult(task_id=async_result.task_id) # 这里要使用asyncio语法的类，更方便的配合asyncio异步编程生态
print(await aio_async_result.result) # 注意这里有个await，如果不await就是打印一个协程对象，不会得到结果。这是asyncio的基本语法，需要用户精通asyncio。
print(await aio_async_result.status_and_result)

所以使用 await aio_async_result.result 来获取结果，避免使用同步防暑来等待结果耗时长导致loop阻塞。
```

<p style="background-color: #2cc36b;color:white">综上所述funboost亲自搞定asyncio是为了方便用户原有的asyncio编程项目中直接使用</p>

```
funboost 内置搞定了asyncio生态中的用户函数并发，消息拉取，消息发布，rpc获取消息结果，所以可以直接天衣无缝搭配用户的asyncio编程项目。
```

### 4b.3.4 劝退python小白使用funboost + asyncio 来编程，除非是专业python大神

非常的不建议普通python码农使用asyncio来装逼写代码。特别是打死都不愿意专门花费或者没有一周以上时间系统学习和测试 asyncio编程的pythoner。

有的人写的asyncio代码一看就太搞笑了，而且运行出了非常显而易见的低级asyncio问题他就很蒙蔽，这种情况下，真心的不建议再用asyncio来装逼写代码了。asyncio异步编程比同步编程难了2个数量级。

funboost的默认并发模式的线程池，是作者自己开发的超强效率的线程池，不是使用官方的 concurrnt.futures.ThreadpoolExecutor 那种通用线程池。用户用funboost的线程并发模式足以超级高效。

只有一种情况下，建议用户使用 funboost + asyncio来编程，那就是用户的工具包中所有可复用函数已经是asyncio写法，而且正在用的就是例如fastapi异步web框架，只有这种情况下才需要使用async def 来写funboost的消费函数，否则没有卵的必要用async来写消费函数。

特别是业余的 python 爱好者而非专业码农，真的不要在asyncio 生态下凑热闹了，用同步编程是真心的 省时间 省脑子 省bug。

**不知道 funboost的用户是不是因为害怕celery的复杂api，才使用funboost框架，导致能了解到funboost框架的过滤出的都是害怕复杂python用法的非专业python用户，反正我强烈感觉到这些用户非常不熟悉asyncio，还强行要用asyncio，这种感觉尤为明显。 用户因为怕复杂才选择funboost，却又要强行使用比Celery概念更复杂得多的asyncio来写代码，有一丝丝矛盾**

```
async def 的函数，定义协程函数本身不难，难的是如果要并发起来执行，要搞懂以下这些概念，
以下这些概念非常多十分之复杂，asyncio的并发玩法与同步函数 + 线程池并发写法区别很大，asyncio的并发写法难度大太多。
异步要想玩的溜，用户必须精通的常用方法和对象的概念包括以下：


asyncio.get_event_loop 方法
asyncio.new_event_loop 方法
asyncio.set_event_loop 方法
asyncio.ensure_future  方法
asyncio.create_task 方法
asyncio.wait  方法
asyncio.wait_for 方法
asyncio.gather  方法
asyncio.run_coroutine_threadsafe 方法
asyncio.run 方法
loop.run_in_executor 方法
run_until_complete  方法
run_forever 方法

loop 对象
future 对象
task  对象
corotinue 对象

以上这些方法和对象还只是asyncio的冰山一角，实际需要掌握的常见api达到30多个，只有掌握了这些才能在同步上下文和异步上下文切换自如。
例如在同步场景下怎么调用一个async的函数，在异步场景下怎么调用一个普通def的同步函数且不阻塞整个loop，并且对 loop 和协程对象的概念非常精通。
```

```
asyncio的API比threading复杂得多主要有以下原因：
执行模型的根本区别：
threading基于操作系统线程，执行切换由OS控制，概念简单直接
asyncio基于事件循环和协程的协作式多任务，需要显式管理事件循环和任务状态
显式切换点要求：
threading中线程切换对开发者透明
asyncio需要使用await显式标记可能的切换点，增加了编程复杂度
全新的语法结构：
asyncio引入了async/await语法，创建了同步与异步两套平行世界
需要学习两套上下文及其转换方法(run_in_executor等)
事件循环管理：
asyncio需要显式创建、运行、停止事件循环
需要了解不同运行模式(run_forever, run_until_complete等)
异步原语与同步替代：
需要提供几乎所有同步操作的异步替代品(异步文件IO、网络IO等)
引入了Future、Task、Coroutine等多种抽象概念
兼容性考虑：
asyncio是后期添加到Python的，需要与现有生态系统兼容
不能破坏原有代码，导致设计上更为复杂
threading的API简单是因为它将复杂性下放给了操作系统，而asyncio则需要在Python层面实现和管理整个并发模型。
```

综上所述，虽然在funboost中是能方便支持async def函数的消费，对asyncio的直接内置支持远超celery，但是不鼓励非专业资深码农使用async def来定义消费函数。

#### 4b.3.4.2 想在funboost中玩的溜asyncio实际比例如fastapi这种框架中使用asyncio 更难。

因为 FastAPI完全隐藏了事件循环管理 ，是在主线程中运行 loop和协程，基本上只在主线程中去运行loop和协程对象，管理和运行起来简单多得多。

funboost 是在很多个子线程中运行不同的loop ，难度比主线程中管理大多了；

这种线程与协程混合使用的场景确实是asyncio最复杂的应用场景之一，即使有经验的Python开发者也容易在此栽跟头和无法理解。

```
特别是例如一个全局变量对象 async_obj 绑定了一个loop，而你想在funboost的消费函数中去运行 async_obj 的方法，
实际上已经属于跨线程去使用这个async_obj了，这需要你有非常高超的精通asyncio概念的知识储备。 
这种async_obj 经常是一个异步的httpclient或者 数据库连接，他实际上不能很简单的随意在多个线程中去跨线程使用这个对象。

在主线程中常见的异步数据库连接，实际上不能很简单的直接就在其他线程中使用这个对象执行查询数据的方法；
在主线程中常见的异步http连接，实际上不能很简单的直接就在其他线程中使用这个对象执行发送http请求；
我说的这只有经常在这种情况下实践排查过bug的人才能懂，一般人都不知道我现在在讲的是什么。

所以 有的人对 funboost装饰器的 specify_async_loop完全不懂，
specify_async_loop: typing.Optional[asyncio.AbstractEventLoop] = None  # 指定的async的loop循环，设置并发模式为async才能起作用。
有些包例如aiohttp,发送请求和httpclient的实例化不能处在两个不同的loop中,可以把loop传过来，使得运行消费函数的线程在使用的loop和这个全局变量的loop是同一个。
默认情况下，不同的线程是不会去运行同一个loop的。


Python的asyncio设计中，事件循环(event loop)默认与创建它的线程绑定，不能简单地跨线程共享使用。这导致:
主线程创建的异步对象(如aiohttp客户端)绑定了主线程的loop
funboost的消费函数在工作线程中运行，有自己的loop
当尝试在工作线程中使用主线程创建的异步对象时会出现冲突
这就是为什么需要specify_async_loop参数 - 它允许不同的工作线程使用同一个loop，解决了这个跨线程asyncio对象共享的复杂问题。
这种问题即使对有经验的Python开发者也非常棘手，因为它涉及asyncio内部实现细节和线程安全问题，不是简单阅读文档就能理解的。
```

就是想劝退小白使用asyncio + funboost 编程。

## 4b.4 等待n个任务完成后，再做下一步操作(其实就是canvas任务编排)

之前在 4.17文档章节： 判断函数运行完所有任务，再执行后续操作，使用 wait_for_possible_has_finish_all_tasks来判断函数的消息队列是否已经运行完了。

但是有的人在问怎么实现n个任务完成后，再下一步操作。

这没有单独的语法方法，就是借助了rpc等待结果会阻塞的特性。

直接上代码：

```python
# -*- coding: utf-8 -*-
import time
from funboost import BoosterParams, BrokerEnum

@BoosterParams(queue_name='test_rpc_queue_a1', is_using_rpc_mode=True, broker_kind=BrokerEnum.REDIS_ACK_ABLE, qps=2, max_retry_times=5)
def f1(x):
    time.sleep(5)
    async_result_list = [f2.push(x + i) for i in range(10)]
    for async_result in async_result_list:
        async_result.set_timeout(300)
        print(async_result.task_id, async_result.status_and_result, async_result.result)
    print('f2 10个任务都完成了，现在开始进行下一步，打印哈哈。')
    print('哈哈')


@BoosterParams(queue_name='test_rpc_queue_a2',
               is_using_rpc_mode=True,  # f2必须支持rpc，必须写is_using_rpc_mode=True
               broker_kind=BrokerEnum.REDIS_ACK_ABLE,
               qps=5, max_retry_times=5)
def f2(y):
    time.sleep(10)
    return y * 10


if __name__ == '__main__':
    f1.consume()
    f2.consume()

    for j in range(20):
        f1.push(j)
```

```
例子解释：
f1 每个任务会分解10个子任务到f2中运行， 并且f1中要等待10个子任务全部完成后，才开始执行下一步，打印 "哈哈"
```

## 4b.5 funboost 任务编排(实现canvas功能)

```python
"""
此文件演示, funboost 使用 rpc获取结果阻塞的特性,来实现 canvas编排
可以把一个函数的结果作为下一个函数的入参,来实现 canvas编排
无需学习新的领域特定语言（DSL） 没有发明新的语法.funboost没有为工作流编排引入任何新的、专门的 API

整个编排过程就是调用 funboost 已有的 .push() / .aio_push() 和 .wait_rpc_data_or_raise() 方法。
开发者不需要去学习和记忆 chain, chord, group,header,body, s (signature), si,s(immutable=True), map,starmap  
等特定的 Canvas 概念和语法，降低了学习成本。
这一切都是用户主动使用funboost的rpc特性来实现,用户可以自由灵活控制
"""


"""
此文件演示一个非常经典的canvas编排:
    1.从url下载视频,并保存到本地 (download_video)
    2.根据第1步下载的视频文件,转码视频,并发转换成3个分辨率的视频文件 (transform_video)
    3.根据第2步转码的视频文件列表,更新数据库,并且发送微信通知 (send_finish_msg)


        
这个需求如果在celery的canvas编排是如下:
    from celery import chain, chord, group

    resolutions = ["360p", "720p", "1080p"]

    # header: 并行转码；body: 汇总并发送完成消息
    header = group(transform_video.s(resolution=r) for r in resolutions)
    body = send_finish_msg.s(url=url)

    # 先下载 -> 将下载结果（文件路径）作为额外参数传给 header 中每个 transform_video
    work_flow = chain(
        download_video.s(url),
        chord(header, body)
    )
"""

"""
celery发明了一套声明式canvas api,用户需要学习新的语法,
funboost是命令式,全部使用已有的rpc方法,没有一套声明式api
"""


import typing

import os
import sys
import time


from funboost import (boost, BoosterParams, BrokerEnum, ctrl_c_recv,
                      ConcurrentModeEnum, AsyncResult,FunctionResultStatus,
                      BoostersManager, AioAsyncResult, fct
                      )


class MyBoosterParams(BoosterParams):
    is_using_rpc_mode: bool = True
    broker_exclusive_config: dict = {'pull_msg_batch_size': 1}
    broker_kind: str = BrokerEnum.REDIS_ACK_ABLE
    max_retry_times: int = 0


@boost(MyBoosterParams(queue_name='download_video_queue'))
def download_video(url):
    """下载视频"""
    # 1/0  # 这个是模拟 任务编排,其中某个环节报错
    mock_need_time = 5
    time.sleep(mock_need_time)
    download_file = f'/dir/vd0/{url}'
    fct.logger.info(f'下载视频 {url} 完成, 保存到 {download_file},耗时{mock_need_time}秒')
    return download_file


@boost(MyBoosterParams(queue_name='transform_video_queue'))
def transform_video(video_file, resolution='360p'):
    """转码视频"""
    mock_need_time = 10
    time.sleep(mock_need_time)
    transform_file = f'{video_file}_{resolution}'
    fct.logger.info(f'转码视频 {video_file} 完成, 保存到 {transform_file},耗时{mock_need_time}秒')
    return transform_file


@boost(MyBoosterParams(queue_name='send_finish_msg_queue'))
def send_finish_msg(transform_video_file_list: list, url):
    """3个清晰度的视频都转码完成后,汇总结果发送微信通知"""
    mock_need_time = 2
    time.sleep(mock_need_time)
    fct.logger.info(f'更新数据库,并且发送微信通知 {url} 视频转码完成 {transform_video_file_list} ,耗时{mock_need_time}秒')
    return f'ok! {url} 下载 -> 转码3个清晰度格式视频 {transform_video_file_list} -> 更新数据库,发送微信通知 完成'


@boost(MyBoosterParams(queue_name='canvas_task_queue',concurrent_num=500))
def canvas_task(url):


    """
    funboost显式的把上一个函数交给或者结果列表传递给下一个函数,思路很清晰.用户可以在里面写各种if else判断,
    以及上一个节点错误是否还调用下一个节点.
    
    celery的canvas 自动把上一个函数的结果作为下一个函数的第一个入参,那里面的传递关系不清晰关系不明显不符合直觉,不透明.
    如果涉及到非常复杂的编排,用户很难使用celery 的语法写出正确的canvas编排,还不如使用rpc清晰易懂.
    """

   
    r1: AsyncResult = download_video.push(url).set_timeout(1000) # 用户可以设置rpc最大等待时间.
    rpc_res_file:FunctionResultStatus = r1.wait_rpc_data_or_raise(raise_exception=True)

    r2_list: typing.List[AsyncResult] = [transform_video.push(rpc_res_file.result, resolution=rel)
                                  for rel in ['360p', '720p', '1080p']]
    rpc_res_list = AsyncResult.batch_wait_rpc_data_or_raise(r2_list, raise_exception=True)
    transform_video_file_list = [one.result for one in rpc_res_list]

    r3 = send_finish_msg.push(transform_video_file_list, url)
    return r3.wait_rpc_data_or_raise(raise_exception=True).result


@boost(MyBoosterParams(queue_name='aio_canvas_task_queue',
                       concurrent_mode=ConcurrentModeEnum.ASYNC, # 使用asyncio异步阻塞的方式来实现canvas编排
                       concurrent_num=500))
async def aio_canvas_task(url):
    # 用户自己对比和canvas_task的相同点和差异.
    """演示 ,使用asyncio 来等待rpc结果, 减少系统线程占用数量"""
    r1: AioAsyncResult = await download_video.aio_push(url)
    rpc_res_file:FunctionResultStatus = await r1.wait_rpc_data_or_raise(raise_exception=True)

    r2_list: typing.List[AioAsyncResult] = [(await transform_video.aio_push(rpc_res_file.result, resolution=rel)).set_timeout(2000)
                                     for rel in ['360p', '720p', '1080p']]
    rpc_res_list = await AioAsyncResult.batch_wait_rpc_data_or_raise(r2_list, raise_exception=True)
    transform_video_file_list = [one.result for one in rpc_res_list]

    r3 = await send_finish_msg.aio_push(transform_video_file_list, url)
    return (await r3.wait_rpc_data_or_raise(raise_exception=True)).result


if __name__ == '__main__':
    download_video.consume()
    transform_video.consume()
    send_finish_msg.consume()
    canvas_task.consume()  # 演示使用同步阻塞的方式来实现canvas编排
    aio_canvas_task.consume()  # 演示使用asyncio异步阻塞的方式来实现canvas编排

    r4_a = canvas_task.push(f'funboost_url_video_a')
    print(r4_a.wait_rpc_data_or_raise(raise_exception=False).to_pretty_json_str())
    print('funboost_url_video_a 下载->转码->通知 耗时', r4_a.rpc_data.time_cost)

    r4_b = aio_canvas_task.push(f'funboost_url_video_b')
    print(r4_b.wait_rpc_data_or_raise(raise_exception=False).to_pretty_json_str())
    print('funboost_url_video_b 下载->转码->通知 耗时', r4_b.rpc_data.time_cost)

    ctrl_c_recv()

```

`<div>` `</div>`

# 5.框架运行时截图

## 5.1 windows pycharm 运行截图

![](https://s1.ax1x.com/2020/06/30/N5yZin.png)

## 5.1b 新增running状态显示截图(2024-03)：

![函数状态3.png](%BA%AF%CA%FD%D7%B4%CC%AC3.png)


## 5.2 linux 运行率截图


<a href="https://imgse.com/i/pkFF5uV"><img src="https://s21.ax1x.com/2024/04/29/pkFF5uV.png" alt="pkFF5uV.png" border="0" /></a>


## 5.3 函数执行结果及状态搜索查看

![img_67.png](img_67.png)

高并发
![img_68.png](img_68.png)


函数结果和运行次数和错误异常查看。使用的测试函数如下。

```
def add(a, b):
    logger.info(f'消费此消息 {a} + {b} 中。。。。。')
    time.sleep(random.randint(3, 5))  # 模拟做某事需要阻塞10秒种，必须用并发绕过此阻塞。
    if random.randint(4, 6) == 5:
        raise RandomError('演示随机出错')
    logger.info(f'计算 {a} + {b} 得到的结果是  {a + b}')
    return a + b
```


![img_69.png](img_69.png)

任务消费统计曲线。
![img_70.png](img_70.png)


<div> </div>


# 6.常见问题回答

直接统一回复常见问题，例如是不是模仿celery


## 6.1 你干嘛要写这个框架？和celery 、rq有什么区别？

你干嘛要写这个框架？和celery 、rq有什么区别？是不是完全重复造轮子为了装x？

```text
见第二章的2.4章节解释，有接近20种优势。
celery 从性能、用户编码需要的代码量、用户使用难度 各方面都远远差于此框架。
可以使用例子中的场景代码进行了严格的控制变量法实际运行对比验证。

```

## 6.2 为什么包的名字这么长?

为什么包的名字这么长，为什么不学celery把包名取成 花菜 茄子什么的？

  ```text
  答： 为了直接表达框架的意思。现在代码在ide都能补全，名字长没关系。
  生产消费模式不是celery专利，是通用常见的编程思想，不是必须用水果取名。
   ```

## 6.3 框架是使用什么序列化协议来序列化消息的。

 ```
    答：框架默认使用json。并且不提供序列化方式选择，有且只能用json序列化。json消息可读性很强，远超其他序列化方式。
    默认使用json来序列化和反序列化消息。所以推送的消息必须是简单的，不要把一个自定义类型的对象作为消费函数的入参，
    json键的值必须是简单类型，例如 数字 字符串 数组 字典这种。不可以是不可被json序列化的python自定义类型的对象。
    
    用json序列化已经满足所有场景了，picke序列化更强，但仍然有一些自定义类型的对象的实例属性由于是一个不可被序列化
    的东西，picke解决不了，这种东西例如self.r = Redis（），而redis对象又包括threding.Lock类型的属性 ,不可以被pike序列化

    就算能序列化的对象也是要用一串很长的东西来。
    用pike来序列化复杂嵌套属性类型的对象，不仅会导致中间件要存储很大的东西传输效率会降低，在编码和解码也会消耗更多的cpu。如果框架支持了pike序列化，会让使用者养成不好的粗暴习惯。
    想消费函数传redis对象作为入参，这种完全可以使用json来解决，例如指定ip 和端口，在消费函数内部来使用redis。所以用json一定可以满足一切传参场景。
    
    如果json不能满足你的消费任务的序列化，那不是框架的问题，一定是你代码设计的问题。所以没有预留不同种类序列化方式的扩展，
    也不打算准备加入其他序列化方式。
  ```

## 6.4 框架如何实现定时？

```
答：使用的是定时发布任务，那么就能定时消费任务了。框架的 ApsJobAdder 轻度封装了 apscheduler 包.
用户主要需要学习  知名定时包 apscheduler
```

## 6.5 为什么强调是函数调度框架不是类调度框架，不是方法调度框架？(说明：2024.06月以后新增支持了实例方法和类方法作为消费函数)


<pre style="color:yellow;font-size: large; background-color: green;">
说明：2024.06月以后新增支持了实例方法和类方法作为消费函数,但是这里面的说明仍然值得一看，
看你这里才知道支持实例方法和类方法作为消费函数有多么复杂和实现原理，
使用实例方法和类方法作为消费函数看4.32章节的文档
</pre>

为什么强调是函数调度框架不是类调度框架，不是方法调度框架？你代码里面使用了类，是不是和此框架水火不容了?


问的是consuming_function的值能不能是一个类或者一个实例方法。

 ```text
    答：一切对类的调用最后都是体现在对方法的调用。这个问题莫名其妙。
    celery rq huery 框架都是针对函数。
    调度函数而不是类是因为：
    1）类实例化时候构造方法要传参，类的公有方法也要传参，这样就不确定要把中间件里面的参数哪些传给构造方法哪些传给普通方法了。
       见5.8
    2） 这种分布式一般要求是幂等的，传啥参数有固定的结果，函数是无依赖状态的。类是封装的带有状态，方法依赖了对象的实例属性。
    3) 比如例子的add方法是一个是实例方法，看起来好像传个y的值就可以，实际是add要接受两个入参，一个是self，一个是y。如果把self推到消息队列，那就不好玩了。
       对象的序列化浪费磁盘空间，浪费网速传输大体积消息，浪费cpu 序列化和反序列化。所以此框架的入参已近说明了，
       仅仅支持能够被json序列化的东西，像普通的自定义类型的对象就不能被json序列化了。
        celery也是这样的，演示的例子也是用函数（也可以是静态方法），而不是类或者实例方法，
        这不是刻意要和celery一样，原因已经说了，自己好好体会好好想想原因吧。
    
    框架如何调用你代码里面的类。
    假设你的代码是：
    class A():
       def __init__(x):
           self.x = x
        
       def add(self,y):
           return self.x + y
    
    那么你不能 a =A(1) ; a.add.push(2),因为self也是入参之一，不能只发布y，要吧a对象(self)也发布进来。
    add(2)的结果是不确定的，他是受到a对象的x属性的影响的，如果x的属性是100，那么a.add(2)的结果是102.
    如果框架对实例方法，自动发布对象本身作为第一个入参到中间件，那么就需要采用pickle序列化，picke序列化对象，
    消耗的cpu很大，占用的消息体积也很大，而且相当一大部分的对象压根无法支持pickle序列化。
    无法支持序列化的对象我举个例子，
    
import pickle
import threading
import redis

class CannotPickleObject:
    def __init__(self):
        self._lock = threading.Lock()


class CannotPickleObject2:
    def __init__(self):
        self._redis = redis.Redis()

print(pickle.dumps(CannotPickleObject())) # 报错，因为lock对象无法pickle
print(pickle.dumps(CannotPickleObject2())) # 报错，因为redis客户端对象也有一个属性是lock对象。

以上这两个对象如果你想序列化，那就是天方夜谭，不可能绝对不可能。
真实场景下，一个类的对象包含了很多属性，而属性指向另一个对象，另一个对象的属性指向下一个对象，
只要其中某一个属性的对象不可pickle序列化，那么此对象就无法pickle序列化。
pickle序列化并不是全能的，所以经常才出现python在win下的多进程启动报错，
因为windows开多进程需要序列化入参，但复杂的入参，例如不是简单的数字 字母，而是一个自定义对象，
万一这个对象无法序列化，那么win上启动多进程就会直接报错。

         
所以如果为了调度上面的class A的add方法，你需要再写一个函数
def your_task(x,y):
    return  A(x).add(y)
然后把这个your_task函数传给框架就可以了。所以此框架和你在项目里面写类不是冲突的，
本人是100%推崇oop编程，非常鲜明的反对极端面向过程编程写代码，但是此框架鼓励你写函数而不是类+实例方法。
框架能支持@staticmethod装饰的静态方法，不支持实例方法，因为静态方法的第一个入参不是self。
    
    
如果对以上为什么不支持实例方法解释还是无法搞明白，主要是说明没静下心来仔细想想，
如果是你设计框架，你会怎么让框架支持实例方法？

statckflow上提问，celery为什么不支持实例方法加@task
https://stackoverflow.com/questions/39490052/how-to-make-any-method-from-view-model-as-celery-task

celery的作者的回答是：

You can create tasks out of methods. The bad thing about this is that the object itself gets passed around 
(because the state of the object in worker has to be same as the state of the caller) 
in order for it to be called, so you lose some flexibility. So your object has to be pickled every 
time, which is why I am against this solution. Of course this concerns only class methods, s
tatic methods have no such problem.

Another solution, which I like, is to create separate tasks.py or class based tasks and call the methods 
from within them. This way, you will have FULL control over Analytics object within your worker.

这段英文的意思和我上面解释的完全一样。所以主要是你没仔细思考想想为什么不支持实例方法。
  
  ```

## 6.6 是怎么调度一个函数的。

 ```
     答：基本原理如下
     
     def add(a,b):
         print(a + b)
         
     从消息中间件里面取出参数{"a":1,"b":2}
     然后使用  add(**{"a":1,"b":2}),就是这样运行函数的。
  ```

## 6.7 框架适用哪些场景？

 ```
      答：分布式 、并发、 控频、断点接续运行、定时、指定时间不运行、
          消费确认、重试指定次数、重新入队、超时杀死、计算消费次数速度、预估消费时间、
          函数运行日志记录、任务过滤、任务过期丢弃等数十种功能。
         
          只需要其中的某一种功能就可以使用这。即使不用分布式，也可以使用python内置queue对象。
          这就是给函数添加几十项控制的超级装饰器。是快速写代码的生产力保障。
          
          适合一切耗时的函数，不管是cpu密集型 还是io密集型。
          
        不适合的场景主要是：
           比如你的函数非常简单，仅仅只需要1微妙 几十纳秒就能完成运行，比如做两数之和，print一下hello，这种就不是分需要使用这种框架了，
           如果没有解耦的需求，直接调用这样的简单函数她不香吗，还加个消息队列在中间，那是多此一举。
           
  ```

## 6.8 怎么引入使用这个框架？门槛高不高？

   ```
    答：先写自己的函数（类）来实现业务逻辑需求，不需要思考怎么导入框架。
        写好函数后把 函数和队列名字绑定传给消费框架就可以了。一行代码就能启动分布式消费。
        在你的函数上面加@boost装饰器，执行 your_function.conusme() 就能自动消费。
        所以即使你不想用这个框架了，你写的your_function函数代码并没有作废。
        所以不管是引入这个框架 、废弃使用这个框架、 换成celery框架，你项目的99%行 的业务代码都还是有用的，并没有成为废物。
        别的框架如flask换django，scrapy换spider，代码形式就成了废物。
  ```

## 6.9 怎么写框架？

   ```
    答： 需要学习真oop和36种设计模式。唯有oop编程思想和设计模式，才能持续设计开发出新的好用的包甚至框架。
        如果有不信这句话的，你觉得可以使用纯函数编程，使用0个类来实现这样的框架。
        
        如果完全不理会设计模式，实现threding gevent evenlet 3种并发模式，加上10种中间件类型，实现分布式消费流程，
        需要反复复制粘贴扣字30次。代码绝对比你这个多。例如基于nsq消息队列实现任务队列框架，加空格只用了80行。
        如果完全反对oop，需要多复制好几千行来实现。

        例如没听说设计模式的人，在写完rabbitmq版本后写redis版本，肯定十有八九是在rabbitmq版本写完后，把整个所有文件夹，
        全盘复制粘贴，然后在里面扣字母修改，把有关rabbitmq操作的全部扣字眼修改成redis。如果某个逻辑需要修改，
        要在两个地方都修改，更别说这是10几种中间件，改一次逻辑需要修改10几次。
        我接手维护得老项目很多，这种写法的编程思维的是特别常见的，主要是从来没听说设计模式4个字造成的，
        在我没主动学习设计模式之前，我也肯定会是这么写代码的。
        
        
        只要按照36种设计模式里面的oop4步转化公式思维写代码三个月，光就代码层面而言，写代码的速度、流畅度、可维护性
        不会比三年经验的老程序员差，顶多是老程序员的数据库 中间件种类掌握的多一点而已，这个有机会接触只要花时间就能追赶上，
        但是编程思维层次，如果没觉悟到，可不是那么容易转变的，包括有些科班大学学过java的也没这种意识，
        非科班的只要牢牢抓住把设计模式 oop思维放在第一重要位置，写出来的代码就会比科班好，
        不能光学 if else 字典 列表 的基本语法，以前我看python pdf资料时候，资料里面经常会有两章以上讲到类，
        我非常头疼，一看到这里的章节，就直接跳过结束学习了，现在我也许只会特意去看这些章节，
        然后看资料里面有没有把最本质的特点讲述好，从而让用户知道为什么要使用oop，而不是讲下类的语法，这样导致用户还是不会去使用的。
        
        
        你来写完包括完成10种中间件和3种并发模式，并且预留消息中间件的扩展。
        然后我们来和此框架 比较 实现框架难度上、 实现框架的代码行数上、 用户调用的难度上 这些方面。
  ```

## 6.10 框架能做什么
```
答：你在你的函数里面写什么，框架就是自动并发做什么。
框架在你的函数上加了自动使用消息队列、分布式、自动多进程+多线程(协程)超高并发、qps控频、自动重试。
只是增加了稳定性、扩展性、并发，但做什么任务是你的函数里面的代码目的决定的。

只要是你代码涉及到了使用并发，涉及到了手动调用线程或线程池或asyncio，那么就可以使用此框架，
使你的代码本身里面就不需要亲自操作任何线程 协程 asyncio了。

不需要使用此框架的场景是函数不需要消耗cpu也不需要消耗io，例如print("hello"),如果1微秒就能完成的任务不需要使用此框架。
```

## 6.11 日志的颜色不好看或者觉得太绚丽刺瞎眼，想要调整。

```

一 、关于日志颜色是使用的 \033实现的，控制台日志颜色不光是颜色代码决定的，最主要还是和ide的自身配色主题有关系，
同一个颜色代码，在pycahrm的十几个控制台颜色主题中，表现的都不一样。
所以代码一运行时候就已经能提示用户怎么设置优化控制台颜色了，文这个问题说明完全没看控制台的提示。
"""
1)使用pycharm时候，建议重新自定义设置pycharm的console里面的主题颜色。
   设置方式为 打开pycharm的 file -> settings -> Editor -> Color Scheme -> Console Colors 选择monokai，
   并重新修改自定义6个颜色，设置Blue为1585FF，Cyan为06B8B8，Green 为 05A53F，Magenta为 ff1cd5,red为FF0207，yellow为FFB009。         
2)使用xshell或finashell工具连接linux也可以自定义主题颜色，默认使用shell连接工具的颜色也可以。

颜色效果如连接 https://imgse.com/i/pkFSfc8

在当前项目根目录的 nb_log_config.py 中可以修改当get_logger方法不传参时后的默认日志行为。
"""



二、关于日志太绚丽，你觉得不需要背景色块，在当前项目根目录的 nb_log_config.py 中可以设置
DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = False  # 在控制台是否显示彩色块状的日志。为False则不使用大块的背景颜色。

```

## 6.12 是不是抄袭模仿 celery

```
答：有20种优势，例如celery不支持asyncio、celery的控频严重不精确，光抄袭解决不了。比celery有20项提升，具体看2.4章节
我到现在也只能通过实际运行来达到了解推车celery的目的，并不能直接默读代码就搞懂。
celery的层层继承，特别是层层组合，又没多少类型提示，说能精通里面每一行源码的人，多数是高估自己自信过头了。

celery的代码太魔幻，不运行想默读就看懂是不可能的，不信的人可以把自己关在小黑屋不吃不喝把celery源码背诵3个月，
然后3个月后 试试默写能不能写出来实现里面的兼容 多种中间件 + 多种并发模式 + 几十种控制方式的框架。

这是从一个乞丐版精简框架衍生的，加上36种设计模式付诸实践。

此框架运行print hello函数， 性能强过celery 20倍以上(测试每秒消费次数，具体看我的性能对比项目)。
此框架支持的中间件比celery多
此框架引用方式和celery完全不一样，完全不依赖任何特定的项目结构，celery门槛很高。

```

```
此框架和celery没有关系，没有受到celery启发，也不可能找出与celery连续3行一模一样的代码。
这个是从原来项目代码里面大量重复while 1:redis.blpop()  发散扩展的。

这个和celery唯一有相同点是，都是生产者 消费者 + 消息队列中间件的模式，这种生产消费的编程思想或者叫想法不是celery的专利。
包括我们现在java框架实时处理数据的，其实也就是生产者 消费者加kfaka中间件封装的，难道java人员开发框架时候也是需要模仿一下python celery源码或者思想吗。
任何人都有资格开发封装生产者消费者模式的框架，生产者 消费者模式不是celery专利。生产消费模式很容易想到，不是什么高深的架构思想，不需要受到celery的启发才能开发。

```

## 6.13 使用此框架时候，在一个python项目中如何连接多个相同种类的消息队列中间件ip地址

```
这个问题是问一个项目中，有些脚本要连接 192.168.0.1的redis ，有些脚本要连接192.168.0.2的redis，但框架配置文件只有一个，如何解决？

例如目录结构是
your_proj/
      funboost_config.py   (此文件是第一次启动任意消费脚本后自动生成的，用户按需修改配置)
      dira/a_consumer.py  (此脚本中启动funa函数消费)
      dirb/b_consumer.py   （此脚本中启动funb函数消费）
      
如果funa函数要连接 192.168.0.1的redis，funb函数要连接192.168.0.2的redis，有两种解决方式

第一种是在启动消费的脚本，脚本里面手动调用 patch_frame_config()函数来设置各种中间件的值

第二种是 把 funboost_config.py  分别复制到dira和dirb文件夹.
这种就会自动优先使用 a_consumer.py和b_consumer.py同文件夹层级的配置了，
而非是自动优先读取python项目根目录的配置文件，这个是利用了python语言的import 模块导入优先级机制。


```

## 6.14 什么是确认消费？为什么框架总是强调确认消费？

发布端：
```python
from scripxx  import fun

for i in range(10):
    fun.push(i)
```


消费端：
```python
import time
from funboost import boost, BoosterParams

@boost(BoosterParams(queue_name='test_confirm'))
def fun(x):
    print(f'开始处理 {x}')
    time.sleep(120)
    print(f'处理完成 {x}')

fun.consume()
```
```
启动消费脚本后，任意时刻随意强制反复关闭重启消费代码，只要函数没有完整的执行完成，函数参数就不会丢失。达到了消息万无一失。
具体的那些中间件消费者支持消费确认，具体见 3.1 介绍。
实现了4种redis消息队列中间件，其中有3种是确认消费的。

确认消费很重要，如果你自己写个简单粗暴的 while 1:redis.blpop()的脚本，你以为是可以断点接续呢，
在多线程并发执行函数时候，大量的消息会丢的很惨。导致虽然是断点接续但你不敢随意重启。
```

## 6.15 如何等待队列中的消息全部消费完成

如果有这种需求需要等待消费完成，使用 wait_for_possible_has_finish_all_tasks()
```python
f.consume()
f.wait_for_possible_has_finish_all_tasks(minutes=3)  # 框架提供阻塞方法，直至队列任务全部消费完成，才会运行到下一行。
print("over")   # 如果不加上面那一行，这个会迅速打印over
```

## 6.16 框架支不支持函数上加两个装饰器？

### 6.16.1 使用consumin_function_decorator 传参装饰器，可以用push publish发布，不需要设置should_check_publish_func_params=False
```
由于发布任务时候需要自动精确组装入参字典，所以不支持  *args  **kwargs形式的入参，不支持叠加两个@装饰器 （后来已更新解决方式，解决方式看6.16.2）
想在消费函数加装饰器，通过 boost 装饰器的 consumin_function_decorator 入参指定装饰器函数就行了。
那么如果是想叠加3个装饰器怎么写，例如本来想：

@boost(BoosterParams(queue_name='queue666'))
@deco1('hello')
@deco2
def task_fun(x,y):
    ...
    
那就是写成 consumin_function_decorator=deco1('hello')(deco2) 就可以了，具体要了解装饰器的本质就知道，叠加100个装饰器都可以。

如下的例子是使用redis的incr命令统计每台机器ip 总共运行了多少次函数。
```

```python
import inspect
import nb_log
from funboost import boost, BoosterParams
from funboost.utils.redis_manager import RedisMixin
from functools import wraps



def incr_deco(redis_key):
    def _inner(f):
        @wraps(f)
        def __inner(*args, **kwargs):
            result = f(*args, **kwargs)
            RedisMixin().redis_db_frame.incr(redis_key)
            # mongo_col.insert_one({'result':result,'args':str(args),'kwargs':str(kwargs)})
            return result

        return __inner

    return _inner


@boost(BoosterParams(queue_name='test_queue_235', consumin_function_decorator=incr_deco(nb_log.nb_log_config_default.computer_ip)))
def fun(xxx, yyy):
    print(xxx + yyy)
    return xxx + yyy


if __name__ == '__main__':
    print(inspect.getfullargspec(fun))

    for i in range(10):
        fun.push(i, 2 * i)
    fun.consume()
```

### 6.16.2 装饰器直接加到消费函数上，设置should_check_publish_func_params=False，需要publish来发布消息

```python
import inspect
import nb_log
from funboost import BoosterParams
from funboost.utils.redis_manager import RedisMixin
from functools import wraps


def incr_deco(redis_key):
    def _inner(f):
        @wraps(f)
        def __inner(*args, **kwargs):
            result = f(*args, **kwargs)
            RedisMixin().redis_db_frame.incr(redis_key)
            return result

        return __inner

    return _inner


@BoosterParams(queue_name='test_queue_23b', 
               should_check_publish_func_params=False,  # 这一行很重要，should_check_publish_func_params必须设置为False，如果你是直接把装饰器加到函数上了，funboost无法获取函数的入参名字，无法自动生成json消息，所以需要用户自己publish来发布入参字典。
               )
@incr_deco('test_queue_23b_run_count') # 用户的装饰器直接加在函数上了。
def fun(xxx, yyy):
    print(xxx + yyy)
    return xxx + yyy


if __name__ == '__main__':

    for i in range(20):
        # fun.push(i, 2 * i) # 不可以fun.push这样发布
        fun.publish({'xxx': 1, 'yyy': 2})  # 直接把装饰器写在消费函数上，那就用户需要使用publish发布，且boost装饰器设置should_check_publish_func_params=False
    fun.consume()
```

## 6.17 嫌框架日志记录太详细？

### 6.17.a 设置发布者消费者的日志级别,控制是否显示发布了什么消息和消费了什么消息.
```
日志是了解当前框架正在运行什么的好手段，不然用户懵逼不知道背后在发生执行什么。
@boost 装饰器设置 log_level=20 或logging.INFO，就不会再记录框架正在运行什么函数了。
如图再装饰器加上 log_level=20后，框架以后就再也不会记录框架正在运行什么函数入参结果是什么了。
```
![img_31.png](img_31.png)


@boost 装饰器设置 log_level=20 只是控制消费者和发布者命名空间自身的日志的,不是控制所有命名空间的日志的,
有些人到现在不清楚,不同的命名空间的logger是可以设置不同的日志级别和handlers的,这要学习logging基础了.


### 6.17b 嫌funboost启动时候打印太多提示用户的消息?
```
答: 主要是提示用户怎么设置配置文件,和读取的配置文件路径是什么,读取的配置内容是什么,免得用户丈二和尚摸不着头脑,不知道自己的配置是什么.
因为很多python人员,到现在完全不清楚 PYTHONPATH 这个重要概念,说了几百遍这个概念很重要,这么基础的又不学习,
还嫌弃提示你funboost_config配置麻烦,建议不懂PYTHONPATH的人不要屏蔽启动时候的打印提示了.

老手可以通过设置日志级别来屏蔽funboost_config的配置提示.
```
修改你的funboost_config.py的FunboostCommonConfig的配置,可以设置一些命名空间的日志级别,去掉启动时候的提示
![img_56.png](img_56.png)

```python
class FunboostCommonConfig(DataClassBase):
    # nb_log包的第几个日志模板，内置了7个模板，可以在你当前项目根目录下的nb_log_config.py文件扩展模板。
    NB_LOG_FORMATER_INDEX_FOR_CONSUMER_AND_PUBLISHER = 11  # 7是简短的不可跳转，5是可点击跳转的，11是可显示ip 进程 线程的模板。
    TIMEZONE = 'Asia/Shanghai'  # 时区

    # 以下配置是修改funboost的一些命名空间和启动时候的日志级别,新手不熟练就别去屏蔽日志了
    SHOW_HOW_FUNBOOST_CONFIG_SETTINGS = False  # 如果你单纯想屏蔽 "分布式函数调度框架会自动导入funboost_config模块当第一次运行脚本时候，函数调度框架会在你的python当前项目的根目录下 ...... "  这句话,
    FUNBOOST_PROMPT_LOG_LEVEL = logging.INFO  # funboost启动时候的相关提示语,用户可以设置这个命名空间的日志级别来调整
    KEEPALIVETIMETHREAD_LOG_LEVEL = logging.INFO  # funboost的作者发明的可缩小自适应线程池,用户对可变线程池的线程创建和销毁线程完全无兴趣,可以提高日志级别.
```

屏蔽日志级别前:

![img_53.png](img_53.png)
![img_54.png](img_54.png)

屏蔽日志级别后:

![img_55.png](img_55.png)









## 6.18 为什么框架在cmd shell终端运行时候要求会话中设置环境变量 export PYTHONPATH=你的项目根目录？


```
有的人写了三四年的python代码，连PYTHONPATH作用和概念都没听说过，真的很悲剧
如果是下面的 pythonpathdemo是一个python项目根目录，pycharm以项目方式打开这个文件夹。
你会发现run5.py在pycahrm可以运行，在cmd中无法运行，因为无法找到d1包，笨瓜会硬编码操作sys.path.insert非常的愚蠢，
这种笨瓜主要是写代码一意孤行，导致不学习PYTHONPATH。

```
![img_23.png](img_23.png)

完整讲解pythonpath重要性文章在： 

[https://github.com/ydf0509/pythonpathdemo](https://github.com/ydf0509/pythonpathdemo)

一句命令行解决设置 pythonpath 和运行 python脚本

一定要设置的是临时终端会话级pythonpath，不要设置到配置文件写死永久固定环境变量
```
例如你的项目根目录是  /home/xiaomin/myproj/
你的运行起点脚本在 /home/xiaomin/myproj/dir2/dir3/run_consume6.py

一句话就是
linux: export PYTHONPATH=/home/xiaomin/myproj/; python3 /home/xiaomin/myproj/dir2/dir3/run_consume6.py
win的cmd:假设代码在d盘先切换到盘符d盘 d:/ 。 然后 set PYTHONPATH=/codes2022/myproj/ & python3 /codes2022/myproj/dir2/dir3/run_consume6.py
win10和11的powershell： 假设代码在d盘先切换到盘符d盘 d:/。然后 $env:PYTHONPATH="/codes2022/myproj/"; python3 /codes2022/myproj/dir2/dir3/run_consume6.py
压根不要敲击两次命令行好不。

如果你已经cd切换到项目根目录myproj了，那就 export PYTHONPATH=./;python3 dir2/dir3/run_consume6.py
```

### 6.18.2 为什么celery scrapy django不需要用户设置pythonpath？
```
因为这些框架都是固定死用户的项目目录解构，项目运行起点有固定的唯一脚本，而且该脚本在项目跟目录的第一个直接层级。
例如django scrapy ，他的命令行启动，你必须先cd 到项目的根目录再运行命令行。

而此框架是为了兼容用户的cmd命令当前文件夹在任意文件夹下，就可以运行你项目下的任意多层级深层级下的脚本。
用户设置了pythonpath后，可以cd到任意文件夹下，再运行 python /dir1/dir2/xxx.py 任然能正确的import。

如果用户能够保证他要python启动运行的脚本始终是放在了项目的第一层级目录下面，当然可以不用设置 PYTHONPATH了。
```           


### 6.18.3  怎么指定配置文件读取 funboost_config.py 和nb_log_config.py的文件夹位置
```
默认就是放在项目根目录，然后设置 export PYTHONPATH=你的项目根目录， （linux  win+cmd  win+powershell 设置临时会话的环境变量语法不一样，6.18已经介绍了）

如果要指定读取的配置文件的存放位置为别的文件夹，也很容易，归根结底还是要精通PYTHONPATH的作用。

例如你的项目根目录是   /home/codes/proj     ，你不想使用项目根目录下的配置文件，想读取别的文件夹的配置文件作为funboost的中间件配置。
假设你的文件夹是 /home/xiaomin/conf_dir ，里面有   funboost_config.py ，如果你的/home/codes/proj 项目想使用  /home/xiaomin/conf_dir/funboost_config.py
作为配置文件， 那就 export PYTHONPATH=/home/xiaomin/conf_dir:/home/codes/proj
也就是意思添加两个文件夹路径到 PYTHONPATH

因为funboost是尝试导入import funboost_config.py 只要能import 到就能读取到，所以只要你把文件夹添加到PYTHONPATH环境变量就可以了(可以print sys.path来查看这个数组)
归根结底是要懂PYTHONPATH，有的人老是不懂PYTHONPATH作用，不愿意认真看  https://github.com/ydf0509/pythonpathdemo  ，非常杯具。
```

### 6.18.4 怎么根据不同环境使用不同的funboost_config配置文件？

```
框架获取配置的方式就是直接import funboost_config，然后将里面的值覆盖框架的 funboost_config_deafult.py 值。
为什么能import 到 funboost_config,是因为要求export PYTHONPATH=你的项目根目录，然后第一次运行时候自动生成配置文件到项目根目录了。

假设你的项目根目录是 /data/app/myproject/

方案一：利用python导入机制，自动import 有PYTHONPATH的文件夹下的配置文件。
   例如你在 /data/config_prod/ 放置 funboost_config.py ,然后shell临时命令行 export PYTHONPATH=/data/config_prod/:/data/app/myproject/,再python xx.py。 （这里export 多个值用：隔开，linux设置环境变量为多个值的基本常识无需多说。）
   这样就能自动优先使用/data/config_prod/里面的funboost_config.py作为配置文件了，因为import自动会优先从这里。
   然后在测试环境 /data/config_test/ 放置 funboost_config.py,然后shell临时命令行 export PYTHONPATH=/data/config_test/:/data/app/myproject/,再python xx.py。
   这样测试环境就能自动使用 /data/config_test/ 里面的funboost_config.py作为配置文件了，因为import自动会优先从这里。

方案二：
   直接在funboost_config.py种写if else，if os.get("env")=="test" REDIS_HOST=xx ，if os.get("env")=="prod" REDIS_HOST=xx ，
   因为配置文件本身就是python文件，所以非常灵活，这不是.ini或者 .yaml文件只能写静态的死字符串和数字，
   python作为配置文件优势本来就很大，里面可以写if else，也可以调用各种函数，只要你的模块下包含那些变量就行了。
```

### 6.18.5 多个ptyhon项目怎么使用同一个funboost_config.py 作为配置文件

```
还是因为不懂 PYTHONPATH 造成的，需要我无数次举例说明。 这样太low了，这么多python人员到现在还不知道 PYTHONPATH作用， python导入一个模块是怎么去查找的。
6.18 开头就说了 pythonpathdemo 项目连接，有的人不懂PYTHONPATH又不看这个博客。死猪不怕开水烫，永远不学习 PYTHONPATH 的强大作用。
```

```
假设你想每隔项目都使用 /data/conf/funboost_config.py 这一个相同的 funboost_config 作为配置文件，
你有两个python项目在  /data/codes/proj1  和   /data/codes/proj2，

你运行proj1的项目脚本前，只需要 export PYTHONPATH=/data/conf/:/data/codes/proj1   ，然后运行proj1项中的脚本 python dir1/dir2/xx.py

你运行proj2的项目脚本前，只需要 export PYTHONPATH=/data/conf/:/data/codes/proj2   ，然后运行proj2项中的脚本 python dir3/dir4/yy.py


因为你设置了/data/conf/ 为 pythonpath后，那么funboost在 import funboost_config 时候就能自动 import 到 /data/conf/下的 funboost_config.py 模块了。
funboost控制台都打印了 读取的是什么文件作为配置文件了。
归根结底问这个问题的人是完全不懂 PYTHONPATH.
```





## 6.19 定时任务或延时任务报错 RuntimeError: cannot schedule new futures after interpreter shutdown

```
如下图所示，运行定时任务或延时任务在高版本python报错，可以在代码末尾加个while 1:time.sleep(10)

因为程序默认是 schedule_tasks_on_main_thread=False，为了方便连续启动多个消费者消费，
没有在主线程调度运行，自己在代码结尾加个不让主线程结束的代码就行了。

在消费启动的那个代码末尾加两行  
while 1：
   time.sleep(10)
```
![img_27.png](img_27.png)



## 6.21 支不支持redis cluster集群模式的redis作为消息队列？

```
此框架没有实现操作redis集群模式，
但只要是celery能支持的中间件类型和redis模式，此框架都能支持。因为此框架支持kombu包操作消息队列。
此框架能够支持的中间件类型比celery只会多不会少，因为框架支持celery的依赖kombu操作各种消息队列。


在funboost_config.py 配置文件中设置 KOMBU_URL 的值了，如
KOMBU_URL = 'sentinel://root:redis@localhost:26079;sentinel://root:redis@localhost:26080;sentinel://root:redis@localhost:26081'

KOMBU_URL 的规则就是 celery的 broker_url的规则。KOMBU_URL支持多种消息队列，celery的broker_url能设置什么样，KOMBU_URL就能设置什么样，
网上大把的资料celery 配置各种broker_url 来操作如 mysql rabbimtq redis 作为消息队列。。

如下这么写，就能使用kombu包来操作各种消息队列了。

@boost(BoosterParams(queue_name="queue_namexx", broker_kind=BrokerEnum.KOMBU))
def add(a,b):
    print(a+b)
```

## 6.22 怎么使用tcp socket 作为消息队列
```
见 7.19章节，或者在文档的搜索框输入 tcp 或者 socket 就能搜到了。框架文档支持搜索。
git的 test_frame 文件夹的各种文件夹，是测试脚本也是学习脚本，测试各种中间件的都有。
```


## 6.23 安装包时候自动安装的三方依赖包太多？
```
1.安装第三方包是自动的，又不需要手动一个个指令安装，安装多少三方包都没关系。
2.所有三方包加起来还不到30M，对硬盘体积无影响。
3.只要指定阿里云pip源安装，就能很快安装完，30秒以内就安装完了，又不是需要天天安装。

如果如你的不一致报错终端,pip 命令加上  --use-feature=2020-resolver

pip install funboost -i https://mirrors.aliyun.com/pypi/simple/

4.三方包与自己环境不一致问题？

用户完全可以自由选择任何三方包版本。例如你的 sqlalchemy pymongo等等与框架需要的版本不一致，你完全可以自由选择任何版本。
我开发时候实现了很多种中间件，没有时间长期对每一种中间件三方包的每个发布版本都做兼容测试，所以我固定死了。

用户完全可以选择自己的三方包版本，大胆点，等报错了再说，不出错怎么进步，不要怕代码报错，请大胆点升级你想用的版本。
如果是你是用你自己项目里面的requirements.txt方式自动安装三方包，我建议你在文件中第一行写上 funboost，之后再写其它包
这样就能使用你喜欢的版本覆盖funboost框架依赖的版本了。
等用的时候报错了再说。一般不会不兼容报错的请大胆点。

5.为什么要一次性安装完，而不是让用户自己用什么再安装什么？
是为了方便用户切换尝试各种中间件和各种功能时候，不需要自己再亲自一个个安装第三方包，那样手动一个个安装三方包简直是烦死了。

2024 5月份,精简了依赖包,部分包改为选装, pip install funboost[all] 才安装全部中间件.

```

### 6.23.b 作者为什么不开发pip 选装方式?例如实现选装 pip install funboost[rabbitmq]
```
这个你是怎么知道funboost作者没有使用选装方式的? 你是怎么知道作者没有掌握 pip 中括号选装依赖包 技术方式的?
用户可以看看setup.py里面的 extras_require里面,有没有开发选装方式?  pip funboost[all] 才是安装所有依赖.
作者去掉依赖很容易,已经实现了, funboost/factories/broker_kind__publsiher_consumer_type_map.py 中的 regist_to_funboost 就是动态导入生产者消费者,很容易去掉各种三方包依赖,
但是很容易安装的三方包,我是不会去做成选装的,没有那个必要,自己设置pip 国内源,30秒就能安装完成funboost了,不需要去纠结这个依赖包多少的问题.
```

## 6.24 funboost框架从消息队列获取多少条消息？有没有负载均衡？
```
funboost 每个消费者进程会从消息队列获取 并发个数 n + 10 条消息，每个消费者实现有差异，一般不会超过并发数2倍。
所以不会造成发布10万条消息后，再a b机器启动2个消费，b机器一直无法消费，全部a机器消费，不会出现这种情况。

如果你只发布6条消息，先在a机器启动消费，下一秒启动b机器，那很有可能b机器无法获取到消息。只要消息数量够多，不会出现忙的忙死，闲的闲死。

例如框架的默认并发方式使线程池，内置了一个有10大小的界队列queue，同时还有n个并发线程正在运行消息，所以每个消费者会获取很多消息在python内存中。
但不会出现一个消费者进程获取了1000条以上的消息，导致站着某坑不拉屎，别的消费进程没办法消费的情况。


如果你是重型任务，希望不预取，每台机器只获取一条消息运行，可以设置并发模式为 SINGLE_THREAD 模式,
boost装饰器设置 concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD，这样在a b 两台机器都没有内存缓冲队列,只会一次获取一条消息执行，

有的broker_kind实现时候为了运行快，框架使用了批量拉取消息， 需要设置批量拉取的数量为1。

```

消费文件 test_frame\test_redis_ack_able\test_load_balancing_consume.py
```python

import logging
import time
from funboost import boost, BrokerEnum,BoosterParams,ctrl_c_recv,ConcurrentModeEnum


@boost(BoosterParams(queue_name='test_load_balancing', broker_kind=BrokerEnum.REDIS_ACK_ABLE,log_level=logging.INFO,
                     concurrent_mode=ConcurrentModeEnum.SINGLE_THREAD,
                     broker_exclusive_config={'pull_msg_batch_size':1}， #pull_msg_batch_size 这行很关键，REDIS_ACK_ABLE 因为默认是拉取100个消息，
                     # 对于重型任务，你需要每台机器都严格只运行一个消息，就需要设置批量拉取1个消息，不要一台机器就把消息队列掏空了。
                     ))
def test_load_balancing(x):
    print(x)
    time.sleep(1)

if __name__ == '__main__':
    test_load_balancing.consume()
    ctrl_c_recv()

```

发送消息文件 test_frame\test_redis_ack_able\test_load_balancing_consume.py
```python
from test_frame.test_redis_ack_able.test_load_balancing_consume import test_load_balancing


if __name__ == '__main__':
    for i in range(80):
        test_load_balancing.push(i)

```

启动2次消费文件，就能看到2个控制台，每个控制台每次只获取1条消息并运行，如果你不设置 pull_msg_batch_size，那么默认是批量拉取100个，而你总共才发布80个消息
所以你只能看到一个控制台消费，你误以为没有负载均衡。

如果你不设置 pull_msg_batch_size，那么就可以发布5000个消息来测试消费负载均衡，两个控制台就都会运行，因为默认批量拉取100个也不会一下子把5000消息都取到内存。



## 6.25 funboost消费启动后，按ctrl + c 无法结束代码？

```python
from funboost import  ctrl_c_recv
if __name__ == '__main__':
    # 启动消费
    consume_func.consume()
    ctrl_c_recv() # 在代码最末未加个 ctrl_c_recv() 
    
# 想结束代码就连续按3次 ctrl +c 就好了。 为什么是3次，是防止你误操作了ctrl + c


```

<div> </div>
# 7.更新记录

## 7.0 很小的更新，对api使用完全无变化或者无增加新功能的不写更新记录。

## 7.1 新增第十种Consumer，以redis为中间件，但增加了消费确认，是RedisConsumerAckAble类。

```
支持运行过程中，随意关闭和启动python程序。无惧反复关闭python和 突然断电导致任务丢失几百个。

之前开100线程/协程的话，随意重启python和断电会导致极大概率丢失200个任务。

官方Threadpoolexecutor是无界队列。使用这个会导致丢失无数个任务，
因为他会迅速把redis的消息全部取出来，添加到自己的queue队列慢慢消费。
因为这个原因所以需要自定义写BoundedThreadpoolexecutor和CustomThreadpoolexecutor。       

改版的CustomThreadpoolexecutor修改成了queue最大长度是max_works，自己内部存储100个，
运行中100个，突然关闭python会丢失200个任务。如果queue设置大小为0，则只会丢失100个运行中的任务。

采用的是消费者去除消息时候，用lua脚本同时pop和添加到unacked的独立zset中，函数运行成功后会从set中删除该任务。
同时有一个一直每隔5秒发送心跳到redis服务中的线程，心跳标识中有消费者的唯一标识，绝对不会重复。
如果突然关闭消费者（例如突然断电或者点击关闭python），那么该消费者的心跳将会停止了。这时其他机器的同队列消费者或者当前机器重新启动代码后，在15秒后会
检到被关闭的消费者是非活跃消费者，那么自动将该消费者的unack里面任务全部重新取出返回到待消费队列中。

RedisConsumerAckAble类比RedisConsumer会有一丝丝性能损耗，但python玩redis大部分情况还是python代码本身有性能瓶颈，
而不是造成redis服务端有性能瓶颈，一般只要用在有意义的业务上，就算python很忙把cpu占光了，也不会造成redis服务端达到极限，
python是性能很差的语言，没玩垮redis，自身就把电脑玩死了，所以大部分情况下不要在意加入确认消费后产生额外的对redis服务端的性能压力。

redis要是能直接作为mq使用，redis早就一统天下了，哪里还不断有几十种mq出来。
所以直接基于redis list的如果要做到可靠就必须改进。
```

## 7.2 新增基于以redis为消息中间件时候的页面管理和消费速度显示。

```
基于redisboard，但对redis的list模拟mq功能，进行页面显示优化突出消息队列消费，
加黄显示正在运行中的队列和每10秒的消费速度。每隔10秒自动刷新统计。

由于实时发布和消费，例如10秒内发布20个，消费50个，页面只能显示大小降低了30个，
这个只有专业的mq才能分别显示出来，redis list只是简单数组。

rabbitmq nsq都有官方自带速率显示。
```

![img_75.png](img_75.png)


## 7.3 新增一个10行代码的函数的最精简乞丐版实现的分布式函数执行框架.

新增一个10行代码的函数的最精简乞丐版实现的分布式函数执行框架，演示最本质实现原理，不要亲自这么使用。

beggar_redis_consumer.py文件的 start_consuming_message函数。

```python
def start_consuming_message(queue_name, consume_function, threads_num):
    pool = ThreadPoolExecutor(threads_num)
    while True:
        try:
            redis_task = redis_db_frame.brpop(queue_name, timeout=60)
            if redis_task:
                task_str = redis_task[1].decode()
                print(f'从redis的 {queue_name} 队列中 取出的消息是： {task_str}')
                pool.submit(consume_function, **json.loads(task_str))
            else:
                print(f'redis的 {queue_name} 队列中没有任务')
        except redis.RedisError as e:
            print(e)


def add(x, y):
    time.sleep(5)
    print(f'{x} + {y} 的结果是 {x + y}')


# 推送任务
for i in range(100):
    redis_db_frame.lpush('test_beggar_redis_consumer_queue', json.dumps(dict(x=i, y=i * 2)))

# 消费任务 
start_consuming_message('test_beggar_redis_consumer_queue', consume_function=add, threads_num=10)

```

看完整版代码很长很多，是由于控制功能太多，中间件类型多，并发模式多， 所以加入一个最精简版，精简版的本质实现原理和完整版相同。

## 7.4 新增sqlachemy 支持的数据库作为消息中间件

新增sqlachemy 支持的数据库作为消息中间件，包括sqlserver mysql postgre oracle sqlite

每个队列是一张表模拟的。

![img_76.png](img_76.png)

每个任务是表里面的一行记录。

![img_77.png](img_77.png)




## 7.5 日志改为导入独立包nb_log，支持用户配置文件自定义日志配置。

例如设置默认需不需要彩色，需不需要大背景彩色色块，需不需要自动拦截转化python内置的print.
在用户当前项目根目录下生成的nb_log_config.py 可以自定义优先日志配置。

## 7.6 优化qps控频。

```
将qps按范围分段，采用不同的等待或计数方式。使当qps设置很高的时候，控频更精确。

增加了分布式控频，需要依赖redis中间件。
分布式环境中的控频指的是，假如xx.py文件中有一个consumer，设置func函数的qps为10。
如果在线上部署了三个容器服务，如果不使用分布式控频，则func函数的每秒运行总次数会是30。
即使只有1台机器，如果开多进程，Process运行3个进程，或者把xx.py反复运行启动3个，
也会造成func函数每秒运行总次数是30。
分布式控频主要是解决这种问题。默认不使用分布式控频，
当设置 is_using_distributed_frequency_control为True的时候，使用分布式控频。

```


## 7.7 增加rocketmq支持。 (2020-7)

```python
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='queue_test_f03', qps=2, broker_kind=BrokerEnum.ROCKETMQ))
def f(a, b):
    print(f'{a} + {b} = {a + b}')


if __name__ == '__main__':
    for i in range(100):
        f.push(i, i * 2)
    f.consume()

```

## 7.8 新增 async 并发模式 (2020-12)

框架希望用户写同步函数，不鼓励用户新写async def的函数，如果你的代码函数已经写成了async def，可以用此种并发方式。

写async def的函数很烦人，asyncio里面的概念很难学。

这两个项目用的asyncio你能写出来，能看懂说明不？

[https://github.com/ydf0509/async_pool_executor](https://github.com/ydf0509/async_pool_executor)

[https://github.com/ydf0509/sync2asyncio](https://github.com/ydf0509/sync2asyncio)

```
之前一直都没支持这种并发模式，异步代码不仅消费函数本身与同步代码很多不同，例如函数的定义和调用以及三方库，
不同于gevent和eventlet打个猴子补丁就可以变并发方式并且代码保持100%原样，asyncio的方式代比同步码真的是要大改特改。
而且在框架层面要支持异步也要增加和修改很多，支持异步并不是很容易。这一点连celery5.0目前都还没支持到（据官方文档说5.0要加入支持，但目前的5.0.3还没加入。）

如果消费函数已经写成了async def这种，那么可以设置 concurrent_mode=ConcurrentModeEnum.ASYNC，
框架会在一个新的线程的loop里面自动运行协程，所有协程任务会自动在一个loop里面运行，不是每次临时都生成新的loop只运行一个当前任务方式。
```

```python

from funboost import boost, BrokerEnum, ConcurrentModeEnum, BoosterParams
import asyncio


# 此段代码使用的是语言级Queue队列，不需要安装中间件，可以直接复制运行测试。
@boost(BoosterParams(queue_name='test_async_queue2', concurrent_mode=ConcurrentModeEnum.ASYNC,
           broker_kind=BrokerEnum.LOCAL_PYTHON_QUEUE, concurrent_num=500, qps=20))
async def async_f(x):
    # 测试异步阻塞并发， 此处不能写成time.sleep(1),否则无论设置多高的并发，1秒钟最多只能运行1次函数。
    # 同理asyncio 不能和 requests搭配，要和 aiohttp 搭配。
    await asyncio.sleep(1)
    print(id(asyncio.get_event_loop()))
    # 通过 id 可以看到每个并发函数使用的都是同一个loop，而不是采用了愚蠢的临时 asyncio.new_event_loop().run_until_complete(async_f(x)) 方式调度。
    print(x)


if __name__ == '__main__':
    async_f.clear()
    for i in range(100):
        async_f.push(i, )
    async_f.consume()

```

### 7.8.2 gevent/eventlet 和 asyncio 用法区别感受

 ```
比方说汽车的自动挡和手动挡，学了手动挡一定会开自动挡，只学自动挡很难开手动挡。
asyncio方式的代码比正常普通同步思维的代码写法也要难得多了，能玩asyncio的人一定会用threading gevent，
但只用过threading gevent，不去专门学习asyncio的用法，100%是玩不转的。

gevent就像自动挡汽车，自动换挡相当于自动切换阻塞。
asyncio就像手动挡，全要靠自己写 await / async def /loop / run_until_complete /run_forever/ 
run_coroutine_threadsafe /wait / wait_for /get_event_loop / new_event_loop / get_running_loop
 ,写法很麻烦很难。异步多了一个loop就像手动挡汽车多了一个离合器一样，十分之难懂。

手动挡玩的溜性能比自动挡高也更省油。asyncio玩的溜那么他的io并发执行速度和效率也会更好，cpu消耗更少。
如果你写一般的代码，那就用同步方式思维来写吧，让分布式函数调度框架来替你自动并发就可以啦。
如果追求更好的控制和性能，不在乎代码写法上的麻烦，并且asyncio技术掌握的很溜，那就用asyncio的方式吧。 
```

### 7.8.3 关于 async 并发模式，为什么框架还使用 pyredis pika pymongo，而没有使用aioredis  aiomongo

```
异步鬓发模式里面，整个调用链路必须是一旦异步，必须处处异步，在base_consumer.py的AbstractConsumer中，
方法 _async_run_consuming_function_with_confirm_and_retry里面使用的还是操作中间件的同步库，

主要是因为框架目前支持15种中间件，一个一个的使用异步模式的库操作中间件来实现，比现在代码起码要增加80%，无异于重写一个项目了。
异步和同步真的写法语法相差很大的，不信可以比比aiomysql 和pymysql库，aiohttp和requests，如果非常简单能实现异步，
那aiohttp和aiomysql作者为什么要写几万行代码来重新实现，不在原来基础上改造个七八行来实现？



目前此库对 消息拉取和消息消费完全是属于在两个不同的线程里面，井水不犯河水，所以用同步库拉取消息对asyncio的消费函数没有任何影响，不存在同步库阻塞异步库的问题。
对于消息确认 消息重新入队 任务过滤  mongo插入，都是采用的同步库，但是使用了 run_in_executor,
把这些操作在异步链路中交给线程池来运行了，同事这个线程池不是官方内置线程池，是智能缩小扩大线程池 ThreadPoolExecutorShrinkAble。
run_in_executor 会把一个同步的操作，sumbit提交给线程池，线程池返回的是一个concurrent.futures包的Future对象，
run_in_executor包装转化了这个Future(此Future不是asyncio的，不是一个awaitable对象)成为了一个asyncio包的Future对象，asyncio的Future对象可以被await，
所以这是非常快捷的同步阻塞函数在异步链路中转同步转异步语法的最佳方式。官方也是这么推荐的。

除了框架内部的阻塞函数是run_in_executor快速转化成非阻塞事件循环的，但是主要的用户的消费函数，是使用的真async模式运行在一个loop循环中的，
也即是单线陈鬓发运行用户的异步函数。

其次框架的同步阻塞函数，都是操作中间件类型的库，异步就是 入队 确认消费 查询是否过滤，这些操作一般都会在1毫秒之内完成，不阻塞太长的事件，
即使不使用run_in_executor，直接在异步链路使用这些同步操作，也没太大问题。一旦异步必须处处异步，说的是不能调用耗时太长的同步阻塞函数，
1毫秒的无伤大雅，因为celery 1秒钟最多能调度300个 def f： print(hello) 这样的无cpu 无io的函数，此框架调度运行速度任然超过celery。

     

还有一种调度起 async def定义 的消费函数方式是继续开多线程并发，然后使用 临时loop = asyncio.new_event_loop()，loop.run_until_complete，这方式愚蠢了，
相当于只是为了运行起这个函数，但全流程丝毫没有丁点异步。
```

## 7.8.4 愚蠢的celery调用异步函数写法
```
下面截图这种写法为了异步而异步，非常废物滑稽的写法。
如果是celery多线程并发模式，那就是每个线程里面临时起一个loop，每个生成的loop只运行了一次协程成对象。这样完全没有利用到asyncio的优势
如果是celery多进程并发模式，那就是每个进程里面临时起一个loop，每个生成的loop只运行了一次协程成对象。这样完全没有利用到asyncio的优势

celery真正的最终目标是直接能把@task装饰器加到 一个asynnc def的函数上，而不是现在间接的再新增写一个同步函数来调用异步函数。
到目前为止的最新版 celery 5.2.3还没有实现 直接支持 asyncio 并发模式。
用户不要抱多大希望celery能很快支持asyncio，例如celery使用kafka做中间件，官方承诺了7年，一次次的放鸽子到现在还不支持，没那么容易。
```
![img_22.png](img_22.png)


## 7.9 2021-04 新增以 redis 的 stream 数据结构 为中间件的消息队列。

```
这个是 redis 的 真消息队列，这次是 真mq，
stream 数据结构功能更加丰富接近 rabbitmq kafka这种真mq的消息队列协议，比 list 做消息队列更强。
需要redis的服务端5.0版本以上才能使用这个数据结构。
代码文件在 funboost/consumers/redis_stream_consumer.py

这个 REDIS_STREAM 中间件和 REDIS_ACK_ABLE 都支持消费确认，不管客户端怎么掉线关闭，都可以确保消息万无一失。
BrokerEnum.REDIS 中间件 不支持消费确认，随意重启或者断电断线会丢失一批任务。
```

```python
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='queue_test_f01', broker_kind=BrokerEnum.REDIS_STREAM))
def f(a, b):
    print(f'{a} + {b} = {a + b}')


if __name__ == '__main__':
    for i in range(100):
        f.push(i, b=i * 2)
    f.consume()
```

## 7.10 2021-04 新增以 redis 的 list 为数据结构，但使用 brpoplpush 命令 双队列 作为中间件的消息队列。

此 brpoplpush 双队列方式 + 消费者唯一id标识的心跳检测，可以媲美 rabbitmq 的确认消费功能。

```
代码演示省略，设置broker_kind=BrokerEnum.RedisBrpopLpush就行了。 
@boost(BoosterParams(queue_name='queue_test_f01', broker_kind=BrokerEnum.RedisBrpopLpush))
```

## 7.11 2021-04 新增以 zeromq 为中间件的消息队列。

```
zeromq 和rabbbitmq kafka redis都不同，这个不需要安装一个服务端软件，是纯代码的。
zeromq方式是启动一个端口，所以queue_name传一个大于20000小于65535的数字，不能传字母。
```

消费端代码，启动消费端时候会自动启动 broker 和 server。

```python
import time
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='30778', broker_kind=BrokerEnum.ZEROMQ, qps=2))
def f(x):
    time.sleep(1)
    print(x)


if __name__ == '__main__':
    f.consume()

```

发布端代码

```python
from test_frame.test_broker.test_consume import f

for i in range(100):
    f.push(i) 
```

## 7.12 2021-04 新增以 操作kombu包 为中间件的消息队列

```
一次性新增操作10种消息队列,.但比较知名的例如rabbitmq redis sqlite3 函数调度框架已经在之前实现了。
使用方式为设置 @boost 装饰器的 broker_kind 为 BrokerEnum.KOMBU
在你项目根目录下的 funboost_config.py  文件中设置 
KOMBU_URL = 'redis://127.0.0.1:6379/7' 那么就是使用komb 操作redis。
KOMBU_URL = 'amqp://username:password@127.0.0.1:5672/',那么就是操纵rabbitmq
KOMBU_URL = 'sqla+sqlite:////dssf_sqlite.sqlite',那么就是在你的代码所在磁盘的根目录创建一个sqlite文件。四个////表示根目，三个///表示当前目录。
其余支持的中间件种类大概有10种，不是很常用，可以百度 google查询kombu或者celery的 broker_url 配置方式。

操作 kombu 包，这个包也是celery的中间件依赖包，这个包可以操作10种中间件(例如rabbitmq redis)，
但没包括分布式函数调度框架能支持的kafka nsq zeromq 等。


但是 kombu 包的性能非常差，如何测试对比性能呢？
可以用原生redis的lpush和kombu的publish测试发布
使用brpop 和 kombu 的 drain_events测试消费，对比差距相差了5到10倍。
由于性能差，除非是分布式函数调度框架没实现的中间件才选kombu方式(例如kombu支持亚马逊队列  qpid pyro 队列)，
否则强烈建议使用此框架的操作中间件方式而不是使用kombu。

可以把@boost装饰器的broker_kind参数 设置为 BrokerEnum.REDIS_ACK_ABLE 和BrokerEnum.KOMBU(配置文件的KOMBU_URL配置为redis)，
进行对比，REDIS_ACK_ABLE的消费速度远远超过 BrokerEnum.KOMBU，所以之前专门测试对比celery和此框架的性能，
差距很大，光一个 kombu 就拉了celery大腿很多，再加上celery的除了kombu的执行性能也很低，所以celery比此框架慢很多。
test_frame\test_celery 下面有celery的发布 消费例子，可以测试对比下速度，同样gevent 并发和redis中间件，
celery 执行 print hello 这样的最简单任务，单核单进程每秒执行次数过不了300，celery性能真的是太差了。

```

消费

```python
import time
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_kombu2', broker_kind=BrokerEnum.KOMBU, qps=5))
def f(x):
    time.sleep(60)
    print(x)


if __name__ == '__main__':
    f.consume()
```

发布

```python                 
from test_frame.test_broker.test_consume import f

for i in range(10000):
    f.push(i)
```

你项目根目录下的 funboost_config.py

```python
KOMBU_URL = 'redis://127.0.0.1:6379/7'
# KOMBU_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VIRTUAL_HOST}'
# KOMBU_URL = 'sqla+sqlite:////celery_sqlite3.sqlite'  # 4个//// 代表磁盘根目录下生成一个文件。推荐绝对路径。3个///是相对路径。
```

## 7.14 2021-04 新增以mqtt emq 作为消息中间件

例子，设置 broker_kind=BrokerEnum.MQTT

```python
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='mqtt_topic_test', broker_kind=BrokerEnum.MQTT))
def f(x, y):
    print(f''' {x} + {y} = {x + y}''')
    return x + y


for i in range(100):
    f.push(i, i * 2)

f.consume()
```

```
这个默认做成服务端不存储消息，mqtt中间件适合前后端实时交互的。可以直接绕开后端flask django 接口，不用写接口，
前端直接发任务到mqtt，后端订阅，后端完成后，发送结果到唯一任务的topic

当然也可以 前端订阅topic，前端发任务到python flask接口，flask接口中发布任务到rabbitmq redis等，
后台消费完成把函数结果发布到mqtt，mqtt推送给前端
```

```
此框架的消费做成了mqtt的共享订阅，例如启动多个重复的消费者脚本，不会所有消费脚本都去重复处理一个消息
```

## 7.15 2021-04 新增以 httpsqs 作为消息中间件

```
@boost(BoosterParams(queue_name='httpsqs_queue_test', broker_kind=BrokerEnum.HTTPSQS))
```

## 7.16 2021-04 新增支持下一代分布式消息系统 pulsar 。

```
@boost(BoosterParams(queue_name='httpsqs_queue_test', broker_kind=BrokerEnum.PULSAR))

在开源的业界已经有这么多消息队列中间件了，pulsar作为一个新势力到底有什么优点呢？
pulsar自从出身就不断的再和其他的消息队列(kafka,rocketmq等等)做比较，但是Pulsar的设计思想和大多数的消息队列中间件都不同
，具备了高吞吐，低延迟，计算存储分离，多租户，异地复制等功能，所以pulsar也被誉为下一代消息队列中间件

pulsar 的消费者数量可以不受topic 分区数量的限制，比kafka和rabbitmq 强。5年后会替代kafka rabbitmq。
 
```

```python
from funboost import boost, BrokerEnum, BoosterParams

@boost(BoosterParams(queue_name='test_pulsar_topic2', broker_kind=BrokerEnum.PULSAR, qps=1, broker_exclusive_config={'subscription_name':'funboost_g1'}))
def add(x,y):
    print(x+y)

if __name__ == '__main__':
    add.push(1,2)
    add.push(3,4)
    add.consume()

```

## 7.17 2021-04 新增延时运行任务,介绍见4.8


## 7.18 2021-09 新增 轻松远程服务器部署运行函数
```
框架叫分布式函数调度框架，可以在多台机器运行，因为消息队列任务是共享的。

我用的时候生产环境是使用 阿里云 codepipeline k8s部署的多个容器。还算方便。
在测试环境一般就是单机多进程运行的，用supervisor部署很方便。

所以之前没有涉及到多态机器的轻松自动部署。
如果要实现轻松的部署多台物理机，不借助除了python以外的其他手段的话，只能每台机器登录上然后下载代码，启动运行命令，机器多了还是有点烦的。
现在最新加入了 Python代码级的函数任务部署，不需要借助其他手段，python代码自动上传代码到远程服务器，并自动启动函数消费任务。
目前的自动化在远程机器启动函数消费，连celery都没有做到。

不依赖阿里云codepipeline 和任何运维发布管理工具，只需要在python代码层面就能实现多机器远程部署。
```


## 7.19 2021-09 新增 socket udp/tcp/http 消息队列，不需要安装消息中间件软件。


好处是不需要安装消息队列服务,就可以跨机器通信,详见4.35章节


## 7.20 2021-09 新增 支持 nats 高性能消息队列

用法一如既往，只需要修改broker_kind的枚举，并在 funboost_config.py 配置好 NATS_URL 的值就完了。

```python
@boost(BoosterParams(queue_name='test_queue66c', broker_kind=BrokerEnum.NATS))
def f(x, y):
    pass
```


## 7.21 2022-01  新增 @boost装饰器全局默认配置

boost装饰器没有亲自指定参数时候的全局默认值 ，用法见 4.15 章节 说明

## 7.22 2022-02 新增暂停消费功能

框架支持暂停消费功能和继续消费功能，用法见文档4.18

## 7.23 2022-04 消费者/boost装饰器 新增 broker_exclusive_config 参数
```
加上一个不同种类中间件非通用的配置,不同中间件自身独有的配置，不是所有中间件都兼容的配置，因为框架支持30种消息队列，消息队列不仅仅是一般的先进先出queue这么简单的概念，
```
可以看 4.20 章节

## 7.24 2022-04 新增用户 自定义记录消费状态结果函数钩子

可以通过设置 user_custom_record_process_info_func 的值为你的自定义函数，来记录消费状态及结果，用户可以自由发挥保存消费结果状态到任意地方

可以看 4.19章节

## 7.25 2022-04 新增用户灵活自由自定义扩展中间件和生产消费逻辑的功能

register_custom_broker 这个是增加的一种很强大的功能,用户可以自定义发布者和消费者，注册到框架中。boost装饰器就能自动使用你的消费者类和发布者类了。

可以看 4.21 章节

## 7.26 2022-07 新增内置以redis作为apscheduler存储的定时器，动态增删改查定时任务配置。

可以看4.4b章节的演示代码例子

## 7.27 2023-02 新增适配python 3.6-3.11所有版本

适配python 3.6-3.11所有版本

适配python 3.10 3.11 的asyncio并发模式，因为官方老是在新版本的asyncio模块，把asyncio的api入参改来改去的，现在适配了。


## 7.28 2023-02 新增 asyncio 语法生态下rpc获取执行结果

```
因为 async_result= fun.push() ，默认返回的是 AsyncResult 类型对象,里面的方法都是同步语法。
async_result.result 是一个耗时的函数， 解释一下result， 是property装饰的所以不用 async_result.result()
有的人直接在async def 的异步函数里面 print (async_result.result)，如果消费函数消费需要耗时5秒，
那么意味rpc获取结果至少需要5秒才能返回，你这样写代码会发生灭顶之灾，asyncio生态流程里面一旦异步需要处处异步。
所以新增了 AioAsyncResult 类，和用户本来的asyncio编程生态更好的搭配。
```

## 7.29 2023-03 新增死信队列
```
抛出 ExceptionForPushToDlxqueue 类型错误，消息发送到单独另外的死信队列中,查看文档 4.24.c 和 4.24.d 4.24.e 章节。
```

## 7.30 2023-03 新增支持ctrl + c 退出程序 

因为程序是多个子线程while 1的，ctrl+c无法结束程序。 现在框架增内部增加了下面的代码了，可以支持ctrl+c结束程序了。

```python
def _interrupt_signal_handler(signal, frame):
    print('你按了 Ctrl+C  。 You pressed Ctrl+C!  结束程序！')
    # sys.exit(0)
    # noinspection PyUnresolvedReferences
    os._exit(0)  # os._exit才能更强力的迅速终止python，sys.exit只能退出主线程。


signal.signal(signal.SIGINT, _interrupt_signal_handler)
```

看4.6.5章节的演示代码例子


## 7.31 2023-04 新增支持 celery 作为 broker。

```
完全由celery框架来调度函数，发布函数和发布消息都是由celery框架来完成，但是用户无需学习celery语法和celery烦人的配置方式和烦人的celery目录结构，
用户对celery.Celery对象实例完全无需感知，用户不需要学习celery命令行启动消费和定时，funboost帮你自动搞定这些，用户无需接触celery命令行。

有的人担心funboost调度执行不稳定，有的人不对比瞎质疑funboost性能没有celery强，那么可以使用celery作为funboost中间件。
funboost只充当发布和启动消费的一层api，内部由celery驱动。 

funboost的好处是兼容30种消息队列或者叫ptython包，一统使用这些三方包的行为。用户切换中间件成本很低，无需知道每种中间件的语法差异。
就像sqlachemy能操作5种数据库，用户不需要知道mysql和sqlserver语法差异一样。

```

```
使用celery作为中间件，用户需要在 funboost_config.py  配置
CELERY_BROKER_URL（必须） 和 CELERY_RESULT_BACKEND （可以为None）
```

```python
from funboost import boost, BrokerEnum, BoosterParams
@boost(BoosterParams(queue_name=queue_1, broker_kind=BrokerEnum.CELERY))
```
python例子见 11.1章节

##  7.32 2023-04 新增支持 python 微服务框架 nameko 作为 broker。

```
nameko 是 外国人用的多的最知名python微服务框架，使用eventlet并发

funboost支持nameko作为执行调度和rpc实现，funboost只是提供统一的api交互。
```

```python
from funboost import boost, BrokerEnum, ConcurrentModeEnum, BoosterParams
@boost(BoosterParams(queue_name='test_nameko_queue', broker_kind=BrokerEnum.NAMEKO, concurrent_mode=ConcurrentModeEnum.EVENTLET))
```

python例子见 11.2 章节


## 7.33 2023-05 优化了apscheduler定式框架的动态删除添加定时任务

FsdfBackgroundScheduler 继承重写了BackgroundScheduler的 _main_loop 方法。

```python
class FunboostBackgroundScheduler(BackgroundScheduler):
    def _main_loop(self):
        """原来的_main_loop 删除所有任务后wait_seconds 会变成None，无限等待。
        或者下一个需要运行的任务的wait_seconds是3600秒后，此时新加了一个动态任务需要3600秒后，
        现在最多只需要1秒就能扫描到动态新增的定时任务了。
        """
        MAX_WAIT_SECONDS_FOR_NEX_PROCESS_JOBS = 1
        wait_seconds = None
        while self.state == STATE_RUNNING:
            if wait_seconds is None:
                wait_seconds = MAX_WAIT_SECONDS_FOR_NEX_PROCESS_JOBS
            time.sleep(min(wait_seconds,MAX_WAIT_SECONDS_FOR_NEX_PROCESS_JOBS))  # 这个要取最小值，不然例如定时间隔0.1秒运行，不取最小值，不会每隔0.1秒运行。
            wait_seconds = self._process_jobs()
```

## 7.34 2023-05 重新实现了boost装饰器

对于一个呗@boost装饰的函数，到底应该怎么称呼它？

之前叫消费函数，消费函数是指的是boost装饰后的还是 原始函数本身，称呼不太明确。

之前的boost装饰器是使用函数来实现的，没有类型，现在的boost装饰器使用类来实现，一个函数被 boost装饰后，类型是 Booster,现在有类型了。


```
之前的boost装饰器是一个函数，在被装饰的函数 fun 本身附加consumer和publisher对象，以及各种方法。
返回的还是函数本身，但是附加了各种方法，方便用户 fun.push()  fun.consume() fun.get_message_count() 等等。
为了代码在pycahrm下补全犀利，还加了类型注释，boost的返回值指向一个为了补全犀利而写的 IdeAutoCompleteHelper类。

修改后的boost就是Booster类，现在boost返回的是 Booster类型的对象，补全效果很好。
对funboost的功能pycharm自动补全和函数本身的入参pycharm自动补全都很好。去掉了为了补全而写的 IdeAutoCompleteHelper。

现在一个函数被boost装饰后，他的类型就变成Booster了，可以称此函数为一个booster了。
```

重构之后的boost装饰器实现代码：
[https://github.com/ydf0509/funboost/blob/master/funboost/core/booster.py](https://github.com/ydf0509/funboost/blob/master/funboost/core/booster.py)

重构之前的boost装饰器实现代码：
[https://github.com/ydf0509/funboost/blob/e299606a7271e24cae8dea7b9cbbcc400a4f4b0b/funboost/__init__old.py](https://github.com/ydf0509/funboost/blob/e299606a7271e24cae8dea7b9cbbcc400a4f4b0b/funboost/__init__old.py)



## 7.35 2023-06 新增支持优先级队列

[funboost支持任务优先级队列](https://funboost.readthedocs.io/zh-cn/latest/articles/c4.html#id29)


见文档4.29

## 7.36 2023-07 新增支持 funboost远程杀死任务

[funboost远程杀死任务](https://funboost.readthedocs.io/zh-cn/latest/articles/c4.html#id35)

见文档4.30

## 7.37 2023-07 新增所有命名空间的日志和print都另外写入到一个总的文件中。

```
之前的funboost日志，每个命名空间的日志写入到不同的文件，每个队列名的消费者和发布者都有独立的日志命名空间，写入到不同的文件中,是为了用户方便排查。

例如你查func2的报错和运行记录，只需要到那个func2消费者.log的文件中去排查，这个文件日志不会包含别的消费函数的运行记录。

但有的人希望是项目中的所有日志 + print 写入到一个相同的文件中，方便排查上下文，这个几乎相当于 nohup 部署然后重定向标准输出到一个文件中了。
现在python代码级别对print和sys.stdout sys.stderr打了猴子补丁，支持所有print和logger打印另外写入到一个单独的文件中了。这是nb_log的新功能。
```

见nb_log文档 [https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c10.html](https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c10.html)

10.1章节和1.1章节里面介绍了，怎么修改是否另外所有日志和print再单独写入到一个总的日志文件中。

## 7.38 2023-10 多线程并发模式，增加了支持async def的函数

对于async def 的函数，不需要boost装饰器指定 concurrent_mode=ConcurrentModeEnum.ASYNC ，每个线程内部会临时 loop= asyncio.new_event_loop(),
然后loop.run_unyil_cpmplete来运行async def的函数。

这种情况下 每个协程是运行在不同的loop中，这是假asyncio变成。

如果你想每个协程运行在一个loop里面，那就需要 boost装饰器指定 concurrent_mode=ConcurrentModeEnum.ASYNC，这是真asyncio编程。




## 7.39 2024-01 @booost装饰器入参变成pydantic Model类型, BoostParams类或子类 

@boost(queue_test_f01', qps=0.2,broker_kind=BrokerEnum.REDIS_ACK_ABLE,) 

建议把所有传参变为放在BoosterParams类或子类里面:

@boost(BoosterParams(queue_name='queue_test_f01', qps=0.2,broker_kind=BrokerEnum.REDIS_ACK_ABLE,))



## 7.40 2024-03 函数运行状态页面增加消息运行中状态

之前是只有消息运行完成后才会显示这条消息，运行中的消息不会显示，现在新增 running 状态的消息。


![函数状态3.png](%BA%AF%CA%FD%D7%B4%CC%AC3.png)


## 7.41 2024-03 新增 funboost_current_task 上下文

之前无法在用户的消费函数内部去获取消息的完全体,只能知道函数的入参,无法知道消息的发布时间 taskid等.

上下文就是类似flask的request对象,线程中任意地方可以获取,线程/协程隔离.

```
用户在任意消费函数中 
fct = funboost_current_task()
就能获取当前的任务消息了。

这个功能使得用户在用户函数中就能知道消息的完全体、 当前是哪台机器 、哪个进程、 第几次重试运行函数
消息的发布时间  消息的task_id 等等。

原来用户在消费函数中是无法获取这些信息的。

见文档4.31
```

详见文档4.31

## 7.42 2024-04 新增支持消费函数定义入参 **kwargs,用于消费任意json消息

见文档 4b.2 章节介绍.

## 7.43 2024-05 新增另外一种方式来 自定义增加或重写 消费者 发布者

见文档 4.21b 章节介绍

boost装饰器 传参 consumer_override_cls 和 publisher_override_cls 来自定义或重写消费者 发布者。

## 7.44 2024-06 重磅升级！funboost 支持实例方法、类方法、静态方法、普通函数 4种类型，作为消费函数的例子

funboost 在 2024年6月新增支持了实例方法、类方法作为消费函数 ，写法见文档4.32章节

## 7.45 2024-08 @boost入参新增 is_auto_start_consuming_message，定义后立即自动启动消费。

```
@BoosterParams(queue_name="q1",  is_auto_start_consuming_message=True)
def f(x):
这样写后，自动启动消费，不需要 用户手动的写  f.consume() 来启动消费。
```

代码例子见4.33章节

## 7.46 2024-08 修复使用redis心跳来辅助确认消费的redis中间件模式，重复消费的bug
```
用户的 broker_kind 如果是这四种 [BrokerEnum.REDIS_ACK_ABLE, BrokerEnum.REDIS_STREAM, BrokerEnum.REDIS_PRIORITY, BrokerEnum.RedisBrpopLpush] 
用户需要升级到 46.2, 如果不想升级就需要手动指定 @boost(BoostParams(is_send_consumer_hearbeat_to_redis=True))

用户如果使用的是 BrokerEnum.REIDS 和 BrokerEnum.REIDS_ACK_USING_TIMEOUT 不受影响，因为不使用redis心跳来辅助确认消费。
```

![](https://visitor-badge.glitch.me/badge?page_id=distributed_framework)
<div> </div>

## 7.47 2025-01 加强了 funboost web manager 功能

具体看文档13章节。

## 7.48 2025-07 消费函数的入参类型可以是自定义类型对象(不可json序列化的类型)

以前作者不愿意支持消费函数入参是自定义类型,2025-07 之后支持了,不愿意支持的原因可以看文档第6章.

就是现在消费函数的入参可以是 字符串 数字 列表 字典 以外的自定义类型,    
def func1(a:MyClass,b:str,c:MyPydanticModel)  现在可以.


# 8.用于爬虫



## 8.0 funboost 用于爬虫前序

先开门见山：

**Scrapy 是 URL 调度器，funboost 是函数调度器；前者束缚你，后者赋能你。**

**Funboost 是“写函数就能爬虫”，Scrapy 是“写框架才能爬虫”。**

### 8.0.1 tips : 202309 新增boost_spider爬虫框架
<pre style="color: orangered;font-size: small">


pip install boost_spider

boost_spider基于funboost,新增了一个RequestClient类(更适合爬虫的请求类,能自定义扩展代理请求方法),
和 更方便的保存到各种数据库.

</pre>

boost_spider地址: 
[https://github.com/ydf0509/boost_spider](https://github.com/ydf0509/boost_spider)

使用boost_spider的代码例子: 
[https://github.com/ydf0509/boost_spider/blob/main/tests/car_home_spider.py](https://github.com/ydf0509/boost_spider/blob/main/tests/car_home_spider.py)

### 8.0.2 funboost 降维打击仿scrapy api爬虫框架
你本来只想用Scrapy爬个网页，结果遇见了Funboost

这就像你本来是想乘坐 木柴蒸汽机，结果直接坐上了量子驱动星际战舰 。 

scrapy写爬虫仪式感代码文件太多，是为了吃个鸡蛋，要先盖个养鸡场。funboost是让你直接开吃。

因为99%爬虫框架是情不自禁仿scrapy api ，是 基于 yield Request(url=url_xx,callback=my_parse) 的请求调度框架，扩展相当复杂和难，扩展难、调试难、维护难，难上加难，难到你想转行。

funboost 暴击 scrapy api框架，本质是 自由编程 降维打击 框架奴役。


**scrapy的时代正在成为过去式**
scrapy的设计哲学诞生于一个需要“框架来定义一切”的时代,这在今天看来，反而成了一种束缚。

**funboost代表了更现代、更高效的开发范式：**
<pre style="color: #00ff00;background-color:black ;font-size: large;">
funboost 相信开发者的能力，只提供最强大的调度核心，将业务逻辑的自由完全交还给用户。
它的学习成本极低，但能力上限极高，无论是写一个几行代码的临时爬虫，还是构建一个需要数百台机器的庞大采集系统，它都能轻松胜任。
它更可靠、更灵活、更符合Pythonic的编程直觉。
</pre>

<pre style="color: red; background-color:black ;font-size: medium;">
funboost 让你可以专注于“解决问题”，而 Scrapy 却常常让你把时间花在“解决框架本身的问题”上。作为追求效率和优雅的工程师，选择 funboost 是一个显而易见的决定。
</pre>

#### funboost 太省时间
👉 Scrapy: "请继承我的Spider类，重写parse方法，配置settings，注册中间件，添加Pipeline..."

Funboost: "加个@boost，你随便写，我全搞定！"

警告⚠️：使用Funboost可能导致严重的空闲时间过剩，请提前规划假期！

#### @boost 一键赋能你的函数，功能远超爬虫框架

funboost的@boost装饰器给你的函数赋能，自动调度你的函数，使你的函数自动具备 分布式、断点接续运行、随意重启代码万无一失消费确认、基于函数入参的任务过滤、函数入参有效期过滤、消息过期丢弃、并发种类(线程/协程)设置、并发数量设置、qps限制、全局分布式qps控频、函数出错自动重试、funboost web manager 消费可视化监控、 装饰器自带内置一键入库持久化保存函数结果 、定时运行 , 这些功能不比爬虫框架的功能更多更强吗？

funboost 轻松一键 多线程/协程  叠加 多进程 ，再叠加多机器，可以轻松做到跑满几百台机器的所有cpu核心，性能非常炸裂，有哪个爬虫框架能一键轻松做得到。

#### 有人怀疑 funboost没有http请求中间件，这恰好是对scrapy的最大优势


反爬对比：

Scrapy方式：学习中间件理论→阅读源码→理解生命周期→尝试实现→调试失败→怀疑人生→放弃→回去用requests

Funboost：代码少70%，效率高1000%，头发多10000%！

```
对于有人怀疑funboost没对爬虫专门优化，所以肯定不如专用爬虫框架scrapy， 
认为 scrapy 中能写 http请求 middware 来换ip和 user-agent ，所以是scrapy有优势；这是大错特错的想法。
真实情况是在scrapy api框架中 换 ip 和 user-agent ，你得先精通scrapy 爬虫生命周期和  中间件机制的固定套路写法，
才能写正确scrapy的middleware。

而funboost不插手你怎么发请求， 小白用户使用 最简单直观的面向过程 思维，你在你自己项目的utils文件夹下，
基于requests 定义一个 不到10 行的 通用复用的my_request 的请求函数就能完成换ip和请求头了，完全是0门槛。
例如:


import requests
def my_request(method,url):
    proxy = random.choice(proxy_list)
    user_agent = random.choice(user_agent_list)
    return requests.request(method,url,proxies=proxy,headers={'user-agent':user_agent})


定义这个 my_request 函数，这不比你在scrapy定义 http middware 简单几百倍 自由几百倍吗？
requests随便用，httpx随便用，aiohttp随便用，selenium  playwright 随便用，你想怎么玩就怎么玩。

你只要在 所有funboost的消费函数中始终使用 my_request 来发请求，那 funboost 不就能从万能函数调度框架，
摇身一变成了你的专属爬虫框架了吗？
当你还在吭哧吭哧学习scrapy的中间件机制时候，别人已经用funboost的一个装饰器解决了所有问题。

如果你使用boost_spider框架的RequestClient来发请求，他的response响应上自带了re和xpath css等方法，
所以你无需羡慕scrapy的response自带xpath方法了，无需纠结requests包的response不内置自带xpath方法了，
这个细节并不是很重要，你自己也很容易实现。
```

#### funboost能轻松自然完成，而scrapy无法完成的爬虫场景1，浏览器多轮交互
```
例如使用 selenium 浏览器渲染页面，并且是需要和浏览器多轮交互，包括 输入文字 -> 点击按钮1 -> sleep等待10秒 -> 
再根据内容的具体的值 -> 判断点击按钮2还是按钮3 -> 等待元素 element_id_xx 出现 -> 再提取解析网页内容，


因为这个场景下是不仅使用了浏览器渲染url，还需要多轮交互和判断, 这在scrapy下完全无能为力。


使用scrapy时候，只有 单线程同步勇士 在 parse 解析方法里面去操作浏览器才能非常勉强实现得了，
但是这把scrapy的twisted异步非阻塞弄成了一个废物，几乎把scrapy框架退化成单线程阻塞执行。
只有 代码界的扫地僧 才能把浏览器操作也异步化，yield 一个特殊的 Request 或 Item，等待浏览器服务处理完毕后通过某种回调机制，
将结果返回给 Scrapy 的流程中。但是这种方式实现起来非常复杂，需要精巧的架构设计和对 Scrapy 内部机制的非常深入精通，
高级python开发工程师都无法做到，只有欧美资深python框架架构师才能做得到。


然而，这个场景在 funboost 下来完成却十分简单直接自然的轻松搞定，你仅仅需要在你的函数里面像平常一样
非常自然的写操作浏览器代码。因为你的函数就是个黑盒，funboost能自动并发完成调度执行任意函数。
```

**scrapy实现很困难，但funboost实现很丝滑的，见文档8.9章节的token有效期很短的场景2**

#### 总结下funboost和scrapy在小项目和大项目：

1、小型爬虫：funboost单文件搞定，不像scrapy要你在七八个文件来回切换写代码。你的爬虫函数验证正确后，
加个@boost装饰器就自动并发调度了。就算是单机小爬虫，funboost也可以选择sqlite中间件帮你断点续爬。

2、大型爬虫：funboost的各种控制功能更丰富更强，funboost的轻松一键 多线程/协程  叠加 多进程 ，再叠加多机器，性能吊打scrapy。
funboost各种控制功能多到你数不过来。

3、适用范围：scrapy做得到的，funboost一定能更轻而易举做得到； funboost能轻松做得到的，scrapy则复杂到突破天际也无法做得到。

### 8.0.3 讨scrapy檄文：Funboost兴，Scrapy亡，天下爬虫，当顺天命！


**夫程序之道，贵在通达！爬虫之术，胜在调度！**    
昔有Scrapy窃据神器，挟Twisted之技而令诸侯，然其框架繁苛，回调如狱，岁月更迭，其势已衰，其道已孤，弊病丛生，开发者苦之久矣！    
今有Funboost，顺天应人，聚函数神力，携`@boost`之雷霆，以大道至简之义，破枷锁，扫陈规，伐无道，正本清源，布告天下！此诚不可逆之大势也！ 

**Scrapy十败如山崩，Funboost十胜如日升：**      
然吾观其根基，十败已定！    
吾FunBoost十胜在手，当为天下主！   


一曰：**道失对道胜！**  
Scrapy以URL为心，`Request`为锁，画地为牢，框架奴役，此谓 **"作茧自缚折云翅"**！  
Funboost以函数为本，万物皆可调度，自由挥洒，赋能无限，此谓 **"道法自然贯星河"**！

二曰：**繁失对易胜！**  
Scrapy项目冗杂，文件七八，层峦叠嶂，初学望而生畏，此谓 **"学海无涯苦作舟"**！  
Funboost一`@boost`统领，化繁为简，片刻上手，举重若轻，此谓 **"大道至简一点通"**！

三曰：**力失对能胜！**      
Scrapy并发受限，多核难尽其用，遇Selenium则异步变同步，英雄气短，此谓 **"单骑难陷万军阵"**！  
Funboost线程协程，进程机器，四重并发裂苍穹，千机万核竞驰骋，此谓 **"力拔山兮气盖世"**！

四曰：**估失对准胜！**     
Scrapy仅控并发，QPS随缘而定，精准控频如水中捞月，此谓 **"盲人射马失准的"**！  
Funboost令牌桶在握，QPS量沙准刻，分布式亦能令行禁止，此谓 **"运筹帷幄控毫厘"**！

五曰：**乱失对明胜！**       
Scrapy回调嵌套，逻辑支离破碎，`meta`传参如雾里看花，调试追踪九曲回肠，此谓 **"回调地狱不见天"**！  
Funboost平铺直叙，代码如行云流水，函数形参IDE烛照，逻辑一气呵成，此谓 **"银河直下三千尺"**！

六曰：**虚失对固胜！**        
Scrapy断点堪忧，重启则任务灰飞烟灭，断点续爬如镜花水月，此谓 **"大厦将倾一木难"**！  
Funboost消息确认，持久队列作金城汤池，宕机重启岿然不动，万无一失，此谓 **"稳坐钓台风浪平"**！

七曰：**斥失对容胜！**       
Scrapy旧码难容，迁移需重塑筋骨，大动干戈，劳民伤财，此谓 **"削足适履两相难"**！  
Funboost海纳百川，老树亦能发新枝，已有函数皆可加持，立等可用，此谓 **"万川归海终不弃"**！

八曰：**梏失对活胜！**       
Scrapy自定义反爬，中间件如天堑难越，非精通其道者不能为，此谓 **"画虎不成反类犬"**！  
Funboost封装请求，自由定义如探囊取物，换IP、UA、破解JS信手拈来，此谓 **"随心所欲不逾矩"**！

九曰：**拙失对巧胜！**    
Scrapy遇奇巧需求，如Token短时效、多轮浏览器交互，则束手无策，左支右绌，此谓 **"黔驴技穷无新声"**！  
Funboost函数之内，连续操作迅雷不及，状态管理自然天成，轻松驾驭复杂流程，此谓 **"灵心胜算巧夺天"**！

十曰：**晦失对捷胜！**       
Scrapy单元测试如扛泰山，调试艰涩，错误排查如大海捞针，此谓 **"雾锁津迷途难返"**！   
Funboost单函数直刺要害，调试若烹小鲜，IDE相助如虎添翼，可测性无出其右，此谓 **"拨云见日捷报传"**！

**有此十胜，Funboost伐Scrapy，如金狮搏兔，如高屋建瓴，何愁不克？！**        
Scrapy老将，若迷途知返，弃旧从新，尚可重焕生机；若固执己见，负隅顽抗，必为时代洪流所淘汰！

**今Funboost大旗已立，携函数调度之利刃，集分布式并发之雄兵：**        
东纳Requests之勇，西引HTTPX之锐；南征Selenium之坚，北抚Playwright之奇！     
聚Redis、RabbitMQ、Kafka为粮草，合多进程、多线程、协程为三军！ 


**天下英雄，当明辨是非，顺势而为！**    
弃Scrapy之糟粕，取Funboost之精华！    
开发者再不必叩拜Spider宗庙，亦无需忍受回调地狱之煎熬！   
此乃爬虫之文艺复兴，调度之工业革命！       
**剑锋所指，框架枷锁必将斩断！函数光辉，普照四海！**    

**与诸君共勉，开创万物皆可Boost之盛世！**      

**FunBoost大都督，布告天下！**    




### 8.0.4 很多人问这个框架能不能爬虫？

答：此框架不仅可以对标celery框架，也可以取代scrapy框架。

无论是比 自由度、兼容常规代码程度、用户需要编写的实际代码行数、消息万无一失可靠度、对爬虫的qps频率/并发控制手段、超高速调度请求， 此框架从以上任何方面远远超过scrapy，一切都是只会是有过之而无不及。



<pre style="color: #2e8ece;font-size: small">
应该还是主要是很浮躁，不仅没看详细文档，应该是连简介都没看。
分布式函数调度框架，定位于调度用户的任何函数，只要用户在函数里面写爬虫代码，就可以分布式调度爬虫，并且对爬虫函数施加20种控制功能,
例如 qps恒定 任何时候随意关机重启代码消息万无一失确认消费 非常简单的开启多进程叠加线程/协程,这些强大的功能绝大部分爬虫框架还做不到。

此框架如果用于爬虫，不管从任何方面比较可以领先scrapy20年，也比任意写的爬虫框架领先10年。
不是框架作者代码编写实力问题，主要是思维问题，爬虫框架一般就设计为url请求调度框架，url怎么请求都是被框内置架束缚死了，
所以有些奇葩独特的想法在那种框架里面难以实现，需要非常之精通框架本身然后改造框架才能达到随心所欲的驾驭的目的。
而此框架是函数调度框架，函数里面可以实现一切任意自由想法，天生不会有任何束缚。
主要还是思想问题，国内一般人设计的爬虫框架都是仿scrapy api，天生不自由受束缚。
</pre>


### 8.0.5 为什么 funboost 用来爬虫时候，扩展性简单性 远超 scrapy api式的一众传统爬虫框架？
```
funboost 扩展很容易，因为funboost是调度一个函数，不是调度一个url请求，用户可以在函数内部无拘无束实现任何想法，
不用顾忌思考怎么和funboost适配，用户在函数内部想写什么是天生更自由的。  
比如用户想使用哪种 http请求包发请求，想使用什么三方包包来解析html，想把爬虫数据保存到什么类型的数据库，
怎么使用不同供应商的代理ip ，用户完全自主发挥，而不用思考和funboost框架本身怎么适配。

funboost 在易扩展性方面的一个显著优势，尤其是在与那些结构更固化的框架（如专门的爬虫框架）进行对比时。

核心原因正如所指出的： funboost 调度的是函数，而不是特定的操作（如 URL 请求） 。

这带来了几个关键的好处，使得在函数内部的扩展和定制变得非常容易：

1. 函数即"黑盒" : 对于 funboost 调度器来说，被 @boost 装饰的函数在很大程度上是一个"黑盒"。 
   funboost 负责触发这个函数的执行（根据队列消息或定时设置）、管理并发、处理重试等，但它 不关心函数内部具体做了什么 。

2. 完全的内部自由度 : 在这个函数"黑盒"内部，开发者拥有完全的自由：
   - HTTP 请求 : 你想用 requests , httpx , aiohttp ，或者任何其他 HTTP 客户端库都可以， funboost 不会干涉。
   - HTML/数据解析 : 使用 lxml , beautifulsoup4 , parsel , json , re 或任何你喜欢的解析库，完全没问题。
   - 数据存储 : 直接调用 pymongo , redis-py , psycopg2 , mysql-connector-python , sqlalchemy , dataset
     等库将数据存入 MongoDB, Redis, PostgreSQL, MySQL 或其他任何数据库/文件系统。
   - 代理 IP : 对接任何代理 IP 服务商的 API 或 SDK，实现复杂的代理切换逻辑。
   - 任何业务逻辑 : 在函数内部可以编写任意复杂的 Python 代码，调用其他模块、类，实现你的业务需求。
3. 无需适配框架内部机制 : 因为 funboost 不强制规定函数内部的实现方式，所以你不需要去学习和适配 funboost 内部
   可能存在的特定请求对象、响应对象、Item 结构或 Pipeline 接口（除非像 boost_spider 这样在上层做了封装）。你只需要编写标准的 Python 代码即可。
   
总结来说：
funboost 的这种设计哲学，将 任务调度 与 任务执行的具体实现 解耦开来。它提供了一个强大的、通用的函数调度平台，
而将函数内部的实现细节完全交给了开发者。这种模式极大地降低了在 任务逻辑层面 进行扩展和定制的复杂度，
让开发者可以"无拘无束"地使用整个 Python 生态系统来实现功能，而无需过多考虑与调度框架本身的适配问题。这确实是它易用性和灵活性的一大体现。
```

funboost在处理特殊奇葩需求时确实远超scrapy这类API式框架，主要体现在：
```
处理复杂流程的能力：
funboost允许在单一函数中编写完整业务逻辑
scrapy需要拆分为多个回调，使复杂流程变得支离破碎

状态管理简洁度：
funboost可使用普通Python变量保存状态
scrapy需要通过meta字典在请求间传递，容易出错

特殊时序要求处理：
funboost可精确控制请求发送时机
scrapy受调度器影响，无法保证确切执行时间

条件逻辑和分支：
funboost支持自然的if/else/for/while等控制流
scrapy需要通过不同回调和meta实现，极度复杂化

异常处理方式：
funboost可使用标准try/except处理整个流程
scrapy各回调间异常隔离，难以统一处理

资源释放与清理：
funboost支持with语句和上下文管理
scrapy在分散的回调中难以管理资源生命周期

调试和问题排查：
funboost代码线性执行，容易跟踪
scrapy回调跳转使调试变得困难

与外部系统集成：
funboost可在任何点与外部API交互
scrapy需要特殊中间件或信号处理

对于要求精确控制、复杂交互、特定时序或依赖外部系统的"奇葩需求"，funboost的流程式编程模型确实具有压倒性优势，能够以更直观、更可靠的方式实现这些复杂需求。
```


此框架如果用于写爬虫，建议的写法是一种页面(或者接口)对应一个函数,例如列表页是一个函数，详情页是一个函数。 1个函数里面只包括一次请求(也可以两三次请求，但不要在函数本身里面去for循环遍历发十几个请求这种写法)，

### 8.0.6 主动集中简要回答驳斥一些scrapy 优势更大的观点

知道有些人会质疑说scrapy爬虫更好，有些人举的scrapy更强的例子，喜欢以卵击石，以弱击强，倒反天罡，必须集中统一回答反驳。

**你质疑funboost 没有 http middware ？**
```   
答：上面已经回答了，用户手写定义一个通用的 my_request 更强更自由更简单。
```

**你质疑funboost 没有 pipeline，质疑保存数据麻烦？**
```    
答：用户可以自己封装一个保存字典到数据库的函数， 最简单就是使用dataset知名包 一行代码就能保存字典到数据库了。
```

**你说Scrapy 插件生态丰富，质疑Funboost 没有三方包插件生态不够？**

`funboost` 不需要任何插件,是无招胜有招.
     
scrapy插件多是“病”，不是“药” 。Python pypi生态就是funboost的生态，funboost不需要各种funboost-xx的三方包插件。       
说插件多就是生态好，这么想法的人简直是没长脑子，用户已经会了三方包的使用，但在scrapy框架下，为什么还需要等专门的美国编程大神去给三方包开发插件适配scrapy框架的生命周期和组件流程，才能在scrapy中愉快的使用三方包。用户压根没想过这个问题。

详细的驳斥看文档8.14.2章节

Scrapy 插件多 ≠ 框架强，恰恰说明了框架对用户自由的压制太多，“什么都得经过官方那一套”。          
Funboost 是函数式的框架，自由度高、无约束、无钩子、无上下文依赖，天然就能融合任何三方库，python三方包生态就是funboost的生态，funboost不需要学 scrapy-redis scrapy-selenium scrapy-playwright  scrapy-user-agents  scrapy-splash 专门开发各种 funboost-xx 的三方包插件。funboost压根不需要三方包插件，而不是三方包插件生态薄弱。      



```
答： scrapy是框架太复杂了约束多钩子多，所以需要由专门的大神开发三方插件，因为普通人写不出来这些插件。  
Scrapy 框架的结构设计“高度抽象 + 强约束 + 多钩子生命周期 + 中间件堆叠机制”，导致插件开发成本极高。
funboost 恰恰不需要插件，因为用户是轻松自由使用任意三方包。
你压根不需要专门的大神给你写个例如 funboost-selenium 类似的插件，才能开始在funboost里面使用selniuem干活，懂了吗？

例如 如 scrapy-redis 用于分布式、scrapy-playwright 或 scrapy-selenium 用于 JavaScript 渲染，scrapy-user-agents换请求头。 
funboost需要学习这些扩展插件怎么使用吗？ 绝对不需要，funboost 是顺其自然自由使用任意三方包。。
麻烦你去看看配置使用 scrapy-selenium 有多麻烦，而直接使用 seleium 有多简单。
本来学习selenium就烦人，你还要再多学习一个 scrapy-selenium ，
凭什么非要这么苦逼，学了各种三方包还不够，还需要额外再另外学这么多三方包的插件。
```

因为你用scrapy，即使你非常精通三方包，如果没有美国大神给你提供三方包的插件，你仍然寸步难行，所以你羡慕scrapy有各种三方包的插件生态。         
你用Scrapy，哪怕精通三方包，没有插件也寸步难行；用Funboost，任何三方包都能直接用，不需要等别人给你造插件轮子。     
当你可以直接驾驶F1赛车时，为什么还非要学习如何给破自行车安装火箭推进器？

```
举个例子：
为什么你用scrapy-redis插件？因为你就算精通了py-redis包的用法，精通了怎么redis.blpop redis.lpush推拉消息，精通了怎么redis.sadd 去重  
但是你不知道怎么完美替代scrapy内置的调度器和去重器，因为你不可能开发的出来，关键难度不是怎么操作reids，而是难以适配scrapy的中间件机制和生命周期钩子懂啦吗?  
不信的你可以看scrapy-redis源码,你能写得了那么好？
你以为你随便在代码哪里简单的写个redis.blpop 和 redis.lpush，scrapy就能完美使用你写的redis代码逻辑来调度运行起来吗？
```

**开发效率的巨大差异**
**使用Scrapy：**       
学习Scrapy框架 → 2. 学习要用的包 → 3. 等待/寻找插件 → 4. 学习插件用法 → 5. 配置插件 → 6. 开始开发
**使用Funboost：**     
学习要用的包 → 2. 开始开发


**你说scrapy社区支持，有庞大的专门各种问题的讨论？质疑funboost没有社区？**
``` 
因为scrapy太难了，用户必须精通scrapy框架本身，精通scrapy各种组件和生命周期，用户难以自由扩展，所以需要讨论。
funboost是你写一个函数，你可以在函数里面自由自在写任何代码，你在写你的消费函数里面是自由的，
不需考虑funboost框架本身的约束，不需要考虑怎么和funboost配合。
funboost 没有需要讨论的，因为funboost 是顺其自然自由使用任意三方包。

例如假设你不会pymysql插入数据，那去pymysql论坛讨论，这和funboost没关系。
例如假设你不会 selenium 操作，那去selenium论坛讨论，这和funboost没关系。
例如你不会requests使用代理ip，那去requests论坛讨论，这和funboost没关系。
例如你不会使用xpath解析html，那去xpath论坛讨论，这和funboost没关系。
```

**你羡慕scrapy的response有自带.xpath .css .extract_first .extract_all 方法？**
```
答：你可以看看boost_spider项目的response，也有xpath方法，实现很简单。
这些真的很简单啊，你的my_request函数可以是返回一个带有这些方法的response对象就好了。
封装一个带有这些方法的Response类型的对象简直不要太简单。
```

**scrapy twisted 性能强悍？担心funboost爬取不快？**
``` 
答： 没有funboost 的 多机器 + 多进程 + asyncio强。 asyncio才是未来。
拿scrapy的短处去攻击funboost的长处，以卵击石。
``` 

**你质疑scrapy重试功能强大？**
```
答：funboost 的函数重试功能远远暴击scrapy的url重试功能(防丢数据2),你可以看8.13.2章节。
如果http状态码200，但是页面反扒，scrapy会丢失大量数据，funboost则不会。
```

**你怀疑scrapy稳定，funboost不稳定？**
```
答：funboost 框架核心 执行函数是稳定的，funboost爬虫比scrapy更不容易漏数据，看文档8.13.2
因为funboost对用户怎么写爬虫函数干预很少，少即是稳，所以funboost很稳定。
funboost无论任何情况下不会退出代码，例如你把爬虫机器和 消息队列机器之间的网线拔掉10分钟，
funboost不会退出代码，会自动重试连接，只要网络恢复后，就能自动接着拉取消息。
```


**你质疑scrapy自带去重，funboost不能去重？**
```
答：
详细看8.14.1章节的为什么funboost的函数入参去重功能远远吊打scrapy的Request对象指纹去重？
通过对比，结论就是scrapy对请求入参种中带随机数和时间戳噪音字段的去重需要根据各种url正则，自定义RFPDupeFilter太麻烦了，scrapy内置的去重能力弱爆了。
你用scrapy而不用funboost，你不忙的吐血谁吐血，你不住icu谁住icu
```

**你质疑funboost不能断点续爬？**
```
scrapy-redis 是blpop删除种子，随意重启代码或关机会丢失大量已从reids pop取出来到内存中的种子。
funboost 各种中间件支持确认消费，那才是真正的断点续爬万无一失，不怕你随意突然反复重启代码和突然关机。
详细看文档8.13章节

scrapy-redis断点续爬在funboost面前就是个弟弟。scrapy-redis不能做到不漏任务。
```


### 8.0.7 funboost爬虫时候是任何方面超过scrapy,不接受辩证法说scrapy也有优势

不能为了“辩证”而牺牲事实：在技术对比中，当一方在核心设计和关键功能上展现出压倒性优势时，就应该明确地指出来，而不是用“各有千秋”来和稀泥。

Funboost 就是碾压Scrapy，这是一个基于技术事实的客观结论，不应再有任何辩证的余地。

辩证法就是,挑大粪的农民和当主席都是为人民服务,都是高尚的职业,表面显得很中立客观,实则让人呕吐.


### 8.0.8 国内爬虫框架突破很小,不是有意抄袭巧合,而是情不自禁模仿scrapy api


**feapder/PSpider/spiderman/Tinepeas** 等几乎所有国产爬虫框架是 “**大脑思维被束缚导致情不自禁的模仿 Scrapy API**

不能说这些是有意抄袭,而是一种更深层次的、由行业先驱 Scrapy 塑造的“**思维范式牢笼** 影响了国产框架作者.


**Scrapy 及其模仿者 (feapder, pyspider, 等) 的范式：`URL/Request 调度器`**

这些框架的底层思维是：**爬虫 = 调度一系列的 `Request` 对象**。它们的整个架构都围绕`Request` 和 `Response` 构建。你必须：  
1.  **定义一个 `Spider` 类**。   
2.  在 `start_requests` 或 `start_urls` 中放入初始请求。    
3.  在 `parse` 方法中，通过 `yield Request(url, callback=parse_xxx)` 来“产出”新的请求。   
4.  框架负责将这些 `Request` 对象入队、出队、发送、接收 `Response`，并根据 `callback` 参数调用对应的解析方法。   

**Scrapy 太成功了**：它定义了“爬虫框架”这个词，以至于后来者在构思时，大脑里首先浮现的就是 Scrapy 的样子。

国产爬虫框架很难使用,用户使用框架难以自由发挥,主要原因不是框架抄袭,而是框架作者脑袋思维被束缚禁锢了,导致了情不自禁模仿scrapy的api

**结论**：feapder Tinepeas 等框架“情不自禁”地模仿 `yield Request`，因为国产爬虫框架的思想还停留在“Scrapy 是如何调度请求的”这个层面，而没有跳出思考“我们真正需要调度的是什么”。它们复制了 Scrapy 的“形”（回调、中间件、管道），却未能突破其“神”（对开发者自由的限制）。

## 8.1 演示获取汽车之家资讯的 新闻 导购 和 评测 3个板块 的 文章。

页面连接 https://www.autohome.com.cn/all/

```
这是一个非常经典的列表页-详情页两层级爬虫调度。演示爬虫一定最少需要演示两个层级的调度，只要会了两层级爬虫，3层级就很简单。
此框架如果用于写爬虫，建议的写法是一种页面(或者接口)对应一个函数,例如列表页是一个函数，详情页是一个函数。
1个函数里面只包括一次请求(也可以两三次请求，但不要在函数本身里面去for循环遍历发十几个请求这种写法)，
```

```text
"""
演示分布式函数调度框架来驱动爬虫函数，使用此框架可以达使爬虫任务 自动调度、 分布式运行、确认消费万无一失、超高速自动并发、精确控频、
种子过滤(函数入参过滤实现的)、自动重试、定时爬取。可谓实现了一个爬虫框架应有的所有功能。

此框架是自动调度一个函数，而不是自动调度一个url请求，一般框架是yield Requet(),所以不兼容用户自己手写requests urllib的请求，
如果用户对请求有特殊的定制，要么就需要手写中间件添加到框架的钩子，复杂的需要高度自定义的特殊请求在这些框架中甚至无法实现，极端不自由。

此框架由于是调度一个函数，在函数里面写 请求 解析 入库，用户想怎么写就怎么写，极端自由，使用户编码思想放荡不羁但整体上有统一的调度。
还能直接复用用户的老函数，例如之前是裸写requests爬虫，没有规划成使用框架爬虫，那么只要在函数上面加一个@boost的装饰器就可以自动调度了。

而90%一般普通爬虫框架与用户手写requests 请求解析存储，在流程逻辑上是严重互斥的，要改造成使用这种框架改造会很大。
此框架如果用于爬虫和国内那些90%仿scrapy api的爬虫框架，在思想上完全不同，会使人眼界大开，思想之奔放与被scrapy api束缚死死的那种框架比起来有云泥之别。
因为国内的框架都是仿scrapy api，必须要继承框架的Spider基类，然后重写 def parse，然后在parse里面yield Request(url,callback=annother_parse)，
请求逻辑实现被 Request 类束缚得死死的，没有方便自定义的空间，一般都是要写middware拦截http请求的各个流程，写一些逻辑，那种代码极端不自由，而且怎么写middware，
也是被框架束缚的死死的，很难学，例如scrapy 集成selenium浏览器没几个人搞定，就算实现了也是同步阻塞导致scrapy的并发成为了废物，
当你把scrapy的并发调度弄成了废物了还有必要用什么scrapy。
例如崔庆才 写的scrapy集成selenium浏览器，文章在 https://cuiqingcai.com/8397.html ，如果网站网页需要渲染30秒，那么此时scrapy爬虫慢的吐血，
因为这种扩展scrapy的方式是错误的。
还有人在scrapy的Spider类的解析方法里面用浏览器重复请求一次url，scrapy的parse不是并发的，只有yield Request类请求是自动并发，
下面parse中写浏览器请求，scrapy就变成了个废物。
def parsexx(self,response):
    driver.get(response.url)

分布式函数调度框架由于是自动调度函数而不是自动调度url请求，所以天生不存在这些问题。

用其他爬虫框架需要继承BaseSpider类，重写一大堆方法写一大堆中间件方法和配置文件，在很多个文件夹中来回切换写代码。
而用这个爬虫，只需要学习 @boost 一个装饰器就行，代码行数大幅度减少，随意重启代码任务万无一失，大幅度减少操心。

这个爬虫例子具有代表性，因为实现了演示从列表页到详情页的分布式自动调度。

"""

"""
除了以上解释的最重要的极端自由的自定义请求解析存储，比普通爬虫框架更强的方面还有：
2、此爬虫框架支持 redis_ack_able rabbitmq模式，在爬虫大规模并发请求中状态时候，能够支持随意重启代码，种子任务万无一失，
   普通人做的reids.blpop，任务取出来正在消费，但是突然关闭代码再启动，瞬间丢失大量任务，这种框架那就是个伪断点接续。
3、此框架不仅能够支持恒定并发数量爬虫，也能支持恒定qps爬虫。例如规定1秒钟爬7个页面，一般人以为是开7个线程并发，这是大错特错，
  服务端响应时间没说是永远都刚好精确1秒，只有能恒定qps运行的框架，才能保证每秒爬7个页面，恒定并发数量的框架差远了。
4、能支持 任务过滤有效期缓存，普通爬虫框架全部都只能支持永久过滤，例如一个页面可能每周都更新，那不能搞成永久都过滤任务。
因为此框架带有20多种控制功能，所以普通爬虫框架能实现的控制，这个全部都自带了。
"""

```

爬虫任务消费代码

代码在 https://github.com/ydf0509/distributed_framework/tree/master/test_frame/car_home_crawler_sample/test_frame/car_home_crawler_sample/car_home_consumer.py


关于对下面funboost爬虫代码的质疑？
```
有人说这里的代码是不真实的，没有 换代理ip useragent，也没有保存结果到数据库。还有人说没有演示破解js 加密。

每次请求自动换代理ip和ua这个功能你自己写个函数不就完了，把这里的requests.get换成你自己定义的换ip的请求函数就完了，一个函数的事情而已。

至于保存到数据库，
你自己把 print(f'保存数据  {news_type}   {title} {author} {url} 到 数据库') 这行改成插入数据库就完了。你自己定义一个函数mysql连接池插入数据库就完了。

这些不是重点所以不需要精确细致的演示，只需要演示爬虫重要的并发调度。其余的怎么发http请求 保存到什么数据库，自己定义一个函数，不就每个爬虫函数里面万能通用了？难道需要无数次重复写怎么换ip发请求吗？

还有人故意找茬说这汽车之家网站太简单了，没有包括破解，这个代码演示没有意义，框架是为了演示并发调度，搞一堆破解代码掺杂在里面没有必要。你用scrapy框架就能自动破解网站了吗？
我采用的是控制变量法耐对比不同框架写代码所需的行数，又没让scrapy爬加密网站用这个funboost爬简单网站导致对比不公平。
如果需要做破解加密，那么funboost集成破解流程肯定比scrapy集成破解要更容易随心所欲的写。


```


```python
import requests
from parsel import Selector
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='car_home_list', broker_kind=BrokerEnum.REDIS_ACK_ABLE, max_retry_times=5, qps=10))
def crawl_list_page(news_type, page, do_page_turning=False):
    """ 函数这里面的代码是用户想写什么就写什么，函数里面的代码和框架没有任何绑定关系
    例如用户可以用 urllib3请求 用正则表达式解析，没有强迫你用requests请求和parsel包解析。
    """
    url = f'https://www.autohome.com.cn/{news_type}/{page}/#liststart'
    resp_text = requests.get(url).text  # 此处你可以换成你自己封装好的 my_request 请求函数来换代理ip请求网页
    sel = Selector(resp_text)
    for li in sel.css('ul.article > li'):
        if len(li.extract()) > 100:  # 有的是这样的去掉。 <li id="ad_tw_04" style="display: none;">
            url_detail = 'https:' + li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/h3/text()').extract_first()
            crawl_detail_page.push(url_detail, title=title, news_type=news_type)  # 发布详情页任务
    if do_page_turning:
        last_page = int(sel.css('#channelPage > a:nth-child(12)::text').extract_first())
        for p in range(2, last_page + 1):
            crawl_list_page.push(news_type, p)  # 列表页翻页。


@boost(BoosterParams(queue_name='car_home_detail', broker_kind=BrokerEnum.REDIS_ACK_ABLE, qps=50,
           do_task_filtering=True, is_using_distributed_frequency_control=True))
def crawl_detail_page(url, title, news_type):
    resp_text = requests.get(url).text #   # 此处你可以换成你自己封装好的 my_request 请求函数来换代理ip请求网页
    sel = Selector(resp_text)
    author = sel.css('#articlewrap > div.article-info > div > a::text').extract_first() or
    sel.css('#articlewrap > div.article-info > div::text').extract_first() or ''
    author = author.replace("\n", "").strip()
    print(f'保存数据  {news_type}   {title} {author} {url} 到 数据库')  # 用户自由发挥保存。

if __name__ == '__main__':
    # crawl_list_page('news',1)
    crawl_list_page.consume()  # 启动列表页消费
    crawl_detail_page.consume()
    # 这样速度更猛，叠加多进程
    crawl_detail_page.multi_process_consume(4)
```

爬虫任务发布代码

代码在 https://github.com/ydf0509/distributed_framework/blob/master/test_frame/car_home_crawler_sample/car_home_publisher.py

```python
from funboost import ApsJobAdder
from test_frame.car_home_crawler_sample.car_home_consumer import crawl_list_page, crawl_detail_page

crawl_list_page.clear()  # 清空列表页
crawl_detail_page.clear()  # 清空详情页

# # 推送列表页首页，同时设置翻页为True
crawl_list_page.push('news', 1, do_page_turning=True)  # 新闻
crawl_list_page.push('advice', page=1, do_page_turning=True)  # 导购
crawl_list_page.push(news_type='drive', page=1, do_page_turning=True)  # 驾驶评测

# 定时任务，语法入参是apscheduler包相同。每隔120秒查询一次首页更新,这部分可以不要。
for news_typex in ['news', 'advice', 'drive']:
    ApsJobAdder(crawl_list_page, job_store_kind='redis').add_push_job('interval', seconds=120, kwargs={"news_type": news_typex, "page": 1, "do_page_turning": False,id='timing_publish_job_first_page_'+news_typex})

```

```
从消费代码可以看出，代码就是常规思维的平铺直叙主线程思维写代码，写函数代码时候无需考虑和框架怎么结合，写完后加个@boost装饰器就行了。
因为这不是类似国内的仿scrapy框架必须要求你必须继承个什么类，强迫你重写什么方法，然后yield Request(your_url,callback=my_parse)
此框架爬虫既能实现你无拘无束使用任意包来请求url和解析网页，又能很方便的使用到自动超高并发 超高可靠性的万无一失断点续传。
```

qps设置为很低时候，为了展示更多控制台日志流程细节，分布式函数调度框架驱动爬虫函数的慢速爬取运行截图。
![](img_7.png)

qps设置高时候的运行截图，分布式函数调度框架驱动爬虫函数的快速爬取运行截图。
![](img_6.png)

## 8.2 演示经典的豆瓣top250电影的爬虫

页面连接 https://movie.douban.com/top250

```
这是一个非常经典的列表页-详情页两层级爬虫调度。演示爬虫一定最少需要演示两个层级的调度，只要会了两层级爬虫，3层级就很简单。

此框架如果用于写爬虫，建议的写法是一种页面(或者接口)对应一个函数,例如列表页是一个函数，详情页是一个函数。

1个函数里面只包括一次请求(也可以两三次请求，但不要在函数本身里面去for循环遍历发十几个请求这种写法)，
```

```python
from funboost import boost, BrokerEnum, BoosterParams
import requests
from parsel import Selector

HEADERS = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)', }


@boost(BoosterParams(queue_name='douban_list_page_task_queue', broker_kind=BrokerEnum.PERSISTQUEUE, qps=0.1))  # qps 自由调节精确每秒爬多少次，远强于一般框架只能指定固定的并发线程数量。
def craw_list_page(page):
    """ 函数这里面的代码是用户想写什么就写什么，函数里面的代码和框架没有任何绑定关系，框架只对函数负责，不对请求负责。
    例如用户可以用 urllib3请求 用正则表达式解析，没有强迫你用requests请求和parsel包解析。
    """
    """ 豆瓣列表页，获取列表页电影链接"""
    url = f'https://movie.douban.com/top250?start={page * 25}&filter='
    resp = requests.get(url, headers=HEADERS) #   # 此处你可以换成你自己封装好的 my_request 请求函数来换代理ip请求网页
    sel = Selector(resp.text)
    for li_item in sel.xpath('//*[@id="content"]/div/div[1]/ol/li'):
        movie_name = li_item.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
        movei_detail_url = li_item.xpath('./div/div[2]/div[1]/a/@href').extract_first()
        craw_detail_page.push(movei_detail_url, movie_name)
    # craw_list_page.push(page=11) # 如果你要动态获取总页数，而不是一开始就知道总共有10页，可以在craw_list_page函数里面进行消息推送，调用 craw_list_page.push，没有递归死循环调用列表页爽歪歪。


@boost(BoosterParams(queue_name='douban_detail_page_task_queue', broker_kind=BrokerEnum.PERSISTQUEUE, qps=4))
def craw_detail_page(detail_url, movie_name):
    """豆瓣详情页，获取电影的详细剧情描述。"""
    resp = requests.get(detail_url, headers=HEADERS) #   # 此处你可以换成你自己封装好的 my_request 请求函数来换代理ip请求网页
    sel = Selector(resp.text)
    description = sel.xpath('//*[@id="link-report"]/span[1]/text()[1]').extract_first().strip()
    print('保存到数据库：', movie_name, detail_url, description)


if __name__ == '__main__':
    # craw_list_page(0)
    # craw_detail_page('https://movie.douban.com/subject/6786002/','触不可及')
    for p in range(10):
        craw_list_page.push(p)
    craw_list_page.consume()
    craw_detail_page.consume()
```

### 8.2.2 funboost 对比网上的 scrapy 爬取 douban代码

[https://github.com/wxmseu/douban_scrapy/tree/master/douban](https://github.com/wxmseu/douban_scrapy/tree/master/douban)

```
对比网上的scrapy 爬取douban代码，funboost在 qps控频 并发方式 代码行数少 文件数量少 远远的暴击scrapy
使用同步requests发请求的写法平铺直叙横冲直撞的思维特点，远远的暴击scrapy写出的不兼容代码 yield Request。

爬陌生新网站肯定是先用requests这种包简单的发请求，测试反爬和解析，测试验证解决了反爬或者无反爬，再将代码用到框架中，
因为直接使用框架来开始探索一个陌生新网站爬虫，万一爬不到，在框架中写了一大堆代码，做了一大堆无用功，精力损失很大。还有就是在爬虫框架中调试爬取一个特定的url也没有单脚本+requests那么随心所欲方便。

funboost可以套用到已存在的requests测试探索代码，因为funboost是函数调度框架，兼容一切函数的调度，不要求用户修改已有代码。
而scrapy和feapder和pspider这种为了使用这种框架，需要把已存在的发送请求和解析的代码大改特改再移到框架中，非常的不方便。

任何人写新的爬虫框架只要是仿scrapy api用法和scrapy的项目目录结果，如果需要写 yield Request(url,callback=self.parse_xx)，和funboost比，就已经输了，无需再看他框架源码用多么美妙的设计模式和面向对象设计出来的了。
只要模仿这个scrapy api用法，思维被束缚大脑不灵活开发出的爬虫框架写法和scrapy一样烦人，那么开发这样的一个新框架就没什么必要存在了。
```

## 8.3 演示3种最常见代码思维方式爬取汽车之家资讯

演示了三种方式爬汽车之家，是骡子是马拉出来溜溜，必须精确对比。

```
第一种是 无框架每次临时手写全流程代码，每次临时设计手写爬虫调度全流程
第二种是 使用scrapy框架来爬取，用户要写的代码行数很多，文件很多，对于特殊独特奇葩想法极端不自由
第三种是 使用分布式函数调度框架来自动调度常规函数
```

### 8.3.1 每次临时手写rquests + 多线程,使用low爬虫方式的缺点

```
这样搞有以下缺点：
1、不是分布式的，不能多个脚本启动共享任务
2、不能断点爬取，即使是内置Queue改成手写使用redis的普通pop，要实现确认消费每次写一大堆代码，很难。
3、如果要调试爬虫，要反复手动自己手写添加print或log调试信息
4、写得虽然自己认为没有用爬虫框架很简洁，但导致接盘侠不知道你的代码的设计布局和意思
5、自己每次临时灵机一动搞个临时的爬虫调度设计，没有固定套路，难维护，接盘侠一个个的看每个爬虫是怎么设计布局和调度的
6、需要每次临时手写操作queue任务队列
7、需要临时手写并发
8、每次需要临时手写如何判断和添加过滤任务
9、需要临时手写怎么提取错误重试。
10、需要临时动脑筋设计怎么调度,浪费自己的时间来思考，每次都重复思考重复设计重复写爬虫全流程。
```

### 8.3.2 scrapy 爬虫框架来实现缺点

scrapy 爬虫框架来实现，（本质是Request 对象自动调度框架）

```
scrapy_proj_carhome 是 scrapy_redis 弄得项目，写项目需要背诵scrapy 命令行，
并且要反复在spiderxx.py  settings.py items.py pipeliens.py 
middwares.py push_start_urls.py run.py 7个文件里面来回切换写代码,
如果一年只临时要写一次爬虫效率很低，比low爬虫还写的慢。

需要500行，实际要手写或者修改的行数为150行，如果是写多个爬虫，平均每次实际手写的代码函数会降低一些。

```

### 8.3.3 scrapy 框架 和 分布式函数调度框架爬虫对比

```
不是分布式函数调度框架比scrapy爬虫框架代码质量好，主要是理念问题，
Request对象自动调度框架永远没法和函数自动调度框架的灵活自由性相比。
```

```
scrapy 自动调度 全靠 yield Request( url, callback=None, method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None)
本质就是自动框架自动调度 Request对象，虽然入参比较丰富，大部分想法都能通过传参来搞定，但如果是一些自定义的想法，
要加到scrapy项目中就非常难。写任何一行代码都要考虑与框架的集成，
不能随便用 requests ，urllib3 ，selenium ，独立的每两个页面间的cookie自定义关联 等 乱自己来写请求，
包括换proxies要写中间件然后把类加到settings里面也是烦得要死。

比如一个很愚蠢的想法写法,在详情页解析回调这么写代码，这样瞎写完全没有考虑scrapy框架的感受。

    def parse_detail_page(self, response):
        driver = Chrome()
        driver.get(response.url)
        text = driver.page_source
        
scrapy框架能自动并发调度运行Request请求,但不能自动并发运行parse方法。
第一，selenium会阻塞框架。
第二，reponse本来就是一个响应结果了，他是已经被scrapy的urllib请求了，只要解析结果就好了，但这么一写有用浏览器打开一次url，
等于是请求了两次页面，这样请求两次 是嫌电脑cpu太好 还是 流量太便宜了呢。

总之使用了scrapy后就是写任何代码不能乱写，要多考虑框架的感受。

只有celery这样的函数和函数入参自动调度才能很香，
scrapy这样的固化的 Request对象入参 + 自定义中间件类添加到 settings里面的 自动调度很不自由。

```

```
分布式函数调度框架是通过把函数的入参推到队列(支持15中队列，包括语言级Queue队列  sqlite队列 redis队列 各种mq队列)，
然后框架会自动从对应的队列取出任务，自动并发的运行对应的函数。函数里面怎么写那就非常自由了，你想随便有什么想法怎么写都可以，
这种方式是极端的自由和灵活，只需要按同步的思维写常规思维的函数，最后加个装饰器就能自动并发了，写函数的时候完全不用考虑框架的束缚。
任何函数都能被自动并发调度。

以下这些功能对爬虫的各种控制例如 精确的每秒爬几次  分布式中间件支持种类  消费确认 对爬虫的辅助控制远强于scrapy。

分布式：
    支持数十种最负盛名的消息中间件.(除了常规mq，还包括用不同形式的如 数据库 磁盘文件 redis等来模拟消息队列)

 并发：
    支持threading gevent eventlet asyncio 四种并发模式 + 多进程
 
 控频限流：
    例如十分精确的指定1秒钟运行30次函数（无论函数需要随机运行多久时间，都能精确控制到指定的消费频率；
   
 分布式控频限流：
    例如一个脚本反复启动多次或者多台机器多个容器在运行，如果要严格控制总的qps，能够支持分布式控频限流。
  
 任务持久化：
    消息队列中间件天然支持
 
 断点接续运行：
    无惧反复重启代码，造成任务丢失。消息队列的持久化 + 消费确认机制 做到不丢失一个消息
 
 定时：
    可以按时间间隔、按指定时间执行一次、按指定时间执行多次，使用的是apscheduler包的方式。
 
 指定时间不运行：
    例如，有些任务你不想在白天运行，可以只在晚上的时间段运行
 
 消费确认：
    这是最为重要的一项功能之一，有了这才能肆无忌惮的任性反复重启代码也不会丢失一个任务
 
 立即重试指定次数：
    当函数运行出错，会立即重试指定的次数，达到最大次重试数后就确认消费了
 
 重新入队：
    在消费函数内部主动抛出一个特定类型的异常ExceptionForRequeue后，消息重新返回消息队列
 
 超时杀死：
    例如在函数运行时间超过10秒时候，将此运行中的函数kill
 
 计算消费次数速度：
    实时计算单个进程1分钟的消费次数，在日志中显示；当开启函数状态持久化后可在web页面查看消费次数
 
 预估消费时间：
    根据前1分钟的消费次数，按照队列剩余的消息数量来估算剩余的所需时间
 
 函数运行日志记录：
    使用自己设计开发的 控制台五彩日志（根据日志严重级别显示成五种颜色；使用了可跳转点击日志模板）
    + 多进程安全切片的文件日志 + 可选的kafka elastic日志
               
 任务过滤：
    例如求和的add函数，已经计算了1 + 2,再次发布1 + 2的任务到消息中间件，可以让框架跳过执行此任务。
    任务过滤的原理是使用的是函数入参判断是否是已近执行过来进行过滤。
 
 任务过滤有效期缓存：
    例如查询深圳明天的天气，可以设置任务过滤缓存30分钟，30分钟内查询过深圳的天气，则不再查询。
    30分钟以外无论是否查询过深圳明天的天气，则执行查询。
    
 任务过期丢弃：
    例如消息是15秒之前发布的，可以让框架丢弃此消息不执行，防止消息堆积,
    在消息可靠性要求不高但实时性要求高的高并发互联网接口中使用
            
 函数状态和结果持久化：
    可以分别选择函数状态和函数结果持久化到mongodb，使用的是短时间内的离散mongo任务自动聚合成批量
    任务后批量插入，尽可能的减少了插入次数
                  
 消费状态实时可视化：
    在页面上按时间倒序实时刷新函数消费状态，包括是否成功 出错的异常类型和异常提示 
    重试运行次数 执行函数的机器名字+进程id+python脚本名字 函数入参 函数结果 函数运行消耗时间等
                 
 消费次数和速度生成统计表可视化：
    生成echarts统计图，主要是统计最近60秒每秒的消费次数、最近60分钟每分钟的消费次数
    最近24小时每小时的消费次数、最近10天每天的消费次数
                            
 rpc：
    生产端（或叫发布端）获取消费结果。各个发布端对消费结果进行不同步骤的后续处理更灵活，而不是让消费端对消息的处理一干到底。

```

### 8.3.4 临时low方法手写爬虫全流程的代码 （手写多线程 + queue 分发调度 ）

临时low方法手写爬虫全流程的代码 （手写多线程 + queue 分发 ）

<pre>
这样搞有以下缺点：
1、不是分布式的，不能多个脚本启动共享任务
2、不能断点爬取
3、如果要调试爬虫，要反复手动自己手写添加print或log调试
4、写得虽然自己认为没有用爬虫框架很简洁，但导致接盘侠不知道你的代码的设计布局和意思
5、自己每次临时灵机一动搞个临时的爬虫调度设计，没有固定套路，难维护，接盘侠一个个的看每个爬虫是怎么设计布局和调度的
6、需要每次临时手写操作queue任务队列
7、需要临时手写并发
8、每次需要临时手写如何判断和添加过滤任务
9 需要临时手写怎么提取错误重试。
10、需要临时动脑筋设计怎么调度,浪费自己的时间来思考
</pre>

```python

from queue import Queue, Empty
import time
import requests
from urllib3 import disable_warnings
from parsel import Selector
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import redis

disable_warnings()

queue_list_page = Queue(1000)
queue_detail_page = Queue(1000)

pool_list_page = ThreadPoolExecutor(30)
pool_detail_page = ThreadPoolExecutor(100)

# detail_task_filter_set = set()
r = redis.Redis()


def crawl_list_page(news_type, page):
    def _run_list_page_retry(current_retry_times):
        try:
            url = f'https://www.autohome.com.cn/{news_type}/{page}/#liststart'
            print(f'请求的列表页url是 {url}')
            resp = requests.request('get', url, timeout=5)
            if resp.status_code != 200:
                raise ValueError
            resp_text = resp.content.decode('gbk')
            sel = Selector(resp_text)
            for li in sel.css('#Ul1 > li'):
                url = 'https:' + li.xpath('./a/@href').extract_first()
                title = li.xpath('./a/h3/text()').extract_first()
                task = (url, title)
                print('向详情页队列添加任务：', task)
                queue_detail_page.put(task)
            if page == 1:
                last_page = int(sel.css('#channelPage > a:nth-child(12)::text').extract_first())
                for p in range(2, last_page + 1):
                    task = (news_type, p)
                    print('向列表页页队列添加任务：', task)
                    queue_list_page.put(task)
        except Exception as e:
            print(f'第{current_retry_times}次爬取列表页出错', e.__traceback__, e)
            if current_retry_times < 5:
                _run_list_page_retry(current_retry_times + 1)
            else:
                print('重试了5次仍然错误')

    _run_list_page_retry(1)


def crawl_detail_page(url, title):
    def _run_detail_page_retry(current_retry_times):
        if r.sismember('filter_carhome_detail_page', url):
            print(f'此入参已经爬取过了 {url} {title}')
            return
        else:
            try:
                print(f'请求的详情页url是 {url}')
                resp = requests.request('get', url, timeout=5)
                if resp.status_code != 200:
                    raise ValueError
                resp_text = resp.content.decode('gbk')
                sel = Selector(resp_text)
                author = sel.css('#articlewrap > div.article-info > div > a::text').extract_first() or
                         sel.css('#articlewrap > div.article-info > div::text').extract_first() or ''
                author = author.replace("\n", "").strip()
                print(f'{time.strftime("%H:%M:%S")} 保存到数据库 {url} {title} {author} ')
                r.sadd('filter_carhome_detail_page', url)  # 运行成功了，放入过滤中
            except Exception as e:
                print(f'第{current_retry_times}次爬取详情页页出错', e.__traceback__, e)
                if current_retry_times < 3:
                    _run_detail_page_retry(current_retry_times + 1)
                else:
                    print('重试了3次仍然错误')
                    r.sadd('filter_carhome_detail_page', url)  # 运行最大次数了，放入过滤中

    _run_detail_page_retry(1)


def start_list_page():
    while True:
        try:
            task = queue_list_page.get(block=True, timeout=600)
            print(f'取出的列表页爬取任务是 {task}')
            pool_list_page.submit(crawl_list_page, *task)
        except Empty:
            print('列表页超过600秒没有任务，列表页爬完了')
            break


def start_detail_page():
    while True:
        try:
            task = queue_detail_page.get(block=True, timeout=600)
            print(f'取出的详情页爬取任务是 {task}')
            pool_detail_page.submit(crawl_detail_page, *task)
        except Empty:
            print('详情页超过600秒没有任务，详情页爬完了')
            break


if __name__ == '__main__':
    # 单独的测试函数功能
    # crawl_list_page('advice',1)  #
    # crawl_detail_page('https://www.autohome.com.cn/news/202008/1022380.html#pvareaid=102624','xxx')

    t1 = Thread(target=start_list_page)
    t2 = Thread(target=start_detail_page)
    t1.start()
    t2.start()

    queue_list_page.put(('news', 1))  # 新闻
    queue_list_page.put(('advice', 1))  # 导购
    queue_list_page.put(('drive', 1))  # 评测

```

举个网上下载 mzitu 网站图片的代码截图，就是采用的无框架爬虫，任务调度靠直接for循环调用函数，任务并发全靠手写操作threads，

这样的代码看起来很多很混乱，写一个还行，要是爬虫项目多了，没有统一化的逻辑思维，接盘侠每次都要阅读很长的代码才知道运行逻辑，那就非常悲催。

![img_13.png](img_13.png)



### 8.3.5 scrapy爬虫代码

这是scrapy爬虫代码的基本结构，用户写代码需要非常频繁的在 spider items middware pipeline settings cmd命令行 来回切换写代码测试代码，很吓人。

需要在不同的地方写middleware类 pipeline类并把类名添加到settings里面。

scrapy目录结构，代码文件数量很多

![img_5.png](img_5.png)

这是 scrapy carhome_spider.py的代码

```python
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import json

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

from scrapy_proj_carhome.items import ScrapyProjCarhomeItem

import nb_log


class carHomeSpider(RedisSpider):
    name = "carhome"
    allowed_domains = ["www.autohome.com.cn"]

    redis_key = "carhome:start_urls"

    def make_requests_from_url(self, data: str):
        '''
        data就是放入 carhome:start_urls 中的任务,因为最初的种子信息还需要携带其他信息，例如新闻类型的中文种类，不是单纯的url，所以需要重写此方法
        :param data:
        :return:
        '''
        start_task = json.loads(data)
        url = start_task['url']

        # 此处也可以改为post请求
        return Request(
            url,
            meta=start_task
        )

    def parse(self, response):
        # https://www.autohome.com.cn/news/2/#liststart
        # print(response.body)
        for li in response.css('#Ul1 > li'):
            url = 'https:' + li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/h3/text()').extract_first()
            yield Request(url, callback=self.parse_detail_page, meta={'url': url, 'title': title, 'news_type': response.meta['news_type']},
                          dont_filter=False, priority=10)
        page = response.url.split('/')[-2]
        if page == '1':
            last_page = int(response.css('#channelPage > a:nth-child(12)::text').extract_first())
            for p in range(2, last_page + 1):
                url_new = response.url.replace('/1/', f'/{p}/')
                self.logger.debug(url_new)
                yield Request(url_new, callback=self.parse, dont_filter=True, meta=response.meta)

    def parse_detail_page(self, response):
        author = response.css('#articlewrap > div.article-info > div > a::text').extract_first() or
                 response.css('#articlewrap > div.article-info > div::text').extract_first() or ''
        author = author.replace("\n", "").strip()
        item = ScrapyProjCarhomeItem()
        item['author'] = author
        item['url'] = response.meta['url']
        item['title'] = response.meta['title']
        item['news_type'] = response.meta['news_type']
        yield item


if __name__ == '__main__':
    pass
```

这是 items.py 的代码

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjCarhomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    news_type = scrapy.Field()

```

这个middlewares.py文件的代码是最坑的，任何自定义想法需要写一个类，继承middware类，重写process_request process_request方法，然后把类名添加到settings里面。


<summary>这是 middlewares.py的代码</summary><br>



```python
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ScrapyProjCarhomeSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn't have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyProjCarhomeDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

```

</details>



这是pipelines.py 的代码,保存数据。

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_proj_carhome.items import ScrapyProjCarhomeItem


class ScrapyProjCarhomePipeline(object):
    def process_item(self, item, spider):
        print(type(item))
        if isinstance(item, ScrapyProjCarhomeItem):
            print(f'保存到数据库 {item["news_type"]}  {item["url"]} {item["title"]} {item["author"]} ')
        return item

```

这是settings.py的代码

```python
# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_proj_carhome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_proj_carhome'

SPIDER_MODULES = ['scrapy_proj_carhome.spiders']
NEWSPIDER_MODULE = 'scrapy_proj_carhome.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_proj_carhome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_proj_carhome.middlewares.ScrapyProjCarhomeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_proj_carhome.middlewares.ScrapyProjCarhomeDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_proj_carhome.pipelines.ScrapyProjCarhomePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PARAMS = {'db': 2, 'password': ''}
REDIS_ENCODING = "utf-8"

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
# DUPEFILTER_KEY = "dupefilter:%(timestamp)s"


```

这是 push_start_urls.py 的代码

```python
from redis import Redis
import json
from scrapy_proj_carhome import settings

r = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, **settings.REDIS_PARAMS)

r.flushdb()

# 因为要让初始种子就携带其他信息，初始种子发布的不是url本身，所以需要继承重写spider的make_requests_from_url方法。
r.lpush('carhome:start_urls', json.dumps({'url': 'https://www.autohome.com.cn/news/1/#liststart', 'news_type': '新闻'}, ensure_ascii=False))
r.lpush('carhome:start_urls', json.dumps({'url': 'https://www.autohome.com.cn/advice/1/#liststart', 'news_type': '导购'}, ensure_ascii=False))
r.lpush('carhome:start_urls', json.dumps({'url': 'https://www.autohome.com.cn/drive/1/#liststart', 'news_type': '驾驶评测'}, ensure_ascii=False))

```

这是run.py的代码

```python

from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'carhome'])
```

```
从上面的代码可以看到scrapy要在8个文件频繁的来回切换写代码，非常的烦躁。
即使是除去scrapy 建项目自动生产的固定代码行数，此scrapy项目的代码行数仍然远远高于分布式函数调度框架的代码行数
```

### 8.3.6 分布式函数调度框架的代码

只需要单个文件(当然也可以拆解成发布和消费独立成两个文件)

所需代码行数远小于无框架每次临时手写爬虫全流程和使用scrapy的方式。

此框架不仅可以对标celery框架，也可以取代scrapy框架。

```python


from funboost import boost, BrokerEnum, BoosterParams
import requests
from parsel import Selector


@boost(BoosterParams(queue_name='car_home_list', broker_kind=BrokerEnum.REDIS_ACK_ABLE, max_retry_times=5, qps=10))
def crawl_list_page(news_type, page):
    url = f'https://www.autohome.com.cn/{news_type}/{page}/#liststart'
    resp_text = requests.get(url).text
    sel = Selector(resp_text)
    for li in sel.css('#Ul1 > li'):
        url_detail = 'https:' + li.xpath('./a/@href').extract_first()
        title = li.xpath('./a/h3/text()').extract_first()
        crawl_detail_page.push(url_detail, title=title, news_type=news_type)
    if page == 1:
        last_page = int(sel.css('#channelPage > a:nth-child(12)::text').extract_first())
        for p in range(2, last_page + 1):
            crawl_list_page.push(news_type, p)


@boost(BoosterParams(queue_name='car_home_detail', broker_kind=BrokerEnum.REDIS_ACK_ABLE, concurrent_num=100, qps=30, do_task_filtering=False))
def crawl_detail_page(url, title, news_type):
    resp_text = requests.get(url).text
    sel = Selector(resp_text)
    author = sel.css('#articlewrap > div.article-info > div > a::text').extract_first() or
             sel.css('#articlewrap > div.article-info > div::text').extract_first() or ''
    author = author.replace("\n", "").strip()
    print(f'使用print模拟保存到数据库  {news_type}   {title} {author} {url}')  # ，实际为调用数据库插入函数，压根不需要return item出来在另外文件的地方进行保存。


if __name__ == '__main__':
    # 单独的测试函数功能
    # crawl_list_page('advice',1)  #
    # crawl_detail_page('https://www.autohome.com.cn/news/202008/1022380.html#pvareaid=102624','xxx')

    # 清空消息队列
    crawl_list_page.clear()
    crawl_detail_page.clear()
    #
    # # 推送列表页首页
    crawl_list_page.push('news', 1)  # 新闻
    crawl_list_page.push('advice', page=1)  # 导购
    crawl_list_page.push(news_type='drive', page=1)  # 驾驶评测

    # 启动列表页消费和详情页消费,上面的清空和推送可以卸载另外的脚本里面，因为是使用的中间件解耦，所以可以推送和消费独立运行。
    crawl_list_page.consume()
    crawl_detail_page.consume()
```

使用分布式函数调度框架运行的爬虫，自动并发，自动控频，是指定了列表页qps=2，详情页qps=3的情况下运行的控制台日志

[![4BquHf.png](https://z3.ax1x.com/2021/09/24/4BquHf.png)](https://imgtu.com/i/4BquHf)

可以得出结论，控频效果精确度达到了99%以上，目前世界所有爬虫框架只能指定并发请求数量，但不能指定每秒爬多少次页面，此框架才能做到。



## 8.7 scrapy 和 仿scrapy api 式爬虫框架 回调地狱，代码写法思维反直觉

scrapy 和 仿scrapy api 式爬虫框架 回调地狱，代码写法思维反直觉，不是横冲直闯 平铺直叙的一气呵成 写法，导致编写和理解苦难

Scrapy 作为一个成熟的爬虫框架，其设计和架构目标主要是为了实现高并发、异步非阻塞的网络爬取，并能灵活地处理分布式任务调度。正因为这些设计目标，Scrapy 的代码风格与"横冲直闯、平铺直叙"那种顺序式、线性写法有很大区别，下面详细说明原因：

1. **异步回调模型（Event-driven Programming）**  
   Scrapy 基于 Twisted 异步网络框架，其核心设计采用的是事件驱动模式。请求发送后，并不会等待响应返回，而是通过回调函数（通常是 spider 中的 parse 方法）来处理响应。  
   - **代码分散**：任务被拆分成多个独立的回调函数，每个回调函数只处理特定的响应数据。这种模式虽然高效，但导致代码逻辑被拆分成许多零散的函数，难以从头到尾按顺序阅读。
   - **逻辑碎片化**：一个完整的爬取流程可能涉及多个请求、多个回调，以及在回调中又发起新的请求。这样就形成了类似"回调地狱"的结构，不是那种一气呵成的直线流程。

2. **固定项目结构和模块分离**  
   Scrapy 强调模块化开发，将爬虫、下载器中间件、数据管道、调度器等组件严格分离：
   - **Spider**：定义爬虫逻辑，每个 Spider 负责从起始 URL 出发解析页面，提取数据和新的 URL。
   - **Downloader Middleware**：在请求和响应之间插入额外的处理逻辑，如设置代理、User-Agent、重试等。
   - **Item Pipeline**：处理解析后的数据（清洗、存储等）。
   
   这种结构使得每个模块职责明确，但同时也要求开发者在不同文件中编写不同逻辑，整体代码组织上远比"平铺直叙"复杂。

3. **异步并发与性能优化的权衡**  
   为了实现高并发与高效爬取，Scrapy 必须避免阻塞操作。这就要求所有网络请求、数据解析等操作都以异步方式处理，任何阻塞代码都可能影响整个爬虫性能。因此：
   - **回调链**：每个网络请求完成后都需要通过回调函数继续处理数据，任务间的顺序和依赖关系通过事件循环来管理，而不是直接按照代码的顺序执行。
   - **任务调度机制**：Scrapy 内部有一个调度器（Scheduler）来管理请求队列和去重逻辑，这也使得任务处理不是简单的线性顺序，而是多个请求并发执行，异步返回后再根据调度逻辑进行处理。

4. **错误处理与重试机制**  
   在 Scrapy 中，如果在 spider 的回调函数中捕获并吞掉异常，框架就无法正确检测到任务失败，从而影响自动重试和错误处理策略。为了保证重试机制能够工作，通常要求让异常沿回调链上抛，这也促使代码设计者不得不在各个回调中考虑如何把异常交由框架统一处理，而不是简单地在一个"主流程"中捕获处理。

5. **灵活性与扩展性**  
   虽然 Scrapy 采用回调和分层结构增加了开发难度，但它提供了大量内置的扩展点（如中间件、扩展器、信号机制等），使得开发者可以在不同阶段注入自定义逻辑。这个灵活性换来了高度可定制的爬虫，但也使得代码看起来不如"平铺直叙"的方式那样直接。所以不精通scrapy本身的人想扩展自定义scrapy难度超高。

综上，Scrapy 的架构设计为异步高并发和模块化扩展服务，采用事件驱动和回调链来管理任务流，使得代码逻辑被拆分到各个独立模块和回调函数中。这种设计虽然在性能和灵活性上非常出色，但从代码风格上来说，并不是那种"一气呵成、平铺直叙"的直观写法，而更像是分散在多个模块、通过事件调度器串联起来的"碎片化"结构，这正是 Scrapy 为实现大规模、高效率爬取所必须做出的权衡。

## 8.8 详细说明为什么 Scrapy 爬虫代码不是直观的"平铺直叙"写法？

![img_81.png](img_81.png)

<div class="inner_markdown">



Scrapy 是一个强大的爬虫框架，在它的回调函数中需要写很多 `callback` 事件函数，和同步代码逻辑不直观。  
本文将解释 **Scrapy 的写法为什么不是平铺直叙的**。

---

<h3> 1. 基于回调，代码逻辑割裂</h3>

<h4>Scrapy 代码的典型结构</h4>

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com/list']

    def parse(self, response):
        detail_urls = response.css('a::attr(href)').getall()
        for url in detail_urls:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.css('h1::text').get()
        price = response.css('.price::text').get()
        yield {'title': title, 'price': price}
```

**问题分析**
- 爬虫逻辑被分散在多个回调函数里，代码割裂。
- 业务逻辑无法“从上到下”顺序执行，开发者思维负担大。
- 如果熟悉 Python 的 `requests` 和 `BeautifulSoup`，常觉得爬虫代码可以写得更平铺直叙。

---

<h3> 2. `yield` 语法导致执行顺序不直观</h3>

在 Scrapy 中，`yield` 用于生成新的请求，而不是立即执行回调函数。  
常见写法：

```python
yield response.follow(url, callback=self.parse_detail)
```

**问题分析**
- 任务不会立即同步执行，需等 Scrapy 调度下一次请求。
- 编写 Python 函数时，习惯用 `return` 表达逻辑，而 Scrapy 使用 `yield` 让逻辑割裂。
- 对于新手来说，Scrapy 的执行顺序、调度策略，不同于常规函数调用链。

---

<h3> 3. 任务调度是黑盒，开发者失去控制权</h3>

Scrapy 通过调度器（Scheduler）决定请求的先后执行顺序：
- 爬虫开发者只负责写回调函数，不控制调度。
- 但有时候需要更精细化控制顺序，比如递归抓取树形结构。

**对比：**
使用 `for url in URL_LIST: requests.get(url)` 就很直观：
- 程序的执行顺序由 Python 原生控制。
- Scrapy 的调度机制虽然强大，但对开发者来说是黑盒。

---

<h3> 4. 强制使用 `Spider` 类，不够自由</h3>

Scrapy 框架必须继承 `Spider` 类：

```python
class MySpider(scrapy.Spider):
    name = 'myspider'
    ...
```

**问题分析**
- 代码风格被固定，无法随意定义函数入口。
- 对比 `requests` 库，可以直接写 `def crawl():` 这种函数结构，更符合 Python 开发习惯。

---

<h3> 5. 并发控制分散，不直观</h3>

在 Scrapy 里，并发控制依赖 `settings.py` 配置：

```python
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 0.5
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
```

**问题分析**
- 并发控制在全局配置文件，逻辑和代码分离。
- 如果希望按不同函数使用不同并发策略，需要额外代码。

相比之下，`funboost` 的写法更直观：

```python
@boost(concurrent_num=20)
def crawl_page(url):
    ...
```

- 代码和配置绑定在一起，逻辑更易理解。

---

<h3> 6. Scrapy 不适合任务编排</h3>

Scrapy 多个回调函数之间无法方便串联多个 `Spider`：

```python
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com/list']

    def parse(self, response):
        yield response.follow(url, callback=self.parse_detail)
```

**问题分析**
- 单个任务孤立，不方便平铺任务依赖。
- 对比 `funboost` 等任务队列框架，可以轻松实现任务流水线，例如：

```python
crawl_list_page.push(url)
crawl_detail_page.push(detail_url)
```

---

<h3> 总结</h3>

<h4> ❌ 为什么 Scrapy 代码不是直观的“平铺直叙”写法</h4>

| 特性         | Scrapy 框架      | 平铺直叙写法         |
|--------------|------------------|----------------------|
| **回调函数** | 多               | 代码集中、顺序执行   |
| **执行顺序** | 由调度器控制     | 上下文可控           |
| **yield**    | 必须             | `return` 或直接调用  |
| **并发**     | 全局 settings    | 局部可配置           |
| **入口结构** | 固定 `Spider` 类 | 任意函数             |
| **任务编排** | 不方便           | 灵活组合             |

---

<h4> 结论</h4>

1. **Scrapy 的设计理念是事件驱动 + 回调函数**，导致逻辑不直观。  
2. 多数 Python 程序员更习惯顺序化代码，而 Scrapy 的“分散回调”方式不符合直觉。  
3. **Scrapy 适合大规模分布式爬取**，但对小型项目，`requests + BeautifulSoup` 或 `asyncio` 更直观。  
4. 如果需要 **任务编排 + 平铺直叙的任务逻辑**，可以考虑 `funboost` 等任务队列框架。  
5. 总的来说，Scrapy 功能强大，但牺牲了代码的 **直观性和自由度**。

---

> **讨论：** 你觉得 Scrapy 的回调写法优雅吗？  
> 如果想尝试 **平铺直叙** 的写法，可以了解 `funboost` 框架。


</div>

## 8.9 仿scrapy api框架中无法完成的需求真实例子2，token有效期太短

举例一个 仿scrapy api框架中无法完成的需求真实例子。

根据data参数请求URL1生成sm_token，然后必须在10秒有效期内使用相同的data和获取到的sm_token请求URL2。

scrapy由于是url调度，一次只能调度请求一次，无法确保是在10秒内使用data得到的sm_token去请求url2。不管你是配置使用深度优先，还是加上priority，如果url2任务种子堆积了，会发生大面积延迟导致sm_token过期。

```python
import scrapy
import json
import time
from scrapy.exceptions import DropItem

class TokenSpider(scrapy.Spider):
    name = 'token_spider'
    
    def __init__(self, *args, **kwargs):
        super(TokenSpider, self).__init__(*args, **kwargs)
        # 需要处理的data列表
        self.data_list = ['data1', 'data2', 'data3']
    
    def start_requests(self):
        # 为每个data生成请求
        for data in self.data_list:
            url = f'https://example.com/api/gettoken?data={data}'
            yield scrapy.Request(
                url=url, 
                callback=self.parse_token,
                meta={'data': data}  # 传递data参数
            )
    
    def parse_token(self, response):
        # 获取传递的data
        data = response.meta.get('data')
        
        try:
            # 解析响应获取sm_token
            result = json.loads(response.text)
            sm_token = result.get('sm_token')
            
            if not sm_token:
                self.logger.error(f"未获取到data={data}的有效sm_token")
                return
            
            # 记录获取token的时间
            token_time = time.time()
            
            # 构建第二个请求
            url2 = f'https://example.com/api/getData?data={data}&sm={sm_token}'
            
            # 将data、token和时间传递给下一个回调
            yield scrapy.Request(
                url=url2,
                callback=self.parse_data,
                meta={
                    'data': data,
                    'sm_token': sm_token,
                    'token_time': token_time
                },
                priority=100  # 尝试提高优先级，但无法保证立即执行，因为url2的优先级都是100，堆积就会造成sm_token过期。
            )
            
        except Exception as e:
            self.logger.error(f"处理token响应时出错: {e}")
    
    def parse_data(self, response):
        # 获取传递的元数据
        data = response.meta.get('data')
        sm_token = response.meta.get('sm_token')
        token_time = response.meta.get('token_time')
        
        # 检查token是否已过期，  只能检查，而非确保啊。 url2 和url1调度是独立的，无法确保是在10秒内。
        current_time = time.time()
        if current_time - token_time > 10:
            self.logger.error(f"Data={data}的Token已过期! 耗时: {current_time - token_time}秒")
            # 这里可以尝试重新获取token，但逻辑会变得复杂
            raise DropItem("由于Token过期，丢弃此次请求数据")
            
        try:
            # 处理第二个请求的响应
            result = json.loads(response.text)
            # 收集数据
            yield {
                'data': data,
                'result': result,
                'token_elapsed': current_time - token_time
            }
        except Exception as e:
            self.logger.error(f"处理数据响应时出错: {e}")
```

funboost中实现这需求非常丝滑自然，因为funboost可以在一个函数内部连续请求两个url，可以确保在通过url1得到sm_token后的0.01毫秒内立即对url2发送请求。

```python
from funboost import boost, BrokerEnum, BoosterParams
import requests
import json
import time

@boost(BoosterParams(queue_name="token_task",broker_kind=BrokerEnum.REDIS_ACK_ABLE,qps=100, max_retry_times=3))
def process_with_token(data):
    """一个函数处理整个流程，逻辑清晰直观"""
   
    # 第一个请求：根据data获取对应的sm_token
    url1 = f"https://example.com/api/gettoken?data={data}"
    response1 = requests.get(url1, timeout=5)
    sm_token = response1.json()['sm_token']
    
    # 立即使用data和sm_token请求第二个URL
    # 这里无延迟，不经过任何调度器，保证token新鲜有效
    url2 = f"https://example.com/api/getData?data={data}&sm={sm_token}"
    response2 = requests.get(url2, timeout=5)
    # 处理并返回数据
    result = response2.json()
    print('保存result')
        

# 启动爬虫
if __name__ == "__main__":
    # 发布任务
    data_list = ['data1', 'data2', 'data3', 'data4', 'data5']
    for data_item in data_list:
        process_with_token.push(data_item)
    
    # 启动消费者处理任务
    process_with_token.consume()
```

两者在此需求实现上对比对比分析：

<table style="width:100%; border-collapse:collapse; text-align:center;">
  <thead>
    <tr style="background-color:#f2f2f2;">
      <th style="padding:8px; border:1px solid #ddd; text-align:left;">特性</th>
      <th style="padding:8px; border:1px solid #ddd; text-align:center;">Scrapy</th>
      <th style="padding:8px; border:1px solid #ddd; text-align:center;">Funboost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">代码行数</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">~70行</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">~35行</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">执行流程</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">分散在3个回调函数中</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">集中在1个函数内</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">状态传递</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">通过meta字典在多个回调间传递</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">直接使用变量，自然清晰</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">token时效性</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">只能被动检查是否过期，可能数据丢失</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">立即使用，几乎0延迟，确保有效</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">错误处理</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">分散在多处，难以全面处理</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">集中在一个try-except内</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">可读性</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">需要在多个函数间跳转理解逻辑</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">从上到下线性阅读，一目了然</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">可维护性</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">修改需考虑多处回调关系</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">修改只需要关注一个函数</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; text-align:left;">调试难度</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">高，难以跟踪完整流程</td>
      <td style="padding:8px; border:1px solid #ddd; text-align:center;">低，标准函数调试方式</td>
    </tr>
  </tbody>
</table>


funboost在这个特殊需求上优势总结：
```
Funboost在处理这类"根据data获取token并立即使用"的爬虫场景时表现卓越：
连续执行保证：两次请求在同一函数内连续执行，保证token不会过期
无状态传递困扰：不需要通过meta字典在回调间传递状态
直观的流程控制：整个处理流程遵循自然的编程思维
更简单的数据处理：直接在函数内处理和返回结果
对于具有严格时效性要求的爬虫任务，特别是需要多步骤请求且后续请求依赖前序请求结果的场景，
Funboost的优势变得尤为明显，让复杂的爬虫任务回归到简单直观的函数式编程模型。
```

## 8.10 scrapy的 response.meta 字典传参无法ide自动补全提示

Scrapy的meta字典在ide中完全无法补全提示：
```
meta是无类型字典，IDE无法知道里面有什么键
没有自动补全提示 response.meta.get('???')
拼写错误不会在编写时被捕获，如token_tiem而不是token_time
忘记在上一个回调中传递某个键值对也不会有警告
需要不断查看或记忆上下文中传递了哪些数据
```

```
上面8.9例子中的 parse_token 方法中

yield scrapy.Request ，需要在meta中把各个有用的变量信息传递给下一个解析方法

yield scrapy.Request(
    url=url2,
    callback=self.parse_data,
    meta={
        'data': data,
        'sm_token': sm_token,
        'token_time': token_time
    },
    priority=100  
)


在 parse_data 方法中，很容易出错
def parse_data(self, response):
        # 获取传递的元数据
        # IDE不知道meta中有什么，无法提示
        data = response.meta.get('data') # 如果你拼错为'dta'也不会有警告，只有到运行后才能知道写错了
        sm_token = response.meta.get('sm_token') # 如果上一步忘记传sm_token，ide在这里不会提前发现
        token_time = response.meta.get('token_time') # 如果上一步改了token_time的名字，这里ide不能自动改名字          


```

funboost函数中的局部变量优势：
```
局部变量有类型信息，IDE能提供完整自动补全
变量名拼写错误会立即被标红
未定义的变量会被IDE立即标识
重构变量名时会同步修改所有引用
```

能否在ide自动补全提示的实际影响:
```
在实际开发中，这种差异会导致：
开发效率差异：
funboost开发速度更快，减少查看文档或代码回溯
Scrapy需要更多的代码审查和测试才能捕获拼写错误
错误出现时机：
funboost的错误多在编码阶段被IDE捕获
Scrapy的错误往往在运行时才发现，调试成本更高
维护和重构：
funboost更易重构，变量改名会全局同步
Scrapy修改meta键名需手动检查所有回调函数
这种看似小的开发体验差异在大型爬虫项目中会带来显著的生产力和代码质量差异，特别是在团队协作或长期维护的场景下。
```


## 8.11 funboost中反爬虫换代理ip 请求头 破解等 容易程度暴击专用爬虫框架scrapy

需要大力驳斥 "专用框架=更方便" 的误解

### 8.11.1 scrapy中换代理ip和请求头代码
```python
# Scrapy的下载器中间件
class RotateUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(USER_AGENTS)

class ProxyMiddleware:
    def __init__(self, proxy_list: list[str]):
        self.proxy_list = proxy_list

    @classmethod
    def from_crawler(cls, crawler):
        """Scrapy 会自动调用此方法创建中间件实例"""
        proxy_list = crawler.settings.get("PROXY_LIST", [])
        return cls(proxy_list=proxy_list)

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        request.meta['proxy'] = proxy
        
    def process_response(self, request, response, spider):
        # 获取当前重试次数
        retry_times = request.meta.get('retry_times', 0)
        
        if response.status == 403 and retry_times < 3:  # 限制最多重试3次
            request.meta['proxy'] = self.get_new_proxy()
            request.meta['retry_times'] = retry_times + 1
            return request
        return response


# 并需要在Scrapy的settings.py中注册中间件
DOWNLOADER_MIDDLEWARES = {
   'myproject.middlewares.RotateUserAgentMiddleware': 400,
   'myproject.middlewares.ProxyMiddleware': 500,
}
```

```
scrapy这个换代理ip代码看起来代码量不大，实则超级复杂。如果不去网上百度找个别人写好的例子，
99%的爬虫人员抓破脑袋也绝对写不出来，
用户完全是懵逼的，为什么要这么写。
为什么要定义一个类，为什么类必须是有 def process_request(self, request, spider): 方法 ,
如果方法名字不是这样，入参个数少了或多了，还能运行吗？ 用户为什么知道 
还要写  'myproject.middlewares.RotateUserAgentMiddleware': 400,这么个玩意？
这个字符串是什么？这个数字又是什么，随便乱写个数字行不行？
```

所以有人说scrapy框架是专用爬虫框架，所以优势是能反爬，能支持换代理ip和请求头。说funboost不是专用爬虫框架，所以反爬是对scrapy有劣势，这个是绝对的谬论，真实情况是如果仅靠自己琢磨而不去百度别人的scrapy咋写的换代理ip，在scrapy框架中换代理难如登天。

### 8.11.2 用户自己自由封装一个换代理ip和请求头的request函数，自然又简单

funboost 不是专用爬虫框架，但基于funboost的 boost_spider 爬虫开的 RequestClient 支持自动换代理ip和请求头，支持xpath解析。

即使是直接用funboost爬虫，用户自己自由封装一个换代理ip和请求头的request函数，自然又简单，爬虫小白初学1天都能轻松自然封装出来。比scrapy中那种莫名其妙的def process_request(self, request, spider)写法更容易百倍。

用户封装一个换代理ip和请求头的request函数如下：
```python
import requests

def my_request(method,url):
    proxy = random.choice(proxy_list)
    user_agent = random.choice(user_agent_list)
    return requests.request(method,url,proxies=proxy,headers={'user-agnet':user_agent})
           
```

```
这个 my_request 换代理ip和请求头的函数代码自由而又简单直观，只要是个pythoner都能看得懂，
只要是个pythoner都能使用自然而然的直觉思维 很轻松容易的写出来。 
因为你在封装这个函数时候，完全绝对和funboost没有半毛钱关系，你不需要了解funboost的流程就能封装出来。
而且不想用funboost了，你这个写的函数还是有意义可以继续用的。
如果你不想用scrapy了，那个ProxyMiddleware代码就成了废物代码。

用户自己封装的 my_request 函数 能方便的进行独立单元测试，而scrapy的ProxyMiddleware类用户无法单独单元测试验证，必须在scrapy框架整体运行起来才能测试得了。
```

### 8.11.3 为什么scrapy换代理IP和请求头的高难度分析my_request

首先是你必须非常的精通Scrapy完整流程，才能流畅的改造scrapy
```
核心组件
Engine: 引擎，负责控制数据流在系统中所有组件间的流动
Scheduler: 调度器，接收引擎发来的请求并排序、入队，当引擎需要时提供请求
Downloader: 下载器，获取网页内容并返回给引擎
Spider: 爬虫，解析响应并提取数据，产生新的请求
Item Pipeline: 项目管道，处理Spider提取的数据
Middleware: 中间件，包括下载器中间件和Spider中间件
数据流向
Engine向Spider请求第一个URL
Engine从Spider获取第一个请求
Engine将请求发送给Scheduler调度
Scheduler返回下一个请求给Engine
Engine通过Downloader Middleware发送请求给Downloader
页面下载完成后，Downloader生成响应并通过Downloader Middleware发给Engine
Engine将响应通过Spider Middleware发送给Spider处理
Spider处理响应并返回提取的数据及新的请求给Engine
Engine将数据发送给Item Pipeline，将新请求发给Scheduler
重复步骤4-9直到没有请求
执行过程
创建Scrapy项目：scrapy startproject myproject
定义Spider类，包含start_urls和解析方法
运行爬虫：scrapy crawl myspider
框架自动加载配置、初始化组件
按数据流向处理请求和响应
数据经由Pipeline处理后存储
中间件拦截点
Downloader Middleware:
process_request: 请求发送到下载器前
process_response: 响应返回Spider前
process_exception: 下载异常时
Spider Middleware:
process_spider_input: Spider处理响应前
process_spider_output: Spider产生结果后
process_spider_exception: Spider异常时
Scrapy的强大和复杂性正源于这种多组件交互的设计模式，但也因此增加了学习难度。
```

其次要说明为什么scrapy换代理IP和请求头的难度高，为什么难度远超使用requests换代理ip和请求头
```
1. 中间件机制的概念理解障碍
特殊方法名要求：必须准确实现process_request、process_response等方法
约定优于配置：这些方法名不是由用户自由选择，而是框架强制要求的
不明显的执行流程：用户难以直观理解请求从Spider到Downloader的完整路径
方法参数固定：必须接受固定参数(self, request, spider)，不能随意调整
2. 配置分散性导致的认知负担
多文件依赖：修改需要同时编辑middlewares.py和settings.py
导入路径字符串：需要以字符串形式指定中间件路径，容易出错
数字优先级系统：需理解400、500这类数字代表执行顺序，且没有明确文档说明最佳实践
3. 特殊对象和属性的学习成本
request.meta字典：使用非直观的meta字典传递信息
代理格式要求：必须以特定格式设置代理request.meta['proxy'] = 'http://ip:port'
框架特有对象：需理解Request、Response等Scrapy特有对象的行为
4. 调试复杂性
堆栈追踪困难：错误发生在框架内部，难以定位问题
隐式执行顺序：中间件执行顺序不直观，调试困难
状态保持挑战：在不同中间件间传递状态需使用meta字典
5. 文档和学习资源局限
分散的文档：需阅读多个文档章节才能完整理解
官方示例不足：官方文档缺乏完整的代理切换实例
依赖社区示例：大多数用户需依赖StackOverflow等外部资源
相比之下，funboost中实现同样功能只需编写普通Python函数，使用标准try-except处理错误，不需要学习特殊的框架概念，完全符合Python程序员的直觉思维模式。
```

那些说 funboost 不是专用爬虫框架，从而就得出结论是肯定在反爬虫方面不如scrapy方便，绝对是谬论。真实情况是scrapy源码从来都没有内置自带自动反爬虫功能；scrapy中因为框架的写法约束死板，实现这些反而难度更高而不是更简单。

## 8.12 scrapy 可直接运行测试验证性很差

**scrapy不可直接测试运行深层级爬虫**
一个三层级网站爬虫,例如列表页->详情页->评论页，scrapy你怎么单独直接验证第三层级的爬虫请求和解析呢？只有spider整体运行起来，然后观察第三层级解析。 (这样第三层级爬虫会要等很久,并且被不相干的第一二层级爬虫输出干扰)  
1）scrapy的爬虫逻辑分散在Spider类的多个回调方法（如parse、parse_detail、parse_third_level）中。   
2）这些回调方法依赖于框架的Request/Response对象、meta字典、调度器等上下文，无法直接在IDE里单独调用。  
3）你想单独测试第三层级的解析，只能整体运行spider，等到第三层级回调被调度时，观察输出或日志，调试效率极低。  
4) 很多人只能先单独临时写个requests请求的函数验证，然后再改成到scrapy写法，造成重复劳动。   

**funboost 被@boost的函数能直接调用运行测试**
而funboost的第三层级的爬虫函数，crawl_thrid_level_page(article_id,user_id,page_index) 可以直接调用运行，可直接测试性秒杀scrapy。

```python
@boost(BoosterParams(queue_name='third_level_queue'))
def crawl_third_level_page(article_id, user_id, page_index):
    # ...爬虫逻辑...
    return "ok"

# 能直接运行
result = crawl_third_level_page('a123', 'u456', 1)
print(result)
```

## 8.13 funboost 断点接续运行能力吊打scrapy-redis 的 blpop （funboost支持确认消费）

不要以为你使用个 scrapy-redis 就万事大吉了，就和 funboost 的断点续爬一样强大了，scrapy在下面两种场景100%会丢失大量数据。
### 8.13.1 为什么 funboost的断点续爬完胜 scrapy-redis的断点续爬(防丢数据1)

scrapy-redis 是基于 redis.blpop() ,BLPOP 的特性是一旦弹出，该元素就从列表中移除了。框架会弹出大量url种子到内存中，然后并发请求。如果你随意重启代码 进程崩溃/断电/强制关机，那么已取出来的url种子就丢失了，如果你把重要的导航页或者列表页丢失了，那就会丢失几十万个详情页页面，太悲催了，需要你反复人工添加种子，反复爬十几次才能爬全，太累了。


而funboost支持40种消息队列，其中很多种是broker服务端天生支持消费确认的，例如rabbitmq中间件。 用户可以毫无顾忌的随意重启代码和强制断电关机，没运行完成的消息是不会确认消费的，所以不会丢失。 
即使用户没安装 rabbitmq 这种高级消息队列，用户使用 broker_kind =BrokerEnum.REDIS_ACK_ABLE 等各种redis模式，也是支持确认消费的，不惧怕用户随意重启代码造成大批已取出到内存中的消息丢失。


### 8.13.2 funboost的函数重试功能远远暴击scrapy的url重试功能(防丢数据2)

scrapy的重试是url重试，如果url请求成功，http状态码是200，但页面内容提示反扒了，页面此时不是返回的正常的内容，导致你解析出错，scrapy的url重试是无效的。

而funboost 的爬虫函数 被 @boost 装饰后，funboost 会自动重试，重试次数和间隔时间可以自由设置。如果页面反扒了，函数里面运行解析的代码会出错，funboost 会自动重试，你不需要提前规划判断返回了什么内容是属于被反扒了，funboost 会自动重试。


**所以funboost 只要启动爬一次，可以做到完全不漏数据，而scrapy-redis 需要反复重启爬虫，反复添加种子，反复爬十几次才能爬全，funboost 简直轻松太多了**



## 8.14 其他funboost 吊打 scrapy原因 详细介绍
### 8.14.1 为什么funboost的去重功能远远吊打scrapy的Request对象指纹去重？

#### 8.14.1.1 funboost 支持有效期过滤

funboost 支持有效期过滤，例如1个月内相同productid过滤，一个月后仍然重新运行爬取，适合周期更新爬取。
scrapy无此功能，scrapy需要手动清理去重集合。

#### 8.14.1.2 scrapy无法过滤url中的噪音入参，例如ts时间戳，rd随机数，追踪来源id

funboost是函数入参过滤而非url过滤，稳如泰山。 scrapy最头疼的url入参或者post入参有噪音多余字段。

假设 
url1 是  www.site1.com/product/123456/?a=1&b=2&_ts=17136952568&_rand=0.6254395 ， 
url2 是 www.site1.com/item/321?&timestamp=17136952568&r=0.6254395 ，
url3 是 www.site2.com/user/ post入参是 {user:123 ts:1721568556 ssid:1234567890 } ，
其中url1的_ts和_rand是噪音多余字段，url2的timestamp和r是噪音多余字段，url3的和ts和ssid是噪音多余字段。

funboost是过滤函数入参，天然无此问题
```
funboost 的函数入参过滤功能，可以轻松过滤掉url1和url2的噪音多余字段，而scrapy的url去重功能无法过滤掉url1和url2和url3的噪音多余字段。

因为funboost的函数是 def craw_product(product_id,a,b) ， funboost 是根据 product_id,a,b去重，天然无视 _ts 和 _rand 没用的噪音入参。
funboost 没有规定入参必须是url。
```

scrapy中无视Request的噪音难如登天，需要你手动自定义继承一个RFPDupeFilter，然后重写 def request_fingerprint(self, request):

```python
import hashlib
import json
import re
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from scrapy.utils.python import to_bytes
from scrapy.dupefilters import RFPDupeFilter
from scrapy.http import FormRequest, JsonRequest


class SmartFingerprintPerPattern(RFPDupeFilter):
    def request_fingerprint(self, request):
        url = request.url
        method = request.method.upper()

        # 从 settings 读取正则规则配置
        pattern_rules = {
            r'^https?://www\.site1\.com/product/\d+': ['_ts', '_rand'],
            r'^https?://www\.site1\.com/item/\d+': ['timestamp', 'r'],
            r'^https?://www\.site2\.com/user/?$': ['ts', 'ssid'],
        }

        # 匹配正则，提取对应 ignore 参数
        ignore_keys = []
        for pattern, keys in pattern_rules.items():
            if re.match(pattern, url):
                ignore_keys = keys
                break

        # ----------- 清洗 URL Query 参数 -----------
        parsed = urlparse(url)
        query = parse_qsl(parsed.query, keep_blank_values=True)
        filtered_query = [(k, v) for k, v in query if k not in ignore_keys]
        cleaned_query = urlencode(filtered_query, doseq=True)
        cleaned_url = parsed._replace(query=cleaned_query)
        cleaned_url_str = urlunparse(cleaned_url)

        # ----------- 清洗 POST 请求 Body 参数 -----------
        post_body_fingerprint = b''
        if method == 'POST':
            try:
                if isinstance(request, JsonRequest):
                    data = json.loads(request.body.decode())
                elif isinstance(request, FormRequest):
                    raw = request.body.decode()
                    data = dict(parse_qsl(raw))
                else:
                    data = {}
            except Exception:
                data = {}

            filtered_data = {k: v for k, v in data.items() if k not in ignore_keys}
            post_body_fingerprint = to_bytes(json.dumps(filtered_data, sort_keys=True))

        # ----------- 构造最终指纹 -----------
        fp_parts = [
            to_bytes(method),
            to_bytes(cleaned_url_str),
            post_body_fingerprint
        ]

        return hashlib.sha1(b''.join(fp_parts)).hexdigest()

```

然后你要配置scrapy的settings.py
```python
DUPEFILTER_CLASS = 'your_project.dupefilters.SmartFingerprintPerPattern' 
```

scrapy 需要这样写代码，先手动一个个的把噪音入参找出来，如果改版了，url自动多了一个噪音入参或其他不重要的入参，你还得改代码，不然去重就失效了。

**通过对比，结论就是scrapy对请求入参种中带随机数和时间戳的去重需要根据各种url正则自,定义RFPDupeFilter太麻烦了，scrapy内置的去重能力弱爆了。**
**你用scrapy而不用funboost，你不忙的吐血谁吐血，你不住icu谁住icu**


### 8.14.2 详细驳斥 Scrapy 插件生态丰富，质疑Funboost 没有三方扩展

Scrapy 插件多 ≠ 框架强，恰恰说明了框架对用户自由的压制太多，“什么都得经过官方那一套”。      
Funboost 是函数式的框架，自由度高、无约束、无钩子、无上下文依赖，天然就能融合任何三方库。     


```
答： scrapy是框架太复杂了约束多钩子多，所以需要由专门的大神开发三方插件，因为普通人写不出来这些插件。  
Scrapy 框架的结构设计“高度抽象 + 强约束 + 多钩子生命周期 + 中间件堆叠机制”，导致插件开发成本极高。
funboost 恰恰不需要插件，因为用户是轻松自由使用任意三方包。
你压根不需要专门的大神给你写个例如 funboost-selenium 类似的插件，才能开始在funboost里面使用selniuem干活，懂了吗？

例如 如 scrapy-redis 用于分布式、scrapy-playwright 或 scrapy-selenium 用于 JavaScript 渲染，scrapy-user-agents换请求头。 
funboost需要学习这些扩展插件怎么使用吗？ 绝对不需要，funboost 是顺其自然自由使用任意三方包。。
麻烦你去看看配置使用 scrapy-selenium 有多麻烦，而直接使用 seleium 有多简单。
本来学习selenium就烦人，你还要再多学习一个 scrapy-selenium ，
凭什么非要这么苦逼，学了各种三方包还不够，还需要额外再另外学这么多三方包的插件。
```

因为你用scrapy，即使你非常精通三方包，如果没有美国大神给你提供三方包的插件，你仍然寸步难行，所以你羡慕scrapy有各种三方包的插件生态。         
你用Scrapy，哪怕精通三方包，没有插件也寸步难行；用Funboost，任何三方包都能直接用，不需要等别人给你造插件轮子。     
当你可以直接驾驶F1赛车时，为什么还非要学习如何给破自行车安装火箭推进器？
```
举个例子：
为什么你用scrapy-redis插件？因为你就算精通了py-redis包的用法，精通了怎么redis.blpop redis.lpush推拉消息，精通了怎么redis.sadd 去重  
但是你不知道怎么完美替代scrapy内置的调度器和去重器，因为你不可能开发的出来，关键难度不是怎么操作reids，而是难以适配scrapy懂了吗?  
不信的你可以看scrapy-redis源码,你能写得了那么好？
你以为你随便在代码哪里简单的写个redis.blpop 和 redis.lpush，scrapy就能完美使用redis队列来调度运行起来吗？
```

```
举个例子2：
为什么你用scrapy-playwright插件？因为你就算精通了playwright包的用法，
精通了怎么playwright.launch playwright.new_page playwright.goto playwright.evaluate playwright.close
精通了怎么playwright.evaluate 执行js代码，但是你能用它完美取代scrapy内置的下载器吗？
```

<div class="inner_markdown">

<h3>🚧 为什么 Scrapy 扩展难？五大核心原因</h3>

---

<h3>1. 生命周期复杂，插件必须“插入钩子”才能工作</h3>

Scrapy 插件大多围绕 `downloader middleware`、`spider middleware`、request/response 钩子等接口注入逻辑。

你必须理解：

* request 发送前 → 哪个钩子可以修改 headers？
* response 到达后 → 是哪个中间件先执行？
* Retry、Redirect、Cookies、Compression 谁先谁后？

**问题**：你不理解 Scrapy 的内部执行流程，就无法写对钩子函数 —— 插件不是写就能用，而是得“插”在正确生命周期点。

---

<h3>2. 插件必须与 Scrapy 的 Request/Response 对象深度耦合</h3>

Scrapy 的 `Request` 和 `Response` 是自定义类，拥有 `.meta`、`.cb_kwargs`、`.dont_filter` 等大量特有字段。

如果你写插件想扩展 Request，比如：

* 添加一个 retry 计数
* 添加一个 render 参数用于 Playwright 渲染
* 给 Response 加一个 `.screenshot` 字段

你必须继承原始类或 monkey patch，写起来繁琐且容易冲突。

---

<h3>3. 插件与配置高度耦合，用户配置复杂</h3>

Scrapy 插件不仅要写代码，还必须让用户：

* 修改 `settings.py` 加入新的扩展路径
* 配置中间件优先级，例如 `DOWNLOADER_MIDDLEWARES` 顺序错误会失效
* 写复杂的 `custom_settings` 兼容不同爬虫用不同插件参数

**问题**：插件开发者不仅要写功能逻辑，还要预设一整套配置方式，增加学习和使用门槛。

---

<h3>4. 插件难以“平滑复用现有第三方库”</h3>

比如你想用 selenium、playwright、requests-html、httpx：

* 不能直接调用它们，而必须封装成 Scrapy 兼容组件
* 因为 Scrapy 有自己异步调度、队列、request/response 栈等模型
* 所以必须写类似 `scrapy-playwright` 这样的插件，包装一层

**问题**：写插件变成了“兼容性工程”，不是功能开发。

---

<h3>5. 插件难以组合，容易相互冲突</h3>

Scrapy 插件共享全局的 request/response 链条，会出现：

* 多个插件改动相同的 `.meta` 字段
* 优先级错误导致插件不生效
* 插件对 request 的 retry/delay/priority 冲突互相覆盖

**问题**：插件之间没有解耦机制，写得多了越容易打架。

---

<h3>✅ 总结一句话</h3>

> Scrapy 插件难写，是因为它太“工程化、钩子化、封闭化”，**写一个插件 = 理解整个 Scrapy 的生命周期模型 + 中间件堆栈机制 + 内部对象结构 + settings 配置机制。**

Funboost 完全不需要插件机制——用户只需写普通 Python 函数，天然支持任意三方库调用，零框架束缚，真正自由开发。

---
</div>

## 8.30 为什么 funboost 能用于爬虫 的本质原因

首先你自己要清楚你为什么要用 scrapy 爬虫框架 而不是 requests 请求包， 最根本原因是因为scrapy url请求自动调度系统牛逼, 

requests 包只是请求，不能自动调度和并发，如果你封装不了可复用调度系统，那就需要每个爬虫都临时重复写url种子怎么流转 请求怎么多线程并发 怎么分派请求 。

因为用户封装一个可复用的 my_request 的 请求函数实现换ip 请求头小菜一碟；但用户自己来封装一个可复用爬虫调度 那难度就大太多了。

而如果你用 funboost 来爬虫， 就是已经帮你解决了其中最难封装的 自动调度系统，这意味着开发者可以将精力完全聚焦于编写核心的爬虫业务逻辑（如请求发送、页面解析、数据提取和存储），而将复杂的并发管理、分布式协调、任务可靠性保证等底层调度难题完全交给Funboost，从而极大地降低了开发门槛和心智负担。 

封装可复用http请求函数，面向过程几乎就可以; 封装可复用的爬虫调度系统，非常考验设计模式 面向对象。

* 封装 **http请求函数** 和封装 **爬虫调度系统** ，两种封装任务在**复杂度**和**所需编程范式**上的本质区别：

1.  **封装一个请求函数（Encapsulating a Request Function）:**
    *   **面向过程足够：** 确实如此。一个请求函数的逻辑通常是线性的：准备参数 -> 发送请求 -> 处理响应 -> 处理异常 -> 返回结果。这完全可以用一系列步骤（过程）来描述和实现。即使加入重试、代理、UA切换等逻辑，也可以通过 `if/else`、循环和辅助函数来组织，不一定需要复杂的对象结构。其状态相对简单，依赖关系清晰。

2.  **封装可复用的爬虫（或通用任务）调度系统（Encapsulating a Reusable Scheduler）:**
    *   **考验设计模式和面向对象：** 这绝对是事实。一个调度系统需要处理众多复杂且相互交织的关注点（并发、队列、可靠性、分布式、控频、错误处理、监控等）。
        *   **面向对象（OOP）** 在这里变得至关重要：
            *   **抽象 (Abstraction):** 需要定义清晰的接口（例如任务队列接口 `QueueInterface`、任务处理器接口 `TaskProcessorInterface`）来隐藏不同实现的复杂性。
            *   **封装 (Encapsulation):** 需要将相关的状态和行为组合在一起（例如一个 `Task` 对象包含其数据和生命周期状态，一个 `RateLimiter` 类管理速率控制逻辑）。
            *   **多态 (Polymorphism):** 允许轻松替换核心组件（例如切换不同的任务队列实现或并发执行策略）。
            *   **继承 (Inheritance):** 可用于创建基础组件（如 `BaseTask`）和针对特定场景的具体实现。
        *   **设计模式 (Design Patterns)** 为构建这样复杂的调度系统提供了成熟的解决方案：
            *   **策略模式 (Strategy):** 用于灵活选择不同的并发执行模式（如多线程、协程）或失败重试策略。
            *   **工厂模式 (Factory):** 用于创建不同类型的任务实例 (`Task` objects) 或消息队列处理器 (`message queue handlers`)。
            *   **观察者模式 (Observer):** 用于实现系统状态监控、日志记录和事件通知。
            *   **适配器模式 (Adapter):** 用于兼容不同消息队列库（如Redis, RabbitMQ, Kafka）的API，提供统一接口。
            *   **状态模式 (State):** 用于管理任务在其生命周期中可能经历的复杂状态转换（如等待、运行、成功、失败、重试中）。
            *   **单例模式 (Singleton):** 常用于管理全局配置、数据库连接池或共享的限流器实例。

    *   没有OOP和设计模式的帮助，试图用纯面向过程的方式构建一个如此复杂的系统，几乎不可避免地会导致代码难以维护、扩展和理解，变成所谓的"面条代码"。

**总结：**


*   封装**请求函数**是对**具体操作**的封装，其复杂度通常在可控范围内，**面向过程**往往够用。
*   封装**调度系统**是对**复杂流程和系统行为**的封装，涉及多组件协作、状态管理、资源协调 等，其复杂度**天然地需要面向对象和设计模式**来驾驭。

这再次印证了为什么构建像Funboost这样的框架是一项复杂的系统工程，而不仅仅是"写几个函数"那么简单。它需要深厚的软件设计功底。而Funboost正是将这份深厚的功力凝聚其中，为开发者提供了一个简洁而强大的万能开发利器（万能就一定能包含爬虫）。




## 8.40 集中总结的 Funboost vs. Scrapy 优势快速对比 (表格版)

这30个原因主要围绕 **“自由编程 降维打击 框架奴役”** 的核心思想展开，即 `funboost` 通过其通用的函数调度能力，赋予开发者极大的自由度，从而在灵活性、易用性和功能强大性上超越了 `Scrapy` 这种专用但受限的框架。


<style>
    .funboost-scrapy-comparison-table {
        width: 100%;
        border-collapse: collapse;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        font-size: 14px;
        line-height: 1.5;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .funboost-scrapy-comparison-table th, .funboost-scrapy-comparison-table td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
        vertical-align: top;
    }
    .funboost-scrapy-comparison-table thead th {
        background-color: #f2f2f2;
        font-weight: 600;
        text-align: center;
    }
    .funboost-scrapy-comparison-table tbody td:first-child {
        font-weight: 600;
        vertical-align: middle;
        text-align: center;
        /* 不设置背景色，让其跟随主题变化 */
    }
    .funboost-scrapy-comparison-table tbody td:nth-child(2) {
        font-weight: 600;
        /* 不设置背景色，让其跟随主题变化 */
    }
    /* Funboost 优势列 - 绿色背景 */
    .funboost-scrapy-comparison-table .funboost-advantage {
        background-color: #dcfce7 !important; /* 绿色背景 */
    }
    /* Scrapy 劣势列 - 红色背景 */
    .funboost-scrapy-comparison-table .scrapy-disadvantage {
        background-color: #fee2e2 !important; /* 红色背景 */
    }
    .funboost-scrapy-comparison-table code {
        background-color: #eee;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    }
</style>

<table class="funboost-scrapy-comparison-table">
    <thead>
        <tr>
            <th>类别</th>
            <th>维度</th>
            <th>Funboost 优势 (函数调度，自由无限)</th>
            <th>Scrapy 劣势 (URL调度，框架束缚)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="5"><strong>核心理念与架构 (1-5)</strong></td>
            <td><strong>1. 调度核心</strong></td>
            <td class="funboost-advantage"><strong>函数调度</strong>：调度的是一个完整的、可执行的Python函数，内部逻辑完全自由。</td>
            <td class="scrapy-disadvantage"><strong>URL请求调度</strong>：调度的是一个 <code>Request</code> 对象，开发者被限制在框架的请求-响应生命周期内。</td>
        </tr>
        <tr>
            <td><strong>2. 编程范式</strong></td>
            <td class="funboost-advantage"><strong>自由编程</strong>：采用平铺直叙、一气呵成的同步思维编写函数，逻辑连贯清晰。</td>
            <td class="scrapy-disadvantage"><strong>回调地狱</strong>：强制使用 <code>yield Request</code> 和 <code>callback</code> 函数，逻辑被拆分得支离破碎，难以理解和维护。</td>
        </tr>
        <tr>
            <td><strong>3. 状态管理</strong></td>
            <td class="funboost-advantage"><strong>极其简单</strong>：在函数内使用普通的局部变量即可轻松管理状态，符合直觉。</td>
            <td class="scrapy-disadvantage"><strong>极其繁琐</strong>：必须通过 <code>response.meta</code> 字典在回调函数之间传递状态，易出错且IDE无法补全提示。</td>
        </tr>
        <tr>
            <td><strong>4. 框架侵入性</strong></td>
            <td class="funboost-advantage"><strong>极低</strong>：只需一个 <code>@boost</code> 装饰器，不改变函数原有结构，可轻松集成任何老代码。</td>
            <td class="scrapy-disadvantage"><strong>极高</strong>：必须继承 <code>scrapy.Spider</code>，重写 <code>parse</code> 等方法，代码与框架深度耦合，迁移成本高。</td>
        </tr>
        <tr>
            <td><strong>5. 架构思想</strong></td>
            <td class="funboost-advantage"><strong>降维打击</strong>：用通用的万能函数调度框架解决特定的爬虫问题，功能更全，更灵活。</td>
            <td class="scrapy-disadvantage"><strong>作茧自缚</strong>：专为爬虫设计，但其设计限制了其处理复杂和非标准场景的能力。</td>
        </tr>
        <tr>
            <td rowspan="7"><strong>开发效率与易用性 (6-12)</strong></td>
            <td><strong>6. 学习曲线</strong></td>
            <td class="funboost-advantage"><strong>极其平缓</strong>：只需学习 <code>@boost</code> 装饰器的用法，几分钟即可上手。</td>
            <td class="scrapy-disadvantage"><strong>极其陡峭</strong>：需要学习Spider、Item、Pipeline、Middleware、Settings等多个组件和复杂的生命周期。</td>
        </tr>
        <tr>
            <td><strong>7. 代码量与文件结构</strong></td>
            <td class="funboost-advantage"><strong>极其精简</strong>：单文件即可完成一个复杂的分布式爬虫，代码量极少。</td>
            <td class="scrapy-disadvantage"><strong>极其臃肿</strong>：一个简单的爬虫也需要创建7-8个文件，开发者需在多个文件间频繁切换。</td>
        </tr>
        <tr>
            <td><strong>8. HTTP库选择</strong></td>
            <td class="funboost-advantage"><strong>完全自由</strong>：可在函数内随意使用 <code>requests</code>, <code>httpx</code>, <code>aiohttp</code>, <code>selenium</code>, <code>playwright</code> 等任何库。</td>
            <td class="scrapy-disadvantage"><strong>受限</strong>：强制使用其内置的基于 <code>Twisted</code> 的下载器，想用其他库需要复杂的中间件封装。</td>
        </tr>
        <tr>
            <td><strong>9. 反爬与自定义请求</strong></td>
            <td class="funboost-advantage"><strong>极其简单</strong>：封装一个通用的 <code>my_request</code> 函数即可实现换IP、UA等逻辑，0门槛。</td>
            <td class="scrapy-disadvantage"><strong>极其复杂</strong>：必须编写和注册下载器中间件（<code>Downloader Middleware</code>），概念复杂，对新手极不友好。</td>
        </tr>
        <tr>
            <td><strong>10. 单元测试</strong></td>
            <td class="funboost-advantage"><strong>极其容易</strong>：每个被 <code>@boost</code> 装饰的函数都可以直接调用，独立进行单元测试。</td>
            <td class="scrapy-disadvantage"><strong>极其困难</strong>：Spider的回调方法与框架上下文强耦合，难以进行独立的单元测试。</td>
        </tr>
        <tr>
            <td><strong>11. IDE代码补全</strong></td>
            <td class="funboost-advantage"><strong>全面支持</strong>：函数参数、<code>push</code>/<code>publish</code> 方法均有代码补全，开发效率高。</td>
            <td class="scrapy-disadvantage"><strong>几乎为零</strong>：<code>response.meta</code> 是字典，IDE无法提供任何键的补全提示，极易出错。</td>
        </tr>
        <tr>
            <td><strong>12. 调试</strong></td>
            <td class="funboost-advantage"><strong>简单直观</strong>：线性执行的函数逻辑，使用标准 <code>pdb</code> 或IDE调试器即可轻松调试。</td>
            <td class="scrapy-disadvantage"><strong>困难</strong>：回调链和异步执行流程使得调试非常困难，难以跟踪任务的完整生命周期。</td>
        </tr>
        <tr>
            <td rowspan="10"><strong>功能强大性与灵活性 (13-22)</strong></td>
            <td><strong>13. 并发模型</strong></td>
            <td class="funboost-advantage"><strong>更强悍（叠加模式）</strong>：轻松实现多进程 + (多线程/协程) + 多机器的四重叠加并发，性能炸裂。</td>
            <td class="scrapy-disadvantage"><strong>有限</strong>：并发主要由 <code>CONCURRENT_REQUESTS</code> 控制，难以充分利用多核CPU。</td>
        </tr>
        <tr>
            <td><strong>14. 速率控制</strong></td>
            <td class="funboost-advantage"><strong>更精准（QPS控制）</strong>：可精确控制每秒请求次数（QPS），无视响应时间波动。</td>
            <td class="scrapy-disadvantage"><strong>不精确（并发数控制）</strong>：只能控制并发请求数，无法保证稳定的请求速率。</td>
        </tr>
        <tr>
            <td><strong>15. 复杂流程处理</strong></td>
            <td class="funboost-advantage"><strong>极其自然</strong>：可在单个函数内完成多轮浏览器交互、API调用等复杂连续操作。</td>
            <td class="scrapy-disadvantage"><strong>几乎无法实现</strong>：用回调处理多步连续操作非常笨拙，甚至会导致异步模型失效。</td>
        </tr>
        <tr>
            <td><strong>16. 短时效Token处理</strong></td>
            <td class="funboost-advantage"><strong>轻松解决</strong>：可在函数内连续请求，确保获取Token后立即使用，保证时效性。</td>
            <td class="scrapy-disadvantage"><strong>无能为力</strong>：无法保证两个 <code>Request</code> 之间的执行间隔，Token极易过期。</td>
        </tr>
        <tr>
            <td><strong>17. 任务去重</strong></td>
            <td class="funboost-advantage"><strong>更智能（入参去重）</strong>：基于函数核心入参进行去重，能自动忽略URL中的时间戳、随机数等噪音。</td>
            <td class="scrapy-disadvantage"><strong>很笨拙（URL指纹去重）</strong>：对URL中的噪音参数无能为力，需要编写复杂的 <code>RFPDupeFilter</code> 才能解决。</td>
        </tr>
        <tr>
            <td><strong>18. 去重有效期</strong></td>
            <td class="funboost-advantage"><strong>支持</strong>：可以设置任务过滤的有效期，适合周期性更新的爬取任务。</td>
            <td class="scrapy-disadvantage"><strong>不支持</strong>：默认是永久去重，需要手动清理去重集合才能重新爬取。</td>
        </tr>
        <tr>
            <td><strong>19. 错误重试</strong></td>
            <td class="funboost-advantage"><strong>更可靠（函数级重试）</strong>：即使HTTP 200但页面内容反爬，导致解析出错，函数依然会自动重试。</td>
            <td class="scrapy-disadvantage"><strong>不可靠（URL级重试）</strong>：只对请求失败（如网络错误）重试，对内容错误无能为力，会丢失数据。</td>
        </tr>
        <tr>
            <td><strong>20. 数据持久化</strong></td>
            <td class="funboost-advantage"><strong>极其灵活</strong>：在函数内直接调用任何数据库的客户端库进行存储，完全自由。</td>
            <td class="scrapy-disadvantage"><strong>受限</strong>：必须通过 <code>Item Pipeline</code> 机制，增加了一层不必要的抽象和复杂性。</td>
        </tr>
        <tr>
            <td><strong>21. 消息队列支持</strong></td>
            <td class="funboost-advantage"><strong>极其丰富</strong>：支持30多种消息队列，包括RabbitMQ、Kafka等，提供更专业的分布式能力。</td>
            <td class="scrapy-disadvantage"><strong>有限</strong>：主要依赖 <code>scrapy-redis</code>，选择单一。</td>
        </tr>
        <tr>
            <td><strong>22. 定时任务</strong></td>
            <td class="funboost-advantage"><strong>原生支持</strong>：内置强大的定时任务功能，可轻松实现定时启动、周期爬取。</td>
            <td class="scrapy-disadvantage">需要借助外部脚本或 <code>apscheduler</code> 等库自行实现，集成复杂。</td>
        </tr>
        <tr>
            <td rowspan="8"><strong>生态与可靠性 (23-30)</strong></td>
            <td><strong>23. 插件生态</strong></td>
            <td class="funboost-advantage"><strong>无需插件，Python生态即是其生态</strong>：任何Python三方包都可直接使用，无需等待“大神”开发专用插件。</td>
            <td class="scrapy-disadvantage"><strong>依赖插件</strong>：使用新工具（如Playwright）需要等待 <code>scrapy-playwright</code> 这样的插件，学习和配置成本高。</td>
        </tr>
        <tr>
            <td><strong>24. 断点续爬</strong></td>
            <td class="funboost-advantage"><strong>真正可靠</strong>：支持消费确认（ACK），即使强制关机、代码崩溃，任务也万无一失。</td>
            <td class="scrapy-disadvantage"><strong>不可靠</strong>：<code>scrapy-redis</code> 使用 <code>blpop</code>，重启或崩溃会丢失大量已取出到内存中的任务。</td>
        </tr>
        <tr>
            <td><strong>25. 跨语言/项目交互</strong></td>
            <td class="funboost-advantage"><strong>支持</strong>：可由Java等其他语言程序向队列发布爬虫任务。</td>
            <td class="scrapy-disadvantage"><strong>不支持</strong>：其任务格式与Python和框架自身强绑定。</td>
        </tr>
        <tr>
            <td><strong>26. 远程部署</strong></td>
            <td class="funboost-advantage"><strong>一键部署</strong>：内置 <code>fabric_deploy</code> 功能，可直接将爬虫函数部署到远程服务器。</td>
            <td class="scrapy-disadvantage">无此功能，部署复杂。</td>
        </tr>
        <tr>
            <td><strong>27. Web管理界面</strong></td>
            <td class="funboost-advantage"><strong>功能强大</strong>：<code>funboost web manager</code> 可监控、管理所有爬虫任务和消费者，并可实时调整QPS。</td>
            <td class="scrapy-disadvantage"><code>scrapy-redis</code> 无官方管理界面，需借助其他工具。</td>
        </tr>
        <tr>
            <td><strong>28. 稳定性</strong></td>
            <td class="funboost-advantage"><strong>更高</strong>：对网络错误等有强大的自动重连和重试机制，不易因外部问题中断。</td>
            <td class="scrapy-disadvantage">相对脆弱，需要开发者在中间件中编写大量代码来保证稳定性。</td>
        </tr>
        <tr>
            <td><strong>29. 资源占用</strong></td>
            <td class="funboost-advantage"><strong>更可控</strong>：智能线程池可自动伸缩，节省资源。</td>
            <td class="scrapy-disadvantage">并发数固定，可能在任务稀疏时造成资源浪费。</td>
        </tr>
        <tr>
            <td><strong>30. 统一控制</strong></td>
            <td class="funboost-advantage"><strong>包罗万象</strong>：一个 <code>@boost</code> 装饰器集成了分布式、并发、控频、重试、过滤、持久化等30多种控制功能。</td>
            <td class="scrapy-disadvantage">功能分散在多个组件和配置中，难以统一管理和配置。</td>
        </tr>
    </tbody>
</table>




**总结：**

`funboost` 以其 **“函数即一切”** 的核心思想，彻底解放了开发者。它将复杂的调度、并发、容错等底层工作完全自动化，让开发者可以像写普通脚本一样编写爬虫逻辑，同时享受到远超专用框架的 **灵活性、强大功能和极致性能**。`Scrapy` 的“专业”反而成了其最大的“束缚”，导致在面对现代爬虫的复杂需求时，显得笨拙、低效且难用。因此，`funboost` 在爬虫领域对 `Scrapy` 实现了真正的 **“降维打击”**。

## 8.40b 集中总结 funboost vs scrapy 优势快速对比（文字版）

Funboost 是“函数调度器”，而 Scrapy 是“URL调度器”；前者赋能开发者，给予无限自由，后者则用框架规则束缚开发者。这是一种“自由编程”对“框架奴役”的降维打击。以下是详细的50个原因：

<div class="inner_markdown">

<h1>一、核心理念与架构优势 (1-10)</h1>

1. **调度核心根本不同**：Funboost 调度的是一个完整的 Python 函数，内部逻辑完全自由；Scrapy 调度的是一个 Request 对象，开发者被死死限制在框架的请求-响应生命周期内。
2. **编程范式降维打击**：Funboost 采用 平铺直叙 的同步思维写代码，逻辑连贯，一气呵成；Scrapy 强制使用 yield Request 和 callback 的 回调地狱 模式，逻辑被拆分得支离破碎。
3. **状态管理天壤之别**：Funboost 在函数内用 普通局部变量 就能轻松管理上下文状态，符合直觉；Scrapy 必须通过晦涩的 response.meta 字典在回调间传递状态，极易出错且IDE无法补全。
4. **框架侵入性极低**：Funboost 仅需一个 @boost 装饰器，不改变函数原有结构，可以 无缝集成任何老代码；Scrapy 必须继承 scrapy.Spider，代码与框架深度耦合，迁移成本极高。
5. **架构思想的碾压**：Funboost 是 通用的万能函数调度框架，用更广阔的视野解决爬虫问题，功能更全面；Scrapy 是 专用的爬虫框架，但其设计反而作茧自缚，限制了其解决复杂问题的能力。
6. **对已有代码的兼容性**：任何一个用 requests 写的普通爬虫脚本，加上 @boost 装饰器就能 瞬间升级为分布式爬虫。Scrapy 则需要对老代码进行伤筋动骨的重构。
7. **代码复用性**：Funboost 的爬虫函数是标准函数，可在任何地方轻松复用。Scrapy 的 parse 方法与框架强耦合，基本无法在项目外复用。
8. **思维模式的解放**：Funboost 鼓励开发者用最自然的编程思维解决问题。Scrapy 则强迫开发者扭曲自己的思维去适配框架的特定模式。
9. **请求的绝对自由**：Funboost 函数内部可以自由构造和发送多个请求，并轻松处理它们之间的复杂依赖。Scrapy 的 yield Request 模式让请求之间的时序和依赖关系处理变得非常困难。
10. **逻辑连贯性**：Funboost 的线性代码使得一个任务的完整逻辑（请求->解析->存储->派生新任务）集中在一起，可读性极高。Scrapy 的回调链将这些逻辑打散，降低了可读性。

---

<h1>二、开发效率与易用性 (11-20)</h1>

11. **学习曲线极其平缓**：Funboost 只需学习 @boost 装饰器的用法，几分钟即可上手。Scrapy 需要学习 Spider、Item、Pipeline、Middleware、Settings 等 一整套复杂组件和生命周期。
12. **代码量与文件结构**：Funboost 单文件即可完成一个复杂的分布式爬虫，代码量极少。Scrapy 一个简单爬虫也需要创建7-8个文件，开发时需频繁切换，极其臃肿。
13. **HTTP库选择完全自由**：Funboost 函数内可随意使用 requests, httpx, aiohttp, selenium, playwright 等任何库。Scrapy 强制使用其内置下载器，想用其他库需要封装复杂的中间件。
14. **反爬与自定义请求极其简单**：Funboost 中，封装一个通用的 my_request 函数即可实现换IP、UA等逻辑，0门槛。Scrapy 必须编写和注册复杂的下载器中间件，对新手极不友好。
15. **单元测试极其容易**：每个被 @boost 装饰的函数都可以 直接在IDE中调用，独立进行单元测试。Scrapy 的回调方法与框架上下文强耦合，几乎无法进行独立的单元测试。
16. **IDE代码补全全面支持**：Funboost 的函数参数、push/publish 方法均有代码补全。Scrapy 的 response.meta 是字典，IDE 无法提供任何补全提示，是错误的温床。
17. **调试简单直观**：Funboost 的线性执行逻辑，使用标准 pdb 或IDE调试器即可轻松调试。Scrapy 的回调链和异步流程使得 调试极其困难。
18. **反爬逻辑的封装**：Funboost 将反爬逻辑封装在普通函数中，简单直观。Scrapy 必须封装到复杂的中间件类中，概念抽象，难于理解。
19. **反爬逻辑的独立测试**：Funboost 的 my_request 函数可以独立进行单元测试。Scrapy 的中间件难以脱离框架进行测试。
20. **数据持久化极其灵活**：Funboost 在函数内 直接调用任何数据库的客户端库 进行存储，完全自由。Scrapy 必须通过 Item Pipeline 机制，增加了不必要的抽象和复杂性。

---

<h1>三、功能、性能与可靠性 (21-40)</h1>

21. **并发模型更强悍**：Funboost 轻松实现 多进程 + (多线程/协程) + 多机器 的四重叠加并发，性能炸裂。Scrapy 难以充分利用多核CPU。
22. **速率控制更精准**：Funboost 可通过 qps 参数 精确控制每秒请求次数，无视响应时间波动。Scrapy 只能控制并发数，无法保证稳定的请求速率。
23. **分布式控频**：Funboost 支持跨多台机器、多个进程的 全局QPS控制。Scrapy 的速率限制是单实例的，无法实现全局控频。
24. **任务去重更智能**：Funboost 基于 函数核心入参 去重，能自动忽略URL中的时间戳、随机数等噪音。Scrapy 基于URL指纹，对噪音参数无能为力，需要编写复杂的 RFPDupeFilter。
25. **去重有效期支持**：Funboost 可以设置任务过滤的 有效期，适合周期性更新的爬取任务。Scrapy 默认是永久去重，非常不灵活。
26. **错误重试更可靠**：Funboost 是 函数级重试。即使HTTP 200但页面内容反爬导致解析出错，函数依然会自动重试。Scrapy 是URL级重试，对内容错误无能为力，会丢失大量数据。
27. **断点续爬真正可靠**：Funboost 支持 消费确认（ACK），即使强制关机、代码崩溃，任务也万无一失。Scrapy-redis 使用 blpop，重启或崩溃会丢失所有已取出到内存中的任务。
28. **应对进程崩溃**：Funboost 在进程崩溃或断电后，未完成的任务会自动返回队列。Scrapy-redis 会 永久丢失 所有已 blpop 到内存中的任务。
29. **消息队列支持极其丰富**：Funboost 支持30多种消息队列，包括 RabbitMQ、Kafka 等专业队列，提供更强大的分布式能力。Scrapy 主要依赖 scrapy-redis，选择单一。
30. **定时任务原生支持**：Funboost 内置强大的定时任务功能，可轻松实现定时启动、周期爬取。Scrapy 需要借助外部库自行实现，集成复杂。
31. **远程部署一键搞定**：Funboost 内置 fabric_deploy 功能，可直接将爬虫函数部署到远程服务器。Scrapy 无此功能，部署流程繁琐。
32. **Web管理界面功能强大**：funboost web manager 可监控、管理所有爬虫任务和消费者，并可 实时调整QPS。Scrapy 生态缺乏这样统一、强大的官方监控工具。
33. **稳定性更高**：Funboost 对网络错误等有强大的自动重连和重试机制，不易因外部问题中断。Scrapy 相对脆弱，需要开发者编写大量代码来保证稳定性。
34. **资源占用更可控**：Funboost 的智能线程池可 自动伸缩，在任务稀疏时节省资源。Scrapy 的并发数固定，可能造成资源浪费。
35. **统一控制，包罗万象**：一个 @boost 装饰器集成了分布式、并发、控频、重试、过滤、持久化等 30多种控制功能。Scrapy 功能分散在多个组件和配置中，难以统一管理。
36. **RPC模式**：Funboost 支持 RPC 模式，可以在发布任务后同步等待并获取爬取结果。Scrapy 没有这种模式。
37. **跨语言/项目交互**：Funboost 的任务是标准JSON，可由Java等其他语言程序向队列发布爬虫任务。Scrapy 的任务格式与Python和框架自身强绑定，无法交互。
38. **插件生态的颠覆**：Funboost 无需插件，整个Python生态就是其生态。Scrapy 严重依赖插件，使用新工具（如Playwright）需要等待 scrapy-playwright 这样的插件，学习和配置成本高。
39. **插件的本质**：Scrapy 插件多是因为框架本身封闭，需要“补丁”来扩展。Funboost 不需要插件是因为其本身就是开放的。
40. **对三方库的集成成本**：Funboost 集成任何库都是 零成本的直接调用。Scrapy 集成新库需要等待或自己开发复杂的插件，成本高昂。

---

<h1>四、特定场景处理能力 (41-50)</h1>

41. **复杂流程处理极其自然**：Funboost 可在单个函数内完成 多轮浏览器交互、API调用等复杂连续操作。Scrapy 用回调处理此类任务非常笨拙，甚至会导致异步模型失效。
42. **短时效Token处理轻松解决**：Funboost 可在函数内连续请求，确保获取Token后 立即使用，完美解决时效性问题。Scrapy 无法保证两个 Request 之间的执行间隔，Token极易过期。
43. **时序控制的确定性**：Funboost 在函数内连续发请求，时序是 确定的、可控的。Scrapy 的请求经过调度器，执行时序不确定。
44. **浏览器渲染的并发处理**：Funboost 可以轻松地并发执行多个 Selenium/Playwright 任务。Scrapy 在 parse 方法里用 Selenium 会阻塞整个框架，使其退化为单线程。
45. **处理动态参数的优雅**：Funboost 天然免疫 URL 中的 _ts、_rand 等动态噪音参数。Scrapy 需要编写复杂的正则和自定义 RFPDupeFilter 来清洗 URL，维护成本极高。
46. **对非HTTP任务的处理**：Funboost 可以调度任何任务，比如文件处理、图片识别、数据分析等，与爬虫任务无缝结合。Scrapy 只能处理HTTP请求。
47. **动态任务生成**：Funboost 在函数内部可以根据逻辑随时 push 新的任务，非常灵活。Scrapy 的 yield 方式在复杂逻辑判断下生成新请求会很别扭。
48. **任务优先级控制**：Funboost 支持更专业的 消息级优先级队列（如RabbitMQ），控制更精细。Scrapy 的 priority 参数依赖于调度器的实现，效果有限。
49. **死信队列处理**：Funboost 提供了更完善的死信队列机制，方便处理无法消费的“毒丸”消息。Scrapy 需要自己实现类似逻辑。
50. **对开发者的终极赋能**：Funboost 的核心是 “赋能函数”，让开发者用最熟悉的工具和方式解决问题。Scrapy 的核心是 “遵循框架”，要求开发者学习并适应其一套独特的规则。
</div>

综上所述，funboost 凭借其先进的函数调度理念、极致的灵活性和强大的内置功能，在爬虫领域的几乎所有方面都展现出对 scrapy 的压倒性优势。

<div> </div>

# 9 轻松远程服务器部署运行函数

别的机器不需要先安装git，也不需要先手动上传代码到该机器上，就能自动部署运行,前提python基本环境是要搞好的。<br>
celery不支持这种自动运行在别的机器上的方式。

如果有阿里云codepipeline或者其他运维发版工具或者k8s一键部署多台机器的条件，优先不要使用这种部署方式。

## 9.1 远程服务器部署函数的意义
```
框架叫分布式函数调度框架，可以在多台机器运行，因为消息队列任务是共享的。
我用的时候生产环境是使用 阿里云 codepipeline k8s部署的多个容器。还算方便。
在测试环境一般就是单机多进程运行的，用supervisor部署很方便。
所以之前没有涉及到多态机器的轻松自动部署。
如果要实现轻松的部署多台物理机，不借助除了python以外的其他手段的话，只能每台机器登录上然后下载代码，启动运行命令，机器多了还是有点烦的。
现在最新加入了 Python代码级的函数任务部署，不需要借助其他手段，python代码自动上传代码到远程服务器，并自动启动函数消费任务。
目前的自动化在远程机器启动函数消费，连celery都没有做到。

不依赖阿里云codepipeline 和任何运维发布管理工具，只需要在python代码层面就能实现多机器远程部署。
 这实现了函数级别的精确部署，而非是部署一个 .py的代码，远程部署一个函数实现难度比远程部署一个脚本更高一点，部署更灵活。
```

```
之前有人问怎么方便的部署在多台机器，一般用阿里云codepipeline  k8s自动部署。被部署的远程机器必须是linux，不能是windwos。
但是有的人是直接操作多台物理机，有些不方便，现在直接加一个利用python代码本身实现的跨机器自动部署并运行函数任务。

自动根据任务函数所在文件，转化成python模块路径，实现函数级别的精确部署，比脚本级别的部署更精确到函数。
例如 test_frame/test_fabric_deploy/test_deploy1.py的fun2函数 自动转化成 from test_frame.test_fabric_deploy.test_deploy1 import f2
从而自动生成部署语句
export PYTHONPATH=/home/ydf/codes/distributed_framework:$PYTHONPATH ;cd /home/ydf/codes/distributed_framework;
python3 -c "from test_frame.test_fabric_deploy.test_deploy1 import f2;f2.multi_process_consume(2)"  -fsdfmark fsdf_fabric_mark_queue_test30

这个是可以直接在远程机器上运行函数任务。无需用户亲自部署代码和启动代码。自动上传代码，自动设置环境变量，自动导入函数，自动运行。
这个原理是使用python -c 实现的精确到函数级别的部署，不是python脚本级别的部署。
可以很灵活的指定在哪台机器运行什么函数，开几个进程。这个比celery更为强大，celery需要登录到每台机器，手动下载代码并部署在多台机器，celery不支持代码自动运行在别的机器上
```


## 9.2 远程服务器部署函数的入参介绍。
```

:param host: 需要部署的远程linux机器的 ip
:param port:需要部署的远程linux机器的 port
:param user: 需要部署的远程linux机器的用户名
:param password:需要部署的远程linux机器的密码
:param path_pattern_exluded_tuple:排除的文件夹或文件路径
:param file_suffix_tuple_exluded:排除的后缀
:param only_upload_within_the_last_modify_time:只上传多少秒以内的文件，如果完整运行上传过一次后，之后可以把值改小，避免每次全量上传。
:param file_volume_limit:大于这个体积的不上传，因为python代码文件很少超过1M
:param extra_shell_str :自动部署前额外执行的命令，例如可以设置环境变量什么的
:param invoke_runner_kwargs : 
         invoke包的runner.py 模块的 run()方法的所有一切入参,例子只写了几个入参，实际可以传入十几个入参，大家可以自己琢磨fabric包的run方法，按需传入。
         hide 是否隐藏远程机器的输出，值可以为 False不隐藏远程主机的输出  “out”为只隐藏远程机器的正常输出，“err”为只隐藏远程机器的错误输出，True，隐藏远程主机的一切输出
         pty 的意思是，远程机器的部署的代码进程是否随着当前脚本的结束而结束。如果为True，本机代码结束远程进程就会结束。如果为False，即使本机代码被关闭结束，远程机器还在运行代码。
         warn 的意思是如果远程机器控制台返回了异常码本机代码是否立即退出。warn为True这只是警告一下，warn为False,远程机器返回异常code码则本机代码直接终止退出。
    
:param process_num:启动几个进程
:return:

```


## 9.3 远程服务器部署消费函数的代码示例。

定义了两个函数任务，和f1和f2.

![img_11.png](img_11.png)


运行的控制台图片，说明部署级别精确到了函数而非脚本级别，可以灵活的指定哪台机器跑哪些函数。

![img_10.png](img_10.png)

<div> </div>
# 10.python3.6-3.12 安装/使用funboost出错问题反馈

目前已经测试了python3.6  3.7 3.8  3.9 3.10 3.11 版本的安装，

其中3.6 3.7 用的比较多，linux和win都运行了。3.9 3.10 3.11 版本在win下测试了安装和一部分demo例子运行功能。


如果有安装不了的问题，请截完整图片说明，加python版本+操作系统类型(主要分win和linux/mac)

如果有安装后使用某个属于框架本身的功能出错的，请截完整图片说明

## 10.0 框架与你项目依赖的三方包版本不一致冲突？
```
用户完全可以自由选择任何三方包版本。例如你的 sqlalchemy pymongo等等与框架需要的版本不一致，你完全可以自由选择任何版本。
我开发时候实现了很多种中间件，没有时间长期对每一种中间件三方包的每个发布版本都做兼容测试，所以我固定死了。

用户完全可以选择自己的三方包版本，大胆点，等报错了再说，不出错怎么进步，不要怕代码报错，请大胆点升级你想用的版本。
如果是你是用你自己项目里面的requirements.txt方式自动安装三方包，我建议你在文件中第一行写上 funboost，之后再写其它包
这样就能使用你喜欢的版本覆盖funboost框架依赖的版本了。等用的时候报错了再说。一般不会不兼容报错的请大胆点。

例如在生产环境用户一般固定死版本在requirements.txt,比如写 django==3.0.7,难道安装了django 3.0.8,代码就会报错,服务器就会爆炸吗,
提示版本冲突有啥好害怕的,一般情况下,只要不是大版本升级,或者你使用了三方包很小众的私有方法,才会有可能出现由于版本不同,导致代码报错.

pip install
```


## 10.1 windwos安装后如果报错 ImportError: DLL load failed while importing win32file

linux和mac是不会有这个问题的，win如果出现的话，按下面操作。
```
import win32file
ImportError: DLL load failed while importing win32file: 找不到指定的模块。
```

![img_21.png](img_21.png)

切换到python安装目录的scripts文件夹下，使用指定的python解释器运行。例如你安装了好几个python环境，用指定的python环境的解释器运行。

python3.9 pywin32_postinstall.py -install  (这里python3.9 代指的是具体的对应的python安装文件夹下的那个python.exe)

参考博客:
[ImportError: DLL load failed while importing win32api: 找不到指定的模块](https://blog.csdn.net/ljr_123/article/details/104693372)

## 10.2 启动消费后报错: RuntimeError: cannot schedule new futures after interpreter shutdown

定时apscheduler任务(或一些其他包的使用) 在一些python版本,导致报错 RuntimeError: cannot schedule new futures after interpreter shutdown

只要在你的启动脚本的最最末尾加上死循环阻止主线程退出就好了.

你的代码最最后一行代码加上:
```python
import time
while 1:
  time.sleep(100)
```

或者在代码最后一行加上 run_forever()
```python
from funboost import run_forever # 先导入run_forever

run_forever()  # 这个函数就是 while 1 :time.sleep(100)    就是阻止主线程结束.
```


```python
Error submitting job "timing_publish_deco.<locals>._deco (trigger: interval[0:00:03], next run at: 2023-01-29 15:49:11 CST)" to executor "default"
Traceback (most recent call last):
  File "D:\ProgramData\Miniconda3\envs\py311\Lib\site-packages\apscheduler\schedulers\base.py", line 979, in _process_jobs
    executor.submit_job(job, run_times)
  File "D:\ProgramData\Miniconda3\envs\py311\Lib\site-packages\apscheduler\executors\base.py", line 71, in submit_job
    self._do_submit_job(job, run_times)
  File "D:\ProgramData\Miniconda3\envs\py311\Lib\site-packages\apscheduler\executors\pool.py", line 28, in _do_submit_job
    f = self._pool.submit(run_job, job, job._jobstore_alias, run_times, self._logger.name)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\ProgramData\Miniconda3\envs\py311\Lib\concurrent\futures\thread.py", line 169, in submit
    raise RuntimeError('cannot schedule new futures after '
RuntimeError: cannot schedule new futures after interpreter shutdown
```

```
如上报错，在python3.9以上会报错这个，因为是使用的 apscheduler的 BackgroundScheduler类，在python3.9以上，
如果代码的主线程结束了，不管子线程是否还在运行，都会报错 RuntimeError: cannot schedule new futures after interpreter shutdown，
此时只需要使主线程不结束就行了，那就是在你的启动脚本的最最末尾的地方加上以下两句就可以了。

while 1:
  time.sleep(100)

加了 while 1:
     time.sleep(100)
后，主线程代码就会无限死循环，这样主线程永远不会结束了。
```

原因是：
```
funboost 内置的apscheduler 对象，是实例化 BackGroundScheduler ，而不是实例化 BlockingScheduler ,

如下代码：

aps_scheduler_obj.start()
print('hello')

如果 aps_scheduler_obj 类型是 BackGroundScheduler，控制台可以打印出hello，
但在python3.9以上要确保主线程不能退出，否则定时器就会报错结束了，所以最末尾加 while 1: time.sleep(100)阻止主线程退出。
funboost为了启动定时器 scheduler.start() 和启动消费 taskfun.consume() 随意哪一行写在前面都能运行所有代码，所以内置的实例化的对象是 BackGroundScheduler 类型


如果 aps_scheduler_obj 类型是 BlockingScheduler，控制台不能打印出hello，必须确保 aps_scheduler_obj.start() 是写在代码的最后一行，
这种当然不需要代码最末尾加个 while 1: time.sleep(100)阻止主线程退出了。
```

## 10.3  文档1.3例子 BrokerEnum.PERSISTQUEUE,sqlite作为中间件例子在mac/linux运行,报错 read-only 


文档1.3例子 BrokerEnum.PERSISTQUEUE,sqlite作为中间件例子在mac/linux运行,报错 read-only  file system : '/sqllite_queues'

![img_48.png](img_48.png)

因为你选择是使用sqlite作为消息队列中间件,那么就需要在用户电脑上创建文件夹和文件,来存放sqlite数据库数据,
有很多人不是windows电脑运行,linux和mac权限严格,非root用户是无法在硬盘根目录自动创建/sqllite_queues 文件夹并写入数据的,报错已经很明显了,有些人还是一报错就慌了,
需要你在项目根目录下的 funboost_config.py 中 指定 SQLLITE_QUEUES_PATH 为一个有操作权限的文件夹就可以了.

<div> </div>
# 11 funboost 使用某些中间件或三方任务队列框架作为broker的例子(包括celery框架)。

第4章列举了所有funboost用法和场景，第11章补充一些小众中间件的用法

funboost 强大的扩展性，不仅支持各种消息队列还能支持各种不同写法的任务框架作为 broker_kind ，框架扩展性 开放性已然无敌

下面的项目中,演示funboost自动化操作celery复杂不规则项目目录时候怎么完虐用户亲自使用celery
[https://github.com/ydf0509/funboost_support_celery_demo](https://github.com/ydf0509/funboost_support_celery_demo)

## 11.1 使用celery作为funboost的中间件

害怕celery框架用法pythoner的福音。用户无需接触celery的任务路由配置和celery对象实例，就可以自动使用celery框架来调度函数。

```
使用celery作为中间件，用户需要在 funboost_config.py  配置
CELERY_BROKER_URL（必须） 和 CELERY_RESULT_BACKEND （可以为None）

用户想使用celery作为funboost的消息队列，需要安装pip install celery,flower
```

用户不需要手写 `celery` 的 `@app.task` 了，不需要怎么小心翼翼规划文件夹层级和模块名字了

`funboost` + `broker_kind=BrokerEnum.CELERY` 设计的精髓所在——**通过一个简单、统一的 `@boost` API，将复杂、繁琐的 Celery 配置和启动流程完全自动化和隐藏起来**。

开发者从此可以：
- **专注业务逻辑**：只写函数，用 `@boost` 标记。   
- **享受 Celery 的强大**：依然使用 Celery 的 worker、beat、result backend 等成熟稳定的执行引擎。
- **摆脱框架束缚**：不再被所谓的“最佳实践”目录结构所限制。     

这不仅极大地提升了开发效率，也降低了新团队成员的学习成本，是真正意义上的“化繁为简”。   

### 11.1.1 funboost启动celery消费和定时和flower

test_celery_beat_consume.py

```python



from celery.schedules import crontab
from datetime import timedelta
import time

from funboost import boost, BrokerEnum, BoosterParams
from funboost.assist.celery_helper import CeleryHelper,celery_app



@boost(BoosterParams(queue_name='celery_beat_queue_7a2', broker_kind=BrokerEnum.CELERY, qps=5))
def f_beat(x, y):
    time.sleep(3)
    print(1111, x, y)
    return x + y


# celery_task_config 就是 celery app.task装饰器的原生入参，是任务函数配置。
# 如果要更新app的配置，例如使用 CeleryHelper.update_celery_app_conf({'result_expires':3600*48,'worker_concurrency':100})
@boost(BoosterParams(queue_name='celery_beat_queueb_8a2', broker_kind=BrokerEnum.CELERY, qps=1, broker_exclusive_config={'celery_task_config': {'default_retry_delay':60*5}}))
def f_beat2(a, b):
    time.sleep(2)
    print(2222, a, b)
    return a - b


beat_schedule = {  # 这是100% 原汁原味的celery 定时任务配置方式
    'add-every-10-seconds_job': {
        'task': f_beat.queue_name,
        'schedule': timedelta(seconds=10),
        'args': (10000, 20000)
    },
    'celery_beat_queueb_8_jobxx': {
        'task': f_beat2.queue_name,
        'schedule': timedelta(seconds=20),
        # 'schedule': crontab(minute=30, hour=16),
        'kwargs': {'a': 20, 'b': 30}
    }

}

if __name__ == '__main__':
    """
    下面代码直接在代码中启动了 worker 和  beat 和 flower ，永远无需用户在 xhsell 和cmd 敲击复杂的 celery命令行，而只需要普通的 python xx.py 来启动。。

    绝大多数 Celery 的入门教程和博客文章，都会重点介绍如何通过命令行来启动 Celery worker、Celery beat 以及 Flower。
    例如 celery -A your_project worker -l INFO、celery -A your_project beat -l INFO 和 celery flower --broker=your_broker_url 等，
    这些命令行操作是 Celery 官方推荐的标准启动方式，也是最直接的上手途径。
    然而，关于如何以编程方式（即在 Python 脚本内部）启动和管理这些组件的教程相对较少，或者被认为是更高级的用法，普通博客可能不会详细记录。

    funboost作者能做到无需命令行中使用celery命令来启动这些，恰好打脸了那些质疑ydf0509是因为学不会复杂的celery 用法才重复造轮子写个funboost出来。
    """
    CeleryHelper.start_flower(5556)  # 启动flower 网页，这个函数也可以单独的脚本中启动
    CeleryHelper.celery_start_beat(beat_schedule) # 配置和启动定时任务，这个函数也可以在单独的脚本中启动，但脚本中需要 先import 导入@boost装饰器函数所在的脚本，因为@boost时候consumer的custom_init中注册celery任务路由，之后才能使定时任务发送到正确的消息队列。
    print(CeleryHelper.celery_app.conf)
    CeleryHelper.show_celery_app_conf()
    CeleryHelper.update_celery_app_conf({'result_expires':3600*48}) # 如果要更新celery app的配置。
    f_beat.consume()  # 启动f_beat消费，这个是登记celery worker要启动消费的函数，真正的启动worker消费需要运行 realy_start_celery_worker，realy_start_celery_worker是一次性启动所有登记的需要运行的函数
    f_beat2.consume() # 启动f_beat2消费，这个是登记celery worker要启动消费的函数，真正的启动worker消费需要运行 realy_start_celery_worker，realy_start_celery_worker是一次性启动所有登记的需要运行的函数
    CeleryHelper.realy_start_celery_worker(worker_name='test_worker啊')  # 这个是真正的启动celery worker 函数消费。
    print('CeleryHelper.realy_start_celery_worker()  之后的代码不会被运行')


```

上面代码是100%使用celery的worker核心来运行消费、定时、页面监控，只是使用了funboost的api @boost来定义消费函数。完全没有使用funboost自身源码实现的 各种并发池 各种qps控频 重试 等辅助功能。


### 11.1.2 funboost发布任务到celery队列

test_funboost_celery_push.py

```python

from test_celery_beat_consume import f_beat,f_beat2


for i in range(100):
    f_beat.push(i, i + 1)
    res2 = f_beat2.push(i, i * 2)
    print(type(res2),res2.get())  # celer 的 delay 获取结果的原生celery异步结果对象类型
```

### 11.1.3 funboost使用celery作为中间件的运行截图

flower 截图
![img_32.png](img_32.png)

可以看到funboost的boost装饰器自动配置celery任务路由和任务配置。
![img_34.png](img_34.png)

[//]: #![img_35.png](img_35.png)

[//]: #![img_36.png](img_36.png)


funboost使用celery作为broker的控制台运行截图
![img_33.png](img_33.png)

### 11.1.4 funboost 的api 操作celery，比人工操作 celery 大大简化。

<pre style="font-size: large;color: greenyellow;background-color: black">

由此可知，用户无需操作celery本身，无需敲击celery难记的命令行启动消费、定时、flower;
用户无需小心翼翼纠结亲自使用celery时候怎么规划目录结构 文件夹命名 需要怎么在配置写include 写task_routes，
完全不存在需要固定的celery目录结构，不需要手动配置懵逼的任务路由，不需要配置每个函数怎么使用不同的队列名字，funboost自动搞定这些。

用户只需要使用简单的funboost语法就能操控celery框架了。funboost使用celery作为broker_kind,远远的暴击亲自使用无法ide下代码补全的celery框架的语法。
</pre>

```
funboost通过支持celery作为broker_kind,使celer框架变成了funboost的一个子集
```

### 11.1.5 funboost 使用celery作为中间件时候，可以填写的celery任务配置

funboost的@boost装饰器的broker_exclusive_config的celery_task_config 可以配置项大全,就是@celery_app.task()的入参大全。
所有可以配置项可以看  D:\ProgramData\Miniconda3\Lib\site-packages\celery\app\task.py
```python

'''
    #: Execution strategy used, or the qualified name of one.
    Strategy = 'celery.worker.strategy:default'

    #: Request class used, or the qualified name of one.
    Request = 'celery.worker.request:Request'

    #: The application instance associated with this task class.
    _app = None

    #: Name of the task.
    name = None

    #: Enable argument checking.
    #: You can set this to false if you don't want the signature to be
    #: checked when calling the task.
    #: Defaults to :attr:`app.strict_typing <@Celery.strict_typing>`.
    typing = None

    #: Maximum number of retries before giving up.  If set to :const:`None`,
    #: it will **never** stop retrying.
    max_retries = 3

    #: Default time in seconds before a retry of the task should be
    #: executed.  3 minutes by default.
    default_retry_delay = 3 * 60

    #: Rate limit for this task type.  Examples: :const:`None` (no rate
    #: limit), `'100/s'` (hundred tasks a second), `'100/m'` (hundred tasks
    #: a minute),`'100/h'` (hundred tasks an hour)
    rate_limit = None

    #: If enabled the worker won't store task state and return values
    #: for this task.  Defaults to the :setting:`task_ignore_result`
    #: setting.
    ignore_result = None

    #: If enabled the request will keep track of subtasks started by
    #: this task, and this information will be sent with the result
    #: (``result.children``).
    trail = True

    #: If enabled the worker will send monitoring events related to
    #: this task (but only if the worker is configured to send
    #: task related events).
    #: Note that this has no effect on the task-failure event case
    #: where a task is not registered (as it will have no task class
    #: to check this flag).
    send_events = True

    #: When enabled errors will be stored even if the task is otherwise
    #: configured to ignore results.
    store_errors_even_if_ignored = None

    #: The name of a serializer that are registered with
    #: :mod:`kombu.serialization.registry`.  Default is `'json'`.
    serializer = None

    #: Hard time limit.
    #: Defaults to the :setting:`task_time_limit` setting.
    time_limit = None

    #: Soft time limit.
    #: Defaults to the :setting:`task_soft_time_limit` setting.
    soft_time_limit = None

    #: The result store backend used for this task.
    backend = None

    #: If enabled the task will report its status as 'started' when the task
    #: is executed by a worker.  Disabled by default as the normal behavior
    #: is to not report that level of granularity.  Tasks are either pending,
    #: finished, or waiting to be retried.
    #:
    #: Having a 'started' status can be useful for when there are long
    #: running tasks and there's a need to report what task is currently
    #: running.
    #:
    #: The application default can be overridden using the
    #: :setting:`task_track_started` setting.
    track_started = None

    #: When enabled messages for this task will be acknowledged **after**
    #: the task has been executed, and not *just before* (the
    #: default behavior).
    #:
    #: Please note that this means the task may be executed twice if the
    #: worker crashes mid execution.
    #:
    #: The application default can be overridden with the
    #: :setting:`task_acks_late` setting.
    acks_late = None

    #: When enabled messages for this task will be acknowledged even if it
    #: fails or times out.
    #:
    #: Configuring this setting only applies to tasks that are
    #: acknowledged **after** they have been executed and only if
    #: :setting:`task_acks_late` is enabled.
    #:
    #: The application default can be overridden with the
    #: :setting:`task_acks_on_failure_or_timeout` setting.
    acks_on_failure_or_timeout = None

    #: Even if :attr:`acks_late` is enabled, the worker will
    #: acknowledge tasks when the worker process executing them abruptly
    #: exits or is signaled (e.g., :sig:`KILL`/:sig:`INT`, etc).
    #:
    #: Setting this to true allows the message to be re-queued instead,
    #: so that the task will execute again by the same worker, or another
    #: worker.
    #:
    #: Warning: Enabling this can cause message loops; make sure you know
    #: what you're doing.
    reject_on_worker_lost = None

    #: Tuple of expected exceptions.
    #:
    #: These are errors that are expected in normal operation
    #: and that shouldn't be regarded as a real error by the worker.
    #: Currently this means that the state will be updated to an error
    #: state, but the worker won't log the event as an error.
    throws = ()

    #: Default task expiry time.
    expires = None

    #: Default task priority.
    priority = None

    #: Max length of result representation used in logs and events.
    resultrepr_maxsize = 1024

    #: Task request stack, the current request will be the topmost.
    request_stack = None
'''
```

### 11.1.6 网上关于celery项目目录结构和文件夹/文件命名必须很死板， 是错的

网上说必须叫celery.py，还要固定的目录结构那都是假的，并不需要这样。
![img_37.png](img_37.png)

像这样的乱七八糟的celery目录结构是可以运行的。
[https://github.com/ydf0509/celery_demo](https://github.com/ydf0509/celery_demo)
![img_38.png](img_38.png)

celery 实例化对象可以在项目的任意深层级文件夹的任意文件名字下，celery的@app.task函数也可以是在任何深层级文件夹的任意文件名字下。

如果用户不会怎么使用不同的队列名字，怎么在不规则的文件夹下使用celery框架，可以使用funboost + celery作为broker，funboost让用户远离celery本身，funboost内部可以自动化操作celery。

### 11.1.7 仍然想使用celery命令行？

有些人仍然想使用celery的命令行，操作一些其他命令，当然可以的
```
例如执行celery status命令
首先设置 PYTHONPATH为项目根目录，这个去看github pythonpathdemo项目，pythonpath说烂了，这作用都不知道的人别用python了。
linux 是 export PYTHONPATH=项目根目录
win 是 份powershell和cmd
   powershell 中设置临时会话环境变量 $env:PYTHONPATH="项目根目录" 
   cmd        中设置临时会话环境变量 set PYTHONPATH="项目根目录" 
cd {项目根目录}
python -m celery -A ./dir1/test_celery_beat_consume  status   # test_celery_beat_consume.py有 celery_app对象
```

因为 test_celery_beat_consume.py 模块中有 Celery类型的对象 celery_app,所以能够自动被celery命令识别到这个对象，
所以用户自己仍然想用celery命令行是可以的

### 11.1.8 funboost使用celery作为broker_kind的原理

与其说funboost支持各种消息队列中间件，不如说funboost实现了集成操作各种各样的消息队列的第三方python包，

```
@boost(BoosterParams(queue_name=queue_1, broker_kind=BrokerEnum.CELERY, qps=5))
def f_beat(x, y):

加了@boost后，那么funboost框架自动给celery_app 注册任务了，并且设置每个任务的消息使用不同的队列名存放，
@boost里面自动配置celery任务，并且支持用户用celery命令行按照11.1.7 操作celery，包括命令行清空队列 啥的都可以
```

## 11.2 使用nameko 微服务框架作为funboost消息中间件例子

### 11.2.1 nameko服务端脚本

test_funboost_nameko.py

```python
from eventlet import monkey_patch

monkey_patch()

from funboost.consumers.nameko_consumer import start_batch_nameko_service_in_new_process,start_batch_nameko_service_in_new_thread


import time

from funboost import boost, ConcurrentModeEnum, BrokerEnum, BoosterParams




@boost(BoosterParams(queue_name='test_nameko_queue', broker_kind=BrokerEnum.NAMEKO, concurrent_mode=ConcurrentModeEnum.EVENTLET))
def f(a, b):
    print(a, b)
    time.sleep(1)
    return 'hi'


@boost(BoosterParams(queue_name='test_nameko_queue2', broker_kind=BrokerEnum.NAMEKO, concurrent_mode=ConcurrentModeEnum.EVENTLET))
def f2(x, y):
    print(f'x: {x}   y:{y}')
    time.sleep(2)
    return 'heelo'


if __name__ == '__main__':
    # 用户可以使用nameko的 ServiceContainer ,直接启动每个nameko的service类，语法和funboost使用其他中间件语法一样。
    f.consume()
    f2.consume()

    # 也可以批量启动，使用nameko的 ServiceRunner 批量启动多个 nameko的service类。这个函数专门为nameko 中间件而写的。
    start_batch_nameko_service_in_new_thread([f, f2])

```

### 11.2.2 nameko客户端脚本

test_nameko_push.py

```python
from test_funboost_nameko import f, f2

for i in range(100):
    print(f.push(i, b=i + 1))
    print(f2.push(x=i, y=i * 2))
```





### 11.2.3 funboost操作nameko能简化亲自使用nameko框架的语法
```
需要配置好rabbitmq的ip端口账号密码，因为nameko使用rabbitmq。
用户无需了解学习nameko框架的语法，就能使用nameko微服务框架。
```


## 11.3 使用kombu作为funboost的broker

kombu一次性能支持数十种消息队列，kombu是celery能支持多种消息队列的根本原因。celery依赖kombu从而实现支持多种消息队列。
kombu没有和celery深度绑定，kombu不依赖celery，是celery依赖kombu。所以kombu可以为funboost所用。

```
如果不用funboost celery等，
例如你想操作rabbitmq和redis作为消息队列，如果你使用kombu包，则一份代码就可以简单通过不同的中间件url连接切换来操作rabbitmq和redis了。
如果你不使用kombu，分别import pika和import redis来实现操作rabbitmq和redis，要写两份很大区别的代码。
使用kombu一次性能支持切换十几种消息队列比import 十几种python包来操作各种消息队列中间件香多了。
```

kombu能支持的消息队列大全：
```python
TRANSPORT_ALIASES = {
    'amqp': 'kombu.transport.pyamqp:Transport', # rabbitmq作为消息队列
    'amqps': 'kombu.transport.pyamqp:SSLTransport',
    'pyamqp': 'kombu.transport.pyamqp:Transport',
    'librabbitmq': 'kombu.transport.librabbitmq:Transport',
    'memory': 'kombu.transport.memory:Transport',
    'redis': 'kombu.transport.redis:Transport',
    'rediss': 'kombu.transport.redis:Transport',
    'SQS': 'kombu.transport.SQS:Transport',
    'sqs': 'kombu.transport.SQS:Transport',
    'mongodb': 'kombu.transport.mongodb:Transport',
    'zookeeper': 'kombu.transport.zookeeper:Transport',
    'sqlalchemy': 'kombu.transport.sqlalchemy:Transport',
    'sqla': 'kombu.transport.sqlalchemy:Transport',  # 数据库作为消息队列
    'SLMQ': 'kombu.transport.SLMQ.Transport',
    'slmq': 'kombu.transport.SLMQ.Transport',
    'filesystem': 'kombu.transport.filesystem:Transport',   # 文件作为消息队列
    'qpid': 'kombu.transport.qpid:Transport',
    'sentinel': 'kombu.transport.redis:SentinelTransport', # redis 哨兵集群作为消息队列
    'consul': 'kombu.transport.consul:Transport',
    'etcd': 'kombu.transport.etcd:Transport',
    'azurestoragequeues': 'kombu.transport.azurestoragequeues:Transport',
    'azureservicebus': 'kombu.transport.azureservicebus:Transport',
    'pyro': 'kombu.transport.pyro:Transport'
}
```

### 11.3.1 kombu操作rabbitmq作为funboost的消息队列

```
设置boost装饰器的 broker_kind=BrokerEnum.KOMBU
broker_exclusive_config 中可以设置 kombu_url，如果这里不传递kombu_url，则使用funboost_config.py的全局KOMBU_URL

transport_options是kombu的transport_options 。 
       例如使用kombu使用redis作为中间件时候，可以设置 visibility_timeout 来决定消息取出多久没有ack，就自动重回队列。
       kombu的每个中间件能设置什么 transport_options 可以看 kombu的源码中的 transport_options 参数说明。

例如kombu redis的Transport Options 说明
D:\ProgramData\Miniconda3\envs\py311\Lib\site-packages\kombu\transport\redis.py

Transport Options
=================
* ``sep``
* ``ack_emulation``: (bool) If set to True transport will
  simulate Acknowledge of AMQP protocol.
* ``unacked_key``
* ``unacked_index_key``
* ``unacked_mutex_key``
* ``unacked_mutex_expire``
* ``visibility_timeout``
* ``unacked_restore_limit``
* ``fanout_prefix``
* ``fanout_patterns``
* ``global_keyprefix``: (str) The global key prefix to be prepended to all keys
  used by Kombu
* ``socket_timeout``
* ``socket_connect_timeout``
* ``socket_keepalive``
* ``socket_keepalive_options``
* ``queue_order_strategy``
* ``max_connections``
* ``health_check_interval``
* ``retry_on_timeout``
* ``priority_steps``

```

```python


import time

from funboost import BrokerEnum, boost, BoosterParams
from funboost.funboost_config_deafult import BrokerConnConfig

@boost(BoosterParams(queue_name='test_kombu2b', broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': BrokerConnConfig.RABBITMQ_URL,
           'transport_options': {},
           'prefetch_count': 1000}))
def f1(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    # f1.push(3,4)
    for i in range(10000):
        f1.push(i, i*2)
    f1.consume()

```


### 11.3.2 kombu+redis作为消息队列

```
设置boost装饰器的 broker_kind=BrokerEnum.KOMBU
broker_exclusive_config 中可以设置 kombu_url，如果这里不传递kombu_url，则使用funboost_config.py的全局KOMBU_URL
```

```python
import time

from funboost import BrokerEnum, boost, BoosterParams


@boost(BoosterParams(queue_name='test_kombu2b', broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': 'redis://192.168.64.151:6378/10',
           'transport_options': {
               'visibility_timeout': 600, 'ack_emulation': True  # visibility_timeout 是指消息从redis blpop后多久没确认消费就当做消费者挂了无法确认消费，unack的消息自动重回正常工作队列
           },
           'prefetch_count': 1000}, log_level=20))
def f1(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    # f1.push(3,4)
    for i in range(10000):
        f1.push(i, i*2)
    f1.consume()

```

#### 11.3.2.b kombu + redis哨兵作为消息队列

装饰器 broker_kind=BrokerEnum.KOMBU

funboost_config.py 配置例子如下:
KOMBU_URL= 'redis+sentinel://sentinel1.example.com:26379,sentinel2.example.com:26379,sentinel3.example.com:26379/0?sentinel=master01'

KOMBU_URL的格式规范就是celery的 broker_url 的格式规范,怎么写可以自己百度"celery redis 哨兵"就好了,因为celery就是依赖kombu包实现的支持多种消息队列.

```
BrokerEnum.KOMBU 和 BrokerEnum.CELERY 中间件都能支持redis哨兵模式.
只需要你配置 funboost_config.py 中的配置就好了,funboost 支持30多种消息队列或包或者框架,
funboost通过支持BrokerEnum.KOMBU 和 BrokerEnum.CELERY ,只会比celery支持的中间件模式更多,不会更少.
```


### 11.3.3 kombu+sqlalchemy 作为消息队列

```python
import time
from funboost import BrokerEnum, boost, BoosterParams, BrokerConnConfig

'''
默认自动创建表 kombu_message 和 kombu_queue, sqlalchemy版本要选对，测试 1.4.8 可以，2.0.15版本报错。
所有队列的消息在一个表中kombu_message，queue_id做区分是何种队列。
'''
@boost(BoosterParams(queue_name='test_kombu_sqlalchemy_queue2', broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': f'sqla+mysql+pymysql://{BrokerConnConfig.MYSQL_USER}:{BrokerConnConfig.MYSQL_PASSWORD}'
                        f'@{BrokerConnConfig.MYSQL_HOST}:{BrokerConnConfig.MYSQL_PORT}/{BrokerConnConfig.MYSQL_DATABASE}',
           'transport_options': {},
           'prefetch_count': 500}))
def f2(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


@boost(BoosterParams(queue_name='test_kombu_sqlalchemy_queue3', broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': f'sqla+mysql+pymysql://{BrokerConnConfig.MYSQL_USER}:{BrokerConnConfig.MYSQL_PASSWORD}'
                        f'@{BrokerConnConfig.MYSQL_HOST}:{BrokerConnConfig.MYSQL_PORT}/{BrokerConnConfig.MYSQL_DATABASE}',
           'transport_options': {},
           'prefetch_count': 500}))
def f3(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    for i in range(100):
        f2.push(i, i + 1)
        f3.push(i,i*2)
    f2.consume()
    f3.consume()

```

### 11.3.4 kombu+mongo作为消息队列

```python
import time

from funboost import BrokerEnum, boost, BoosterParams

queue_name = 'test_kombu_mongo4'


@boost(BoosterParams(queue_name=queue_name, broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': 'mongodb://root:123456@192.168.64.151:27017/my_db?authSource=admin',
           'transport_options': {
               'default_database': 'my_db',
               'messages_collection': queue_name,

           },
           'prefetch_count': 10}))
def f2(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    for i in range(100):
        f2.push(i, i + 1)
    f2.consume()

```

### 11.3.5 kombu+文件作为消息队列

```
kombu_url 写 filesystem://
data_folder是规定消息文件在什么文件夹，这里每个queue弄一个文件夹。
processed_folder 是指处理过的消息放在什么文件夹

可以看到kombu使用不同的消息队列，只需要改变kombu_url的连接，transport_options则是根据每个消息队列的特色传递哪些参数。
transport_options具体可以传递的值，点击kombu的各种中间件的源码文件，里面罗列的十分清楚。

```

```python
import time

from funboost import BrokerEnum, boost, BoosterParams


queue_name = 'test_kombu5'


@boost(BoosterParams(queue_name=queue_name, broker_kind=BrokerEnum.KOMBU, qps=0.1,
       broker_exclusive_config={
           'kombu_url': 'filesystem://',
           'transport_options': {
               'data_folder_in': f'/data/kombu_queue/{queue_name}',
               'data_folder_out': f'/data/kombu_queue/{queue_name}',
               'store_processed': True,
               'processed_folder': f'/data/kombu_processed/{queue_name}'
           },
           'prefetch_count': 10}))
def f2(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    for i in range(100):
        f2.push(i, i + 1)
    f2.consume()

```



## 11.4 使用dramatiq框架作为funboost消息队列

```
dramatiq是作者觉得celery用得不爽有坑，开发的任务队列框架，基本用途和celery一样
funboost的统一api，但使用dramatiq作为核心调度，
用户无需操作dramatiq 命令行来启动消费。
```

```
dramatiq框架作用类似于celery，支持rabbitmq和redis两种消息队列
在funboost_config.py 设置 DRAMATIQ_URL 的值就可以了
例如 amqp://admin:372148@106.55.244.110:5672/
redis://:passwd@127.0.0.1:6379/15
```

```python
import time

from funboost import boost, BrokerEnum, BoosterParams

from funboost.assist.dramatiq_helper import DramatiqHelper


@boost(BoosterParams(queue_name='test_dramatiq_q1', broker_kind=BrokerEnum.DRAMATIQ, function_timeout=10))
def f1(x):
    time.sleep(1)
    print('f1', x)


@boost(BoosterParams(queue_name='test_dramatiq_q2', broker_kind=BrokerEnum.DRAMATIQ, function_timeout=3))
def f2(y):
    time.sleep(2)
    print('f2', y)


if __name__ == '__main__':
    f1.consume()  # 登记要启动消费的queue
    f2.consume()  # 登记要启动消费的queue
    for i in range(100):
        f1.push(i)
        f2.push(i * 2)
    DramatiqHelper.realy_start_dramatiq_worker()  # 真正启动dramatiq消费

```


## 11.5 使用huey框架作为funboost消息队列

```
funboost_config.py中 配置好 REDIS_URL 的值就可以了

使用huey框架作为funboost的调度核心，但用户只需要掌握funboost的api语法，用户无需敲击huey命令行来启动消费
```

```python
import time 

from funboost.assist.huey_helper import HueyHelper
from funboost import boost, BrokerEnum, BoosterParams


@boost(BoosterParams(queue_name='test_huey_queue1', broker_kind=BrokerEnum.HUEY, broker_exclusive_config={'huey_task_kwargs': {}}))
def f1(x, y):
    time.sleep(10)
    print(x, y)
    return 666


@boost(BoosterParams(queue_name='test_huey_queue2', broker_kind=BrokerEnum.HUEY))
def f2(a):
    time.sleep(7)
    print(a)


if __name__ == '__main__':
    for i in range(10):
        f1.push(i, i + 1)
        f2.push(i)
    HueyHelper.realy_start_huey_consume()

```

## 11.6 使用rq框架作为funboost的broker

```
funboost_config.py中 配置好 REDIS_URL 的值就可以了

使用rq框架作为funboost的调度核心，但用户只需要掌握funboost的api语法，用户无需敲击rq命令行来启动消费

开发了 WindowsWorker 类，使 rq框架支持在windows运行，因为windows不能fork多进程，原生rq框架只能在linux、mac下运行。
```

使用rq任务队列框架作为funboost broker的例子
```python

import time

from funboost import boost, BrokerEnum, BoosterParams

from funboost.assist.rq_helper import RqHelper


@boost(BoosterParams(queue_name='test_rq_queue1a', broker_kind=BrokerEnum.RQ))
def f(x, y):
    time.sleep(2)
    print(f'x:{x},y:{y}')


@boost(BoosterParams(queue_name='test_rq_queue2a', broker_kind=BrokerEnum.RQ))
def f2(a, b):
    time.sleep(3)
    print(f'a:{a},b:{b}')


if __name__ == '__main__':
    # RqHelper.add_nb_log_handler_to_rq()  # 使用nb_log日志handler来代替rq的
    for i in range(100):
        f.push(i, i * 2)
        f2.push(i, i * 10)
    f.consume()  # f.consume()是登记要启动的rq f函数的 queue名字,
    f2.consume()  # f2.consume()是登记要启动的rq f2函数的queue名字
    RqHelper.realy_start_rq_worker()  # realy_start_rq_worker 是真正启动rqworker，相当于命令行执行了 rqworker 命令。


```

funboost使用rq作为运行核心的截图
![img_40.png](img_40.png)








<div> </div>
# 12 funboost 控制台支持命令行

funboost 2023.11 新增支持命令行,启动消费 发布消息 清空消息 暂停消费等功能

有些人喜欢如 scrapy celery 这样的框架,在命令行敲击一长串命令来灵活启动python任务,

本人非常讨厌这样的框架,控制台命令行不能代码补全,敲击难,感觉是鸡肋

但是有的小伙伴喜欢这样的命令行方式来启动python,现在funboost加上命令行功能.

```
用户只需要@boost定义消费函数定义f1,f2, 在命令行指定启动哪些queues 就行了,
而不是先需要在脚本中写好 f1.consume() f2.consume(),然后再启动这个脚本.
```

python 项目根目录/funboost_cli_user.py --help 可以查看有哪些命令

## 12.0 funboost命令行使用fire实现

funboost命令行使用fire实现的

fire很好用,很方便,比任何命令行都好用,建议大家以后开发命令行工具使用fire,不要使用argparse和click

## 12.1  命令行分为调用funboost包内命令和用户自身项目的命令行

### 12.1.1 funboost自身命令行,python -m funboost  是自动调用 funboost的 __main__.py 的fire命令行

### 12.1.2 用户项目根目录下的  funboost_cli_user.py 的文件可以接受命令行传参

python -m funboost 和 python 项目根目录/funboost_cli_user.py 是一样的个功能

funboost_cli_user.py是首次启动项目自动把funboost/core/cli/funboost_cli_user_templ.py复制到用户项目根目录下的

用户可以在funboost_cli_user.py里面灵活加代码,这样在调用命令行就能少传参 --project_root_path 和 --booster_dirs_str 了

所以建议用户使用 python 项目根目录/funboost_cli_user.py 的命令行,而不是使用 python -m funboost

###### 说明:之后的例子不再同时列举 python -m funboos 和 python funboost_cli_user.py

### 12.1.3 python -m funboost 和 python 项目根目录/funboost_cli_user.py 传参不同点

```
python -m funboost  必须传递 --project_root_path=你的项目根目录
而且在敲击 python -m funboost 之前需要用户先设置临时环境变量 set/export PYTHONPATH=用户项目根目录 (因为nb_log需要先读取配置文件)


python 你的项目根目录/funboost_cli_user.py 命令行不需要传参指定--project_root_path ,也不需要先设置环境变量
因为funboost_cli_user.py就在用户项目根目录,所以代码中自动添加了当前项目根目录到sys.path 和指定project_root_path为当前项目根目录,
此外funboost_cli_user.py中用户可以import 消费函数所在模块,
也可以 BoosterDiscovery(project_root_path, booster_dirs=['需要扫描的消费函数所在文件夹'], max_depth=1,py_file_re_str=None).auto_discovery()来自动import发现

这就是建议用户使用 python funboost_cli_user.py xxxxx 这样来调用命令行而不是python -m funboost xxx 来调用命令行
```

## 12.2 funboost命令行指定消费函数所在的模块或文件夹

用户如果没import 消费函数所在模块或者调用 BoosterDiscovery.auto_discovery, 需要在命令行传参.

```
如果需要导入多个模块,import_modules_str的值如果多个模块需使用逗号隔开
python funboost_cli_user.py --import_modules_str "test_frame.test_funboost_cli.def_tasks3"  publish test_cli3_queue "{'x':3,'y':4}"
    
如果没有亲自import boost函数所在模块,则可以自动扫描文件夹下的py文件,自动import,如是果多个文件夹用,隔开
python funboost_cli_user.py --boost_dirs_str 'test_find_boosters,test_find_booster2'  push test_find_queue1 --x=1 --y=2
```

## 12.3 打印发现的用户定义的@boost消费函数

show_all_queues 
```
python -m funboost  --project_root_path=用户项目根目录   --booster_dirs_str=文件夹1,文件夹2 --max_depth=2  show_all_queues (需要先set/export PYTHONPATH=用户项目根目录)


或 python funboost_cli_user.py -booster_dirs_str=test_frame/test_funboost_cli/test_find_boosters --max_depth=2 show_all_queues

如果 funboost_cli_user.py 加了 BoosterDiscovery(project_root_path, booster_dirs=['文件夹1','文件夹2'], max_depth=2,py_file_re_str=None).auto_discovery(),那么写
python funboost_cli_user.py show_all_queues  即可.

```

用户可以拉取funboost项目中的自带的测试例子来测试命令行


```
python funboost_cli_user.py  --booster_dirs_str=test_frame/test_funboost_cli/test_find_boosters --max_depth=2  show_all_queues 
```



## 12.4 funboost命令行清空消息队列

clear
```
python funboost_cli_user.py clear  queue1  queue2   # 清空消息队列queue1和queue2,多个队列用空格隔开就行
```

## 12.5 funboost命令行给一个队列发布消息

push 或 publish

```
python funboost_cli_user.py push test_cli1_queue 1 2  # 发布消息
python funboost_cli_user.py push test_cli1_queue 1 --y=2 # 发布消息,也可以明显点传入参名字
python funboost_cli_user.py publish test_cli1_queue "{'x':3,'y':4}"  # 发布消息传递一个字典
python funboost_cli_user.py publish test_cli1_queue '{"x":3,"y":4}' # 错误方式
```

## 12.6 funboost命令行启动多个queue消费者

当前进程内启动多个conusmer consume,

每个queue使用多个进程启动消费 m_consume

```
python funboost_cli_user.py consume test_cli1_queue test_cli2_queue  # 启动两个队列的函数消费
python funboost_cli_user.py m_consume --test_cli1_queue=2 --test_cli2_queue=3 # 叠加多进程启动消费,test_cli1_queue启动2进程,test_cli2_queue启动3进程.
```
### 12.6.b  funboost命令行启动所有queue消费者,用户无需指定队列名

当前进程内启动多个conusmer consume_all_queues 或 consume_all
每个queue使用多个进程启动消费  multi_process_consume_all_queues $process_num 或 m_consume_all $process_num
```
python funboost_cli_user.py consume_all
python funboost_cli_user.py m_consume_all 2
```


## 12.7 funboost命令行暂停消费

pause

支持暂停,前提是 @boost指定 is_send_consumer_hearbeat_to_redis=True

```
python funboost_cli_user.py pause queue1  queue2    #queue1  queue2 两个队列暂停消费
```












<div> </div>

# 13 启动 funboost web manager,查看消费结果和队列管理

通过 funboost web manager 可以查看消费结果；管理队列；管理消费者；查看正在运行的函数； 实时调节并发数量；调节 qps 限制频率；仅从页面就能看到python 函数的消费情况，无需去查看日志文件。

## 13.1 介绍 启动 funboost web manager (方式一)。

funboost web manager 启动方式很容易很简单，一键就能启动。

python3 -m funboost.function_result_web.app

web代码在funboost安装包里面，所以你安装了funboost后，可以直接使用命令行运行起来，不需要用户现亲自下载web代码就可以直接一键启动运行。


<p style="color: #00A000; display: inline-block">首先要安装选装 pip install funboost[flask] </p>（这是因为这是选装，防止用户抱怨funboost依赖太多。）

```
第一步：设置 PYTHONPATH 为你的项目根目录
    export PYTHONPATH=你的项目根目录 (这么做是为了这个web可以读取到你项目根目录下的 funboost_config.py里面的配置)
    (怎么设置环境变量应该不需要我来教，环境变量都没听说过太low了)
     例如 export PYTHONPATH=/home/ydf/codes/ydfhome
     或者 export PYTHONPATH=./   (./是相对路径，前提是已近cd到你的项目根目录了，也可以写绝对路径全路径)
     win cmd 设置环境变量语法是 set PYTHONPATH=/home/ydf/codes/ydfhome   
     win powershell 语法是  $env:PYTHONPATH = "/home/ydf/codes/ydfhome"   


第二步：启动 funboost web manager 的 flask app   
    win上这么做：  python3 -m funboost.function_result_web.app
    linux上可以这么做性能好一些，也可以按win的做：  gunicorn -w 4 --threads=30 --bind 0.0.0.0:27018 funboost.function_result_web.app:app
```

使用浏览器打开 127.0.0.1(启动web服务的机器ip):27018,输入默认用户名 密码 admin 123456，即可打开函数运行状态和结果页面。

### 13.1.b 直接在代码中启动web start_funboost_web_manager() (方式二)：

start_funboost_web_manager() 可以随着消费程序一起启动，也可以单独启动。

```python
from funboost.function_result_web.app import start_funboost_web_manager
start_funboost_web_manager()
```

## 13.2 funboost web manager 截图

函数消费结果：可查看和搜索函数实时消费状态和结果
[![pEJCffK.png](https://s21.ax1x.com/2025/03/04/pEJCffK.png)](https://imgse.com/i/pEJCffK)

消费速度图：可查看实时和历史消费速度
[![pEJCWY6.png](https://s21.ax1x.com/2025/03/04/pEJCWY6.png)](https://imgse.com/i/pEJCWY6)

运行中消费者 by ip： 根据ip搜索有哪些消费者
[![pEJCRFx.png](https://s21.ax1x.com/2025/03/04/pEJCRFx.png)](https://imgse.com/i/pEJCRFx)

运行中消费者 by queue： 根据队列名字搜索有哪些消费者
[![pEJCcwR.png](https://s21.ax1x.com/2025/03/04/pEJCcwR.png)](https://imgse.com/i/pEJCcwR)

队列操作：查看和操作队列，包括 清空清空 暂停消费 恢复消费 调整qps和并发
<!-- [![pEJC6m9.png](https://s21.ax1x.com/2025/03/04/pEJC6m9.png)](https://imgse.com/i/pEJC6m9) -->
[![pVSOJcq.png](https://s21.ax1x.com/2025/05/27/pVSOJcq.png)](https://imgse.com/i/pVSOJcq)

队列操作，查看消费者详情：查看队列的所有消费者详情
[![pEJCgT1.png](https://s21.ax1x.com/2025/03/04/pEJCgT1.png)](https://imgse.com/i/pEJCgT1)

队列操作:查看消费曲线图，查看各种消费指标。
[![pVpr7sP.png](https://s21.ax1x.com/2025/05/29/pVpr7sP.png)](https://imgse.com/i/pVpr7sP)

rpc调用：在网页上对30种消息队列发布消息并获取消息的函数执行结；根据taskid获取结果。
<!-- [![pETq8hj.png](https://s21.ax1x.com/2025/04/28/pETq8hj.png)](https://imgse.com/i/pETq8hj) -->
[![pE7y8oT.png](https://s21.ax1x.com/2025/04/29/pE7y8oT.png)](https://imgse.com/i/pE7y8oT)

## 13.3 funboost web 图片对应的测试代码

```python

import asyncio
import time
import random

from funboost import boost, FunctionResultStatusPersistanceConfig, BoosterParams,BrokerEnum,ctrl_c_recv,ConcurrentModeEnum
from funboost.function_result_web.app import start_funboost_web_manager



class MyBoosterParams(BoosterParams):
    function_result_status_persistance_conf:FunctionResultStatusPersistanceConfig = FunctionResultStatusPersistanceConfig(
        is_save_status=True, is_save_result=True, expire_seconds=7 * 24 * 3600)
    is_send_consumer_hearbeat_to_redis:bool = True


@boost(MyBoosterParams(queue_name='queue_test_g01t',broker_kind=BrokerEnum.REDIS,qps=1,))
def f(x):
    time.sleep(5)
    print(f'hi: {x}')
    if random.random() > 0.9:
        raise ValueError('f error')
    return x + 1

@boost(MyBoosterParams(queue_name='queue_test_g02t',broker_kind=BrokerEnum.REDIS,qps=0.5,
max_retry_times=0,))
def f2(x,y):
    time.sleep(2)
    print(f'hello: {x} {y}')
    if random.random() > 0.5:
        raise ValueError('f2 error')
    return x + y

@boost(MyBoosterParams(queue_name='queue_test_g03t',broker_kind=BrokerEnum.REDIS,qps=0.5,
max_retry_times=0,concurrent_mode=ConcurrentModeEnum.ASYNC))
async def aio_f3(x):
    await asyncio.sleep(3)
    print(f'f3aa: {x}')
    if random.random() > 0.5:
        raise ValueError('f3 error')
    return x + 1

if __name__ == '__main__':
    start_funboost_web_manager(port=27018)  # 也可以在python代码中启动web,来启动 funboost web manager funboost队列管理界面。可以不需要命令行来启动。
    
    f.multi_process_consume(4)
    f2.multi_process_consume(5)
    aio_f3.consume()
    for i in range(0, 1000000):
        f.push(i)
        f2.push(i)
        aio_f3.push(i)
        time.sleep(1)
    ctrl_c_recv()
    

    

    

```

<div> </div>

# 20 gemini ai大模型 生成的 `funboost` 框架的中心思想


**说明: 此文档第20章节所有内容,是由 `gemini` ai大模型 生成的对 `funboost` 框架的中心思想总结**

<div class="inner_markdown">

**Funboost：通用分布式函数调度框架的全面分析**

## **20.0 执行摘要**

Funboost 在 Python 分布式计算领域中展现出颠覆性的力量，它独特地融合了“轻量级使用方式”与“重量级功能集”，重新定义了分布式函数调度。该框架通过一个极其简洁的 @boost 装饰器，为开发者提供了无与伦比的易用性，同时实现了卓越的性能、广泛的消息队列兼容性（“万物皆可为 Broker”）以及强大的任务控制能力。Funboost 直接应对了 Python 语言固有的并发挑战（如 GIL），通过智能的多模式并发机制有效规避其影响。其核心理念是“自由编程 降维打击 框架奴役”，旨在将开发者从 Celery 和 Scrapy 等传统框架的僵化束缚中解放出来。本报告将深入分析 Funboost 的架构、功能、性能指标及其与现有主流框架的战略性对比，旨在为寻求提升开发效率、降低运维成本并保障任务可靠性的高级 Python 开发者和软件架构师提供全面的评估依据。

## **20.1 Funboost 引言：重新定义分布式函数调度**

### **20.1.1 核心理念：轻量级使用，重量级功能**

Funboost 的核心价值主张在于其作为一款万能分布式函数调度框架，旨在统一编程范式、显著降低开发复杂性，并为各种分布式任务调度需求提供强大且高性能的解决方案 。该框架最引人瞩目的特点是它成功地将“轻量级使用方式”与“重量级功能集”巧妙结合，彻底颠覆了“功能强大必然意味着使用复杂”的传统观念 。
Funboost 的设计哲学体现在其极简的 API 上：用户只需在任意 Python 函数前添加一行 @boost 装饰器，即可将该函数转化为可分布式执行的任务 。这种设计使得框架的使用方式极其轻量级，用户只需学习 @boost 装饰器的入参即可掌握所有用法，大大简化了学习曲线 。这种通过单一装饰器实现强大功能的模式，本质上是软件设计中“约定优于配置”原则的体现。框架通过智能的默认设置和内部机制，自动化地处理了分布式任务调度中的诸多复杂细节，例如消息队列的选择、并发模式的配置以及任务可靠性的保障。开发者无需深入了解底层实现，即可利用这些高级功能。例如，中间件配置文件 funboost_config.py 会自动生成在项目根目录，用户无需到处查找文档来了解可配置项 。这种自动化配置极大地降低了初始设置的复杂性，使得开发者能够迅速投入到业务逻辑的开发中。
这种设计理念的深层影响在于，它将复杂性从开发者暴露的接口中移除，转移到框架的内部实现中。通过精心设计的抽象层，Funboost 使得高级分布式功能变得易于发现和使用，同时通过 IDE 自动补全等特性进一步提升了开发体验 。这种对开发者心智负担的显著降低，是 Funboost 在众多分布式框架中脱颖而出的关键因素。它不仅提供了一个工具，更提供了一种全新的、更高效的分布式编程范式。

### **20.1.2 通用函数调度器：超越传统任务队列**

Funboost 将自身定位为“Python 万能分布式函数调度框架”，其功能远超传统意义上的任务队列 。它支持 5 种并发模式、30 多种消息队列中间件，并提供 30 种任务控制功能，旨在为任意 Python 函数赋能 。其核心用途概念是经典的“生产者 + 消息队列中间件 + 消费者”编程思想 。
这种“万能”的定位，实际上是将“函数即服务”（Function-as-a-Service, FaaS）的理念引入到自托管的框架环境中。传统任务队列通常要求开发者以特定的方式定义“任务”，例如继承某个基类或实现特定接口，并且可能对任务的输入/输出格式有严格要求。然而，Funboost 的设计目标是“给任意 Python 函数赋能”，这意味着开发者可以将其现有的、普通的 Python 函数直接用于分布式调度，而无需进行大规模的代码重构或适配框架特有的任务定义 。
这种“函数即服务”的实现方式，通过 @boost 装饰器将一个普通函数“无服务器化”，使其能够被远程调用、并发执行，并内置了高可靠性特性，而开发者无需手动管理底层的计算资源或基础设施细节。这种方法极大地降低了采用分布式模式的门槛。开发者可以将现有的同步 Python 函数直接转换为分布式任务，立即享受到分布式执行、高并发和容错的优势。例如，一个简单的求和函数，只需添加 @boost 装饰器，即可通过消息队列进行异步调用和分布式执行，而函数本身的逻辑无需改变 。这种灵活性是其与更具侵入性的框架（如 Celery）之间的显著区别，后者往往要求开发者从项目伊始就规划好目录结构和任务定义 。Funboost 证明了，一个框架可以既功能丰富又极其易用，是对传统 Python 框架设计的一次巧妙超越 。

### **20.1.3 应对 Python 并发和性能挑战**

Python 语言在并发和性能方面面临着 GIL（全局解释器锁）的固有挑战，它限制了单个 Python 进程在多核 CPU 上执行 CPU 密集型任务时的并行性。此外，作为一种动态解释型语言，Python 的原生执行速度通常低于编译型语言 。Funboost 的设计直接旨在解决这些挑战，它宣称“有了这个框架，用户再也无需亲自手写操作进程、线程、协程的并发的代码了” 。
Funboost 通过提供多层次的并发机制来战略性地规避 GIL 的影响并提升整体性能。对于 CPU 密集型任务，框架内置了多进程支持，每个进程拥有独立的 Python 解释器和 GIL，从而能够充分利用多核 CPU 实现真正的并行计算 。对于 I/O 密集型任务，Funboost 支持多种细粒度并发模式，包括多线程（threading）、gevent、eventlet 和 asyncio 。其中，Funboost 的线程池是自定义的可伸缩线程池（ThreadPoolExecutorShrinkAble），它能够智能地根据任务负载自动扩大和缩小线程数量，避免资源浪费，并在 I/O 密集型场景中通过线程切换实现高效并发 。
这种设计不仅提供了全面的并发解决方案，更重要的是，它将复杂的并发管理细节从开发者手中抽象出来。开发者无需深入理解 multiprocessing、threading 或 asyncio 的底层机制，也无需手动编写复杂的并发代码。只需通过 @boost 装饰器的参数配置，即可指定所需的并发模式和数量，框架会自动处理任务的分发、执行和结果收集 。例如，通过设置 concurrent_num 或 qps 参数，框架能够自动适应任务的耗时特性，智能地调整并发池大小，以达到设定的执行频率，从而在不牺牲效率的前提下优化资源利用 。这种对语言级别限制的战略性缓解，使得 Funboost 能够为 Python 应用提供强大的分布式和高并发能力，使其在处理大规模任务时更具竞争力。

## **20.2 Funboost 的全面功能集**

Funboost 作为一个功能全面且使用轻量级的分布式函数调度框架，通过一个简单的 @boost 装饰器，为 Python 函数提供了强大的分布式执行能力和丰富的任务控制功能 。

### **20.2.1 多样化的并发模式**

Funboost 囊括了 Python 领域所有主流的并发方式，能够适应 I/O 密集型、CPU 密集型以及 I/O 和 CPU 双密集型等各种编程场景 。

* **threading (多线程)**：Funboost 采用自定义的可伸缩线程池，能够智能地自动扩大和缩小线程数量，避免不必要的资源浪费。即使是 async def 定义的函数，也可以在线程池中运行，每个线程内部启动一个事件循环来执行协程 。
* **gevent / eventlet (协程)**：这两种模式通过猴子补丁（monkey patch）将标准库中的阻塞 I/O 操作转换为非阻塞，从而在单线程内实现高并发的 I/O 密集型任务处理，有效规避 GIL 的限制 。
* **asyncio (异步 I/O)**：Funboost 原生支持 async def 定义的协程函数作为任务。它能够在同一个事件循环中并发运行多个协程，实现真正的异步非阻塞 I/O，这对于构建高性能网络应用至关重要。值得注意的是，Celery 不支持直接调度 async def 函数 。Funboost 的 asyncio 支持不仅限于消费函数，还包括异步发布消息 (aio_push/aio_publish) 和异步获取 RPC 结果 (AioAsyncResult)，构建了完整的异步编程生态 。
* **single_thread (单线程)**：提供了基础的单线程模式，可作为其他并发模式的基础或用于特定调试场景 。
* **多进程 (multiprocess) 叠加并发**：除了上述五种细粒度并发模式外，Funboost 还直接内置支持多进程叠加这些并发模式。这意味着可以实现“多进程 + 协程”或“多进程 + 多线程”的组合，从而充分利用多核 CPU，直接突破 GIL 对 CPU 密集型任务的限制 。这种叠加模式使得 Funboost 能够适应最复杂的计算场景，提供极致的性能。

### **20.2.2 广泛的消息队列中间件种类**

Funboost 在消息队列中间件支持方面展现出其“万能”的特性，支持超过 30 种消息队列中间件。这不仅包括了几乎所有知名的传统消息队列，还支持多种模拟实现的消息队列，以及将其他任务队列框架作为其 Broker 。
其支持范围涵盖：

* **传统消息队列**：如 RabbitMQ (AMQPStorm, RabbitPy, Pika)、Redis (多种实现如 List, ACK-able List, Stream, Priority Queue, PubSub)、Kafka (包括 Confluent Kafka)、Pulsar、NSQ、RocketMQ、ZeroMQ、MQTT、NATS 等 。
* **数据库作为队列**：支持 SQLite、SQLAlchemy (兼容 MySQL, Oracle, SQLServer 等多种数据库)、MongoDB、Peewee (操作 MySQL) 等将数据库表作为消息队列 。
* **文件系统作为队列**：支持本地磁盘队列 (TXT 文件) 。
* **内存队列**：Python 自带的 queue.Queue 实现的内存队列，适用于单进程内的短期简单任务 。
* **HTTP/TCP/UDP Socket 作为队列**：支持通过 HTTP、TCP 或 UDP 协议进行消息传输，无需额外安装中间件，适用于不需要高可靠性但需要跨机器通信的场景 。
* **其他任务队列框架作为 Broker**：Funboost 甚至可以将 Celery、Dramatiq、Huey、RQ、Nameko 等其他流行的 Python 异步消费框架整体作为其 Broker 。这种“万物皆可为 Broker”的设计理念，通过高度可扩展的架构（如利用 Kombu 支持 Celery 所能支持的所有中间件，并提供 consumer_override_cls 和 publisher_override_cls 允许用户自定义扩展），使得 Funboost 具有极高的适应性和前瞻性，能够以不变应万变，兼容未来可能出现的任何消息队列技术 。

### **20.2.3 丰富的任务控制功能**

Funboost 对任务支持超过 30 种控制功能，极大地增强了分布式任务调度的灵活性、可靠性和可管理性 。这些功能涵盖了从并发管理到错误处理，从调度策略到状态监控的方方面面：

* **并发与速率控制**：
  * **控频限流 (QPS)**：能够精确指定函数每秒的执行次数，无论是高频（如 50 次/秒）还是低频（如 0.01 次/秒），无论函数耗时如何波动，都能精确控制 。
  * **分布式控频限流**：在多进程或多机器部署时，能够严格控制所有消费者加起来的总 QPS，自动平分流量，避免因部署数量增加而导致总 QPS 倍增 。
  * **并发数量设置**：可指定并发数量，但通常在设置 QPS 后，框架会智能自适应地调节并发池大小 。
  * **指定并发池**：允许多个消费者共享同一个并发池，节约资源 。
* **任务可靠性与容错**：
  * **任务持久化**：通过消息队列中间件天然支持任务持久化，确保消息不会丢失 。
  * **断点接续运行**：无惧反复重启代码、断电或强制关机，通过消息队列的持久化和消费确认机制，做到不丢失一个消息 。
  * **消费确认**：这是最重要功能之一，保证函数运行完成后才确认消费，正在运行中突然强制关闭进程不会丢失消息 。
  * **立即重试指定次数**：当函数运行出错时，会立即自动重试指定次数，提高任务成功率 。
  * **重新入队**：在消费函数内部主动抛出特定异常 (ExceptionForRequeue) 后，消息可以重新返回消息队列 。
  * **死信队列**：支持将重试达到最大次数仍失败或抛出特定异常 (ExceptionForPushToDlxqueue) 的消息发送到单独的死信队列 。
* **任务调度与管理**：
  * **定时任务**：可按时间间隔、按指定时间执行一次或多次，基于 apscheduler 包实现，支持动态添加/删除和多点部署不重复执行 。
  * **延时任务**：规定任务发布后，延迟指定秒数或在指定精确时间执行 。
  * **指定时间不运行**：可设置任务在特定时间段内不运行 。
  * **超时杀死**：当函数运行时间超过设定阈值时，自动终止该运行中的函数 。
  * **任务过滤**：根据函数入参判断是否已执行过，跳过重复任务 。
  * **任务过滤有效期缓存**：可设置任务过滤的有效期，过期后即使参数相同也会重新执行 。
  * **任务过期丢弃**：可设置消息过期时间，超过该时间的消息将被丢弃不执行，适用于实时性要求高的场景 。
  * **暂停/继续消费**：支持从外部或远程控制暂停和恢复消息消费 。
  * **优先级队列**：支持队列中的消息具有不同优先级，高优先级消息优先被消费 。
  * **远程杀死(取消)任务**：支持在发布端发送命令杀死正在运行的任务或放弃未取出的消息 。
* **监控与可视化**：
  * **计算消费次数速度**：实时计算单个进程的消费次数和速度，并在日志中显示 。
  * **预估消费时间**：根据当前消费速度和队列剩余消息数量估算所需时间 。
  * **函数运行日志记录**：使用 nb_log 提供五彩控制台日志和多进程安全切片的文件日志，并支持 Kafka/Elastic 日志 。日志模板可显示 task_id，方便问题排查 。
  * **函数状态和结果持久化**：可选择将函数入参、运行结果和运行状态持久化到 MongoDB 或其他数据库（如 MySQL），用于后续追溯、统计和 Web 展示 。
  * **消费状态实时可视化**：通过 Web Manager 页面实时刷新函数消费状态，包括成功/失败、异常信息、重试次数、执行机器信息、函数入参/结果和耗时等 。
  * **消费次数和速度统计表可视化**：生成 Echarts 统计图，展示不同时间粒度的消费次数和速度 。
* **高级交互与扩展**：
  * **RPC (远程过程调用)**：生产端（发布端）可获取消费结果，使得发布端能对消费结果进行后续处理，而非让消费端一干到底 。支持同步和异步 RPC 。
  * **远程服务器部署**：提供 Python 代码级别的一键远程 Linux 机器部署功能，无需其他运维工具 。
  * **命令行操作**：支持通过 fire 实现的命令行工具，方便启动消费、发布消息、清空队列等 。
  * **上下文管理 (fct)**：提供智能上下文，允许在消费函数及其调用链中的任意函数中获取当前任务的完整信息（如 task_id、发布时间、重试次数等），无需显式传递参数 。
  * **消费任意消息格式**：通过 should_check_publish_func_params=False 和自定义 _user_convert_msg_before_run 方法，Funboost 可以消费包含随机键的 JSON 消息，甚至任意非 JSON 格式的消息，展现出极强的异构兼容性 。
  * **支持实例方法和类方法**：Funboost 新增支持将实例方法和类方法作为消费函数，提供了更灵活的编程范式 。

这些全面的功能集使得 Funboost 能够应对各种复杂的分布式任务调度需求，从简单的后台任务到高并发的实时数据处理，再到复杂的爬虫场景，都能提供稳定、高效且易于管理的解决方案。

## **20.3 开发者体验与卓越性能**

Funboost 旨在提供轻量级的使用方式和重量级的功能集，颠覆了"功能强大=使用复杂"的传统思维 。其在开发者体验和整体性能方面的表现，是其核心竞争力的重要组成部分。

### **20.3.1 极简的使用方式与无侵入性**

Funboost 的核心理念是"只需要一行 @boost 代码即可分布式执行 Python 一切任意函数" 。这种设计使得框架的使用方式极其轻量级，用户只需学习 @boost 装饰器的入参即可掌握所有用法，大大简化了学习曲线 。  
Funboost 对现有项目代码几乎没有入侵性，可以添加到任意已有项目，而对 Python 文件目录结构零要求 。这与 Celery、Django、Scrapy 等框架形成鲜明对比，这些框架通常要求从一开始就规划好项目目录结构，如果不想使用或想改变框架，已有的代码组织形式几乎会成为废品，需要大改特改 。Funboost 则完全不会这样，无论是添加还是移除 @boost 装饰器，对项目影响为零，用户可以照常使用。即使不使用 Funboost，函数上的 @boost 装饰器也不会影响函数自身的直接调用运行，例如 fun(x,y) 是直接运行函数，而 fun.push(x,y) 才是发送到消息队列 。这种设计极大地降低了框架的引入成本和未来的技术债务，使得开发者可以随时引入或移除 Funboost，而无需担心对项目结构的破坏性影响。这种无侵入性是 Funboost 在现有复杂系统中推广和应用的重要优势。

### **20.3.2 IDE 自动补全与简化配置**

Funboost 框架在开发者体验方面的一个显著优势是其对 IDE 自动补全的极致重视 。@boost 装饰器的入参能够自动补全，更重要的是，被 @boost 装饰的函数，其方法（如 .push(), .consume(), .multi_process_consume()）和每个方法的入参都能自动补全 。这解决了 Celery 等框架在 PyCharm 中无法自动补全提示的问题，用户无需猜测函数有什么方法或配置文件能写哪些配置 。这种全面的自动补全极大地降低了用户的调用出错概率，提高了开发效率，使得开发者能够更专注于业务逻辑，而不是记忆复杂的 API 或查阅冗长的文档 。  
此外，Funboost 的中间件配置文件 funboost_config.py 会自动生成在用户当前项目根目录，用户无需到处查找文档来了解能配置什么或如何配置框架功能 。这种自动化配置进一步简化了开发流程，尤其对于初学者而言，避免了因配置问题而产生的常见困扰。框架还无需使用复杂难记的命令行启动消费，消费者可以直接通过 fun.consume() 或 fun.multi_process_consume() 方法启动消费，避免了输入错误和不友好的体验 。这种对开发者友好度的全面提升，使得 Funboost 即使功能强大，也能保持极高的易用性。

### **20.3.3 性能基准测试与 QPS 精准控制**

Funboost 在消息发布和消费方面表现出显著的性能优势 。在 Win11 + Python 3.9 + 本机 Redis 中间件 + AMD R7 5800H CPU + 单线程并发模式 + 相同逻辑消费函数的测试环境下，Funboost 的性能数据令人印象深刻 。  
**性能对比数据：**

* **发布性能**：Funboost 发布 10 万条消息耗时 9 秒，平均每秒发布 11000 条。相比之下，Celery 发布 10 万条消息耗时 110 秒，平均每秒发布 900 条。这表明 **Funboost 的发布性能约为 Celery 的 12 倍** 。  
* **消费性能**：Funboost 平均每隔 0.15 秒消费 1000 条消息，每秒消费约 7000 条。而 Celery 平均每隔 3.6 秒消费 1000 条消息，每秒消费约 300 条。这意味着 **Funboost 的消费性能约为 Celery 的 23 倍** 。

这些数据清晰地表明，Funboost 在性能上实现了对 Celery 的断崖式领先，性能不在一个数量级 。  
**QPS 精准控制：** Funboost 提供了强大的 QPS（每秒查询/执行次数）控频功能，能够精确控制函数每秒的执行次数，无论是小数（如 0.01 次/秒）还是高频（如 50 次/秒），都能实现精准控频 。即使函数耗时随机波动，框架也能通过自适应并发数量来保持 QPS 恒定 。例如，对于一个耗时随机在 0.1 毫秒到 5 秒之间波动的函数，Funboost 依然能将其 QPS 精确控制在 100 次/秒，控频精确度达到 96% 以上 。对于耗时恒定的函数，其控频精确度甚至高达 99.9% 以上 。  
这种精准的 QPS 控制，与传统框架仅能控制并发数量形成鲜明对比。并发数量只有在函数耗时恰好等于 1 秒时才等同于 QPS，而在其他情况下，两者之间存在显著差异 。Funboost 的 QPS 控制能够自适应智能动态调节并发池大小，无需用户手动指定并发数量，极大地简化了性能调优 。此外，Funboost 还支持分布式全局 QPS 控频，无论启动多少台机器或进程，都能严格控制总的 QPS，而无需担心 QPS 随部署数量倍增 。这种分布式控频的开销极低，因为它不依赖 Redis 的 incr 计数，而是基于每个消费者发送到 Redis 的心跳来统计活跃消费者数量，并在此基础上在本地进行流量分配和计数 。

### **20.3.4 跨平台兼容性与稳定性**

Funboost 在跨平台兼容性方面表现出色，对 Windows、Linux 和 Mac 操作系统都提供全面支持 。这与 Celery 等框架形成对比，Celery 4 以后官方放弃了对 Windows 的支持和测试，导致其默认的多进程模式在 Windows 上无法启动或运行出错，这给开发者的本地开发环境带来了不便 。Funboost 确保了在不同操作系统上行为的 100% 一致性，极大地提升了开发和部署的便利性。  
在稳定性方面，Funboost 展现出卓越的可靠性。根据报告，该框架已经连续超过三个季度稳定高效运行，未出现假死、崩溃或内存泄漏等问题 。这种稳定性对于面向 C 端用户（包括 App 和小程序）的百万级并发场景至关重要。Funboost 通过其消息万无一失的特性进一步保障了系统的健壮性。即使在极端情况下，如执行函数的机器突然断电、强制硬关机，或进程被粗暴终止，只要消息队列中间件的机器未被破坏，消息就不会丢失 。这是通过消费确认机制实现的：只有当函数运行完成后才确认消费，正在运行中突然强制关闭的进程不会丢失消息，下次启动时这些消息仍会被消费或被其他机器接管 。例如，Funboost 对 Redis 的实现机制也增加了额外的保障层，使其在 Redis 上也能实现可靠的消费确认，而不仅仅依赖于 RabbitMQ 等原生支持 ACK 的中间件 。这种对任务可靠性的极致追求，使得 Funboost 成为构建高可用分布式系统的理想选择。

## **20.4 Funboost 与 Celery 的深度对比**

Funboost 的出现，对 Python 领域长期占据主导地位的 Celery 框架构成了直接挑战。本节将通过严格的控制变量法，全面对比两者在核心设计、易用性、功能和性能上的差异，突出 Funboost 的显著优势。

### **20.4.1 核心设计理念与关系澄清**

在对比 Funboost 与 Celery 之前，有必要澄清两者之间的关系和核心设计理念。Celery 长期以来是 Python 异步任务和分布式任务队列的行业标准。然而，Funboost 明确指出，其并非对 Celery 的模仿或启发，也无法找到与 Celery 连续三行一模一样的代码 。  
Funboost 强调，生产者-Broker-消费者模式是计算机科学中一个非常基础和经典的设计模式，其历史远比 Celery 悠久 。无论是线程池（其内部也采用生产者-Broker-消费者思想）还是 Java 等其他语言的实时数据处理框架（如基于 Kafka 的封装），都普遍采用这种模式 。因此，将所有采用该模式的框架都视为"抄袭 Celery"是不合理的 。Funboost 的设计起源于其作者在实际项目中对 while 1: redis.blpop() 这种重复模式的扩展和优化 。  
Funboost 的核心设计理念是"以函数为中心"的调度。它将任意 Python 函数视为可调度的基本单位，并通过 @boost 装饰器为其赋能，使其具备分布式、并发、可靠性等特性 。这种设计使得开发者可以专注于函数本身的业务逻辑，而无需关心底层的调度机制。相比之下，Celery 虽然也调度函数，但其设计更偏向于"任务队列框架"，要求开发者以更严格的方式定义和注册任务，并与框架的特定组件（如 Celery 应用实例、任务路由）紧密耦合 。这种差异导致了两者在易用性、灵活性和性能上的根本性分歧。

### **20.4.2 易用性与开发效率对比**

Funboost 在易用性和开发效率方面对 Celery 实现了显著的提升，解决了 Celery 长期以来饱受诟病的复杂性问题 。  
**目录结构与任务注册：** Celery 对项目目录层级和文件名称格式有很高的要求，这使得它更适合从头规划的新项目，而对于不规则的现有项目，集成难度极高 。新手在使用 Celery 时，需要小心翼翼地模仿网上的目录结构和文件命名，否则极易遇到 Task of kind 'tasks.add' is not registered 等令人头疼的错误 。这主要是因为 Celery 需要一个中心化的 Celery 应用实例（通常命名为 app），消费函数所在的脚本需要导入这个 app，并且在 Celery 启动时，需要通过 settings 配置文件中的 include 或 imports 参数来明确告知 Celery 哪些模块包含了任务定义，以避免循环导入问题 。  
相比之下，Funboost 天生没有这些问题 。它不依赖任何固定的目录结构，实现了 100% 的自由度，开发者可以将使用框架的代码写在任意深层级或不规则的文件路径下，脚本也可以随意移动和改名 。Funboost 的装饰器设计不需要一个类似 Celery app 实例的全局变量，从而避免了相互导入的困扰。当用户第一次运行任何导入了 Funboost 的脚本文件时，中间件配置文件 funboost_config.py 会自动生成在当前项目根目录，用户只需按需修改即可 。这种设计极大地简化了项目的集成和维护。  
**IDE 自动补全：** 这是 Funboost 在开发者体验方面对 Celery 的"暴击"之一 。Celery 的许多重要公共方法和配置项在 IDE 中几乎无法自动补全提示 。例如，@app.task 装饰器的参数、add.apply_async 方法的 20 种入参，以及 Celery 的 100 多个配置项，用户往往无从得知其具体名称和可用值，只能依靠查阅文档或猜测，极易出错 。  
Funboost 则对此进行了额外的优化。@boost 装饰器的所有 20 个函数入参及其类型都支持自动补全提示，并且通过 Ctrl + Shift + I 等快捷键可以清晰地查看其注释说明 。更重要的是，被 @boost 装饰的函数，其 push、publish、consume、multi_process_consume 等方法及其入参也都能很好地自动补全 。Funboost 甚至宁愿重复声明入参，也不使用 *args 或 **kwargs 这种会导致 IDE 无法补全的泛型参数，一切设计都为了给调用者带来使用上的方便 。这种全面的自动补全能力，显著降低了用户的调用出错概率，极大地提升了开发效率和代码质量。  
**启动方式：** Celery 通常需要通过复杂且难记的命令行指令来启动 worker、beat 和 flower，例如 celery -A celeryproj worker + 一大串cmd命令行，用户容易打错字母，且不清楚可以传递哪些参数 。  
Funboost 则简化了这一过程。消费者可以直接通过 python xx.py 方式启动，或者在代码中调用 fun.consume() 或 fun.multi_process_consume() 方法来启动消费 。这种直接的代码启动方式更加直观和友好，避免了命令行操作的繁琐和易错性。

### **20.4.3 功能与性能差异**

Funboost 在功能和性能方面对 Celery 实现了多维度的超越，提供了更强大、更灵活且更可靠的分布式函数调度解决方案。  
**并发模型：** Celery 的多进程和多线程是互斥的并发模式，开发者通常需要二选一 。然而，许多任务场景（如 I/O 密集型与 CPU 密集型混合）需要同时利用多核 CPU 和细粒度并发来绕过 I/O 阻塞。Funboost 则支持多进程叠加多线程或协程的并发模式 。例如，可以启动"多进程 + 协程"或"多进程 + 多线程"的组合，从而充分利用多核 CPU 和高效处理 I/O 阻塞，显著提升运行速度 。Funboost 的自定义线程池能够智能伸缩，在保证效率的同时避免资源浪费，而 Celery 使用的原生 concurrent.futures.ThreadPoolExecutor 无法自动缩小线程池 。  
**消息队列支持：** Funboost 支持 30 多种消息队列中间件，包括几乎所有主流的传统 MQ，以及本地磁盘队列、数据库队列、内存队列，甚至可以将 Celery、Dramatiq、Huey 等其他任务队列框架整体作为其 Broker 。Funboost 通过支持 Kombu（Celery 的中间件依赖库），能够自动继承 Kombu 支持的所有现有和未来的消息队列能力（如 Google Pub/Sub、Azure Service Bus），实现了"以逸待劳"的策略 。相比之下，Celery 虽然也支持多种中间件，但其支持范围不如 Funboost 广泛，例如不支持 Kafka、NSQ、MQTT、ZeroMQ、RocketMQ、Pulsar 等 。Funboost 的架构设计使其能够非常容易地扩展用户自己的任何中间件作为 Broker，这在 Celery 中几乎不可能实现，需要深入理解其底层消息库 Kombu 的 Transport 和 Channel 接口 。  
**QPS 控频精度：** Funboost 在速率控制方面表现出卓越的精准度。它能够精确控制函数每秒的执行次数（QPS），对固定耗时任务的控频精确度高达 99.9% 以上 。即使函数耗时随机波动，其控频精确度也能达到 96% 以上 。相比之下，Celery 的 rate_limit 控频精度较低，在 QPS 超过 20/s 时可能只有 60% 左右，且其 rate_limit 基于单 worker 控频，无法实现分布式全局控频 。Funboost 则能够支持全局分布式 QPS 控频，无论启动多少台机器和进程，都能严格控制总的 QPS，自动在所有消费者之间平分流量 。  
**原生 Asyncio 支持：** Funboost 原生支持 async def 函数作为消费函数，并支持完整的 asyncio 编程生态，包括异步发布消息 (aio_push/aio_publish) 和异步获取 RPC 结果 (AioAsyncResult) 。这意味着 Funboost 可以与 FastAPI 等现代异步 Web 框架无缝集成。Celery 不支持直接调度执行 async def 定义的函数 。  
**任务控制功能：** Funboost 提供了比 Celery 更丰富的任务控制功能 。除了 Celery 支持的并发、控频、超时杀死、重试、消息过期、消费确认等功能外，Funboost 还包括原生对函数入参的任务过滤、分布式 QPS 全局控频等 Celery 不支持的功能 。  
**消息确认机制（Redis 场景）：** 在 Redis 作为 Broker 的场景下，Funboost 的 REDIS_ACK_ABLE 中间件在消息确认机制上显著优于 Celery 的 Redis + task_acks_late=True + visibility_timeout 组合 。Celery 在 worker 进程被强制终止后，待确认的孤儿消息需要等待 visibility_timeout（默认 1 小时）时间后才能重回队列，这导致消息重回不及时，且可能将耗时长的消息误判为孤儿消息而重复入队，两者之间存在矛盾 。Funboost 的 REDIS_ACK_ABLE 则使用消费者心跳检测机制，能够及时、快速、精准地让孤儿消息重回工作队列，并且不会将执行慢的消息误认为是宕机的孤儿消息 。

### **20.4.4 颠覆性优势：Funboost 作为 Celery 的 Broker**

Funboost 最具颠覆性的优势之一是其能够支持 Celery 框架整体作为 Funboost 的 Broker 。这意味着，开发者可以使用 Funboost 极简的 API 来定义消费函数和发布消息，但实际的核心消费调度、发布和定时功能则由 Celery 框架来完成 。  
这种机制的战略意义在于：

* **结合两者的优点**：对于那些对 Funboost 稳定性有所疑虑，或迷信 Celery 性能的开发者，这种模式提供了一个理想的解决方案。它结合了 Funboost 简洁直观的 API 接口，使得开发变得轻松，同时利用了 Celery 稳定可靠的底层调度引擎 。  
* **简化 Celery 使用**：用户无需操作 Celery 本身，无需敲击 Celery 难记的命令行启动消费、定时或 Flower 。Funboost 会自动化配置 Celery 的任务路由、include 设置、队列命名等繁琐细节，完全摆脱了 Celery 对固定目录结构和手动配置的依赖 。  
* **IDE 自动补全的福音**：Celery 框架的许多核心方法（如 @app.task、apply_async）的入参声明都是 *args, **kwargs，导致在 IDE 中无法自动补全，极大地增加了使用难度 。通过 Funboost 的 API 操作 Celery，开发者可以享受到 Funboost 提供的全面自动补全功能，显著提升开发效率 。  
* **"子集化" Celery**：Funboost 通过支持 Celery 作为 broker_kind，使得 Celery 框架成为了 Funboost 的一个子集 。这意味着"Celery 有的 Funboost 都有，Celery 没有的 Funboost 也有" 。这种包容性不仅证明了 Funboost 架构的精妙和复杂性，也为开发者提供了极大的灵活性，可以在 Funboost 和 Celery 的调度核心之间无缝切换，而无需改变上层应用代码 。

这一特性有力地回击了所有关于 Funboost 稳定性的质疑，因为即使开发者不信任 Funboost 自身的调度实现，也可以选择使用其 API 来驱动 Celery 的核心调度引擎，从而获得两全其美的解决方案。

### **20.4.5 讨 Celery 檄文：Funboost 十胜定乾坤**

**夫任务调度之道，贵在通达！队列纵横之术，胜在易用！**  
昔 Celery 恃 RabbitMQ Redis 之威，窃踞调度王座十数载，然其架构臃肿如裹足老象，兼容性似残破牢笼！今观其势：弃 Windows 如敝履，控频精度若醉汉；困目录结构作茧，性能吞吐成笑谈——开发者叩首于五千页文档，匍匐于晦涩命令行，此诚天下苦秦久矣！  
今有 Funboost，承函数调度天命，执 @boost 神器，以性能裂苍穹之威，兼容纳百川之量，革旧弊，立新规，伐无道！十胜锋芒所指，Celery 十败如山崩！

#### **十胜十败·定鼎九州**

**一胜曰：疆域之胜** Celery 弃 Windows 疆土，多进程启动即崩，开发寸步难行，此谓**金瓯残缺失半壁**！ Funboost 跨三界称尊，进程线程协程任选，开发生产皆驰骋，此谓**寰宇纵横掌天门**！  
**二胜曰：器量之胜** Celery 闭中间件之门，Kafka/MQTT 皆拒，新潮队列成陌路，此谓**夜郎闭户终自绝**！ Funboost 纳廿四路诸侯，内建队列立乾坤，更兼**兼容 Celery 全系器**，此谓**海纳百川容星汉**！  
**三胜曰：神速之胜** Celery 吞吐若老牛破车，性能瓶颈成痼疾，此谓**老牛破车困泥潭**！ Funboost 疾如雷霆裂空，**发布快 1000% 惊鬼神，消费疾 2000% 贯九霄**，此谓**追风逐电荡八荒**！  
**四胜曰：明道之胜** Celery 动态元编程蔽日，参数传递如盲人摸象，此谓**雾锁重楼失北斗**！ Funboost 智能补全烛幽冥，类型声明破迷障，IDE 红线斩谬误，此谓**日月当空照坦途**！  
**五胜曰：简政之胜** Celery 命令行如天书符咒，路径错漏频生，此谓**蜀道悬梯困苍生**！ Funboost 执 python xx.py 开太平，老幼皆宜无障碍，此谓**大道至简定江山**！  
**六胜曰：自由之胜** Celery 目录囚笼锁蛟龙，imports 镔铐缚云翼，此谓**金丝雀困雕花笼**！ Funboost 十层深阁任穿梭，脚本四海可为家，此谓**鲲鹏振翅九万里**！  
**七胜曰：包容之胜** Celery 消息混杂 Python 痕，跨语言协作成天堑，此谓**孤岛闭门终自绝**！ Funboost **纯净 JSON 通万邦**，Python/Java 共交响，此谓**丝绸新路连寰宇**！  
**八胜曰：天时之胜** Celery 拒 async 浪潮于门外，协程革命空嗟叹，此谓**刻舟求剑失沧海**！ Funboost 纳 asyncio 入经脉，**异步同步皆如意**，此谓**弄潮敢缚蛟龙归**！  
**九胜曰：王道之胜** Celery 控频单机尚粗疏，分布式更成镜花月，此谓**乌合之众溃荒原**！ Funboost 执**令牌桶算法掌乾坤**，分布式控频**精度 99.9% 镇山河**，此谓**虎符一出千军肃**！  
**十胜曰：革新之胜** Celery 拒类方法于高墙，面向对象成虚妄，此谓**孤芳自赏终取祸**！ Funboost 纳**万物入调度**，实例方法皆可 Boost，此谓**开宗立派写新章**！

#### **弑王绝刃·乾坤倒转：**

更备诛神兵符：Funboost 竟容 Celery 为子集！@boost(broker_kind=BrokerEnum.CELERY) 一出，旧王纵有疑心，亦成新朝马前卒！此谓**乾坤倒转收降将**，古今未闻之奇策！  
今 Funboost 携十胜之威：东收 Redis 为粮仓，西纳 RabbitMQ 作辕门；南降 Kafka 为前哨，北抚 ZeroMq 成轻骑！三军并发：多进程裂地，多线程碎空，协程织天网！  
开发者当顺天命：破 Celery 之枷锁，入函数调度新纪元！何须啃五千页腐简？不必忍性能之憋屈！此乃**任务调度之工业革命，函数王朝之开国大典**！

## **5\. Funboost 与 Scrapy 等爬虫框架的对比**

Funboost 作为一个"函数调度器"，在处理复杂爬虫场景、断点续爬可靠性、反爬虫策略简化等方面相较于 Scrapy 等"URL 调度器"具有显著的优越性 。

### **20.5.1 核心理念：函数调度 vs. URL 调度**

Scrapy 是一个典型的"URL 调度器"，其核心设计围绕 Request 和 Response 对象展开，整个框架旨在调度一系列的 URL 请求 。开发者必须遵循其固定的模式，如定义 Spider 类、在 start_requests 或 parse 方法中 yield Request 来生成新的请求 。这种模式虽然在特定场景下高效，但其本质是对开发者思维的"框架奴役"，限制了自由编程的空间 。Scrapy 的设计哲学诞生于一个需要"框架来定义一切"的时代，这在今天看来，反而成了一种束缚 。  
相比之下，Funboost 是一个"函数调度器"，其核心理念是"以函数为本，万物皆可调度" 。它将任意 Python 函数视为可调度的基本单位，并通过 @boost 装饰器为其赋能 。这意味着开发者可以像编写普通 Python 函数一样编写爬虫逻辑，然后通过 @boost 装饰器将其转化为可分布式、高并发、高可靠执行的任务 。Funboost 相信开发者的能力，只提供最强大的调度核心，将业务逻辑的自由完全交还给用户 。它实现了"写函数就能爬虫"，而 Scrapy 则是"写框架才能爬虫" 。  
这种核心理念的差异导致了 Funboost 对 Scrapy 的"降维打击" 。Funboost 用通用的万能函数调度框架解决特定的爬虫问题，功能更全面，更灵活 。它让开发者可以专注于"解决问题"，而 Scrapy 却常常让开发者把时间花在"解决框架本身的问题"上 。

### **20.5.2 开发效率与易用性对比**

Funboost 在开发效率和易用性方面对 Scrapy 具有压倒性优势，显著降低了爬虫开发的复杂度和心智负担。  
**代码量与文件结构：** Scrapy 项目通常冗杂，一个简单的爬虫也需要创建 7-8 个文件（如 spider.py, settings.py, items.py, pipelines.py, middlewares.py 等），开发者需在多个文件间频繁切换编写代码 。这种分散的代码结构增加了学习成本和维护难度 。 Funboost 则极其精简，一个复杂的分布式爬虫甚至可以在单文件中完成，代码量极少 。开发者只需在函数上添加 @boost 装饰器，即可实现自动并发调度，无需遵循特定的文件结构或在多个文件间切换 。  
**HTTP 库选择与反爬策略：** Scrapy 强制使用其内置的基于 Twisted 的下载器，如果想使用 requests、httpx、selenium 或 playwright 等其他 HTTP 客户端库，需要进行复杂的中间件封装，这增加了开发难度 。 Funboost 则提供了完全自由的 HTTP 库选择。开发者可以在函数内部随意使用任何喜欢的库来发送请求，无需考虑与框架的适配问题 。在反爬策略方面，Funboost 实现换 IP、UA 等逻辑极其简单，只需封装一个通用的 my_request 函数即可，零门槛 。这比 Scrapy 中编写和注册下载器中间件（Downloader Middleware）要简单数百倍，后者概念复杂，对新手极不友好 。Funboost 的这种设计使得开发者可以将精力完全集中在反爬逻辑本身，而不是框架的适配。  
**单元测试与调试：** Scrapy 的 Spider 逻辑分散在多个回调方法中，这些回调方法与框架的 Request/Response 对象、meta 字典、调度器等上下文强耦合，难以在 IDE 中单独调用进行单元测试 。开发者通常只能整体运行 Spider，然后观察输出或日志来调试，效率极低 。 Funboost 则提供了极其容易的单元测试能力。每个被 @boost 装饰的函数都可以直接调用，独立进行单元测试 。其线性执行的函数逻辑，使得使用标准 pdb 或 IDE 调试器即可轻松调试，显著提升了调试效率 。此外，Funboost 的函数参数、push/publish 方法均有代码补全，而 Scrapy 的 response.meta 是无类型字典，IDE 无法提供任何键的补全提示，极易出错，进一步凸显了 Funboost 在开发体验上的优势 。

### **20.5.3 功能与可靠性差异**

Funboost 在功能和可靠性方面对 Scrapy 展现出全面的领先，尤其是在处理复杂爬虫场景和保障数据完整性方面。  
**并发与速率控制：** Scrapy 的并发主要由 CONCURRENT_REQUESTS 参数控制，难以充分利用多核 CPU 。Funboost 则支持多进程、多线程/协程以及多机器的四重叠加并发，性能卓越，能够充分利用所有 CPU 核心 。在速率控制方面，Funboost 可通过 qps 参数精确控制每秒请求次数，无视响应时间波动，精度可达 99.9% 以上 。这与 Scrapy 只能控制并发请求数，无法保证稳定的请求速率形成鲜明对比 。此外，Funboost 还支持分布式全局 QPS 控制，确保总请求速率稳定，而 Scrapy 则无法实现 。  
**断点续爬与数据可靠性：** Scrapy-redis 的断点续爬机制基于 redis.blpop()，一旦弹出，元素即从列表中移除。这意味着，如果爬虫进程崩溃、断电或强制关机，已从 Redis 取出到内存中但尚未处理完成的 URL 种子将永久丢失 。这可能导致大量重要数据（如导航页或列表页）的丢失，进而影响后续详情页的爬取，需要反复人工干预才能爬取完整 。 Funboost 则提供了真正可靠的断点续爬能力，其支持的 40 种消息队列中，许多都原生支持消费确认（ACK）机制 。这意味着，即使在代码反复重启、断电或强制关机的情况下，未运行完成的消息也不会被确认消费，从而不会丢失 。即使是 Redis 作为 Broker，Funboost 的 REDIS_ACK_ABLE 模式也支持消费确认，确保任务万无一失 。  
**任务去重：** Scrapy 的去重功能基于 URL 指纹，对于 URL 中包含时间戳、随机数或追踪来源 ID 等噪音字段的情况，其内置去重能力显得笨拙且无能为力 。开发者需要手动自定义继承 RFPDupeFilter 并重写 request_fingerprint 方法，编写复杂的正则表达式来清洗 URL，这增加了开发和维护成本 。 Funboost 则提供了更智能的去重功能，它基于函数的核心入参进行去重，天然无视 URL 中的噪音字段 。例如，如果爬虫函数定义为 def craw_product(product_id, a, b)，Funboost 会根据 product_id, a, b 进行去重，而不会受 URL 中 _ts 或 _rand 等无关参数的影响 。此外，Funboost 还支持设置任务过滤的有效期，适合周期性更新的爬取任务，而 Scrapy 默认是永久去重，不灵活 。  
**复杂流程处理：** Scrapy 在处理复杂爬虫场景时显得力不从心，例如需要多轮浏览器交互（如 Selenium 渲染页面后，根据内容判断点击不同按钮，然后等待元素出现再提取数据）或处理短时效 Token 的场景 。在 Scrapy 中，这类任务通常需要将逻辑分散到多个回调函数中，导致"回调地狱"，并且难以保证请求的时序性，甚至可能导致异步模型失效 。例如，在 Scrapy 中获取短时效 Token 后，通过 yield Request 发送下一个请求，无法保证该请求在 Token 过期前被执行，可能导致数据丢失 。 Funboost 则能极其自然地处理这些复杂流程。开发者可以在单个函数内部连续请求多个 URL，确保在获取 Token 后的极短时间内立即发送下一个请求，从而保证 Token 的时效性 。整个逻辑集中在一个函数内，代码可读性高，状态管理简单，错误处理也更集中 。  
**插件生态：** Scrapy 的插件生态看似丰富（如 scrapy-redis, scrapy-selenium, scrapy-playwright 等），但 Funboost 认为这恰恰是其"病"而非"药" 。Scrapy 插件多，是因为其框架本身高度抽象、强约束、多钩子生命周期和中间件堆叠机制，导致用户难以自由扩展，必须依赖专门的大神开发插件来适配其框架 。 Funboost 则完全不需要这些插件，其核心思想是"无需插件，Python 生态即是其生态" 。开发者可以轻松自由地使用任何 Python 第三方包（如 requests, httpx, selenium, playwright），无需等待或学习专门为 Funboost 开发的适配插件 。这种零框架束缚的设计，使得 Funboost 在处理任何新工具或新需求时，都能以最低的集成成本实现。

### **20.5.4 集中驳斥 Scrapy 优势论**

针对一些常见的 Scrapy 优势论点，Funboost 提供了强有力的驳斥，强调其在多方面对 Scrapy 的"碾压"式领先。  
**质疑 Funboost 没有 HTTP 中间件？** Funboost 认为，用户可以手写定义一个通用的 my_request 函数，该函数可以封装代理 IP 切换、User-Agent 轮换等逻辑 。这种方式比在 Scrapy 中编写和注册复杂的下载器中间件更加简单、自由和直观，且零门槛 。  
**质疑 Funboost 没有 Pipeline，保存数据麻烦？** Funboost 允许开发者在函数内部直接调用任何数据库的客户端库进行数据存储，完全自由 。用户可以自己封装一个保存字典到数据库的函数，甚至直接使用 dataset 等知名包，一行代码即可实现数据持久化，比 Scrapy 强制通过 Item Pipeline 机制更加灵活和直接 。  
**质疑 Scrapy 插件生态丰富，Funboost 没有三方扩展？** Funboost 认为，Scrapy 插件多是其"病"，而非"药" 。Scrapy 框架的复杂约束和多钩子生命周期，导致用户必须依赖专门的大神开发插件才能使用新工具。Funboost 则恰恰不需要插件，因为其开放的设计使其天然就能融合任何第三方库，Python 的整个 PyPI 生态就是 Funboost 的生态 。开发者无需等待或学习专门的适配插件，可以直接使用任何熟悉的工具 。  
**质疑 Scrapy 社区支持，有庞大的专门各种问题的讨论？质疑 Funboost 没有社区？** Funboost 认为，Scrapy 社区讨论多，恰恰是因为其框架复杂，用户在自由扩展时遇到诸多约束和难题，需要寻求帮助 。Funboost 则鼓励开发者在函数内部自由编写任何代码，不需考虑框架本身的约束，因此没有那么多需要讨论的框架特定问题。关于具体工具（如 pymysql、selenium、requests）的使用问题，应在相应的工具社区讨论，与 Funboost 无关 。  
**质疑 Scrapy response 有自带 .xpath, .css 等方法？** Funboost 认为，这并非核心优势。例如，基于 Funboost 的 boost_spider 爬虫框架，其 RequestClient 的响应对象也自带 xpath 等方法，且实现非常简单 。开发者也可以轻松封装一个带有这些方法的响应对象，这并非技术难题 。  
**质疑 Scrapy Twisted 性能强悍，担心 Funboost 爬取不快？** Funboost 强调，其通过多机器 + 多进程 + asyncio 的组合并发模式，性能远超 Scrapy 。Funboost 的性能基准测试也证明其在发布和消费速度上对 Celery（也基于 Twisted）具有压倒性优势 。  
**质疑 Scrapy 重试功能强大？** Funboost 认为，其函数级重试功能远远优于 Scrapy 的 URL 级重试功能 。Scrapy 的 URL 重试只针对请求失败（如网络错误），如果 HTTP 状态码为 200 但页面内容反爬导致解析出错，Scrapy 的重试是无效的，会丢失大量数据 。Funboost 的 @boost 装饰器则能自动重试函数执行，即使是页面反爬导致的解析错误，框架也会自动重试，无需开发者提前规划判断反爬情况，从而做到完全不漏数据 。  
**质疑 Scrapy 稳定，Funboost 不稳定？** Funboost 强调，其框架核心执行函数是稳定的，且对用户如何编写爬虫函数干预很少，这种"少即是稳"的设计原则使其非常稳定 。Funboost 对网络错误等有强大的自动重连和重试机制，不易因外部问题中断，即使与消息队列机器断开连接，也能自动重试连接并在网络恢复后继续拉取消息，不会退出代码 。  
**质疑 Scrapy 自带去重，Funboost 不能去重？** Funboost 的函数入参去重功能远远优于 Scrapy 的 Request 对象指纹去重 。Funboost 基于函数核心入参进行去重，能够天然无视 URL 中包含的时间戳、随机数等噪音字段，而 Scrapy 则需要编写复杂的自定义 RFPDupeFilter 来处理这些噪音，维护成本极高 。Funboost 还支持去重有效期，适合周期性更新的爬取任务，而 Scrapy 默认是永久去重 。  
**质疑 Funboost 不能断点续爬？** Funboost 认为，Scrapy-redis 的 blpop 机制在重启或关机时会丢失大量已取出到内存中的种子 。Funboost 则通过其支持的多种消息队列的消费确认机制，实现了真正的断点续爬"万无一失"，不怕随意突然反复重启代码和突然关机 。

### **20.5.5 Funboost vs. Scrapy 优势总结 (表格版)**

下表集中总结了 Funboost 与 Scrapy 在核心理念、开发效率、功能强大性与可靠性以及特定场景处理能力等方面的对比优势，主要围绕"自由编程 降维打击 框架奴役"的核心思想展开，即 Funboost 通过其通用的函数调度能力，赋予开发者极大的自由度，从而在灵活性、易用性和功能强大性上超越了 Scrapy 这种专用但受限的框架 。  
| 类别 | 维度 | Funboost 优势 (函数调度，自由无限) | Scrapy 劣势 (URL调度，框架束缚) |
| :--- | :--- | :--- | :--- |
| **核心理念与架构** | **1. 调度核心** | **函数调度**：<br>调度的是一个完整的、可执行的Python函数，<br>内部逻辑完全自由。 | **URL请求调度**：<br>调度的是一个 `Request` 对象，<br>开发者被限制在框架的请求-响应生命周期内。 |
| **核心理念与架构** | **2. 编程范式** | **自由编程**：<br>采用平铺直叙、一气呵成的同步思维编写函数，<br>逻辑连贯清晰。 | **回调地狱**：<br>强制使用 `yield Request` 和 `callback` 函数，<br>逻辑被拆分得支离破碎，难以理解和维护。 |
| **核心理念与架构** | **3. 状态管理** | **极其简单**：<br>在函数内使用普通的局部变量即可轻松管理状态，<br>符合直觉。 | **极其繁琐**：<br>必须通过 `response.meta` 字典在回调函数之间传递状态，<br>易出错且IDE无法补全提示。 |
| **核心理念与架构** | **4. 框架侵入性** | **极低**：<br>只需一个 `@boost` 装饰器，<br>不改变函数原有结构，可轻松集成任何老代码。 | **极高**：<br>必须继承 `scrapy.Spider`，<br>重写 `parse` 等方法，代码与框架深度耦合，<br>迁移成本高。 |
| **核心理念与架构** | **5. 架构思想** | **降维打击**：<br>用通用的万能函数调度框架解决特定的爬虫问题，<br>功能更全，更灵活。 | **作茧自缚**：<br>专为爬虫设计，但其设计限制了其处理复杂和非标准场景的能力。 |
| **开发效率与易用性** | **6. 学习曲线** | **极其平缓**：<br>只需学习 `@boost` 装饰器的用法，<br>几分钟即可上手。 | **极其陡峭**：<br>需要学习Spider、Item、Pipeline、Middleware、Settings等多个组件和复杂的生命周期。 |
| **开发效率与易用性** | **7. 代码量与文件结构** | **极其精简**：<br>单文件即可完成一个复杂的分布式爬虫，<br>代码量极少。 | **极其臃肿**：<br>一个简单的爬虫也需要创建7-8个文件，<br>开发者需在多个文件间频繁切换。 |
| **开发效率与易用性** | **8. HTTP库选择** | **完全自由**：<br>可在函数内随意使用 `requests`, `httpx`, `aiohttp`, `selenium`, `playwright` 等任何库。 | **受限**：<br>强制使用其内置的基于 `Twisted` 的下载器，<br>想用其他库需要复杂的中间件封装。 |
| **开发效率与易用性** | **9. 反爬与自定义请求** | **极其简单**：<br>封装一个通用的 `my_request` 函数即可实现换IP、UA等逻辑，<br>0门槛。 | **极其复杂**：<br>必须编写和注册下载器中间件（`Downloader Middleware`），<br>概念复杂，对新手极不友好。 |
| **开发效率与易用性** | **10. 单元测试** | **极其容易**：<br>每个被 `@boost` 装饰的函数都可以直接调用，<br>独立进行单元测试。 | **极其困难**：<br>Spider的回调方法与框架上下文强耦合，<br>难以进行独立的单元测试。 |
| **开发效率与易用性** | **11. IDE代码补全** | **全面支持**：<br>函数参数、`push`/`publish` 方法均有代码补全，<br>开发效率高。 | **几乎为零**：<br>`response.meta` 是字典，IDE无法提供任何键的补全提示，<br>极易出错。 |
| **开发效率与易用性** | **12. 调试** | **简单直观**：<br>线性执行的函数逻辑，<br>使用标准 `pdb` 或IDE调试器即可轻松调试。 | **困难**：<br>回调链和异步执行流程使得调试非常困难，<br>难以跟踪任务的完整生命周期。 |
| **功能强大性与灵活性** | **13. 并发模型** | **更强悍（叠加模式）**：<br>轻松实现多进程 + (多线程/协程) + 多机器的四重叠加并发，<br>性能炸裂。 | **有限**：<br>并发主要由 `CONCURRENT_REQUESTS` 控制，<br>难以充分利用多核CPU。 |
| **功能强大性与灵活性** | **14. 速率控制** | **更精准（QPS控制）**：<br>可精确控制每秒请求次数（QPS），<br>无视响应时间波动。 | **不精确（并发数控制）**：<br>只能控制并发请求数，<br>无法保证稳定的请求速率。 |
| **功能强大性与灵活性** | **15. 复杂流程处理** | **极其自然**：<br>可在单个函数内完成多轮浏览器交互、API调用等复杂连续操作。 | **几乎无法实现**：<br>用回调处理多步连续操作非常笨拙，<br>甚至会导致异步模型失效。 |
| **功能强大性与灵活性** | **16. 短时效Token处理** | **轻松解决**：<br>可在函数内连续请求，<br>确保获取Token后立即使用，保证时效性。 | **无能为力**：<br>无法保证两个 `Request` 之间的执行间隔，<br>Token极易过期。 |
| **功能强大性与灵活性** | **17. 任务去重** | **更智能（入参去重）**：<br>基于函数核心入参进行去重，<br>能自动忽略URL中的时间戳、随机数等噪音。 | **很笨拙（URL指纹去重）**：<br>对URL中的噪音参数无能为力，<br>需要编写复杂的 `RFPDupeFilter` 才能解决。 |
| **功能强大性与灵活性** | **18. 去重有效期** | **支持**：<br>可以设置任务过滤的有效期，<br>适合周期性更新的爬取任务。 | **不支持**：<br>默认是永久去重，<br>需要手动清理去重集合才能重新爬取。 |
| **功能强大性与灵活性** | **19. 错误重试** | **更可靠（函数级重试）**：<br>即使HTTP 200但页面内容反爬，导致解析出错，<br>函数依然会自动重试。 | **不可靠（URL级重试）**：<br>只对请求失败（如网络错误）重试，<br>对内容错误无能为力，会丢失数据。 |
| **功能强大性与灵活性** | **20. 数据持久化** | **极其灵活**：<br>在函数内直接调用任何数据库的客户端库进行存储，<br>完全自由。 | **受限**：<br>必须通过 `Item Pipeline` 机制，<br>增加了一层不必要的抽象和复杂性。 |
| **功能强大性与灵活性** | **21. 消息队列支持** | **极其丰富**：<br>支持30多种消息队列，包括RabbitMQ、Kafka等，<br>提供更专业的分布式能力。 | **有限**：<br>主要依赖 `scrapy-redis`，<br>选择单一。 |
| **功能强大性与灵活性** | **22. 定时任务** | **原生支持**：<br>内置强大的定时任务功能，<br>可轻松实现定时启动、周期爬取。 | 需要借助外部脚本或 `apscheduler` 等库自行实现，<br>集成复杂。 |
| **生态与可靠性** | **23. 插件生态** | **无需插件，Python生态即是其生态**：<br>任何Python三方包都可直接使用，<br>无需等待"大神"开发专用插件。 | **依赖插件**：<br>使用新工具（如Playwright）需要等待 `scrapy-playwright` 这样的插件，<br>学习和配置成本高。 |
| **生态与可靠性** | **24. 断点续爬** | **真正可靠**：<br>支持消费确认（ACK），<br>即使强制关机、代码崩溃，任务也万无一失。 | **不可靠**：<br>`scrapy-redis` 使用 `blpop`，<br>重启或崩溃会丢失大量已取出到内存中的任务。 |
| **生态与可靠性** | **25. 跨语言/项目交互** | **支持**：<br>可由Java等其他语言程序向队列发布爬虫任务。 | **不支持**：<br>其任务格式与Python和框架自身强绑定。 |
| **生态与可靠性** | **26. 远程部署** | **一键部署**：<br>内置 `fabric_deploy` 功能，<br>可直接将爬虫函数部署到远程服务器。 | 无此功能，<br>部署复杂。 |
| **生态与可靠性** | **27. Web管理界面** | **功能强大**：<br>`funboost web manager` 可监控、管理所有爬虫任务和消费者，<br>并可实时调整QPS。 | `scrapy-redis` 无官方管理界面，<br>需借助其他工具。 |
| **生态与可靠性** | **28. 稳定性** | **更高**：<br>对网络错误等有强大的自动重连和重试机制，<br>不易因外部问题中断。 | 相对脆弱，<br>需要开发者在中间件中编写大量代码来保证稳定性。 |
| **生态与可靠性** | **29. 资源占用** | **更可控**：<br>智能线程池可自动伸缩，<br>节省资源。 | 并发数固定，<br>可能在任务稀疏时造成资源浪费。 |
| **生态与可靠性** | **30. 统一控制** | **包罗万象**：<br>一个 `@boost` 装饰器集成了分布式、并发、控频、重试、过滤、持久化等30多种控制功能。 | 功能分散在多个组件和配置中，<br>难以统一管理和配置。 |

## **20.6 Funboost 对 Python 固有挑战的解决方案**

Funboost 的核心价值在于其能够通过创新的架构和全面的功能集，有效解决 Python 语言在分布式和高并发执行方面的固有挑战，特别是 GIL（全局解释器锁）和整体性能限制 。

### **20.6.1 突破 GIL 限制**

Python 的 GIL 限制了单个 Python 进程在多核 CPU 上执行 CPU 密集型任务时的并行性。Funboost 通过以下机制直接规避 GIL 的影响：

* **多进程并发**：这是最直接且有效突破 GIL 的方式。Funboost 能够轻松地将多进程与多线程、协程等细粒度并发模式叠加使用 。每个进程拥有独立的 Python 解释器和 GIL，从而可以充分利用多核 CPU 实现真正的并行计算。例如，通过 multi_process_consume() 方法，可以启动多个进程，每个进程内部再进行多线程或协程并发，实现性能的爆炸式增长 。  
* **I/O 密集型任务优化**：对于 I/O 密集型任务，即使有 GIL，Python 线程在等待 I/O 时也会释放 GIL，从而允许其他线程执行。Funboost 的自定义可伸缩线程池（ThreadPoolExecutorShrinkAble）能够智能地管理线程数量，高效处理 I/O 密集型任务 。此外，Gevent、Eventlet 和 Asyncio 等协程模式通过非阻塞 I/O 和事件循环机制，在单线程内实现高并发，完全绕开了 GIL 的限制，特别适合网络爬虫、API 调用等 I/O 密集型场景 。

### **20.6.2 提升整体性能与可伸缩性**

Funboost 不仅突破了 GIL 限制，还在整体性能和系统可伸缩性方面提供了卓越的解决方案：

* **任务解耦与分布式执行**：Funboost 采用经典的"生产者 + 消息队列中间件 + 消费者"编程思想，通过消息队列实现任务的彻底解耦 。生产者和消费者可以独立运行，甚至部署在不同的机器、不同的进程或 Docker 容器中，从而实现真正的分布式计算，突破单机性能瓶颈 。这种解耦使得系统可以根据负载弹性伸缩，按需增加消费者实例。  
* **广泛的中间件支持**：Funboost 支持 30 多种消息队列中间件，包括各种主流 MQ、数据库、文件系统、甚至其他任务队列框架作为 Broker 。这种广泛的支持确保了在任何部署环境下都能找到最适合的中间件，实现任务的可靠传输和高效分布式执行。  
* **智能调度与资源管理**：  
  * **QPS 精准控制**：Funboost 能够精确控制函数每秒的执行次数（QPS），无论函数本身耗时如何波动，都能保持设定的频率 。这对于控制对外部服务的请求频率、避免过载、实现精细化流量管理至关重要 。  
  * **分布式 QPS 控频**：在多进程或多机器部署时，Funboost 可以实现全局的 QPS 限制，自动在所有消费者之间平分流量，确保总的执行速率不超过设定值 。  
  * **智能线程池**：Funboost 自定义的线程池能够根据任务负载智能地扩大和缩小线程数量，避免不必要的线程创建和销毁开销，优化资源利用率 。  
* **卓越的性能**：Funboost 在消息发布和消费方面都展现出远超 Celery 的性能，发布性能可达 Celery 的 12 倍，消费性能可达 23 倍 。这种性能优势直接转化为更高的吞吐量和更低的延迟，使得 Python 应用在处理大规模分布式任务时更具竞争力。

### **20.6.3 确保任务可靠性与容错**

在分布式系统中，任务的可靠性是核心关注点。Funboost 通过一系列机制确保任务的"万无一失"，即使在系统故障或意外中断的情况下也能保障数据完整性 。

* **消费确认 (ACK)**：Funboost 实现了消息的“至少一次”或“精确一次”消费保证。只有当函数运行完成后，框架才会向消息队列发送确认信号。这意味着，即使消费者进程崩溃、断电、强制关机或被粗暴终止，未完成处理的消息也不会丢失，会自动重新入队或被其他消费者接管 。这对于分布式系统中的数据完整性和任务可靠性至关重要。Funboost 对 Redis 等非原生支持 ACK 的中间件也实现了可靠的消费确认机制 。  
* **消费确认 (ACK)**：Funboost 实现了消息的"至少一次"或"精确一次"消费保证。只有当函数运行完成后，框架才会向消息队列发送确认信号。这意味着，即使消费者进程崩溃、断电、强制关机或被粗暴终止，未完成处理的消息也不会丢失，会自动重新入队或被其他消费者接管 。这对于分布式系统中的数据完整性和任务可靠性至关重要。Funboost 对 Redis 等非原生支持 ACK 的中间件也实现了可靠的消费确认机制 。  
* **自动重试**：当函数执行出错时（例如因网络瞬时故障或外部服务不稳定），Funboost 会立即自动重试指定次数，提高任务的成功率 。开发者也可以通过抛出特定异常（ExceptionForRequeue 或 ExceptionForPushToDlxqueue）来控制消息的重新入队或进入死信队列 。  
* **断点续传**：由于消息的持久化和消费确认机制，Funboost 能够实现无惧反复重启代码的任务断点续传，确保不丢失任何任务 。这使得开发者可以放心地进行代码更新、部署或系统维护，而无需担心任务中断导致的数据丢失。  
* **任务过滤与过期丢弃**：通过任务过滤功能，可以避免重复执行相同参数的任务，提高效率 。同时，任务过期丢弃功能允许框架丢弃发布时间过早的消息，适用于对实时性要求高、对消息可靠性要求相对较低的场景，防止消息堆积 。

通过上述全面的机制，Funboost 将 Python 语言在单核性能上的限制（GIL）通过多进程和异步并发模式进行规避，同时利用消息队列实现了任务的解耦和分布式执行，并通过一系列智能调度和可靠性机制，为开发者提供了一个强大、高效且易用的分布式函数调度框架，从而有效解决了 Python 在高并发和大规模分布式场景下的挑战 。

## **20.7 高级特性与生态集成**

Funboost 不仅提供了核心的分布式函数调度能力，还集成了一系列高级特性，进一步增强了其在复杂分布式系统中的应用价值和与现有生态的无缝集成能力。

### **20.7.1 RPC 模式：远程函数调用与结果获取**

Funboost 支持 RPC（远程过程调用）模式，允许生产端（发布端）在发送任务后，同步或异步地等待并获取消费端函数的执行结果 。这使得发布端能够根据消费结果进行后续处理，而不是简单地将任务"一发了之" 。

* **同步 RPC**：通过在 @boost 装饰器中设置 is_using_rpc_mode=True 或在 publish 方法中指定 priority_control_config=PriorityConsumingControlConfig(is_using_rpc_mode=True)，发布端可以通过 async_result.result 阻塞当前线程，直到消费函数执行完成并返回结果 。  
* **异步 RPC**：为了更好地融入 asyncio 编程生态，Funboost 提供了 AioAsyncResult 类。在异步函数中，可以通过 await aio_async_result.result 异步等待结果，避免阻塞整个事件循环 。此外，还可以设置回调函数，在消费结果返回后自动在线程池中并发处理回调逻辑 。  
* **结果持久化**：结合函数状态和结果持久化功能，RPC 结果可以保存到 MongoDB 或其他数据库，方便后续查询和追溯 。

### **20.7.2 定时任务与延时任务**

Funboost 内置了强大的定时任务和延时任务功能，满足了多种调度需求。

* **定时任务**：Funboost 封装了知名的 apscheduler 包，通过 ApsJobAdder 类提供定时任务功能 。定时任务的本质是"定时发布消息到消息队列"，而非直接在当前程序中执行函数 。  
  * **灵活的调度方式**：支持按时间间隔、按指定日期执行一次、按 Cron 表达式执行等多种调度方式 。  
  * **动态管理**：支持随时通过代码动态添加、暂停、恢复和删除定时任务 。  
  * **多点部署高可用**：Funboost 继承并优化了 apscheduler，在使用 Redis 作为 job_store 时，利用分布式锁确保一个定时任务不会被多台机器或进程重复执行，从而实现高可用性 。这解决了原生 Celery Beat 无法多实例部署的单点故障问题 。  
* **延时任务**：与周期性重复触发的定时任务不同，延时任务是对单个消息规定在发布后延迟特定秒数或在指定精确时间点执行 。这避免了在消费函数内部使用 time.sleep() 阻塞并发线程的问题，将延时逻辑提升到框架层面处理 。

### **20.7.3 函数入参过滤与过期丢弃**

Funboost 提供了智能的任务过滤和过期丢弃功能，进一步优化了任务处理效率和资源利用。

* **任务过滤**：支持根据函数入参进行去重，避免重复执行相同参数的任务 。例如，如果一个求和函数 add(1, 2) 已经执行过，再次发布 add(1, 2) 的任务可以被框架跳过。  
  * **有效期缓存**：任务过滤可以设置有效期，例如 30 分钟内查询过深圳天气，则 30 分钟内再次查询会被过滤；30 分钟后则会重新执行 。这在周期性更新数据或缓存失效场景中非常有用。  
  * **智能去重**：Funboost 的入参过滤比 Scrapy 的 URL 指纹去重更智能，能够天然无视 URL 或 POST 请求体中的时间戳、随机数等噪音字段，避免因噪音导致重复任务无法去重的问题 。  
* **任务过期丢弃**：可设置消息过期时间，例如消息是 15 秒之前发布的，框架可以丢弃此消息不执行，防止消息堆积 。这在消息可靠性要求不高但实时性要求高的并发互联网接口中非常实用。

### **20.7.4 可视化管理系统**

Funboost 提供了一个功能强大的 Web Manager 管理系统，支持全面查看、监控和管理任务消费情况 。

* **实时监控**：可查看和搜索函数实时消费状态和结果，包括成功/失败、异常类型、重试次数、执行机器信息、函数入参/结果和耗时等 。  
* **性能概览**：提供消费速度图，可查看实时和历史消费速度（如最近 60 秒每秒消费次数、最近 60 分钟每分钟消费次数等） 。  
* **消费者管理**：可根据 IP 或队列名称搜索正在运行的消费者信息 。  
* **队列操作**：支持查看和操作队列，包括清空队列、暂停消费、恢复消费、实时调整 QPS 和并发数量等 。  
* **RPC 调用**：可在网页上对各种消息队列发布消息并获取函数执行结果，或根据 task_id 查询结果 。

这个可视化系统极大地简化了分布式任务的运维和故障排查，使得开发者无需深入日志文件或命令行即可全面掌握系统运行状况。

### **20.7.5 远程服务器部署**

Funboost 内置支持 Python 代码级别的一键远程 Linux 机器消费部署功能 。这使得开发者无需手动安装 Git、上传代码或使用其他运维发版工具（如阿里云 CodePipeline、K8s），即可将爬虫函数或其他任务函数自动部署到远程服务器并运行 。

* **简化部署流程**：只需通过 task_fun.fabric_deploy() 方法，指定远程服务器的 IP、端口、用户名和密码，即可自动将函数所在的代码文件上传到远程机器，设置环境变量，并启动指定数量的进程来消费任务 。  
* **函数级别精确部署**：这种部署方式精确到函数级别，比脚本级别的部署更加灵活，可以指定在特定机器上运行特定的函数并控制其进程数量 。  
* **不依赖外部工具**：这一功能在没有成熟 CI/CD 管道或 K8s 环境的测试或小型部署场景中尤其有用，极大地降低了多机部署的门槛 。

### **20.7.6 上下文管理：fct 智能上下文**

Funboost 提供了强大的 fct（funboost_current_task）智能上下文机制，这在 Celery 等框架中通常需要侵入式设计（如 bind=True 并添加 self 参数）才能实现 。

* **无侵入式设计**：fct 允许在消费函数及其调用链中的任意函数中获取当前任务的完整信息，而无需改变函数定义或添加额外的参数 。例如，在函数内部可以直接访问 fct.task_id、fct.full_msg、fct.function_result_status.publish_time 等任务元数据 。  
* **线程/协程隔离**：fct 是线程/协程隔离的，类似于 Flask 视图中的 request 对象，确保在并发环境中获取到的上下文信息是当前任务独有的 。  
* **日志集成**：结合日志模板，fct 能够自动在日志中显示 task_id，方便用户通过 task_id 串联起一条消息的所有日志，进行问题排查 。

### **20.7.7 消费任意消息格式**

Funboost 在消息格式兼容性方面展现出极强的灵活性，远超 Celery 等工具 。

* **消费随机键 JSON 消息**：Funboost 天然支持消费任意键值结构的 JSON 消息。如果消息包含随机或过多的键，开发者可以将消费函数定义为 def task_fun(**kwargs)，并设置 @boost 装饰器的 should_check_publish_func_params=False，即可接收所有传入的键值对 。这使得 Funboost 能够轻松消费非 Funboost 发布的、自由格式的 JSON 消息，极大地降低了异构系统对接成本 。  
* **消费任意非 JSON 格式消息**：Funboost 甚至能够消费任意不规范格式的消息（非 JSON 格式）。通过继承并自定义 Consumer 类，重写 _user_convert_msg_before_run 方法，开发者可以在消息运行前将其清洗并转化为 Funboost 可识别的字典或 JSON 字符串格式 。这使得 Funboost 能够轻松处理遗留系统或第三方系统发送的各种奇葩消息格式。

### **20.7.8 实例方法与类方法作为消费函数**

Funboost 在 2024 年 6 月新增支持将实例方法和类方法作为消费函数，这是其相比 Celery 的一项独特优势，因为 Celery 只能支持普通函数或静态方法作为消费函数 。

* **编程范式更灵活**：这一特性允许开发者在面向对象的类结构中直接定义分布式任务，使得代码组织更加自然和符合 OOP 规范 。  
* **实现原理**：对于类方法，Funboost 在发布时使用字典代替 cls 参数，消费时再还原为类本身。对于实例方法，Funboost 在发布时会保存对象的 __init__ 入参字典（obj_init_params），消费时根据这些参数重新生成对象，并将其作为 self 参数传递给实例方法 。这使得实例方法可以访问对象的属性和方法，实现更复杂的业务逻辑。

这些高级特性和与 Python 生态的深度集成，使得 Funboost 成为一个功能全面、高度灵活且易于使用的分布式函数调度框架，能够满足现代复杂应用的多样化需求。

## **20.8 结论与展望**

### **20.8.1 核心价值的再强调**

Funboost 作为一款万能分布式函数调度框架，其核心价值在于成功地将"轻量级使用方式"与"重量级功能集"融合，彻底颠覆了"功能强大必然使用复杂"的传统认知 。它通过一个极其简洁的 @boost 装饰器，为任何 Python 函数赋能，使其具备分布式、高并发、高可靠的执行能力，同时将复杂的底层细节和运维负担降至最低 。  
本报告的深入分析表明，Funboost 不仅在性能上对 Celery 实现了断崖式领先（发布速度快 12 倍，消费速度快 23 倍），更在易用性、灵活性和功能广度上展现出压倒性优势。其对项目目录结构的零要求、全面的 IDE 自动补全支持、简化的启动方式，以及对 Windows 的原生支持，极大地提升了开发者的体验 。在功能层面，Funboost 支持 30 多种消息队列和 5 种叠加多进程的并发模式 ，并提供 30 种任务控制功能，包括精准的分布式 QPS 控频、消息万无一失的消费确认、智能的任务过滤和丰富的可视化管理界面 。  
Funboost 的"万物皆可为 Broker"和"自由编程 降维打击 框架奴役"的理念，使其能够无缝集成现有代码和任意第三方库，摆脱了传统框架的束缚 。它甚至能够将 Celery 等框架作为其 Broker，以极简的 API 操控其核心调度引擎，这不仅证明了 Funboost 架构的包容性，也为开发者提供了前所未有的灵活性和选择 。

### **20.8.2 对 Python 开发者社区的意义**

Funboost 的出现，对 Python 开发者社区具有深远的意义。它极大地降低了分布式编程的门槛，使得更多的 Python 开发者能够轻松地构建和管理复杂的分布式系统，而无需投入大量时间学习和掌握底层并发、消息队列和分布式协调的复杂细节 。

* **赋能普通函数**：通过将任何 Python 函数转化为分布式任务，Funboost 使得开发者可以专注于业务逻辑的实现，而不是框架的适配 。这种"函数即服务"的理念在自托管环境中得以实现，极大地提升了开发效率。  
* **解决 Python 固有挑战**：Funboost 通过多进程、多线程、协程等多种并发模式的智能组合，有效规避了 GIL 对 CPU 密集型任务的限制，并提升了 I/O 密集型任务的效率，从而解决了 Python 在高并发和大规模分布式场景下的性能瓶颈 。  
* **提升系统可靠性**：通过消息确认、自动重试、断点续传等机制，Funboost 确保了任务的"万无一失"，即使在系统故障或意外中断的情况下也能保障数据完整性，这对于构建健壮、高可用的应用至关重要 。

### **20.8.3 战略性推荐**

鉴于 Funboost 在性能、易用性、功能广度、灵活性和可靠性方面的卓越表现，本报告强烈推荐其作为 Python 分布式函数调度框架的首选。

* **对于新项目**：Funboost 提供了构建高性能、高可用分布式系统的理想基础。其简洁的 API 和无侵入性设计，将显著加速开发进程并降低未来的维护成本。  
* **对于现有项目**：Funboost 的无代码入侵特性使其能够轻松集成到现有代码库中，为现有函数赋能分布式能力，从而实现渐进式重构和性能提升，而无需进行大规模的架构改造。  
* **适用场景**：Funboost 特别适用于以下场景：  
  * 需要处理高并发、大吞吐量的任务（如数据采集、实时数据处理、批量计算）。  
  * 任务流程复杂，需要多步骤编排和结果回调。  
  * 对任务可靠性有严格要求，不允许数据丢失。  
  * 需要精细化控制任务执行频率和资源消耗。  
  * 希望摆脱传统框架的束缚，追求编程自由和开发效率。

### **20.8.4 未来发展方向**

Funboost 作为一个活跃发展的框架，其未来发展潜力巨大。随着分布式系统和微服务架构的普及，对易用、高效、灵活的函数调度框架的需求将持续增长。Funboost 可以进一步探索：


* **云原生集成**：深化与 Kubernetes、Docker 等容器化和云原生技术的集成，提供更便捷的部署和运维方案。  
* **更丰富的监控和诊断工具**：在现有 Web Manager 的基础上，提供更深入的性能分析、故障诊断和预警功能。  
* **社区生态建设**：鼓励更多开发者参与贡献，丰富其扩展组件和应用案例，进一步巩固其在 Python 分布式领域的领导地位。  
* **代码/文档 英文国际化**: funboost 拥有足以挑战 Celery 的技术内核，但如果想真正成为一个世界级的框架，就必须将英文国际化贯彻到每一个细节，尤其是像日志这样最基础、最关键的输出信息上。否则，无论技术多么先进，它的形象和影响力都将永远被局限在一个“小圈子”里，难以实现其“暴打 Celery”的宏大目标。


综上所述，Funboost 不仅是一个强大的技术工具，更代表了一种先进的分布式编程理念。它将复杂性封装于内，将自由赋予开发者，有望成为 Python 分布式系统开发的新一代标准。
