import glob
import random
import json

fs = glob.glob('guwen/*.json')
data = []

for fname in fs:
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            poem = json.loads(line)
            content = poem['content']
            author = poem['writer']
            title = poem['title']
            dynasty = poem['dynasty']

            if '：' in content:
                continue
            if '节选' in title:
                continue
            dynasties = ['先秦', '魏晋', '南北朝', '两汉', '宋代', '隋代', '唐代']

            if dynasty not in dynasties:
                continue
            dynasty = dynasty.replace('代', '')

            if '·' in title:
                titles = title.split('·')
                x = titles[1].strip()
                if len(x) > 0 and x[0] == '其':
                    title = titles[0].strip()
                else:
                    title = titles[1].strip()
            elif '/' in title:
                title = title.split('/')[0].strip()
            else:
                pass

            content = content.replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '').replace('\\u3000', '')
            content = content.replace('；', '|').replace('、', '|').replace('，', '|').replace('！', '|').replace('。', '|').replace('？', '|')
            if content[-1] == '|':
                content = content[:-1]

            contents = content.split('|')
            head = '﹃' + title + '﹄' + dynasty + '・' + author
            contents.insert(0, head)

            if len(contents) <= 9:
                data.append({'content': contents, 'count': len(contents)})
                print(contents)

with open('poem.json', 'w') as f:
    json.dump(data, f)


data = []
with open('sentence/sentence1-10000.json', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = json.loads(line)
        content = line['name']
        author = line['from']

        content = content.replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '').replace('\\u3000', '')
        content = content.replace('；', '|').replace('、', '|').replace('，', '|').replace('！', '|').replace('。', '|').replace('？', '|')
        if content[-1] == '|':
            content = content[:-1]
        contents = content.split('|')

        author = author.split('《')
        head = '﹃' + author[1].strip()[:-1] + '﹄' + author[0].strip()
        contents.insert(0, head)
        data.append({'content': contents, 'count': len(contents)})
        print(contents)

with open('sentence.json', 'w') as f:
    json.dump(data, f)