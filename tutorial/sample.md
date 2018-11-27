# Sample 1 全静态页面内容抓取
以山东滨州FDA局为例实现一个通用爬虫，目标抓取所有标题含有GSP的文章

1. 在crawlList文件夹中新建文件`shandong_binzhou_gsp.py`，继承newsBase类

```
from general_news.crawlList.base import newsBase

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.base_url = 'sy.binzhou.gov.cn'

        self.crawl_list = ['http://sy.binzhou.gov.cn/zhengwu/class/?0.html&page={}&showtj=&showhot=&author=&key=&code='.format(str(y)) for y in range(1, 10)]
        #定义抓取URL列表
        self.contents_title_whitelist = ['GSP']
        #定义白名单列表，若白名单被定义，任何标题不含白名单词汇的文章都不会被保存

        self.contents_title_xpath = '//*[@id="container"]/div[1]/div[3]/ul/ul/li[*]/a'
        # 定义每个目录标题的xpath：注意请把握好[*]的位置，请从页面结构上分析得出**每个标题**的正确位置（无需/text()）

        self.contents_date_xpath = '../div/text()'
        # 定义每个标题的日期：这个xpath的root节点是self.contents_title_xpath，请以这个节点出发找到date的内容，务必以/text()结尾，日期格式必须为%Y-%m-%d否则会raise Exception，如果格式不符请通过重写parse_date()处理为该格式

        self.article_title_xpath = '//*[@id="topic"]/h1'
        # 定义文章页标题的xpath（无需/text()）

        self.article_text_xpath = '//*[@id="nw_content"]'
        # 定义文章页文章内容的xpath，文章内容所有的源代码都会被保留在package['source']中（如表格会以源码形式存在，方便用户做后续处理）

        self.article_href_xpath = '//*[@id="nw_content"]//@href'
        # 定义附件内容的xpath，务必以//@href结尾

    def parse_content_href(self, href):
        # 对目录页抓取的href不准的情况可以通过重写parse_content_href来修改
        return 'http://'+self.base_url+href[1:].replace('/zhengwu/html/','/zhengwu/html/?')

    def parse_article_href(self, href):
        # 对文章页抓取的附件href不准的情况可以通过重写parse_article_href来修改
        return href

    def parse_title(self, title):
        # 标题特殊处理
        return title

    def parse_date(self, date):
        # 日期特殊处理
        return date

    def parse_text(self,text):
        # 文章内容特殊处理
        return text

    def parse_content_response(self, response):
        # 目录页response特殊处理
        return response

    def parse_article_response(self, response):
        # 文章页response特殊处理
        return response

    def parse_package(self, package):
        #最终返回的结果数据特殊处理
        return package
```

2. 在项目根目录执行`scrapy crawl general -a name=shandong_binzhou_gsp -a isAll=1 -o shandong_binzhou_gsp.json`

3. 等待抓取完成，附件将被保存在`attachment/shandong_binzhou_gsp_{date}中。
4. 查看内容`shandong_binzhou_gsp.json`

#### 样例json
```
{
	"meta_version": "",
	"download_config": {
		"url": "http://sy.binzhou.gov.cn/zhengwu/html/?4106.html",
		"method": "GET"
	},
	"download_data": {
		"raw_data": {},
		"parsed_data": {
			"download_timeout": 180.0,
			"title": "滨州市药品经营企业GSP认证公告(第2018011号)",
			"text": "\r\n                \r\n            \t来源:市食品药品监督管理局  时间:2018-08-27 15:49  浏览量:103\r\n\r\n            \t\r\n                    \r\n                    滨州市药品经营企业GSP认证公告(第2018011号)根据《中华人民共和国药品管理法》及其实施条例规定,经我局依照《药品经营质量管理规范认证管理办法》及其规定的程序进行认证检查,对以下20个符合《药品经营质量管理规范》的企业发给认证证书,现予以公布。特此公告                          滨州市食品药品监督管理局                              2018年8月27日\r\n                    附件:5b83ad4b82087.doc\r\n                    \r\n                    编辑:滨州市食品药品监管局\r\n                    分享到:微信新浪微博腾讯微博人人网QQ空间\r\n\r\n                    window._bd_share_config={\"common\":{\"bdSnsKey\":{},\"bdText\":\"\",\"bdMini\":\"2\",\"bdMiniList\":false,\"bdPic\":\"\",\"bdStyle\":\"1\",\"bdSize\":\"16\"},\"share\":{\"bdSize\":16},\"image\":{\"viewList\":[\"weixin\",\"tsina\",\"tqq\",\"renren\",\"qzone\"],\"viewText\":\"分享到:\",\"viewSize\":\"16\"},\"selectShare\":{\"bdContainerClass\":null,\"bdSelectMiniList\":[\"weixin\",\"tsina\",\"tqq\",\"renren\",\"qzone\"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];\r\n\r\n                \r\n\r\n                \r\n\r\n                    \r\n\r\n                    \t\r\n\r\n                        \r\n\r\n\r\n                    \r\n\r\n                \r\n\r\n            ",
			"project": "shandong_binzhou_gsp",
			"source": "<div id=\"nw_content\">\r\n                \r\n            \t<div id=\"time\">来源：市食品药品监督管理局  时间：2018-08-27 15:49  浏览量：103</div>\r\n\r\n            \t<div id=\"nr\" deep=\"4\">\r\n                    \r\n                    <p style=\"text-align: center; text-indent: 2em;\">滨州市药品经营企业GSP认证公告</p><p style=\"text-align: center; text-indent: 2em;\">（第2018011号）</p><p style=\"text-indent: 2em;\">根据《中华人民共和国药品管理法》及其实施条例规定，经我局依照《药品经营质量管理规范认证管理办法》及其规定的程序进行认证检查，对以下20个符合《药品经营质量管理规范》的企业发给认证证书，现予以公布。</p><p style=\"text-indent: 2em;\">特此公告</p><p style=\"text-align: right; text-indent: 2em;\">                          滨州市食品药品监督管理局</p><p></p><p style=\"text-align: right; text-indent: 2em;\">                              2018年8月27日</p><p><br></p>\r\n                    <div style=\"overflow: hidden;\">附件：<br><a href=\"http://sy.binzhou.gov.cn/uploads/attachments/20180827/5b83ad4b82087.doc\" target=\"_blank\">5b83ad4b82087.doc</a><br></div>\r\n                    \r\n                    <div style=\"float: right;\">编辑：滨州市食品药品监管局</div>\r\n                    <div class=\"bdsharebuttonbox bdshare-button-style1-16\" style=\"clear:both\" data-bd-bind=\"1508211635296\"><a href=\"#\" class=\"bds_more\" data-cmd=\"more\">分享到：</a><a href=\"#\" class=\"bds_weixin\" data-cmd=\"weixin\" title=\"分享到微信\">微信</a><a href=\"#\" class=\"bds_tsina\" data-cmd=\"tsina\" title=\"分享到新浪微博\">新浪微博</a><a href=\"#\" class=\"bds_tqq\" data-cmd=\"tqq\" title=\"分享到腾讯微博\">腾讯微博</a><a href=\"#\" class=\"bds_renren\" data-cmd=\"renren\" title=\"分享到人人网\">人人网</a><a href=\"#\" class=\"bds_qzone\" data-cmd=\"qzone\" title=\"分享到QQ空间\">QQ空间</a></div>\r\n\r\n                    <script data-filtered=\"filtered\">window._bd_share_config={\"common\":{\"bdSnsKey\":{},\"bdText\":\"\",\"bdMini\":\"2\",\"bdMiniList\":false,\"bdPic\":\"\",\"bdStyle\":\"1\",\"bdSize\":\"16\"},\"share\":{\"bdSize\":16},\"image\":{\"viewList\":[\"weixin\",\"tsina\",\"tqq\",\"renren\",\"qzone\"],\"viewText\":\"分享到：\",\"viewSize\":\"16\"},\"selectShare\":{\"bdContainerClass\":null,\"bdSelectMiniList\":[\"weixin\",\"tsina\",\"tqq\",\"renren\",\"qzone\"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>\r\n\r\n                </div>\r\n\r\n                <div id=\"tjyd\">\r\n\r\n                    <div id=\"pages\">\r\n\r\n                    \t<!-- <p>上一篇：<a href=\"\"> </a><span>[]</span></p>\r\n\r\n\t\t\t\t\t\t<p>下一篇：<a href=\"\"> </a><span>[]</span></p> -->\r\n\r\n                        <!-- <p></p>\r\n                        <p></p> -->\r\n\r\n\r\n                    </div>\r\n\r\n                </div>\r\n\r\n            </div>",
			"depth": 1,
			"href": "http://sy.binzhou.gov.cn/zhengwu/html/?4106.html",
			"attachment": [{
				"url": "http://sy.binzhou.gov.cn#",
				"filename": "b299c3d7b4b52c07065f4e1c1a6e8a22"
			}, {
				"url": "http://sy.binzhou.gov.cn/uploads/attachments/20180827/5b83ad4b82087.doc",
				"filename": "1e35a3b4c6662058a231cabc3f639966"
			}],
			"date": "2018-08-27",
			"download_latency": 0.979647159576416,
			"download_slot": "sy.binzhou.gov.cn"
		}
	},
	"meta_updated": "2018-11-27T20:08:21"
}
```

# Sample 2 目录页为POST获取静态页面的特殊情况，内容页为静态页面

即便目录页为POST获取，您也依旧可以通过继承`GeneralNewsSpider`来使用通用爬虫的部分功能
以`山东枣庄药监局GSP抓取`这个需求为例，它的目录页通过`POST http://www.zzfda.gov.cn/webnoticelist.shtml`拿到，我们依然可以通过GereralNewsSpider.parse_content来`解析目录`，让通用爬虫完成剩下的工作。
1. spiders中新建一个spider`shandong_zaozhuang_gsp.py`

```
# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import FormRequest

from general_news.spiders.general import GeneralNewsSpider


class NewsSpider(GeneralNewsSpider): #继承GeneralNewsSpider
    name = 'shandong_zaozhuang_gsp' # 建议名称与crawlList中保持一致
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')
    # 这里可以自定义custom_settings

    def start_requests(self):
        url='http://www.zzfda.gov.cn/webnoticelist.shtml'
        for page in range(89):
            yield FormRequest(url,formdata={'fuzzy_title':'', 'gtype': '2','pageNum': page },callback=self.parse_content)
```

2. 剩下的流程就和Sample 1 中一样了，在crawlList中新建一个`shandong_zaozhuang_gsp.py`
```
# encoding=utf8
import re

from general_news.crawlList.base import newsBase

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.base_url = 'www.zzfda.gov.cn/'

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div[4]/div/div[2]/span'

        self.article_text_xpath = '/html/body/div[4]/div/div[3]'

        self.article_href_xpath = '/html/body/div[4]/div/div[3]//@href'

    def parse_date(self, date):
        return date[1:-1]
```

2. 在项目根目录执行`scrapy crawl shandong_zaozhuang_gsp -a name=shandong_zaozhuang_gsp -a isAll=1 -o shandong_zaozhuang_gsp.json`

3. 等待抓取完成，附件将被保存在`attachment/shandong_zaozhuang_gsp{date}中。
4. 查看内容`shandong_zaozhuang_gsp.json`

# Sample 3 目录页中内容完全无法使用Xpath获取，内容页为静态页面

以`山东莱芜药监局新闻抓取`这个需求为例，该网站采用`大汉网络`的通用新闻系统，其目录页是页面里的一个var加载的，只能通过正则等方式拿到。故目录页抓取我们自行完成，但内容页依然可以让通用爬虫来完成。

1. spiders中新建一个spider`shandong_laiwu_gsp.py`
```
# -*- coding: utf-8 -*-
import HTMLParser
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider

def decodeHtml(input):
    h = HTMLParser.HTMLParser()
    s = h.unescape(input)
    return s

class DahanColSpider(GeneralNewsSpider): #继承GeneralNewsSpider
    name = 'shandong_laiwu_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    def start_requests(self):
        url_list = ['http://syjj.laiwu.gov.cn/col/col3242/index.html']
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        body=decodeHtml(response.body)
        record = re.findall('<record>(.*?)</record>', body, re.S) #正则匹配抓取列表
        for r in record:
            package = dict()
            package['href'] = 'http://syjj.laiwu.gov.cn' + re.findall('href=\'(.*?)\'', r, re.S)[0] # 人工定义content_href并塞到package字典中
            date=re.findall(r"href='/art/(.*?)/(.*?)/(.*?)/", r, re.S)[0] # 人工定义content_date并塞到package字典中
            package['date'] =date[0]+'-'+date[1].zfill(2)+'-'+date[2] #修正日期格式为%Y-%m-%d
            if self.is_increment(package=package): # 复用GeneralNewsSpider中的判断增量方法，指定package，GeneralNewsSpider会根据package['date']判断是否抓取该页面
                yield Request(package['href'], callback=self.parse_article, meta=package)
```

2. 剩下的流程就和Sample 1 中一样了，在crawlList中新建一个`shandong_laiwu_gsp.py`
```
# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.base_url = 'syjj.laiwu.gov.cn'
        # 因为这里已经不涉及目录页抓取的相关内容了，所以只要给到article相关信息就可以了
        self.article_title_xpath = '//*[@id="c"]/tr[1]/td'

        self.article_text_xpath = '//*[@id="c"]/tr[3]/td'

        self.article_href_xpath = ''

    def parse_article_href(self, href):
        return 'http://'+self.base_url+href[1:]
```

