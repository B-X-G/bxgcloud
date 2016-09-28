# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
import sys
from env import install_package


def run():
    scripts = {'install'}
    argv = sys.argv
    if len(argv) < 2:
        print('please input script argument')
        exit(-1)
    elif argv[1] not in scripts:
        print('not support this script: {}'.format(argv[1]))
        exit(-1)
    if argv[1] == 'install':
        install_package(argv[2])
    else:
        exit(-1)


if __name__ == '__main__':
    run()
