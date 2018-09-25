#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from connect import connect_production
from model.repository import insert
from model.entities import User

parser = ArgumentParser("Создание пользователя")
parser.add_argument("-n", "--name", required=True)
parser.add_argument("--min", dest="min_", default=0)
parser.add_argument("--max", dest="max_", required=True)
parser.add_argument("-c", "--current", help="Current money amount", default=0)

args = parser.parse_args()

conn = connect_production()
user = User(
    name=args.name,
    min_=args.min_,
    max_=args.max_,
    current=args.current
)
insert(conn, user)
conn.commit()
