import sys


def fizzbuzz(n):
    for i in range(n+1):
        if i%5==0 and i%3==0:print('fizzbuzz')
        elif i%5==0: print('buzz')
        elif i%3==0: print('fizz')
        else: print(i)

if __name__ == '__main__':
    fizzbuzz(int(sys.argv[1]))