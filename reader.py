import glob
import json

fs = glob.glob('guwen/*.json')
data = []
for fname in fs:
    with open('guwen/guwen0-1000.json', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            poem = json.loads(line)
            content = poem['content']
            author = poem['writer']
            title = poem['title']
            dynasty = poem['dynasty']

            if '一作' in content:
                continue
            if '节选' in title:
                continue
            if not ('唐代' in dynasty or '宋代' in dynasty):
                continue

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
            content = content.replace('；', '|').replace('、', '|').replace('，', '|').replace('！', '|').replace('。', '|').replace('？', '|')

            if content[-1] == '|':
                content = content[:-1]
            if len(content.split('|')) <= 8:
                idata = {'content': content, 'author': author, 'title': title, 'dynasty': dynasty}
                print(title, dynasty)
                data.append(idata)

with open('jueju.json', 'w') as f:
    json.dump(data, f)
print(len(data))