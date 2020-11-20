word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return word[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        return terbilang(n // 1_000) + ' thousand ' + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n in range (21,30):
        return 'twenty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (31,40):
        return 'thirty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (41,50):
        return 'forty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (51,60):
        return 'fifty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (61,70):
        return 'sixty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (71,80):
        return 'seventy-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (81,90):
        return 'eighty-' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n in range (91,100):
        return 'ninety-' + (terbilang(n % 10) if n % 10 != 0 else '')
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' tweleve'
        elif n == 13:
            return ' thirteen'
        elif n == 14:
            return ' forteen'
        elif n == 15:
            return ' fifteen'
        elif n == 16:
            return ' sixteen'
        elif n == 17:
            return ' seventeen'
        elif n == 18:
            return ' eighteen'
        elif n == 19:
            return ' nineteen'
        elif n == 20:
            return ' twenty'
        elif n == 30:
            return ' thirty'
        elif n == 40:
            return ' forty'
        elif n == 50:
            return ' fifty'
        elif n == 60:
            return ' sixty'
        elif n == 70:
            return ' seventy'
        elif n == 80:
            return ' eighty'
        elif n == 11:
            return ' ninety'
        else:
            return terbilang(n % 10) + ' belas'        


# test
import os
while True:
    os.system('cls')
    try:
        n = int(input('angka ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('data input anda tidak benar ...')
    os.system('pause')