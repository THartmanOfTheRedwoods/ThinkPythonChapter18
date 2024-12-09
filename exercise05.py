#!/usr/bin/env python3

def fibonacci_OLD(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_OLD( n - 1 ) + fibonacci_OLD( n - 2 )


def fibonacci_v1(n):
    if n == 0 or n == 1:
        return n

    return fibonacci_v1( n - 1 ) + fibonacci_v1( n - 2 )

def fibonacci_v2(n):
    return n if n == 0 or n == 1 else fibonacci_v2( n - 1 ) + fibonacci_v2( n - 2 )

def main():
    num = 10
    print(f'OLD: {fibonacci_OLD(num)}, V1: {fibonacci_v1(num)}, V2: {fibonacci_v2(num)}')
    num = 1
    print(f'OLD: {fibonacci_OLD(num)}, V1: {fibonacci_v1(num)}, V2: {fibonacci_v2(num)}')

if __name__ == '__main__':
    main()