General_news_spider

# What's this？
General_news_spider是一个scrapy实现的通用内容抓取模板，这里的**通用内容**定义为任何抓取路径为`目录分页->目录页->内容页（包括附件）`的内容，并实现了通用的`增量（从指定日期开始）/全量抓取`,`附件下载`,`爬虫测试`等功能，大幅节约您的开发时间。

# How it works?
借助xpath将内容解析部分通用化，同时根据通用的`日期格式`实现了增量抓取，借助`FilesPipeline`实现了附件下载，同时在spider内部增加了测试功能，方便用户判断xpath出错等问题。

# How to use?
Sample: [tutorial/sample.md][1]
同时spiders和crawlList文件夹中都有足够多的示例方便用户理解使用方法。

- Run `scrapy crawl general`
##Options:
- `-a name=` 爬虫名称,路径为crawlList/{name}.py
- `-a mode=` 0 - 增量抓取 1 - 全量抓取 99 - 测试模式
- `-a increment_date=` 当指定为增量抓取时，从此日期开始抓取（如不指定默认以当日作为increment_date）

测试模式样例：
`> scrapy crawl general -a name=shandong_binzhou_gsp -a mode=99`
```
2018-11-27 20:59:37 [root] WARNING: Run in TEST/PART-CRAWL Mode!
2018-11-27 20:59:37 [root] WARNING:
Content URL: http://sy.binzhou.gov.cn/zhengwu/class/?0.html&page=1&showtj=&showhot=&author=&key=&code=

2018-11-27 20:59:38 [root] WARNING:
Count:15 articles per content page

2018-11-27 20:59:38 [root] WARNING:
Article URL:http://sy.binzhou.gov.cn/zhengwu/html/?4204.html

2018-11-27 20:59:38 [root] WARNING:
Article Date:2018-11-26,[u'2018-11-26']

2018-11-27 20:59:39 [root] WARNING:
Article Title:2018年滨州市食品生产环节市级监督抽检合格产品信息

2018-11-27 20:59:39 [root] WARNING:
Article Text:

            	来源:市食品药品监督管理局  时间:2018-11-26 15:53  浏览量:30



                    2018年滨州市食品生产环节市级监督抽检合格产品信息
                    附件:2018年滨州市食品生产环...

2018-11-27 20:59:39 [root] WARNING: Article Attachment:http://sy.binzhou.gov.cn#
2018-11-27 20:59:39 [root] WARNING: Article Attachment:http://sy.binzhou.gov.cn/uploads/attachments/20181126/2018年滨州市食品生产环节市级监督抽检合格产品信息.xlsx
```

# Documentation
on the way...



  [1]: https://github.com/SunlightData/General_News_Crawler/blob/master/tutorial/sample.md
