import requests,SignerPy,secrets,random,binascii,uuid,os

tokens = secrets.token_hex(16)
def xor(string):
    return "".join([hex(ord(c)^5)[2:] for c in string])

url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"

params = {
    "passport-sdk-version": "6031990",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    "cdid": str(uuid.uuid4()),
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "240",
    "device_type": "SM-S908E",
    "device_brand": "samsung",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "DE",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1754825061",
    "mcc_mnc": "26202",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "262",
    "residence": "DE",
    "app_language": "en",
    "carrier_region": "DE",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "content_language": "en,",
    "ac2": "wifi",
    "uoo": "1",
    "op_region": "DE",
    "build_number": "37.8.5",
    "region": "GB",
    "ts":str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    "iid": str(random.randint(1, 10**19)),
    "device_id": str(random.randint(1, 10**19)),
    "openudid": str(binascii.hexlify(os.urandom(8)).decode()),
    "support_webview": "1",
    "reg_store_region": "de",
    "device_redirect_info": "15SCqoVmGScbE2sP6cWQ_aldzAqBU4FkiszCXucwL9WB2Oi9YkkCAuCs-62hr0911Nd_EVz0loRX5DFlIqLeOc6GnlZw-eTYHju1Eur3-YqdaTIkoV9W1J8mNnsPqe0gYjCjbylYeXtCorxJXh5D5Irxd_I5jt8Ht4KqW-PTJlY",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5"
}
cookies = {

    "passport_csrf_token": tokens,
    "passport_csrf_token_default":tokens,
    "install_id":params["iid"]
}
payload = {
  'rules_version': "v2",
  'account_sdk_source': "app",
  'mix_mode': "1",
  'multi_login': "1",
  'type': "3436",
  'email':xor(input("enter email :")),
  'email_theme': "2",
  'use_passport_ticket': "1"
}
m=SignerPy.sign(params=params,cookie=cookies,payload=payload)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)",
  'Accept-Encoding': "gzip",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-pba-enable': "1",
  'x-tt-multi-sids': "6639559680287080453%3A915a130007d6776fba343499969874eb",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket':m['x-ss-req-ticket'],

  'x-tt-passport-csrf-token': tokens,
 
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
 
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'x-tt-bypass-dp': "1",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos':m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon':m['x-gorgon'],
  
}

response = requests.post(url, data=payload, headers=headers,cookies=cookies,params=params)

print(response.text)
passport_ticket=response.json()["data"]["passport_ticket"]



url = "https://api32-normal-alisg.tiktokv.com/passport/auth/available_ways/"

params = {
    "passport_ticket":passport_ticket,
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    "cdid":params["cdid"],
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "240",
    "device_type": "SM-S908E",
    "device_brand": "samsung",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "DE",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1754825061",
    "mcc_mnc": "26202",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "262",
    "residence": "DE",
    "app_language": "en",
    "carrier_region": "DE",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "content_language": "en,",
    "ac2": "wifi",
    "uoo": "1",
    "op_region": "DE",
    "build_number": "37.8.5",
    "region": "GB",
    "ts":str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    "iid": params["iid"],
    "device_id": params["device_id"],
    "openudid": params["openudid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version":"37.8.5"
}
m=SignerPy.sign(params=params,cookie=cookies)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-tt-pba-enable': "1",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket': m['x-ss-req-ticket'],

  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
 
  'tt-ticket-guard-version': "3",
  'passport-sdk-settings': "x-tt-token",
  'passport-sdk-sign': "x-tt-token",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-pba-enable': "1",
  'x-ladon': m['x-ladon'],
  'x-khronos':m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon':m['x-gorgon'],
}

response = requests.get(url, headers=headers,cookies=cookies,params=params)

print(response.text)
has_email=response.json()["data"]["has_email"]
has_mobile = response.json()["data"]["has_mobile"]
has_outh = response.json()["data"]["has_oauth"]
platforms = response.json()["data"]["oauth_platforms"]
safe = response.json()["data"]["safe"]
mobile = response.json()["data"]["mobile"]
email = response.json()["data"]["email"]
has_pas = response.json()["data"]["has_pwd"]
# {"data":{"email":"a***a@gmail.com","email_ticket":"APH9YB7F3BGYMJ5UKKTCURNE95PRXQ6U","passport_ticket":"PPTSGO67S4WYB4MQMA3JDG6NCA8677F38JCP9N"},"message":"success"}
# {"data":{"has_pwd":true,"has_mobile":false,"has_oauth":true,"has_email":true,"mobile":"","email":"a***a@gmail.com","oauth_platforms":["google"],"safe":false},"message":"success"}
