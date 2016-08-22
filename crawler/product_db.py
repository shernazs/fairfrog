import sqlite3 as sqlite
import glob
import json 
import logging
from datetime import datetime

"""
def set_logger():
	logfile = '/home/fairfrog/Logs/crawler_DB_' + datetime.today().strftime('%y-%m-%d') + '.log'
	logger = logging.getlogger('database_insert')
	handler = logging.filehandler(logfile, mode='a')
	formatter = logging.formatter('%(asctime)s\t[%(levelname)s]\t%(message)s')
	handler.setformatter(formatter)
	logger.addhandler(handler) 
	logger.setlevel(logging.debug)
	return logger
"""


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
		Image VARCHAR(2000), Style VARCHAR(3), Brand VARCHAR(100), Price DOUBLE, Discount_price DOUBLE, Sizes TEXT,\
		 Categories TEXT)')
	cursor.execute('CREATE TABLE IF NOT EXISTS Popular_Products (id INTEGER PRIMARY KEY, Product_Id VARCHAR(5))')


def storeInDb(con, cursor):
#	logger = set_logger()
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
			#logger.info("Item already in Database: " + '\t\t'.join((item.get('webshop_name'), 
			print("Item already in Database: " + '\t\t'.join((item.get('webshop_name'), 
				item.get('title'), item.get('url'))))
		else:
			cursor.execute("Insert Into Products ( Webshop, Title, Description, Url, Image, Style, \
				Brand, Price, Discount_price, Sizes, Categories) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
				( item.get('webshop_name', ''), item.get('title', ''), item.get('description', ''), 
				item.get('url',''), item.get('image',''), item.get('style',''), item.get('brand',''), 
				item.get('price',''), item.get('discount_price',''), item.get('sizes',''), 
				item.get('product_cat','')))
			#logger.debug("Item stored in Database: " + '\t\t'.join((item.get('webshop_name'), 
			print("Item stored in Database: " + '\t\t'.join((item.get('webshop_name'), 
				item.get('title'), item.get('url'))))

	con.commit()


def main():
	connection, cursor = setupDBCon()
	createAndCheckTables(cursor)
        storeInDb(connection, cursor)
	closeDB(connection)


if __name__ == "__main__":
	main()
