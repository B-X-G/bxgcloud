# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import subprocess
import os

requirements_path = '{}/requirements.txt'.format(os.getcwd())


def install_package(package_name):
    """
    安装python包规则：
        1. 检查系统是否已安装该包
        2. 如果系统已安装该包，则检查已装的版本号与 “requirements.txt” 中对应的版本号
        3. 如果系统已安装该包并 “requirements.txt” 已记录该包名称及版本号，但已装的版本号与 “requirements.txt” 中对应的版本号不一致，则按照 “requirements.txt” 中重新装包
        4. 如果系统已安装该包并 “requirements.txt” 未记录该包名称及版本号，则直接将包的名称及版本号记录到 “requirements.txt” 中
        5. 如果系统未安装该包并 “requirements.txt” 已记录该包名称及版本号，则根据 “requirements.txt” 的记录安装包
        6. 如果系统未安装该包并 “requirements.txt” 未记录该包名称及版本号，则安装指定版本包（未指定版本则默认为最新包）并将包的名称和版本号记录到 “requirements.txt” 中
    """
    package_name_term = package_name if '==' in package_name else '{}=='.format(package_name)
    exist_package_name_and_version_in_env = subprocess.Popen('sudo pip freeze |grep -i {}'.format(package_name_term), stdout=subprocess.PIPE, shell=True).communicate()[0]
    with open(requirements_path, 'a+') as r:
        lines = [line.split('\n')[0] for line in r.readlines()]
        exist_package_name_and_version_list = [line for line in lines if line.lower().startswith(package_name_term.lower())]
        exist_package_name_and_version = exist_package_name_and_version_list[0].strip() if exist_package_name_and_version_list else None
        if exist_package_name_and_version:  # requirements.txt中含有该安装包
            if exist_package_name_and_version.strip() == exist_package_name_and_version_in_env.strip():  # 本地包名和版本 与 requirements.txt 相同
                print('you already install this package')
            else:
                os.system('sudo pip install {}'.format(exist_package_name_and_version))  # 本地包名和版本 与 requirements.txt 不一致，以requirements.txt为准 并安装
                print('successfully change the package version by requirements.txt')
        else: # requirements.txt中不含该安装包
            if exist_package_name_and_version_in_env: # 如果本地已经安装该安装包，将该包和其版本写入requirements.txt中
                r.write(exist_package_name_and_version_in_env)
                print('successfully record package name and version in requirements.txt')
            else: # 否则本地未安装该安装包， 进行安装， 并将包和其版本号写入requirements.txt中
                new_package_name_and_version = subprocess.Popen('sudo pip install {}; sudo pip freeze |grep {}'.format(package_name, package_name_term), stdout=subprocess.PIPE, shell=True).communicate()[0].split('\n')[4]
                r.write(new_package_name_and_version)
                print('successfully install {}'.format(new_package_name_and_version))
