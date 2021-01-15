import requests

with open('/Users/nikashsethi/Desktop/ids.txt', 'r+') as f:
    ids = f.read().splitlines()
    
with open('/Users/nikashsethi/Desktop/test.txt', 'r+') as newfile:
    for i in range(len(ids)):
        url = 'http://www.image-net.org/api/text/wordnet.synset.getwords?wnid=' + ids[i]
        page = requests.get(url)
        names = [label.title() for label in page.content.decode("utf-8").split('\n')]
        name = ', '.join(names)[:-2]
        entry = '(\''+ids[i]+'\', \''+name+'\'),\n'
        newfile.write(entry)
        print (i)
