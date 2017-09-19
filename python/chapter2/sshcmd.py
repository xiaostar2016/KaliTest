#!/usr/bin/env python
# coding=utf-8

import threading
import paramiko
import subprocess


def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # paramiko支持用密钥认证代，实际环境推荐使用密钥认证，这里设置账号和密码认证
    # client.load_host_keys('/home/justin/.ssh/known_hosts')

    # 设置自动添加和保存目标SSH服务器的SSH密钥
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)  # 连接
    ssh_session = client.get_transport().open_session()  # 打开会话
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return


# 调用函数，以用户pi机器密码连接自己的树莓派，并执行ｉｄ这个命令
ssh_command('210.12.221.154', 'pi', 'raspberry', 'id')
