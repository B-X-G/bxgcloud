# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import subprocess
import os


def install_package(name):
    os.system('sudo pip install {}'.format(name))
    result = subprocess.Popen('sudo pip freeze', stdout=subprocess.PIPE, shell=True)
    output = result.communicate()[0]
    package_names = output.split('\n')
    for package_name in package_names:
        if package_name.lower().startswith(name.lower()):
            with open('{}/requirements.txt'.format(os.getcwd()), 'a+') as r:
                all_packages = set(readline.split('\n')[0] for readline in r.readlines())
                if package_name in all_packages:
                    print ('the package is exist')
                else:
                    r.write(package_name)
                break
        else:
            continue
