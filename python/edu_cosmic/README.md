# 一个在线教育平台， 拥有内容管理系统CMS(Content Management System)

## 建立一个灵活的CMS系统，让讲师可以创建课程并且管理课程的内容

### 提供不同的主题(subject)的课程，每个课程会被分成一定数量的可能章节(module), 每一个章节
### 有一定数量的内容(content)

# django 支持数据模型中之间的继承关系
* Abstract model 接口模型继承， 用于方便的向不同的数据模型中添加相同的信息，基类不会在数据库中建立数据表，子类会建立数据表
* Muti-table model inheritance： 多表模型继承，在继承关系中每个表都认为时一个完整的模型，每个表都会建立真实的数据表
* Proxy model 代理模型集成，在继承的时候需要改变模型的行为时使用

# 创建自定义字段
- PositiveIntegerField字段

# 如果想为一些基于类的视图，提供特定的功能和行为，可以是使用mixins
- 给类提供一系列可选的特性
- 在很多类中实现一种特定的功能


# 表单集（formsets）
- 表单集由多个Form类或者是ModelForm类的实例组成
- 表单集内所有的表单在提交的时候回忆起提交，可以对其中所有的表单进行验证
- 表单集包含一个is_valid()方法，用于一次验证所有表单

#rest框架提供的序列化器
* Serializer 为普通的Python类提供实例序列化
* ModelSerializer 为数据模型的实例提供序列化

# rest 提供的认证方式
* basicAuthentication 这是基础的app认证，用户名和密码放再http请求的Authentication 头部数据中，以base64格式发送
* TokenAuthentication 这是基于token的认证，token存放在http请求头Authentication头部数据中
* SessionAuthentication 使用django中的session后端进行验证，对于前端发来的Ajax请求一般使用这种方式验证
