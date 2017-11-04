##########################################################
##
## File: Bid.py
## Author: Priysha Pradhan
## Description: This is a database access class for bid
## table. This class handles all the SQL queries executed
## for maintaining the bid table
##
##########################################################

import DataBaseDriver
from datetime import datetime

class Bid(DataBaseDriver.DataBaseDriver):
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
    def createBid(self, bidInfo):
        query = "INSERT INTO " + Bid.BID_TABLENAME + " (project_id, buyer_id, bid_amount) VALUES (%s, %s, %s, %s)"
        params = (bidInfo['project_id'], bidInfo['buyer_id'], bidInfo['bid_amount'])
        return self.runInsertQuery(query, params)

    def getAllBids(self):
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + Bid.BID_TABLENAME
        return self.runSelectDfQuery(query)

    def getBidInfo(self, bidId):
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + Bid.BID_TABLENAME + " WHERE bid_id = " +bidId
        return self.runSelectDfQuery(query)

    def setBidAmountForBid(self, bidAmount, bidId):
        query = "UPDATE " + Bid.BID_TABLENAME + " SET bid_amount = " + bidAmount + " WHERE bid_id = " + bidId

    def getBidsForProject(self, projectId):
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, creation_time FROM " + Bid.BID_TABLENAME + " WHERE project_id = " + projectId
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
            #project_id, buyer_id, bid_amount, bid_start_time
            bid_dict = {'project_id' : row['project_id'], 'buyer_id' : row['buyer_id'],
                    'bid_amount': row['bid_amount'], 'bid_start_time' : row['bid_start_time']}
            if not self.createBid(bid_dict):
                check = False
        return check