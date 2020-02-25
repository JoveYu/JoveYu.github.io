import glob
import datetime

files = glob.glob('*.md')
for path in files:
    with open(path) as file:
        title=''
        date=''
        content = ''
        content_flag=False
        code_type=''
        code = ''
        code_flag = False
        for line in file.readlines():
            line = line.strip('\r\n')
            if not content_flag and '.. title' in line:
                title=line.split(':',1)[1].strip()
            elif not content_flag and '.. date' in line:
                date=line.split(':',1)[1].strip()
                date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S+08:00')
            elif '\t:::' in line:
                code_type = line.split(':::')[1].strip()
                code = ''
                code_flag=True
            elif code_flag:
                if line == '' or line.startswith('\t'):
                    code = code + line[1:] + '\n'
                else:
                    code_flag=False
                    content += '```{}\n{}\n```'.format(code_type, code)
                    code = ''
            elif content_flag:
                if line.startswith('#'):
                    tmp = line.split('#')
                    line = '#' * (len(tmp)-1) + ' '+ tmp[-1].strip()
                content = content + line + '\n'
            elif '-->' in line and content_flag==False:
                content_flag=True
                content='''
---
title: {}
date: {}
tags:
  - 归档导入
---
'''.format(title, date.strftime('%Y-%m-%d %H:%M:%S'))
        if code != '':
            content += '```{}\n{}\n```'.format(code_type, code)

        #print(content)


        with open('new/{}'.format(path), 'w') as file2 :
            file2.write(content)


