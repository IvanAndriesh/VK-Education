s = input()
if 'a' in s or 'o' in s:
    if 'i' not in s and 'e' not in s:
        print('True')
    else:
        print('False')
else:
    print('False')