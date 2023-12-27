import random
import time
num = int(time.time()) // 2023
random.seed(num)
flag = list(input('Flag: '))
for i in range(50):
    x = random.randint(0, len(flag) - 1)
    y = random.randint(0, len(flag) - 1)
    flag[x], flag[y] = flag[y], flag[x]
    x = random.randint(0, len(flag) - 1)
    y = random.randint(0, len(flag) - 1)
    flag[x], flag[y] = flag[y], flag[x]
shuff = ''.join(flag)
if shuff == 'CT{619e07bec9}98b1c26633WeF51b576641c497':
    print('Congratulations! it is the flag.')
else:
    print('Sorry! it is not the flag.')
