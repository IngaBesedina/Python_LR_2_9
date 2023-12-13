#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit as ti
from functools import lru_cache


def factorial(n):
    """Рекурсивное вычисление факториала"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    """Рекурсивное вычисление числа фибонначи"""
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def factorial_iter(n):
    """Вычисление факториала итеративно"""
    rez = 1
    while n > 1:
        rez *= n
        n -= 1

    return rez


def fib_iter(n):
    """Вычисление числа фибонначи итеративно"""
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1

    return a


@lru_cache
def factorial_lru(n):
    """
    Рекурсивное вычисление факториала
    Оптимизация с помощью lru_cache
    """
    if n == 0:
        return 1
    else:
        return n * factorial_lru(n - 1)


@lru_cache
def fib_lru(n):
    """
    Рекурсивное вычисление числа фибонначи
    Оптимизация с помощью lru_cache
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_lru(n - 2) + fib_lru(n - 1)


def timer(func, n):
    repeat = 30
    print(f'{func[1]} время работы: ', ti.timeit(lambda: func[0](n), number=repeat) / repeat)


def main():
    funcs = {
        factorial: "Рекурсивный факториал",
        factorial_iter: "Итеративный факториал",
        fib: "Рекурсивный фибонначи",
        fib_iter: "Итеративный фибонначи",
        factorial_lru: "Рекурсивный факториал c lru_cache",
        fib_lru: "Рекурсивный фибонначи c lru_cache"
    }

    n = 15
    for func in funcs.items():
        timer(func, n)


if __name__ == '__main__':
    main()
