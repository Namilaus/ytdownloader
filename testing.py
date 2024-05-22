import requests

url = 'https://rr3---sn-4g5ednly.googlevideo.com/videoplayback?expire=1716346260&ei=NAlNZpHKMJ-I6dsPoKOwqAc&ip=2003%3Ad0%3Adf2e%3A4e00%3A65e4%3A360b%3Aa635%3A29c5&id=o-AB2x5jdVUuvwEzaKkD7Gkz_ybcKzTAjCQPsECT3vJxln&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=zx&mm=31%2C29&mn=sn-4g5ednly%2Csn-4g5e6nzl&ms=au%2Crdu&mv=m&mvi=3&pl=36&initcwndbps=1995000&bui=AWRWj2T17i_Pa5MQb1BkO8ZslN7IKM1HAJMwzmRi7JR0tzNHlcYdRJR51fMEvcheWIxArjxHL1ZWnyF4&spc=UWF9f0QpTz3xIT-ok5KeoAKyHVDpW5QcXm59z4sX2f2RYlKzqR1Ex0qgm51n&vprv=1&svpuc=1&mime=video%2Fmp4&ns=7OiAnAOK5sntfO9VmUQH6OgQ&rqh=1&cnr=14&ratebypass=yes&dur=1472.191&lmt=1716115985716862&mt=1716324302&fvip=1&c=WEB&sefc=1&txp=5532434&n=Ziek2DxdbyBy8w&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIgCFT9MqGvjH8gb_dTlvN4nyR75ipW6i9M8GZnEuHXcF0CIQCiZVPRIOFAQwc10MiQKM_wYPWrxaYrzOTamrsPK4xv_g%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRAIgdWEnZ-DI0btIDWRAB1J03ZtLHc51Gnk8lIeIHhfRQ8ACIHjXER1ZoirJLrR1W1VxGGg5gzVk3qwrBsbsEVjWzCXS'

response = requests.get(url,stream=True)

with open('/Users/s.atayi/Desktop/projects/ytdownloader/videooo.mp4', 'wb') as file:
    for c in response.iter_content(chunk_size = 8192):
        file.write(c)

print("downloaded succesfully")


