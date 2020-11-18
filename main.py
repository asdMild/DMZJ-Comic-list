import requests
import json, os

if not os.path.exists('./comic/'):
    os.makedirs('./comic/')


USERNAME = 'username'
PASSWARD = 'passward'

loginurl = 'http://i.dmzj.com/api/login?callback=&nickname='+USERNAME+'&password='+PASSWARD+'&type=1'
mysubscribeurl = 'http://m.dmzj.com/mysubscribe'
#getcomicurl = 'http://v3api.dmzj.com/comic/comic_' + str(0) + '.json'


r = requests.get(loginurl)
header = r.headers
cookies = r.cookies
r = requests.get(mysubscribeurl, headers=header,cookies=cookies )
j = r.json()


for item in j:
    t = 3
    while t > 0:
        try:
            comicid = item['sub_id']
            getcomicurl = 'http://api.dmzj.com/dynamic/comicinfo/' + str(comicid) + '.json'
            print(getcomicurl)
            r = requests.get(getcomicurl)
            js = r.json()
            js = js['data']
            filename = js['info']['title']
            print(js)
            with open('./comic/' + filename, 'w+', encoding='utf-8') as fp:
                a = json.dumps(js, ensure_ascii=0)
                fp.write(a)
                fp.close()
            t = -1
        except:
            t = t - 1
            if t == 0:
                print(item['sub_id'])
                with open('./comic/' + str(item['sub_id']), 'w+', encoding='utf-8') as fp:
                    fp.write('http://v3api.dmzj.com/comic/comic_' + str(item['sub_id']) + '.json')
