#!/home/fairfrog/.conda/envs/kush_checkout/bin/python
import sqlite3 as sqlite
import glob
import json 
from datetime import datetime
import logging

def set_log():
	logfile = '/home/fairfrog/Logs/crawler_DB_' + datetime.today().strftime('%y-%m-%d') + '.log'
	logger = logging.getLogger('database_insert')
	handler = logging.FileHandler(logfile, mode='a')
	formatter = logging.Formatter('%(asctime)s\t[%(levelname)s]\t%(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler) 
	logger.setLevel(logging.DEBUG)
	return logger


def setupDBCon():
	con = sqlite.connect('/home/fairfrog/Database/products.db')
	cursor = con.cursor()
        return con, cursor


def closeDB(con):
	con.close()


def createAndCheckTables(cursor):
	#title url description webshop_name product_cat style image price discount_price sizes brand
	cursor.execute('CREATE TABLE IF NOT EXISTS Products \
		(id INTEGER PRIMARY KEY, Webshop VARCHAR(50), Title VARCHAR(100), Description TEXT, Url VARCHAR(2000), \
		Image VARCHAR(2000), Logo VARCHAR(2000), Style VARCHAR(3), Brand VARCHAR(100), Price DOUBLE, Discount_price DOUBLE,\
		Sizes TEXT, Categories TEXT, Tags TEXT)')
	cursor.execute('CREATE TABLE IF NOT EXISTS Popular_Products (id INTEGER PRIMARY KEY, Product_Id VARCHAR(5))')


def storeInDb(logger, con, cursor):
	product_files = glob.glob('/home/fairfrog/FairFrog/Code/fairfrog/crawler/*/products.json')
	data = []
	for product_file in product_files:
		with open(product_file) as data_file:
			data.extend(json.load(data_file))
	result = cursor.execute("select Webshop, Title, Url from Products")
	test_data = map(lambda x: (x.get('webshop_name'), x.get('title'), x.get('url')), data)	
	data_DB = filter(lambda x: x in test_data, result)
	for item in data:
		if (item.get('webshop_name'), item.get('title'), item.get('url')) in data_DB: 
			logger.info("Item already in Database: " + '\t\t'.join((item.get('webshop_name'), 
				item.get('title'), item.get('url'))))
		else:
			cursor.execute("Insert Into Products ( Webshop, Title, Description, Url, Image, Logo, Style, \
				Brand, Price, Discount_price, Sizes, Categories, Tags) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
				( item.get('webshop_name', ''), item.get('title', ''), item.get('description', ''), 
				item.get('url',''), item.get('image',''), item.get('webshop_logo',''),item.get('style',''), 
				item.get('brand',''), item.get('price',''), item.get('discount_price',''), item.get('sizes',''), 
				item.get('product_cat',''), item.get('tags','')))
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
