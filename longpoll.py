import requests,json
import vk
from time import sleep
from settings import auth,ids



session = vk.AuthSession(user_login=auth.login,
                         user_password=auth.password,
                         app_id=auth.app_id,
                         scope=auth.scope)

session2 = vk.AuthSession(access_token=auth.purple_haze,
                          scope=auth.group_scope)

vkapi = vk.API(session)
bot = vk.API(session2)
v = 5.73


r = vkapi.messages.getLongPollServer(v=v)
server = r['server']
key = r['key']
ts = r['ts']


def req():
    global key,server,ts,n
    n = 'https://{}?act=a_check&key={}&ts={}&wait=25&version=2'.format(server, key, ts)


req()
while True:
    r = json.loads(requests.get(n).text)
    ts = r['ts']
    for i in r['updates']:
        if i[0] == 61:
            print(i)
            bot.messages.send(user_id=ids.myID, message = 'https://vk.com/im?sel='+str(i[1]),v=v)
            req()
    sleep(1)
print(r)
