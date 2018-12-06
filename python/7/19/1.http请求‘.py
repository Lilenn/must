#
# http请求的特点
# 1.数据类出行比较广泛 json text xml html data
#    最常见的 json   音频视频文件data
# 2.请求是无状态协议 这次的请求和上次的请求没有任何关系
# 请求完以后服务器和客户端的链接会断掉
#   sockt 保持长连接 请求以后服务器和客户端的链接不会断掉
# 3.http有请求报文和响应报文
#   请求报文：
#     请求行：链接  http/1.1
#     请求头：Usre-Agent 标识目标（通过什么方式来访问对方）
#       Host：主机  connection ：服务器和客户端之间的连接状态
#     请求体：参数 请求体为在请求里边放的参数
#   响应报文：
#     状态行：
#     响应头：
#     响应体：请求数据就是为了得到响应体
#
# 协议+ 域名\ip +路径 以？分割 ？后面的为参数
# 参数以=分割   =前面的是参数 后面的为参数值
# 参数与参数之间以&符号隔开
# 4.http请求方法
#   method（pose get delete)
# post： 可以对数据进行增删改查
# get： 可以对数据进行增删改查
# get和post的区别（面试必问）
#   1.get的参数放在url的后面 是暴露的
#     post的参数放在请求体当中，是隐藏的
#   2.url的长度大小不能超过1KB
#    get将所有的想要发送到服务器的内容都放到url当中
#    上传文件要使用post方法