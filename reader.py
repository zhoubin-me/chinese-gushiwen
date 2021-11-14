import glob
import json

with open('guwen/guwen0-1000.json', encoding='utf-8') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        poem = json.loads(line)
        content = poem['content']
        author = poem['writer']
        title = poem['title']
        if '·' in title:
            titles = title.split('·')
            if titles[1].strip()[0] == '其':
                title = titles[0].strip()
            else:
                title = titles[1].strip()
        elif '/' in title:
            title = title.split('/')[0].strip()
        else:
            pass

        content = content.replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
        content = content.replace('；', '|').replace('、', '|').replace('，', '|').replace('。', '|').replace('？', '|')
        if content[-1] == '|':
            content = content[:-1]
        if len(content.split('|')) == 4:
            idata = {'content': content, 'author': author, 'title': title}
            print(title)
            data.append(idata)

with open('jueju.json', 'w') as f:
    json.dump(data, f)
print(len(data))

with open('jueju.json', 'r') as f:
    x = f.read()

with open('jueju2.json', 'w') as f:
    f.write("jueju2=" + x)