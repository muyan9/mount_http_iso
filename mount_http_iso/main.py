#coding=utf-8

import binascii

filename = "test.iso"
f = open(filename, 'rb')
f.seek(0x8000)
'''
在图4分别是矩形的
1标准标识符，
2系统标识符，
3卷空间大小（检查，如果你能找到二进制回文），
4卷集大小，
5卷序列号
6逻辑块大小，
7路径表大小，
8目录记录根目录。
加上图3中可以按照图4中的参数。
此外，连同图4和图5，你应该能够发现目录记录在CD-ROM（以下段落解释）表示根目录的方式。
'''
standard_id = f.read(8)
system_id = f.read(32)
f.read(32)
vol_size = ''
vol_set_size = ''
vol_Sequence_Number = ''
logical_block_size = ''
path_table_size = ''
root = ''