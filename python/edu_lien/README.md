# 在线教育平台，拥有内容管理系统CMS（Content Management System）

## 建立一个灵活的CMS系统，让讲师可以创建课程并且管理课程内容

### 提供不同的主题（subje）的课程，每个课程会被划分成一定数量的章节（model），每个章节有一定数量的内容（content）


# django 支持数据模型之间的继承关系
* Abstract model 接口模型继承，用于方便的向不同的数据模型中添加相同的信息，基类不会在数据库中建立数据表，子类会建立数据表
* Muti-table model inheritance： 多表模型继承，在继承关系中，每个表都认为是一个完整的模型，每个表都会建立真实的数据表
* Proxy model：代理模型集成，在继承的时候需要改变模型的行为时使用

# 创建自定义字段
- PositiveIntegerField字段

# 如果想为一些基于类的视图，提供特定的功能和行为，可以使用mixins
- 给雷提供一些可选的特性
- 在很多类中实现一种特定的功能

# 表单集（formsets）
- 表单集由多个form类或者是ModelForm类的实例组成的
- 表单集内多有的表单在提交的时候回忆起提交，可以对其中所有的表单进行验证
- 表单集包含一个is_vaild（）方法，用于一次验证所有的表单