# 曹蔚然的PYTHON大作业
project source can be downloaded form https://github.com/jondlerjostar/tjuhomework
---
---
Author & Contributor List
Cao weiran
All other known bug can be sent to sdwfcwr@163.com
---
---
环境依赖
Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

额外安装的库
jieba、beautifulsoup、requests

---

# 文件目录

```
readme.md
_pycache_
```
```
head.py
homeworkall.py
hash.py
prograssbar.py
seg7.py
seeker.py
matchAnalysis,py
url.py
compiler.py
checker.py
```
```
seg7.txt
hamlet.txt
bar.txt
hash.txt
correct.txt
```
# 文件功能及使用方法
## head.py
```
头文件中包含了全部程序的主程序介绍，便于直接在homeworkall.py中调用子程序
```
## homeworkall.py
```
主体和控制程序
内嵌七种主要功能的入口
进入后输入密码启动主程序，并通过选择菜单选择欲运行的子程序
```
## hash.py
```
哈希函数，能够实现任意字符串的指定位数加盐加密
输入：待加密字符串、加密位数
输出：加密后字符串及其原码
```
## prograssbar.py
```
文本进度条程序，基于turtle库实现任意图像绘制，并实时显示绘制进度
输入：总笔画数（用于规划进度条）
      对笔画颜色、尺寸、速度的设置
      对笔画朝向、性质（直线/曲线）、长度/半径的设置
输出：绘图及进度条
本程序可实现任意颜色尺寸速度的修改，且可自由设置笔画性质，加入多次默认判定以减少使用时的累赘感
```
## seg7.py
```
七段数码管绘制程序，基于turtle库实现七段数码管和任意文字的显示
主要功能：自定义输入/时间查询
输入：功能选择
      数码管和文字的颜色、尺寸、速度设置
      自定义输入输入内容
输出：数字信息以七段数码管形式输出，汉字及英语使用turtle内置程序直接输出
```
## seeker.py
```
文本查询器，查询输入词汇是否在指定文本中并显示出现频率
主要功能：保留字查询/自定义查询
输入：功能选择、自定义字符选取
输出：词频统计
```
## matchAnalysis,py
```
比赛分析器，根据输入的能力对比模拟棒球比赛结果
输入：能力值，适应天气，比赛场次
输出：胜率
```
## url.py
```
爬虫URL，获取指定网页的URL，并进行递归扒取
```
## compiler.py
```
语法检查器，检查输入程序中的语法问题
输入：待检查语篇
输出：语法错误类型及其行数位置
可检查类型： if、elif、else、while、try、except、def的语法错误(':''()'情况及内部逻辑(如elif、else是否有对应的if；try和except能否对应))
  
```
- 新添加对注释的改进，现在程序不会由于注释产生误识别了 
- 新添加对空格的判定，现在多余的空格不会影响判定了
- 新添加对前置的判定，现在关键词前有信息会被检测出来
- 优化了对':'问题的归类
- 新增了对同一语句中的错误数目的显示
- 新增了头部检查，现在"有elif无else""有try无except"能够第一时间显示了

## checker.py
```
语法检查器第二版，在老师建议下，以Flake8为基础编写，减少了工作量
输入：待检查语篇
输出：语法错误类型及其行数位置
```

# 备注
- 全部程序采用自顶而下编程逻辑
- 子程序均配备简要注释
- 程序中均已加入异常处理，如测试出新BUG请联系开发者

# 修改时间轴
- 5.13 初版提交
- 5.26 上传
    - README.md
    - url.py
    - compiler.py
    - 对主程序和程序逻辑进行了相应的重做
- 6.18 上传checker.py
