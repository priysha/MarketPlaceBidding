##########################################################
##
## File: BidDB.py
## Author: Priysha Pradhan
## Description: This is a database access class for bid
## table. This class handles all the SQL queries executed
## for maintaining the bid table
##
##########################################################

# Module Import #
import DataBaseDriver
import datetime
from constants import *
import json
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BidDB
## Description: This class is the database driver for Bid
##
class BidDB(DataBaseDriver.DataBaseDriver):
    bidTablename = BID_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BidDB constructor")
        DataBaseDriver.DataBaseDriver.__init__(self)

    ##
    ## Name: createBuyer
    ## Description: This function creates a new buyer
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if buyer is created
    ##
    def createBid(self, bid_info):
        self.logger.info("IN - BidDB.createBid")
        #bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time
        query = "INSERT INTO " + BidDB.bidTablename + \
                " (bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time) " \
                "VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY " \
                "UPDATE bid_amount =%s, bid_type =%s, bid_hours =%s"
        params = (bid_info['bid_id'], bid_info['project_id'], bid_info['buyer_id'], bid_info['bid_amount'], bid_info['bid_type'], bid_info['bid_hours'],
                bid_info['bid_amount'], bid_info['bid_type'], bid_info['bid_hours'])
        self.logger.debug("Query: " + query)
        self.logger.debug("Params: %s, %s, %s, %s, %s",
                          bid_info['project_id'], bid_info['buyer_id'], bid_info['bid_amount'], bid_info['bid_type'], bid_info['bid_hours'])
        return self.runInsertQuery(query, params)

    ##
    ## Name: getAllBids
    ## Description: This function gets all the bids
    ## from the db
    ##
    ## Parameters:
    ##
    ## Returns: Returns dataframe with all the bids
    ##
    def getAllBids(self):
        self.logger.info("IN - BidDB.getAllBids")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidDB.bidTablename
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getBidInfo
    ## Description: This function gets bid info
    ## for a bid_id
    ##
    ## Parameters: bid_id
    ##
    ## Returns: Returns dataframe with bid's info
    ##
    def getBidInfo(self, bid_id):
        self.logger.info("IN - BidDB.getBidInfo")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type," \
                " bid_hours, creation_time FROM " + BidDB.bidTablename + " WHERE bid_id = " + str(bid_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getBidsForBuyer
    ## Description: This function gets all the bids
    ## for a buyer_id
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: Returns dataframe with bids for a buyer_id
    ##
    def getBidsForBuyer(self, buyer_id):
        self.logger.info("IN - BidDB.getBidsForBuyer")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, " \
                "bid_hours, creation_time FROM " + BidDB.bidTablename + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getBidAmount
    ## Description: This function gets bid's amount
    ## from the db on the basis if the bid made is fixed
    ## or hourly
    ##
    ## Parameters: bid_id
    ##
    ## Returns: Returns bid's amount (float) else False
    ##
    def getBidAmount(self, bid_id):
        self.logger.info("IN - BidDB.getBidAmount")
        bid_info = self.getBidInfo(bid_id)
        if bid_info.bid_type[0] == "hourly":
            self.logger.debug("Bid type of 'hourly'")
            bid_amount = float(bid_info.bid_amount[0] * bid_info.bid_hours[0])
            self.logger.debug("Bid amount: " + str(bid_amount))
        elif bid_info.bid_type[0] == "fixed":
            self.logger.debug("Bid type of 'fixed'")
            bid_amount = float(bid_info.bid_amount[0])
            self.logger.debug("Bid amount: " + str(bid_amount))
        else:
            bid_amount = False
            self.logger.error("Wrong bid_amount is asked, no bid_type")
        return bid_amount

    ##
    ## Name: removeBid
    ## Description: This function removes bid
    ## from the db
    ##
    ## Parameters: bid_id
    ##
    ## Returns: Returns True if deleted else False
    ##
    def removeBid(self,bid_id):
        self.logger.info("IN - BidDB.removeBid")
        query = "DELETE FROM " + BidDB.bidTablename + " WHERE bid_id=" + str(bid_id)
        self.logger.debug("Query: " + query)
        return self.runDeleteQuery(query)

    ##
    ## Name: load
    ## Description: This function loads the bid info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        self.logger.info("IN - BidDB.load")
        check = True
        for index, row in df.iterrows():

            bid_dict = {'bid_id' : row['bid_id'], 'project_id' : row['project_id'], 'buyer_id' : row['buyer_id'],
                    'bid_amount': row['bid_amount'], 'bid_type': row['bid_type'], 'bid_hours' : row['bid_hours'],
                        'creation_time' :str(datetime.datetime.now())}
            if not self.createBid(bid_dict):
                self.logger.error("Could not load data in Bid table: ")
                self.logger.error(row)
                check = False
            self.logger.debug("Loaded data in Bid table: " )
            self.logger.debug(row)
        return check

    ##
    ## Name: jsonEncoder
    ## Description: This function converts the passed
    ## dataframe for BidDB Class into json and
    ## checks the format of code sent
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: returns json data
    ##
    def jsonEncoder(self,input_df):
        try:
            #bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time
            column_list = input_df.columns.tolist()
            if 'bid_id' not in column_list or 'project_id' not in column_list \
            or 'buyer_id' not in column_list or 'bid_amount' not in column_list \
            or 'bid_type' not in column_list or 'bid_hours' not in column_list or 'creation_time' not in column_list:
                return None
            output_json = input_df.to_json(orient='records')
            return output_json
        except Exception, e:
            self.logger.error("Cannot convert input dataframe to json: " + str(e))
            return None

    ##
    ## Name: jsonDecoder
    ## Description: This function converts passed json data
    ## for BidDB Class into dict and checks if the
    ## json has required fields
    ##
    ## Parameters: json
    ##
    ## Returns: Returns dict
    ##
    def jsonDecoder(self, input_json):
        try:
            output_dict = json.loads(input_json)[0]
            # the dict should have bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time
            key = output_dict.keys()
            if 'bid_id' not in key or 'project_id' not in key or 'buyer_id' not in key \
                    or 'bid_amount' not in key or 'bid_type' not in key or 'bid_hours' not in key or 'creation_time' not in key:
                return None
            else:
                return output_dict

        except IndexError, e:
            self.logger.error("Input data passed is not correct: " + str(e))
            return None