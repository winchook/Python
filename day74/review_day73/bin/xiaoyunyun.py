from src.script import run

# 解释常用导入方式：
# 导入指定的py文件
# from src.plugins import base
# 导入文件夹，也叫包、模块或者类库
# from src import plugins
# 此时将默认加载(将文件中所有内容执行后加载到内存)导入__init__文件的内容，且仅执行__init__这一个文件

if __name__ == '__main__':
    run()