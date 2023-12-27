x = input('Message: ')
y = x[1:] + x[0]
code = []
for i in range(len(x)):
    code.append(ord(x[i]) ^ ord(y[i]))
check = [54, 26, 85, 67, 2, 15, 78, 68, 11, 79, 73, 29, 88, 12, 72, 13, 23, 23, 69, 73, 26, 83, 84, 28, 13, 69, 70, 10, 13, 6, 71, 26, 26, 119, 20, 23, 18, 116, 1, 72, 77, 14, 14, 87, 85, 0, 81, 0, 83, 2, 12, 93, 85, 6, 82, 5, 5, 87, 85, 5, 1, 81, 86, 1, 85, 0, 3, 83, 80, 9, 92, 2, 27, 36]
if code == check:
    print('Valid Message')
else:
    print('Invalid Message')
