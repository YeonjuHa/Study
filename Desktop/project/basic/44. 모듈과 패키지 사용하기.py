# import로 모듈 가져오기
import math
math.pi

import math
math.sqrt(4.0)
math.sqrt(2.0)


# import as로 모듈 이름 지정하기
import math as m
m.sqrt(4.0)
m.sqrt(2.0)


# from import로 모듈의 일부만 가져오기
from math import pi
pi

from math import sqrt
sqrt(4.0)
sqrt(2.0)


from math import pi, sqrt
pi
sqrt(4.0)
sqrt(2.0)


from math import *
pi
sqrt(4.0)
sqrt(2.0)


# 모듈의 일부를 가져온 뒤 이름 지정하기
from math import sqrt as s
s(4.0)
s(2.0)

from math import pi as p, sqrt as s
p
s(4.0)
s(2.0)

# 모듈 해제
import math
del math
math.pi

# 다시 가져오기
import importlib
import math
importlib.reload(math)
math.pi


# import로 패키지 가져오기
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
response.status


# 패키지 모듈 이름 지정하기
import urllib.request as r
response = r.urlopen('http://www.google.co.kr')
response.status


# 패키지의 모듈에서 일부만 가져오기
from urllib.request import Request, urlopen
req = Request('http://www.google.co.kr')
response = urlopen(req)
response.status

from urllib.request import *
req = Request('http://www.google.co.kr')
response = urlopen(req)
response.status

# 패키지의 모듈의 일부를 가져온 뒤 이름 지정하기
from urllib.request import Request as r, urlopen as u
req = r('http://www.google.co.kr')
response = u(req)
response.status

import requests
r = requests.get('http://www.google.co.kr')
r.status_code