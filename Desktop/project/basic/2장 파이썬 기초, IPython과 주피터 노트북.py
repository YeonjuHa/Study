# 바이트와 유니코드
val = "español"
val

val_utf8 = val.encode('utf-8')
val_utf8
type(val_utf8)

val_utf8.decode("utf-8")

val.encode("latin1")
val.encode("utf-16")
val.encode("utf-16le")


# 불리언
True and True
False or True

int(False)
int(True)

a = True
b = False
not a
not b

# 형 변환
s = "3.14159"
fval = float(s)
s, fval
type(fval)
int(fval)
bool(fval)
bool(0)


# None
a = None
a is None
b = 5
b is not None


def add_maybe_mutiply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c
    return result

add_maybe_mutiply(10, 20)
add_maybe_mutiply(10, 20, 30)


# 날짜와 시간
from datetime import datetime, date, time
dt = datetime(2023, 11, 1, 15, 40, 10)
dt.day
dt.minute
dt.date()
dt.time()

dt.strftime("%Y-%m-%d %H:%M")
datetime.strptime("20231101", "%Y%m%d")

dt_hour = dt.replace(minute=0, second=0)
dt_hour
dt


dt2 = datetime(2023, 11, 1, 17, 40)
delta = dt2 - dt
delta
type(delta)
dt + delta


# 제어 흐름
# if, elif, else
x = -5
if x < 0:
    print("It's negative")
elif x == 0:
    print("Equal to zero")
elif 0 < x < 5:
    print("Positive but smaller than 5")
else:
    print("Positive but larger than or equal to 5")


a = 5; b = 7
c = 8; d = 4
if a < b or c > d:
    print("Made it")

4 > 3 > 2 > 1

# for 문
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value


for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))


# while 문
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2


# pass
if x < 0:
    print("negative!")
elif x == 0:
    # TODO: 여기에 내용 추가
    pass
else:
    print("positive!")


# range
range(10)
list(range(10))
list(range(0, 20, 2))
list(range(5, 0, -1))


seq = [1, 2, 3, 4]
for i in range(len(seq)):
    print(f"element {i}: {seq[i]}")

total = 0
for i in range(100_000):
    # %는 나머지 연산자다.
    if i % 3 == 0 or i % 5 == 0:
total += i

print(total)
