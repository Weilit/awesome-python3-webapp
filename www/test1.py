#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import asyncio
import orm
from models import User, Blog, Comment
# from webapp.www.models import Blog
# from webapp.www.models import Comment
from datetime import datetime


def gen_rand_string():
    unique_id = datetime.now().strftime('%Y%m%d%H%M%S')
    test_name = 'test' + unique_id
    test_email = test_name + '@example.com'
    test_passwd = unique_id
    return test_name, test_email, test_passwd


async def test(in_loop):
    await orm.create_pool(loop=in_loop, user='root', password='root', db='awesome')
    test_name, test_email, test_passwd = gen_rand_string()
    u = User(name=test_name, email=test_email, passwd=test_passwd, image='about:blank')
    print(u)
    await u.save()
    print('tested ok...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)

'''
{'name': 'test20160909003306', 'image': 'about:blank', 'email': 'test20160909003306@example.com', 'passwd': '20160909003306'}
tested ok...
'''