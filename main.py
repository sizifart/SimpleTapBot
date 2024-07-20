from pyrogram import Client
from pyrogram.raw.functions.messages import StartBot
from pyrogram.raw.functions.messages import RequestWebView
from loguru import logger
from urllib.parse import unquote
import httpx, time, os, threading, random

API_ID = 
API_HASH = ''

CLICKS_AMOUNT = 5
SLEEP_AFTER_TAP = 5
SLEEP_NO_ENOUGHT_TAPS = 3600

if not os.path.exists('sessions'):
    os.mkdir('sessions')

class SimpleTap():

    def __init__(self, user_id: int, initData: str):
        self.user_id = user_id
        self.initData = initData
        
    def profile(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/profile/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def activate(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/activate/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def tap(self, count: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/tap/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "count": count
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def get_task_list(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/get-task-list-2/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def start_task(self, type: int, id: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/start-task-start-2/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "type": type,
                        "id": id
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def check_task(self, type: int, id: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/check-task-check-2/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "type": type,
                        "id": id
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None

    def claim(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    'https://api.simple.app/api/v1/public/telegram/claim/',
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers={
                        'Accept': 'application/json, text/plain, */*', 
                        'Accept-Encoding': 'gzip, deflate, br, zstd', 
                        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                        'Content-Type': 'application/json', 
                        'Origin': 'https://simpletap.app', 
                        'Referer': 'https://simpletap.app/', 
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
                    }
                )

                return r.json()
            except:
                return None


def thread(user_id, initData, i):
    logger.info(f'Proccess thread №{i} started!')
    api = SimpleTap(user_id=user_id, initData=initData)
    while True:
        profile_data = api.profile()
        if profile_data is not None:
            logger.info(f'Thread №{i} | Current balance: {profile_data["data"]["balance"]}')
            if profile_data['data']['activeFarmingBalance'] == 0:
                activate_status = api.activate()
                if activate_status is not None:
                    if activate_status['result'] == 'OK':
                        logger.success(f'Thread №{i} | Tokens farming is activated.')

                    else:
                        logger.error(f'Thread №{i} | Tokens farming not activated.')

                else:
                    logger.error(f'Thread №{i} | Tokens get invalid response.')
            else:
                if profile_data['data']['activeFarmingSeconds'] == profile_data['data']['maxFarmingSecondSec']:
                    claim_status = api.claim()
                    if claim_status is not None:
                        if claim_status['result'] == 'OK':
                            logger.success(f'Thread №{i} | Tokens claimed. +{profile_data["data"]["activeFarmingBalance"]}')

                        else:
                            logger.error(f'Thread №{i} | Tokens not claimed.')

                    else:
                        logger.error(f'Thread №{i} | Tokens get invalid response.')
                else:
                    pass

            task_list = api.get_task_list()
            if task_list is not None:
                for task in task_list['data']['social']:
                    if task['status'] == 1:
                        t1 = api.start_task(type=task['type'], id=task['id'])
                        if t1 is not None:
                            for tt1 in task_list['data']['social']:
                                if tt1['id'] == task['id']:
                                    if tt1['status'] == 2:
                                        logger.info(f'Thread №{i} | Started task with id {tt1["id"]}')

                        t2 = api.check_task(type=task['type'], id=task['id'])
                        if t2 is not None:
                            for tt2 in task_list['data']['social']:
                                if tt2['id'] == task['id']:
                                    if tt2['status'] == 3:
                                        logger.info(f'Thread №{i} | Completed task with id {tt2["id"]}. Bonus: +{tt2["bonus"]}')

                        time.sleep(3)

            else:
                logger.error(f'Thread №{i} | Tasks get invalid response.')

            if profile_data['data']['availableTaps'] >= CLICKS_AMOUNT:
                tap_data = api.tap(count=CLICKS_AMOUNT)
                if tap_data is not None:
                    if tap_data['result'] == 'OK':
                        logger.success(f'Thread №{i} | Successly tapped. +{CLICKS_AMOUNT}')

                        time.sleep(SLEEP_AFTER_TAP)

            else:
                logger.error(f'Thread №{i} | No enought taps. Sleeping 1 hour.')
                time.sleep(SLEEP_NO_ENOUGHT_TAPS)
        else:
            logger.error(f'Thread №{i} | Profile get invalid response.')


while True:
    print('''

    ███████╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██║╚══███╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ███████╗██║  ███╔╝     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ╚════██║██║ ███╔╝      ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ███████║██║███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

    SimpleTap AUTO BOT
    Prepared and Developed by: F.Davoodi
                                                                     
    Select an action:
          
    1. Add session
    2. Start proccess
    ''')
    opt = input('\nChoose option > ')

    if opt == '1':
        session_name = input('\nEnter session name>')
        if not os.path.exists(f'sessions/{session_name}.session'):
            try:
                app = Client(
                    name=session_name,
                    api_id=API_ID,
                    api_hash=API_HASH,
                    workdir='sessions/'
                )
                with app:
                    me = app.get_me()
                    me.id

                    logger.success(f'Session with name "{session_name}" created!')
            except:
                logger.error('Cannot add session.')
        else:
            logger.error('Session name alredy used!')

    elif opt == '2':
        sessions = os.listdir('sessions')

        if len(sessions) >= 1:
            for i, session in enumerate(sessions, start=1):
                if session.endswith('.session'):
                    try:
                        app = Client(
                            name=session.replace('.session', ''),
                            api_id=API_ID,
                            api_hash=API_HASH,
                            workdir='sessions/'
                        )
                        app.start()

                        web_view = app.invoke(StartBot(
                            peer=app.resolve_peer('Simple_Tap_Bot'),
                            bot=app.resolve_peer('Simple_Tap_Bot'),
                            random_id=random.randint(1000, 9999),
                            start_param='1717785892732'
                        ))
                        web_view = app.invoke(RequestWebView(
                            peer=app.resolve_peer('Simple_Tap_Bot'),
                            bot=app.resolve_peer('Simple_Tap_Bot'),
                            platform='android',
                            from_bot_menu=False,
                            url='https://simpletap.app/'
                        ))

                        user_id = app.get_me().id
                        initData = unquote(string=unquote(string=web_view.url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0]))

                        threading.Thread(target=thread, args=(user_id, initData, i,)).start()
                    except:
                        logger.error(f'Cannot start proccess thread with "{session}" session.')

        break