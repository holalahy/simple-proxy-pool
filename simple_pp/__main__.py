''' __main__, to run:
python -m yeekit_tr
'''

from simple_pp import simple_pp  # , PROXYPOOL
# from proxybroker import Broker


# pragma: no cover
def main():
    '''main'''
    import sys
    from pathlib import Path
    import fileinput
    from pprint import pprint

    files = []
    for file in sys.argv[1:]:
        if Path(file).exists():
            files.append(file)

    if not files:
        pprint(' No file name provided or none exists.')
        pprint(' 未提供文件名或所提供文件名的文件不存在')
        print(f' 请将 ip 代理贴在下面，新起一行按 ctrl-Z （同时按下Ctrl键和zjian）加回车键结束…………\n')
    else:
        print(f' 验证中……\n')
    text = ''
    for line in fileinput.input(files):
        text += line

    print(text)
    pprint(' 按任意键退出。')
    _ = input()

if __name__ == '__main__':
    main()
