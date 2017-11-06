##########################################################
##
## File: BuyerAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for buyer
## table. This class handles all the SQL queries executed
## for maintaining the buyer table
##
##########################################################

# Module Import #
import DataBaseDriver
from constants import *
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BuyerAPI
## Description: This class is the database driver for Buyer
##
class BuyerAPI(DataBaseDriver.DataBaseDriver):
    buyerTablename = BUYER_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BuyerAPI constructor")
        DataBaseDriver.DataBaseDriver.__init__(self)

    ##
    ## Name: createBuyer
    ## Description: This function creates a new buyer
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if buyer is created
    ##
    def createBuyer(self, buyer):
        self.logger.info("IN - BuyerAPI createBuyer method")
        if not self.getBuyerInfo(buyer['buyer_id']).empty:
            self.logger.info("Buyer already exists!")
            return False
        query = "INSERT INTO " + BuyerAPI.buyerTablename + " (buyer_id, first_name, last_name, location, skills) VALUES (%s, %s, %s, %s, %s) "
        params = (buyer['buyer_id'], buyer['first_name'],buyer['last_name'] , buyer['location'], buyer['skills'])
        self.logger.debug("Query: " + query)
        self.logger.debug("Params: %s, %s, %s, %s, %s",
                          buyer['buyer_id'], buyer['first_name'], buyer['last_name'], buyer['location'], buyer['skills'])
        return self.runInsertQuery(query, params)

    ##
    ## Name: getBuyerInfo
    ## Description: This function returns buyer's
    ## info from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: Dataframe containing buyer's info
    ##
    def getBuyerInfo(self, buyer_id):
        self.logger.info("IN - BuyerAPI getBuyerInfo method")
        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM "\
                + BuyerAPI.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllBuyers
    ## Description: This function returns info
    ## of all the buyers in the system
    ##
    ## Parameters: None
    ##
    ## Returns: dataframe with all the buyers' info
    ##
    def getAllBuyers(self):
        self.logger.info("IN - BuyerAPI getAllBuyers method")
        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM " \
                + BuyerAPI.buyerTablename
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getBuyerFirstName
    ## Description: This function returns first_name
    ## of the buyer from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: returns buyer's first_name
    ##
    def getBuyerFirstName(self, buyer_id):
        self.logger.info("IN - BuyerAPI getBuyerFirstName method")
        query = "SELECT first_name FROM " + BuyerAPI.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).first_name[0]

    ##
    ## Name: setBuyerFirstName
    ## Description: This function updates first name
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, first_name
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerFirstName(self, buyer_id, first_name):
        self.logger.info("IN - BuyerAPI setBuyerFirstName method")
        query = "UPDATE " + BuyerAPI.buyerTablename + " SET first_name = '" + first_name + "' WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getBuyerLastName
    ## Description: This function returns last_name
    ## of the buyer from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: returns buyer's last_name
    ##
    def getBuyerLastName(self, buyer_id):
        self.logger.info("IN - BuyerAPI getBuyerLastName method")
        query = "SELECT last_name FROM " + BuyerAPI.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).last_name[0]

    ##
    ## Name: setBuyerLastName
    ## Description: This function updates last_name
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, last_name
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerLastName(self, buyer_id, last_name):
        self.logger.info("IN - BuyerAPI setBuyerLastName method")
        query = "UPDATE " + BuyerAPI.buyerTablename + " SET last_name = '" + last_name + "' WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getBuyerLocation
    ## Description: This function returns location
    ## of the buyer from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: returns buyer's location
    ##
    def getBuyerLocation(self, buyer_id):
        self.logger.info("IN - BuyerAPI getBuyerLocation method")
        query = "SELECT location FROM " + BuyerAPI.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).location[0]

    ##
    ## Name: setBuyerLocation
    ## Description: This function updates location
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, location
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerLocation(self, buyer_id, location):
        self.logger.info("IN - BuyerAPI setBuyerLocation method")
        query = "UPDATE " + BuyerAPI.buyerTablename + " SET location = '" + location + "' WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getBuyerSkills
    ## Description: This function returns skills
    ## of the buyer from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: returns buyer's skills
    ##
    def getBuyerSkills(self, buyer_id):
        self.logger.info("IN - BuyerAPI getBuyerSkills method")
        query = "SELECT skills FROM " + BuyerAPI.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).skills[0]

    ##
    ## Name: setBuyerSkills
    ## Description: This function updates skills
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, skills
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerSkills(self, buyer_id, skills):
        self.logger.info("IN - BuyerAPI setBuyerSkills method")
        query = "UPDATE " + BuyerAPI.buyerTablename + " SET skills = '" + skills + "' WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: load
    ## Description: This function loads the buyer info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        self.logger.info("IN - BuyerAPI load method")
        check = True
        for index, row in df.iterrows():
            buyer_dict = {'buyer_id': row['buyer_id'],'first_name' : row['first_name'], 'last_name' : row['last_name'],
                    'location': row['location'], 'skills' : row['skills']}
            if not self.createBuyer(buyer_dict):
                self.logger.error("Could not load data in Buyer table: " + row)
                check = False
            self.logger.debug("Loaded data in Buyer table: " + row)
        return check
