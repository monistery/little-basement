# Markdown基本语法 
&nbsp;

---

## 一、标题
1. **使用=和-标记一级标题和二级标题：**  
- markdown中的实际代码:
    ``` 
    我展示的是一级标题
    =================

    我展示的是二级标题
    -----------------
    ```
- 生成文件的效果：  
  
    我展示的是一级标题
    =================

    我展示的是二级标题
    ----------------- 
&nbsp;

2. **使用#号标记：**  
- markdown中的实际代码:
    ``` 
    # 一级标题
    ## 二级标题
    ### 三级标题
    #### 四级标题
    ##### 五级标题
    ###### 六级标题
    ```
- 生成文件的效果：  
    # 一级标题
    ## 二级标题
    ### 三级标题
    #### 四级标题
    ##### 五级标题
    ###### 六级标题
&nbsp;
- - -
&nbsp;
- - -
## 二、段落
1. **换行**  
Markdown 段落没有特殊的格式，直接编写文字就好。  
段落的换行是**使用两个以上空格加上回车，或在段落后面使用一个空行来表示重新开始一个段落。**(其中的区别在于---两个空格加回车表示这下一段仍在上一段的区间，而一个空行表示下一段不在上一段的区间)  
&nbsp;
2. **字体**  
Markdown 可以使用以下几种字体：  
- markdown中的实际代码:
    ``` 
    *斜体文本*
    _斜体文本_
    **粗体文本**
    __粗体文本__
    ***粗斜体文本***
    ___粗斜体文本___
    ```
- 生成文件的效果：  
    *斜体文本*  
    _斜体文本_  
    **粗体文本**  
    __粗体文本__  
    ***粗斜体文本***  
    ___粗斜体文本___  
&nbsp; 
3. **分隔线**  
你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，**行内不能有其他东西**。你也可以在星号或是减号中间插入空格。    
- markdown中的实际代码:
    ``` 
    ***
    * * *
    *****
    - - -
    ----------
    ```
- 生成文件的效果：  
    ***
    * * *
    *****
    - - -  
    ----------  
&nbsp; 

4. **删除线**  
如果段落上的文字要添加删除线，只需要在文字的两端加上两个波浪线 ~~ 即可。
- markdown中的实际代码:
    ```
    RUNOOB.COM  
    GOOGLE.COM  
    ~~BAIDU.COM~~  
    ```
- 生成文件的效果：   
    RUNOOB.COM  
    GOOGLE.COM  
    ~~BAIDU.COM~~  
&nbsp;  
5. **下划线**  
下划线可以通过HTML的<u></u>标签来实现。  
- markdown中的实际代码:
    ```
    <u>带下划线文本</u>  
    ```
- 生成文件的效果：   
    <u>带下划线文本</u>   
&nbsp;  
6. **脚注**
脚注是对文本的补充说明。  
- markdown中的实际代码:
    ```
    创建脚注格式类似这样 [^RUNOOB]。
    [^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！ 
    ```
- 生成文件的效果：   
    创建脚注格式类似这样 [^RUNOOB]。  
    [^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！