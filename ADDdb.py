
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
(1, "孫敏德", "su-min-de.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(2, "陳弘軒", "chen_hong.jpg", "副教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(3, "范國清", "范國清.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(4, "何錦文", "he-jin-wun.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(5, "陳國棟", "chen-guo-dong.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(6, "洪炯宗", "洪炯宗教授.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(7, "蘇木春", "su mu chun.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(8, "周立德", "jhou-li-de.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(9, "吳曉光", "wu-hsiao-kuang.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(10, "楊鎮華", "楊鎮華教授.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(11, "梁德容", "liang-de-rong.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(12, "江振瑞", "JiangPhoto2.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(13, "施國琛", "施國琛.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(14, "張嘉惠", "張嘉惠.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(15, "張貴雲", "jhang-guei-yun.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(16, "許富皓", "許富皓.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(17, "蔡宗翰", "cai-zong-han.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(18, "蘇柏齊", "蘇柏齊.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(19, "鄭旭詠", "jheng-syu-yong.bmp", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(20, "王家慶", "王家慶老師.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(21, "陳慶瀚", "陳慶瀚.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(22, "葉士青", "葉士青教授.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(23, "劉晨鐘", "劉晨鐘教授.png", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(24, "鄭永斌", "jheng-yong-bin.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(25, "王尉任", "wang-wei-ren.jpg", "教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(26, "莊永裕", "莊永裕老師.jpg", "副教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(27, "陳增益", "陳增益助理教授.jpg", "副教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(28, "蔡孟峰", "cai-meng-fong.png", "助理教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(29, "楊?琮", "楊?琮老師.jpg", "助理教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(30, "林家瑜", "林家瑜老師.jpeg", "助理教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)}),
(31, "鍾佳儒", "鍾佳儒.jpg", "助理教授",{rd(100,999)} , {rd(0,1)}, {rd(1,99)})
"""

cursor.execute(insert_table_sql)
conn.commit()
conn.close()



# %%
