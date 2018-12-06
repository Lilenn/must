from urllib.request import Request,urlopen
import re

class TiebaSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/p/4893709494?pn='
        #总页数
        self.total_page = 1
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.99'
        }
        self.page_list = []
        self.current_page = 1

    def start_load_url(self,pageIndex):
        #拼接网址
        full_url = self.base_url + str(pageIndex)
        #设置请求头信息
        request = Request(full_url,headers=self.headers)
        #获取响应
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求失败',e)

        else:
            #7.返回获取的源码
            print('请求第{}页的数据成功'.format(self.current_page))
            self.current_page +=1
            return code

    def get_total_page_with_code(self,code):
        pattern = re.compile(r'<li class="l_reply_num".*?>.*?<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)
        #11.获取总页码数
        self.total_page = int(result[1])


    def get_content_with_code(self,code):
        pattern = re.compile(r'<a.*?class="p_author_name.*?".*?>(.*?)</a>.*?<div.*?class="d_post_content j_d_post_content ".*?>(.*?)</div>',re.S)
        result = pattern.findall(code)
        self.update_oldData(result)

    def update_oldData(self,oldData):
        remove_element = re.compile(r'<.*?>',re.S)
        space_element = re.compile(r'\s',re.S)
        list = []

        for name ,content in oldData:
            sublist = []
            name = name.strip('\n')
            name = re.sub(space_element,'',name)
            name = re.sub(remove_element,'',name)

            content = content.strip('\n')
            content = re.sub(space_element,'',content)
            content = re.sub(remove_element,'',content)

            sublist.append(name)
            sublist.append(content)
            list.append(sublist)
            self.page_list  = list

    def spider_manager(self):
        code = self.start_load_url(self.current_page)

        self.get_total_page_with_code(code)

        self.get_content_with_code(code)

        self.get_content_with_code(code)

        self.get_other_page()

    def get_other_page(self):
        print(self.page_list)
        while self.current_page <= self.total_page:
            contentSpider  = input('是否请求下一页，回车确定，E退出')
            if contentSpider == 'E':
                print('所有数据加载完毕')
                return

            self.spider_manager()

tiba = TiebaSpider()
tiba.spider_manager()

