##########################################################
##
## File: SellerDB.py
## Author: Priysha Pradhan
## Description: This is a database access class for seller
## table. This class handles all the SQL queries executed
## for maintaining the seller table
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
## Class: SellerDB
## Description: This class is the database driver for Seller
##
class SellerDB(DataBaseDriver.DataBaseDriver):
    sellerTablename = SELLER_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - SellerDB constructor")
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
        self.logger.info("IN - SellerDB.createSeller")
        if not self.getSellerInfo(seller['seller_id']).empty:
            self.logger.info("Seller already exists!")
            return False
        query = "INSERT INTO " + SellerDB.sellerTablename + \
                " (seller_id, first_name, last_name, location, job_title, company, creation_time) " \
                "VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY " \
                "UPDATE first_name = %s, last_name = %s, location = %s, job_title = %s, company = %s"
        params = (seller['seller_id'], seller['first_name'],seller['last_name'] , seller['location'], seller['job_title'],seller['company'],
                  seller['first_name'], seller['last_name'], seller['location'], seller['job_title'], seller['company'])
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
        self.logger.info("IN - SellerDB.getSellerInfo")

        query = "SELECT seller_id, first_name, last_name, location,job_title, company, creation_time FROM "\
                + SellerDB.sellerTablename + " WHERE seller_id = '" + seller_id + "'"
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
        self.logger.info("IN - SellerDB.getAllSellers")
        query = "SELECT seller_id, first_name, last_name, location,job_title, company, creation_time FROM " \
                + SellerDB.sellerTablename
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: removeSeller
    ## Description: This function removes seller
    ## from the db
    ##
    ## Parameters: seller_id
    ##
    ## Returns: Returns True if deleted else False
    ##
    def removeSeller(self,seller_id):
        self.logger.info("IN - BuyerDB.removeBuyer")
        query = "DELETE FROM " + SellerDB.sellerTablename + " WHERE seller_id='" + seller_id +"'"
        self.logger.debug("Query: " + query)
        return self.runDeleteQuery(query)


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
        self.logger.info("IN - SellerDB load method")
        check = True
        for index, row in df.iterrows():
            seller_dict = {'seller_id' : row['seller_id'],'first_name' : row['first_name'], 'last_name' : row['last_name'],
                    'location': row['location'], 'job_title' : row['job_title'], 'company' : row['company'],
                           'creation_time' :str(datetime.datetime.now())}
            if not self.createSeller(seller_dict):
                self.logger.error("Could not load data in Seller table: " + row)
                check = False
            self.logger.debug("Loaded data in Seller table: " + row)
        return check

    ##
    ## Name: jsonEncoder
    ## Description: This function converts the passed
    ## dataframe for Sellerdb class into json and
    ## checks the format of code sent
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: returns json data
    ##
    def jsonEncoder(self,input_df):
        try:
            # seller_id, first_name, last_name, location, job_title,company creation_time
            column_list = input_df.columns.tolist()
            if 'seller_id' not in column_list or 'first_name' not in column_list \
            or 'last_name' not in column_list or 'job_title' not in column_list \
            or 'location' not in column_list or 'company' not in column_list or 'creation_time' not in column_list:
                return None

            output_json = input_df.to_json(orient='records')
            return output_json
        except Exception, e:
            self.logger.error("Cannot convert input dataframe to json: " + str(e))
            return None

    ##
    ## Name: jsonDecoder
    ## Description: This function converts passed json data
    ## for Sellerdb class into dict and checks if the
    ## json has required fields
    ##
    ## Parameters: json
    ##
    ## Returns: Returns dict
    ##
    def jsonDecoder(self, input_json):
        try:
            output_dict = json.loads(input_json)[0]
            # the dict should have seller_id, first_name, last_name, location, skills
            if not output_dict['seller_id'] or not output_dict['first_name'] \
                or not output_dict['last_name']or not output_dict['location'] \
                    or not output_dict['job_title'] or not output_dict['company']:
                return None
            else:
                return output_dict

        except IndexError, e:
            self.logger.error("Input data passed is not correct: " + str(e))
            return None

