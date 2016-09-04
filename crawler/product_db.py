import sqlite3 as sqlite
import glob
import json 
from datetime import datetime
import logging
import os
from random import shuffle

root = os.getenv('HOME', '/home/fairfrog')


def set_log():
	logfile = root + '/Logs/crawler_DB_' + datetime.today().strftime('%y-%m-%d') + '.log'
	logger = logging.getLogger('database_insert')
	handler = logging.FileHandler(logfile, mode='a')
	formatter = logging.Formatter('%(asctime)s\t[%(levelname)s]\t%(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler) 
	logger.setLevel(logging.DEBUG)
	return logger


def setupDBCon():
	con = sqlite.connect(root + '/Database/products.db')
	cursor = con.cursor()
	return con, cursor


def closeDB(con):
	con.close()


def createAndCheckTables(cursor):
	#title url description webshop_name product_cat style image price discount_price sizes brand
	cursor.execute('CREATE TABLE IF NOT EXISTS Products \
	(Id INTEGER PRIMARY KEY, Webshop VARCHAR(50), Title VARCHAR(100), Description TEXT, Url VARCHAR(200), \
	Image VARCHAR(2000), Logo VARCHAR(2000), Webshop_Url VARCHAR(100), Style VARCHAR(3), Brand VARCHAR(100), Price DOUBLE, Discount_price DOUBLE,\
	Sizes TEXT, Categories TEXT, Hashtags TEXT)')
	cursor.execute('CREATE TABLE IF NOT EXISTS Popular_Products (Id INTEGER PRIMARY KEY, Product_Id VARCHAR(5), FOREIGN KEY(Product_Id) REFERENCES Products(Id))')
	cursor.execute('CREATE TABLE IF NOT EXISTS Advertorial_Products (Id INTEGER PRIMARY KEY, Product_Id VARCHAR(5), FOREIGN KEY(Product_Id) REFERENCES Products(Id))')


def storeInDb(logger, con, cursor):
	product_files = glob.glob('./*/products.json')
	data = []

	for product_file in product_files:
		try:
			with open(product_file) as data_file:
				data.extend(json.load(data_file))
		except:
			continue

	shuffle(data)
	try:
		result = set(cursor.execute("select Webshop, Title, Url from Products"))
	except:
		result = set()
		pass
	identifier_data = set(map(lambda x: (x.get('webshop_name'), x.get('title'), x.get('url')), data))
	data_DB = result & identifier_data
	remove_DB = result - identifier_data

	for product in remove_DB:
		cursor.execute('DELETE FROM Products WHERE Webshop = ? AND Title = ? AND Url = ?',
			(product[0], product[1], product[2]))

	for item in data:
		if item.get('discount_price') < item.get('price') and 'sale' not in item.get('product_cat'):
		    item['product_cat'] += '|sale'
		if ' collectie' in item.get('product_cat'):
		    item['product_cat'] = item['product_cat'].replace(' collectie', '')

		if (item.get('webshop_name'), item.get('title'), item.get('url')) in data_DB: 
			cursor.execute('UPDATE Products SET Price = ?, Discount_price = ?, Categories = ?, Hashtags = ? \
				WHERE Webshop = ? AND Title = ? AND Url = ?', 
				(item.get('price',''), item.get('discount_price',''), item.get('product_cat', ''), item.get('hashtags',''), 
				item.get('webshop_name', ''), item.get('title', ''), item.get('url','')))
			logger.info("Product price and discount price update for item already in Database: " + 
				'\t\t'.join((item.get('webshop_name'), item.get('title'), item.get('url'))))
		else:
			cursor.execute("Insert Into Products ( Webshop, Title, Description, Url, Image, Logo, Webshop_Url, Style, \
				Brand, Price, Discount_price, Sizes, Categories, Hashtags) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
				( item.get('webshop_name', ''), item.get('title', ''), item.get('description', ''), 
				item.get('url',''), item.get('image',''), item.get('webshop_logo',''), item.get('webshop_url',''),
				item.get('style',''), item.get('brand',''), item.get('price',''), item.get('discount_price',''), 
				item.get('sizes',''), item.get('product_cat',''), item.get('hashtags','')))
			logger.debug("Item stored in Database: " + '\t\t'.join((item.get('webshop_name'), 
				item.get('title'), item.get('url'))))

	con.commit()


def main():
	logger = set_log()
	logger.info("Setting up Database connection...")
	connection, cursor = setupDBCon()
	try:
		createAndCheckTables(cursor)
		storeInDb(logger, connection, cursor)
	except Exception as e:
		logger.error(e)
	finally:
		closeDB(connection)


if __name__ == "__main__":
	main()
