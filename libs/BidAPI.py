##########################################################
##
## File: BidAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for bid
## table. This class handles all the SQL queries executed
## for maintaining the bid table
##
##########################################################

# Module Import #
import DataBaseDriver
from datetime import datetime
from constants import *
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BidAPI
## Description: This class is the database driver for Bid
##
class BidAPI(DataBaseDriver.DataBaseDriver):
    bidTablename = BID_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BidAPI constructor")
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
        self.logger.info("IN - BidAPI createBid method")
        query = "INSERT INTO " + BidAPI.bidTablename + " (project_id, buyer_id, bid_amount, bid_type, bid_hours) VALUES (%s, %s, %s, %s, %s)"
        params = (bid_info['project_id'], bid_info['buyer_id'], bid_info['bid_amount'], bid_info['bid_type'], bid_info['bid_hours'])
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
        self.logger.info("IN - BidAPI getAllBids method")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidAPI.bidTablename
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
        self.logger.info("IN - BidAPI getBidInfo method")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type," \
                " bid_hours, creation_time FROM " + BidAPI.bidTablename + " WHERE bid_id = " + str(bid_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: setAmountForBid
    ## Description: This function sets the bid amount
    ## for a bid in db
    ## Parameters: bid_amount, bid_id
    ##
    ## Returns: Returns True if updated successfully
    ##
    def setAmountForBid(self, bid_amount, bid_id):
        self.logger.info("IN - BidAPI setAmountForBid method")
        query = "UPDATE " + BidAPI.bidTablename + " SET bid_amount = " + str(bid_amount) + " WHERE bid_id = " + str(bid_id)
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getBidsForProject
    ## Description: This function gets all the bids
    ## for a project_id
    ##
    ## Parameters: project_id
    ##
    ## Returns: Returns dataframe with bids for a project_id
    ##
    def getBidsForProject(self, project_id):
        self.logger.info("IN - BidAPI getBidsForProject method")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, " \
                "bid_hours, creation_time FROM " + BidAPI.bidTablename + " WHERE project_id = " + str(project_id)
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
        self.logger.info("IN - BidAPI getBidsForBuyer method")
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, " \
                "bid_hours, creation_time FROM " + BidAPI.bidTablename + " WHERE buyer_id = '" + buyer_id + "'"
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
        self.logger.info("IN - BidAPI getBidAmount method")
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
    ## Name: load
    ## Description: This function loads the bid info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        self.logger.info("IN - BidAPI load method")
        check = True
        for index, row in df.iterrows():
            bid_dict = {'project_id' : row['project_id'], 'buyer_id' : row['buyer_id'],
                    'bid_amount': row['bid_amount'], 'bid_type': row['bid_type'], 'bid_hours' : row['bid_hours']}
            if not self.createBid(bid_dict):
                self.logger.error("Could not load data in Bid table: ")
                self.logger.error(row)
                check = False
            self.logger.debug("Loaded data in Bid table: " )
            self.logger.debug(row)
        return check