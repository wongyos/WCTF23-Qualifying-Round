import hashlib
n = int(input('Enter n: '))
flagy = 1
for i in range(1, n + 1):
    flagy *= i
    flagy += 1
flagy = flagy + 2023
flagy = hashlib.md5(str(flagy).encode()).hexdigest()
if flagy == '7546e106b9b1435611fd192c828dd83b':
    flag = hashlib.md5(str(n ** 23 + eval('0x' + flagy)).encode()).hexdigest()
    print('WCTF23{' + flag + '}')
else:
    print('WCTF23{f4k3_f!@g}')
