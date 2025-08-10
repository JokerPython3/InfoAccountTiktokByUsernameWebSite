from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import SignerPy
import secrets
import random
import binascii
import uuid
import os
import time
import json
from requests import get, post, Session


class TikTok:
    def __init__(self, user):
        self.data = {}
        self.user = user

    def check_rest(self):
        cog = secrets.token_hex(6*2+4)
        cookies = {
            "passport_csrf_token": cog,
            "passport_csrf_token_default": cog
        }

        s = Session()
        s.cookies.update(cookies)
        url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"

        params = {
            'request_tag_from': "h5",
            'fixed_mix_mode': "1",
            'mix_mode': "1",
            'account_param': self.user,
            'scene': "4",
            'device_platform': "android",
            'os': "android",
            'ssmix': "a",
            '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
            'cdid': str(uuid.uuid4()),
            'channel': "googleplay",
            'aid': "1233",
            'app_name': "musical_ly",
            'version_code': "370805",
            'version_name': "37.8.5",
            'manifest_version_code': "2023708050",
            'update_version_code': "2023708050",
            'ab_version': "37.8.5",
            'resolution': "720*1448",
            'dpi': "320",
            'device_type': "RMX3269",
            'device_brand': "realme",
            'language': "ar",
            'os_api': "30",
            'os_version': "11",
            'ac': "wifi",
            'is_pad': "0",
            'current_region': "IQ",
            'app_type': "normal",
            'sys_region': "IQ",
            'last_install_time': "1744847306",
            'mcc_mnc': "41840",
            'timezone_name': "Asia%2FBaghdad",
            'carrier_region_v2': "418",
            'residence': "IQ",
            'app_language': "ar",
            'carrier_region': "IQ",
            'timezone_offset': "10800",
            'host_abi': "arm64-v8a",
            'locale': "ar",
            'ac2': "wifi",
            'uoo': "0",
            'op_region': "IQ",
            'build_number': "37.8.5",
            'region': "IQ",
            'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
            'iid': str(random.randint(1, 10**19)),
            'device_id': str(random.randint(1, 10**19)),
            'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
            'support_webview': "1",
            'cronet_version': "75b93580_2024-11-28",
            'ttnet_version': "4.2.210.6-tiktok",
            'use_store_region_cookie': "1",
            'app_version': "37.8.5"
        }
        m = SignerPy.sign(params=params, cookie=cookies)
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
            'Accept': "application/json, text/plain, */*",
            'content-length': "0",
            'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
            'x-tt-passport-csrf-token': cog,
            'content-type': "application/x-www-form-urlencoded",
            'x-argus': m["x-argus"],
            'x-gorgon': m["x-gorgon"],
            'x-khronos': m["x-khronos"],
            'x-ladon': m["x-ladon"],
        }

        response = s.post(url, params=params, headers=headers)
        try:
            p = response.json()['data']['accounts'][0]['passport_ticket']
            ug = response.json()['data']['accounts'][0]['username']
            params = {
                'request_tag_from': "h5",
                'fixed_mix_mode': "1",
                'mix_mode': "1",
                'account_param': self.user,
                'passport_ticket': p,
                'scene': "4",
                'device_platform': "android",
                'os': "android",
                'ssmix': "a",
                '_rticket': params['_rticket'],
                'cdid': params['cdid'],
                'channel': "googleplay",
                'aid': "1233",
                'app_name': "musical_ly",
                'version_code': "370805",
                'version_name': "37.8.5",
                'manifest_version_code': "2023708050",
                'update_version_code': "2023708050",
                'ab_version': "37.8.5",
                'resolution': "720*1448",
                'dpi': "320",
                'device_type': "RMX3269",
                'device_brand': "realme",
                'language': "ar",
                'os_api': "30",
                'os_version': "11",
                'ac': "wifi",
                'is_pad': "0",
                'current_region': "IQ",
                'app_type': "normal",
                'sys_region': "IQ",
                'last_install_time': "1744847306",
                'mcc_mnc': "41840",
                'timezone_name': "Asia%2FBaghdad",
                'carrier_region_v2': "418",
                'residence': "IQ",
                'app_language': "ar",
                'carrier_region': "IQ",
                'timezone_offset': "10800",
                'host_abi': "arm64-v8a",
                'locale': "ar",
                'ac2': "wifi",
                'uoo': "0",
                'op_region': "IQ",
                'build_number': "37.8.5",
                'region': "IQ",
                'ts': params['ts'],
                'iid': params['iid'],
                'device_id': params['device_id'],
                'openudid': params['openudid'],
                'support_webview': "1",
                'cronet_version': "75b93580_2024-11-28",
                'ttnet_version': "4.2.210.6-tiktok",
                'use_store_region_cookie': "1",
                'app_version': "37.8.5"
            }
            self.data.update({'username': ug})

            m = SignerPy.sign(params=params, cookie=cookies)
            headers = {
                'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
                'Accept': "application/json, text/plain, */*",
                'content-length': "0",
                'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
                'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],
                'content-type': "application/x-www-form-urlencoded",
                'x-argus': m["x-argus"],
                'x-gorgon': m["x-gorgon"],
                'x-khronos': m["x-khronos"],
                'x-ladon': m["x-ladon"],
            }
            url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"

            response = s.post(url, params=params, headers=headers)

            kj = json.loads(response.headers["x-tt-verify-idv-decision-conf"])

            for uu in kj['extra']:
                oo = uu['info']
                if '@' in oo:
                    k = oo
                    jj = k.split('@')[1]
                    self.data.update({'rest': k})
                    kk = k.split('@')[0]
                    hu = self.user[0]
                    gf = self.user[-1]
                    y = kk[0]
                    iy = kk[-1]
                    if hu == y and gf == iy:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
                        re = get(f'https://www.tiktok.com/@{self.user}', headers=headers).text
                        followers = str(re).split(':{"followerCount":')[1].split(',')[0]
                        self.data.update({'username': self.user, 'followers': followers, 'email': self.user + jj})
                elif '+' in oo:
                    self.data.update({'number': oo})
                else:
                    self.data.update({'result': oo})

            return self.data

        except Exception as e:
            return {"status": "error", "message": "ksj"}


def xor(string):
    return "".join([hex(ord(c) ^ 5)[2:] for c in string])


class Information:
    def __init__(self, user):
        self.user = user

    def get_info(self):
        headers = {
            'accept': '*/*',
            'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://tikfollowers.com',
            'priority': 'u=1, i',
            'referer': 'https://tikfollowers.com/free-tiktok-followers',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'input': self.user,
            'type': 'getUserDetails',
        }

        response = requests.post('https://tikfollowers.com/api/search', headers=headers, json=json_data)
        # print(response.json())

        try:
            data = response.json()
            id = data["user_id"]
            sec_uid = data["sec_uid"]
            follower = data["followers_count"]
            following = data["following_count"]
            bio = data["bio"]
            name = data["nickname"]
            photo = data["profilePic"]
            praivet = data["profilePic"]

            ma = TikTok(self.user).check_rest()

            if "ksj" in response.text:
                return {"status": "error", "message": "ksj"}
            else:
                return {
                    "status": "success",
                    "id": id,
                    "sec_uid": sec_uid,
                    "followers": follower,
                    "following": following,
                    "bio": bio,
                    "name": name,
                    "photo": photo,
                    "parivet": praivet,
                    "rest_email": ma.get("email", ""),
                    "rest_mobile": ma.get("number", ""),
                    "message": "zb"
                }
        except Exception as e:
            return {"status": "error", "message": "ksj"}


        # try:
        #     id = response.json()["user_id"]
        #     sec_uid = response.json()["sec_uid"]
        #     follower = response.json()["followers_count"]
        #     following = response.json()["following_count"]
        #     bio =response.json()["bio"]
        #     name = response.json()["nickname"]
        #     photo = response.json()["profilePic"]
        #     praivet = response.json()["profilePic"]
		# 	return {"status":"success","id":id,"sec_uid":sec_uid,"followes":follower,"following":following,"bio":bio,"name":name,"photo":photo,"parivet":praivet,"message":"zb"}
        # except:
        #     return{"status":"error","message":'ksj'}
# {'status': 'success', 'token': 'i8VTbOof89HNQpUGJlb8V-Mk8qVqf4MU55bFNNW7lt-QxGHnwJme-YlTmbcUh5eO', 'user_id': '7120974004055426053', 'sec_uid': 'MS4wLjABAAAALeYC8G2XelGSVrtiZgA4F9xcu2pcp8cjA_anG6D9NFPCK0Rjm5DtRThR94QqOUSw', 'region': 'IQ', 'username': 'dzqc', 'followers_count': '850', 'following_count': '10,000', 'bio': 'ه', 'nickname': '.', 'profilePic': 'https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/5f09133d2a3f11cbec8d67b3e980414e~tplv-tiktokx-cropcenter:1080:1080.webp?dr=14579&refresh_token=70f98a20&x-expires=1754920800&x-signature=WJn3BWWgRFkb70NAyEDIaM%2BK%2BLw%3D&t=4d5b0474&ps=13740610&shp=30310797&shcp=c1333099&idc=maliva', 'profilePic': False, 'success': True}

temp = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/",response_class=HTMLResponse)
async def index(request: Request):
    return temp.TemplateResponse("index.html",{"request":request})
@app.post("/info",response_class=HTMLResponse)
async def info(request: Request, text: str = Form(...)):
    data = Information(text).get_info()
    return temp.TemplateResponse("info.html",{"request":request,"data":data})
