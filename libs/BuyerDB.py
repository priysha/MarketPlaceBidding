##########################################################
##
## File: BuyerDB.py
## Author: Priysha Pradhan
## Description: This is a database access class for buyer
## table. This class handles all the SQL queries executed
## for maintaining the buyer table
##
##########################################################

# Module Import #
import DataBaseDriver
from constants import *
import datetime
import json
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BuyerDB
## Description: This class is the database driver for Buyer
##
class BuyerDB(DataBaseDriver.DataBaseDriver):
    buyerTablename = BUYER_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BuyerDB constructor")
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
        self.logger.info("IN - BuyerDB.createBuyer")
        if not self.getBuyerInfo(buyer['buyer_id']).empty:
            self.logger.info("Buyer already exists!")
            return False
        query = "INSERT INTO " + BuyerDB.buyerTablename + \
                " (buyer_id, first_name, last_name, location, skills, creation_time) " \
                "VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY " \
                "UPDATE first_name = %s, last_name = %s, location = %s, skills = %s"
        params = (buyer['buyer_id'], buyer['first_name'],buyer['last_name'] , buyer['location'], buyer['skills'],
                  buyer['first_name'], buyer['last_name'], buyer['location'], buyer['skills'])
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
        self.logger.info("IN - BuyerDB.getBuyerInfo")
        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM "\
                + BuyerDB.buyerTablename + " WHERE buyer_id = '" + buyer_id + "'"
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
        self.logger.info("IN - BuyerDB.getAllBuyers")
        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM " \
                + BuyerDB.buyerTablename
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: removeBuyer
    ## Description: This function removes buyer
    ## from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: Returns True if deleted else False
    ##
    def removeBuyer(self,buyer_id):
        self.logger.info("IN - BuyerDB.removeBuyer")
        query = "DELETE FROM " + BuyerDB.buyerTablename + " WHERE buyer_id='" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runDeleteQuery(query)

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
        self.logger.info("IN - BuyerDB load method")
        check = True
        for index, row in df.iterrows():
            buyer_dict = {'buyer_id': row['buyer_id'],'first_name' : row['first_name'], 'last_name' : row['last_name'],
                    'location': row['location'], 'skills' : row['skills'],'creation_time' :str(datetime.datetime.now())}
            if not self.createBuyer(buyer_dict):
                self.logger.error("Could not load data in Buyer table: " + row)
                check = False
            self.logger.debug("Loaded data in Buyer table: " + row)
        return check

    ##
    ## Name: jsonEncoder
    ## Description: This function converts the passed
    ## dataframe for Buyerdb class into json and
    ## checks the format of code sent
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: returns json data
    ##
    def jsonEncoder(self,input_df):
        try:
            # buyer_id, first_name, last_name, location, skills, creation_time
            column_list = input_df.columns.tolist()
            if 'buyer_id' not in column_list or 'first_name' not in column_list \
            or 'last_name' not in column_list or 'skills' not in column_list \
            or 'location' not in column_list or 'creation_time' not in column_list:
                return None

            output_json = input_df.to_json(orient='records')
            return output_json
        except Exception, e:
            self.logger.error("Cannot convert input dataframe to json: " + str(e))
            return None

    ##
    ## Name: jsonDecoder
    ## Description: This function converts passed json data
    ## for Buyerdb class nto dict and checks if the json
    ## has required fields
    ##
    ## Parameters: json
    ##
    ## Returns: Returns dict
    ##
    def jsonDecoder(self, input_json):
        try:
            output_dict = json.loads(input_json)[0]
            # the dict should have buyer_id, first_name, last_name, location, skills
            if not output_dict['buyer_id'] or not output_dict['first_name'] \
                or not output_dict['last_name']or not output_dict['location'] \
                    or not output_dict['skills']:
                return None
            else:
                return output_dict

        except IndexError, e:
            self.logger.error("Input data passed is not correct: " + str(e))
            return None

