import requests


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
    'input': 'dzqc',
    'type': 'getUserDetails',
}

response = requests.post('https://tikfollowers.com/api/search',  headers=headers, json=json_data)
print(response.json())
try:
    id = response.json()["user_id"]
    sec_uid = response.json()["sec_uid"]
    follower = response.json()["followers_count"]
    following = response.json()["following_count"]
    bio =response.json()["bio"]
    name = response.json()["nickname"]
    photo = response.json()["profilePic"]
    praivet = response.json()["profilePic"]
except:
    print("www")
# {'status': 'success', 'token': 'i8VTbOof89HNQpUGJlb8V-Mk8qVqf4MU55bFNNW7lt-QxGHnwJme-YlTmbcUh5eO', 'user_id': '7120974004055426053', 'sec_uid': 'MS4wLjABAAAALeYC8G2XelGSVrtiZgA4F9xcu2pcp8cjA_anG6D9NFPCK0Rjm5DtRThR94QqOUSw', 'region': 'IQ', 'username': 'dzqc', 'followers_count': '850', 'following_count': '10,000', 'bio': 'ه', 'nickname': '.', 'profilePic': 'https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/5f09133d2a3f11cbec8d67b3e980414e~tplv-tiktokx-cropcenter:1080:1080.webp?dr=14579&refresh_token=70f98a20&x-expires=1754920800&x-signature=WJn3BWWgRFkb70NAyEDIaM%2BK%2BLw%3D&t=4d5b0474&ps=13740610&shp=30310797&shcp=c1333099&idc=maliva', 'profilePic': False, 'success': True}
