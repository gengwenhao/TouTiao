# 今日头条头条的图片爬取
>使用方法, 进入目录, 在shell执行下面命令
```python
pip3 install -r requirements.txt
python3 main.py
```

>爬取后的内容存储在MongoDb中, 需要提前安装好MongoDb数据库
![](https://s1.ax1x.com/2018/01/02/ppVBZQ.png)

>关于配置

config.py中配置抓取关键字, 以及数据库(需要启动MongoDb)
![](https://s1.ax1x.com/2018/01/02/ppVDaj.png)
