magazine
========

django周刊管理

设计思想：
    使用Django Admin模块对实现周刊管理，管理模块的功能包块：文章管理、周刊管理、以及一个文章显示顺序的维护模块。
    
主要功能及部分实现介绍：

  1、文章的增删改查
  
    这部分功能由Django的Admin模块实现，在Admin中注册ArticleAdmin
    
  2、周刊管理
  
    这部分功能由Django的Admin模块实现，在Admin中注册JournalAdmin
    
  3、文章显示顺序
  
    文章显示顺序通过Catalog进行维护，在Admin管理功能中，通过新建、编辑Catalog，设置index属性的方式设置期刊中文章的显示顺序。前台显示某一周刊时会通过对index属性对文章进行排序，从而实现编辑期刊中文章顺序的功能。
  
  4、封面文章与一般文章
  
    在该管理系统中没有明显区别，只不过在某一期中index为1的文章将在周刊首页展示内容，而一般文章则在周刊的目录中按照index属性显示。
  
  5、导航功能
  
    导航功能只包含两个超链接，一个指向当前最新一起的周刊。最新一期是指id最后的一起（未记录周刊创建时间，所以只能勉强这样了）;另一个超链接指向周刊列表，给出所有周刊的入口
  
  6、期刊展示
  
    通过周刊列表进入某一周刊后将看到该周刊的一些基本信息，包括刊名、有多少篇文章、第一篇文章的内容以及一个简单的周刊文章列表点击开始阅读按钮则进入周刊的目录页。
  
  7、浏览期刊
  
    通过期刊的目录页点击文章篇名的方式开始阅读。每一篇文章内容包括：题名、作者、创建时间、图片、内容、评论等。
    
  8、对文章进行评论
  
    在阅读文章内容后可以对文章进行评论，评论要求填写：姓名、邮箱、网址、评论内容。评论内容支持markdown格式。

    
    
