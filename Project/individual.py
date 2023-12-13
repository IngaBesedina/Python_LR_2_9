#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_par(par_str):
    """Проверка правильности расстановки скобок"""
    if len(par_str) == 0:
        return True
    else:
        left = par_str[0]
        right = par_str[-1]
        kf = "([".find(left)
        if kf == -1:
            return False
        if right == ")]"[kf]:
            return check_par(par_str[1:len(par_str) - 1])
        else:
            return False


def main():
    par = input("Введите строку: ")

    if check_par(par):
        print("Скобки расставлены правильно")
    else:
        print("Скобки расставлены не правильно")


if __name__ == '__main__':
    main()
