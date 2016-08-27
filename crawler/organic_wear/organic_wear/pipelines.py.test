# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from sqlite3 import connect, cursor

class IngarPipeline(object):
 
	webshop_url = "http://organicwear.nl/shop/"
	def __init__(self):
		self.setupDBCon()
		self.createTables()


	def __del__(self):
		self.closeDB()


	def setupDBCon(self):
		self.con = connect('/home/fairfrog/Database/products.db')
		self.cursor = self.con.cursor()


	def closeDB(self):
		self.con.close()


	def createTables(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS WebShops \
		(id INTEGER PRIMARY KEY, Name TEXT, url VARCHAR(100), FFattributes TEXT, Certification INTEGER, \
		Country VARCHAR(100), Postcode VARCHAR(8), Address TEXT);')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Categories \
		(id INTEGER PRIMARY KEY, Name TEXT, Description TEXT)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Category_Mapping \
		(id INTEGER PRIMARY KEY, Category_Id INTEGER, Product_Id INTEGER, Webshop_Id INTEGER)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Related_Products \
		(id INTEGER PRIMARY KEY, Product_Id INTEGER, Webshop_Id INTEGER, Related_product_Id INTEGER)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Colors \
		(id INTEGER PRIMARY KEY, Name TEXT, Alias TEXT)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Color_Mapping \
		(id INTEGER PRIMARY KEY, Color_Id INTEGER, Product_Id INTEGER, Webshop_Id INTEGER)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Sizes \
		(id INTEGER PRIMARY KEY, Name TEXT, Alias TEXT)')
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Size_Mapping \
		(id INTEGER PRIMARY KEY, Size_Id INTEGER, Product_Id INTEGER, Webshop_Id INTEGER)')

		self.cursor.execute("select url from WebShops where Name = 'Organic Wear'")
                result = self.cursor.fetchall()
                if webshop_url in result:
			log.msg("Organic Wear (%s) is already in database" % webshop_url, level=log.DEBUG)
		else:
			self.cursor.execute("Insert Into WebShops (Name, url, Country, Postcode, Address) Values (?,?,?,?,?)", ("Organic Wear", "http://organicwear.nl/shop/", "Nederland", "9712JB", "Hofstraat 16C"))

		#product_title, description, webshop_name, product_cat, style, color, size, price, discount_price, url, images
		self.cursor.execute('CREATE TABLE IF NOT EXISTS Organic_Wear \
		(id INTEGER PRIMARY KEY, Name TEXT, url VARCHAR(100), Description TEXT, Webshop INTEGER, Category TEXT, Style VARCHAR(2), Colors TEXT, Price DOUBLE, Discount_Price DOUBLE, Sizes TEXT, Tags TEXT, Images TEXT)')


	def storeInDb(self, item):
		item_str = item.get('title','')
		result = self.cursor.fetchone()
		if result:
			log.msg("Item already in database: %s" % item, level=log.DEBUG)
		else:
			self.cursor.execute(
			"insert into organic_wear () values (?, ?, ?, ? ,?)",
			(item.get('title', ''), item.get('url',''), item.get('price',''),
			item.get('sizes',''), item.get('tags','')
			))
			self.con.commit()

		log.msg("Item stored : " % item, level=log.DEBUG)

	def process_item(self, item, spider):
		products = self.cursor.execute("select * from organic_wear")
		


		self.storeInDb(item)
		return item



