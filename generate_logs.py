#coding=UTF-8

import random

url_paths = {
    "class/112.html",
    "class/131.html",
    "class/145.html",
    "class/163.html",
    "class/150.html",
    "class/246.html",
    "class/774.html",
    "class/130.html",
    "learn/821",
    "learn/888",
    "learn/907",
    "learn/845",
    "course/list",
}

ip_slices = [134,142,153,45,245,250,18,98,34,64,23,35,13,53,63,75,12,65]

def sample_url():
    return random.sample(url_paths,1)[0]

def sample_ip():
    slice = random.sample(ip_slices,4)
    return ".".join([str(item) for item in slice])

def generate_log(count = 10) :
    while count >= 1:
        query_log = "{url}\t{ip}".format(url=sample_url(),ip=sample_ip())
        print(query_log)
        count-=1



if __name__ == '__main__':
    generate_log(20)
