##########################################################
##
## File: BidAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for bid
## table. This class handles all the SQL queries executed
## for maintaining the bid table
##
##########################################################

import DataBaseDriver
from datetime import datetime

class BidAPI(DataBaseDriver.DataBaseDriver):
    BID_TABLENAME = 'bid'
    def __init__(self):
        DataBaseDriver.DataBaseDriver.__init__(self)
        self.curr_date = datetime.now()

    ##
    ## Name: createBuyer
    ## Description: This function creates a new buyer
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if buyer is created
    ##
    def createBid(self, bid_info):
        query = "INSERT INTO " + BidAPI.BID_TABLENAME + " (project_id, buyer_id, bid_amount) VALUES (%s, %s, %s)"
        params = (bid_info['project_id'], bid_info['buyer_id'], bid_info['bid_amount'])
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + BidAPI.BID_TABLENAME
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE bid_id = " + str(bid_id)
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
        query = "UPDATE " + BidAPI.BID_TABLENAME + " SET bid_amount = " + str(bid_amount) + " WHERE bid_id = " + str(bid_id)
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE project_id = " + str(project_id)
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE buyer_id = '" + buyer_id + "'"
        return self.runSelectDfQuery(query)

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
        check = True
        for index, row in df.iterrows():

            bid_dict = {'project_id' : row['project_id'], 'buyer_id' : row['buyer_id'],
                    'bid_amount': row['bid_amount']}
            if not self.createBid(bid_dict):
                check = False
        return check