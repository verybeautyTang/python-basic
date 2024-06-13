# output formating
import reprlib
reprlib1 = reprlib.repr(set('sadfkjhasdlkjhasdjflghwieuzxncbvausydgfal'))
print(reprlib1)  # {'a', 'b', 'c', 'd', 'e', 'f', ...}

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

# The textwrap module formats paragraphs of text to fit a given screen width
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=50))


#
# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# conv = locale.localeconv()
# x = 12345678.9
# print(conv)
# print(locale.format_string('%d', x, grouping=True))
# locale.format_string('%s.*f', (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)


# 模版 Templating
from string import Template
template1 = Template('${village}folk send $$10 to $cause.')
print(template1.substitute(village='helloWorld', cause='the ditch fund'))  # helloWorldfolk send $10 to the ditch fund.

template2 = Template('Return the $item to $owner')
d = dict(item ='unladen swallow')
print(template2.safe_substitute(d))  # Return the unladen swallow to $owner

import time, os.path
photofiles = ['img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')  # hello_%n%f 自己随便输入
template3 = BatchRename(fmt)
datetime = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = template3.substitute(d=datetime, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))




# working with binary data record layouts
import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()
start =0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start + extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # skip to the next header


