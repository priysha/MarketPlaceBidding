##########################################################
##
## File: SellerAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for seller
## table. This class handles all the SQL queries executed
## for maintaining the seller table
##
##########################################################

# Module Import #
import DataBaseDriver
from constants import *
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: SellerAPI
## Description: This class is the database driver for Seller
##
class SellerAPI(DataBaseDriver.DataBaseDriver):
    sellerTablename = SELLER_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - SellerAPI constructor")
        DataBaseDriver.DataBaseDriver.__init__(self)

    ##
    ## Name: createBuyer
    ## Description: This function creates a new buyer
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if buyer is created
    ##
    def createSeller(self, seller):
        self.logger.info("IN - SellerAPI createSeller method")
        if not self.getSellerInfo(seller['seller_id']).empty:
            self.logger.info("Seller already exists!")
            return False
        query = "INSERT INTO " + SellerAPI.sellerTablename + " (seller_id, first_name, last_name, location, job_title, company) " \
                                                              "VALUES (%s, %s, %s, %s, %s, %s) "
        params = (seller['seller_id'], seller['first_name'],seller['last_name'] , seller['location'], seller['job_title'],seller['company'])
        self.logger.debug("Query: " + query)
        self.logger.debug("Params: %s, %s, %s, %s, %s, %s",
                          seller['seller_id'], seller['first_name'], seller['last_name'], seller['location'],
                          seller['job_title'], seller['company'])
        return self.runInsertQuery(query, params)

    ##
    ## Name: getSellerInfo
    ## Description: This function returns info
    ## of a seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: Dataframe with seller info
    ##
    def getSellerInfo(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerInfo method")

        query = "SELECT seller_id, first_name, last_name, location,job_title, company, creation_time FROM "\
                + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllSellers
    ## Description: This function returns info
    ## of all the sellers in the db
    ##
    ## Parameters: None
    ##
    ## Returns: Dataframe with info of all sellers
    ##
    def getAllSellers(self):
        self.logger.info("IN - SellerAPI getAllSellers method")
        query = "SELECT seller_id, first_name, last_name, location,job_title, company, creation_time FROM " \
                + SellerAPI.sellerTablename
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: setSellerFirstName
    ## Description: This function returns first_name
    ## of the seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns first_name of the seller
    ##
    def getSellerFirstName(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerFirstName method")
        query = "SELECT first_name FROM " + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).first_name[0]

    ##
    ## Name: setSellerFirstName
    ## Description: This function updates first_name
    ## of the seller in the db
    ##
    ## Parameters: seller_id, first_name
    ##
    ## Returns: True if updated else false
    ##
    def setSellerFirstName(self, seller_id, first_name):
        self.logger.info("IN - SellerAPI setSellerFirstName method")
        query = "UPDATE " + SellerAPI.sellerTablename + " SET first_name = '" + first_name + "' WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getSellerLastName
    ## Description: This function returns last_name
    ## of the seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns last_name of the seller
    ##
    def getSellerLastName(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerLastName method")
        query = "SELECT last_name FROM " + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).last_name[0]

    ##
    ## Name: setSellerLastName
    ## Description: This function updates last_name
    ## of the seller in the db
    ##
    ## Parameters: seller_id, last_name
    ##
    ## Returns: True if updated else false
    ##
    def setSellerLastName(self, seller_id, last_name):
        self.logger.info("IN - SellerAPI setSellerLastName method")
        query = "UPDATE " + SellerAPI.sellerTablename + " SET last_name = '" + last_name + "' WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getSellerLocation
    ## Description: This function returns location
    ## of the seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns location of the selle
    ##
    def getSellerLocation(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerLocation method")
        query = "SELECT location FROM " + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).location[0]

    ##
    ## Name: setBuyerSkills
    ## Description: This function updates location
    ## of the seller in the db
    ##
    ## Parameters: seller_id, location
    ##
    ## Returns: True if updated else false
    ##
    def setSellerLocation(self, seller_id, location):
        self.logger.info("IN - SellerAPI setSellerLocation method")
        query = "UPDATE " + SellerAPI.sellerTablename + " SET location = '" + location + "' WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getSellerJobTitle
    ## Description: This function returns job_title
    ## of the seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns job_title of the selle
    ##
    def getSellerJobTitle(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerJobTitle method")
        query = "SELECT job_title FROM " + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).job_title[0]

    ##
    ## Name: setSellerJobTitle
    ## Description: This function updates job_title
    ## of the seller in the db
    ##
    ## Parameters: seller_id, job_title
    ##
    ## Returns: True if updated else false
    ##
    def setSellerJobTitle(self, seller_id, job_title):
        self.logger.info("IN - SellerAPI setSellerJobTitle method")
        query = "UPDATE " + SellerAPI.sellerTablename + " SET job_title = '" + job_title + "' WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getSellerCompany
    ## Description: This function returns company
    ## of the seller from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns company of the selle
    ##
    def getSellerCompany(self, seller_id):
        self.logger.info("IN - SellerAPI getSellerCompany method")
        query = "SELECT company FROM " + SellerAPI.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).company[0]

    ##
    ## Name: setSellerCompany
    ## Description: This function updates company
    ## of the seller in the db
    ##
    ## Parameters: seller_id, company
    ##
    ## Returns: True if updated else false
    ##
    def setSellerCompany(self, seller_id, company):
        self.logger.info("IN - SellerAPI setSellerCompany method")
        query = "UPDATE " + SellerAPI.sellerTablename + " SET company = '" + company + "' WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: load
    ## Description: This function loads the seller info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        self.logger.info("IN - SellerAPI load method")
        check = True
        for index, row in df.iterrows():
            seller_dict = {'seller_id' : row['seller_id'],'first_name' : row['first_name'], 'last_name' : row['last_name'],
                    'location': row['location'], 'job_title' : row['job_title'], 'company' : row['company']}
            if not self.createSeller(seller_dict):
                self.logger.error("Could not load data in Seller table: " + row)
                check = False
            self.logger.debug("Loaded data in Seller table: " + row)
        return check
