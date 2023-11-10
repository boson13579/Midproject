
#%% create table
import sqlite3
from random import randint as rd

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS "cart" (
	"image"	text,
	"name"	text,
	"qty"	integer,
	"price"	integer,
	"subtotal"	integer,
	"id"	INTEGER,
	"uid"	text
)"""
cursor.execute(create_table_sql)

create_table_sql = """
CREATE TABLE IF NOT EXISTS "users" (
	"id"	SERIAL NOT NULL,
	"username"	text NOT NULL,
	"password"	text NOT NULL,
	"fname"	text,
	"lname"	text,
	"email"	text,
	PRIMARY KEY("id")
)
"""
cursor.execute(create_table_sql)

create_table_sql = """CREATE TABLE IF NOT EXISTS "professors" (
	"id"	SERIAL NOT NULL,
	"name"	text,
	"image"	text,
    "title" text,
	"price"	integer,
	"onsale"	integer,
	"onsaleprice"  integer,
	PRIMARY KEY("id")
)
"""
cursor.execute(create_table_sql)

create_table_sql = """CREATE TABLE IF NOT EXISTS "purchases" (
	"uid"	text,
	"name"	text,
	"image"	text,
	"quantity"	integer,
	"id"	INTEGER,
	"date"	date NOT NULL DEFAULT CURRENT_DATE
)"""

cursor.execute(create_table_sql)

insert_table_sql = f""" insert into professors values
(1, "�]�Ӽw", "su-min-de.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(2, "�����a", "chen_hong.jpg", "�Ʊб�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(3, "�S��M", "�S��M.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(4, "���A��", "he-jin-wun.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(5, "�����", "chen-guo-dong.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(6, "�x���v", "�x���v�б�.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(7, "Ĭ��K", "su mu chun.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(8, "�P�߼w", "jhou-li-de.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(9, "�d���", "wu-hsiao-kuang.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(10, "�����", "����رб�.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(11, "��w�e", "liang-de-rong.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(12, "������", "JiangPhoto2.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(13, "�I��`", "�I��`.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(14, "�i�Ŵf", "�i�Ŵf.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(15, "�i�Q��", "jhang-guei-yun.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(16, "�\�I�q", "�\�I�q.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(17, "���v��", "cai-zong-han.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(18, "Ĭ�f��", "Ĭ�f��.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(19, "�G����", "jheng-syu-yong.bmp", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(20, "���a�y", "���a�y�Ѯv.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(21, "���y�v", "���y�v.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(22, "���h�C", "���h�C�б�.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(23, "�B����", "�B�����б�.png", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(24, "�G���y", "jheng-yong-bin.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(25, "���L��", "wang-wei-ren.jpg", "�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(26, "���ø�", "���øΦѮv.jpg", "�Ʊб�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(27, "���W�q", "���W�q�U�z�б�.jpg", "�Ʊб�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(28, "���s�p", "cai-meng-fong.png", "�U�z�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(29, "��?�z", "��?�z�Ѯv.jpg", "�U�z�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(30, "�L�a��", "�L�a��Ѯv.jpeg", "�U�z�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(31, "��ξ�", "��ξ�.jpg", "�U�z�б�",{rd(100,999)} , {rd(0,1)}, {rd(1,99)})
"""

cursor.execute(insert_table_sql)
conn.commit()
conn.close()



# %%
