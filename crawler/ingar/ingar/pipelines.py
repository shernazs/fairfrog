# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import sqlite3 as sqlite
import re

class IngarPipeline(object):
    def __init__(self):
        self.setupDBCon()
        self.createAndCheckTables()

    def __del__(self):
        self.closeDB()

    def setupDBCon(self):
        self.con = sqlite.connect('../../../webshop/db.sqlite3')
        self.cursor = self.con.cursor()

    def closeDB(self):
        self.con.close()

    def createAndCheckTables(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS crawled_products \
	    (id INTEGER PRIMARY KEY, webshop VARCHAR(20), title VARCHAR(2000), url VARCHAR(100), img VARCHAR(2000), price DOUBLE, sizes TEXT, tags TEXT)')

        self.cursor.execute("delete from crawled_products where webshop='ingar'")

    def storeInDb(self, item):
        item_str = item.get('title','')
        self.cursor.execute("select * from crawled_products where url=?", [item.get('url','')])
        result = self.cursor.fetchone()
        if result:
            log.msg("Item already in database: %s" % item, level=log.DEBUG)
        else:
            self.cursor.execute(
                "insert into crawled_products (webshop, title, url, img, price, sizes, tags) values (?, ?, ?, ?, ? ,?, ?)",
                    ( 'ingar', item.get('title', ''), item.get('url',''), item.get('img',''), item.get('price',''),
                     item.get('sizes',''), item.get('tags','')
                     ))

            self.con.commit()

            log.msg("Item stored : " % item, level=log.DEBUG)

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item



