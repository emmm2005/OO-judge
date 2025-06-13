# README

- 使用方式：

  将打包好的jar包放在/JAR/judge目录下，运行main.py，输入需要的参数即可

  参数：

  - …… prefix：表示jar包前缀
  - …… num ……：表示jar包后缀数字
  - ……thread(s)：表示对jar包测试启用的线程数
  - …… epoch ……：表示测试轮数

- 要求：

  - jar包命名：需要命名为`“(prefix)(num)”`的形式，即英文前缀加数字后缀，在输入时需要输入前缀以保证测试的jar包是希望运行的jar包