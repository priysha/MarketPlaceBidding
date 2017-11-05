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
        query = "INSERT INTO " + BidAPI.BID_TABLENAME + " (project_id, buyer_id, bid_amount, bid_type, bid_hours) VALUES (%s, %s, %s, %s, %s)"
        params = (bid_info['project_id'], bid_info['buyer_id'], bid_info['bid_amount'], bid_info['bid_type'], bid_info['bid_hours'])
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidAPI.BID_TABLENAME
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE bid_id = " + str(bid_id)
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE project_id = " + str(project_id)
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
        query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, bid_hours, creation_time FROM " + BidAPI.BID_TABLENAME + " WHERE buyer_id = '" + buyer_id + "'"
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
        bid_info = self.getBidInfo(bid_id)
        if bid_info.bid_type[0] == "hourly":
            bid_amount = float(bid_info.bid_amount[0] * bid_info.bid_hours[0])
        elif bid_info.bid_type[0] == "fixed":
            bid_amount = float(bid_info.bid_amount[0])
        else:
            bid_amount = False
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
        check = True
        for index, row in df.iterrows():

            bid_dict = {'project_id' : row['project_id'], 'buyer_id' : row['buyer_id'],
                    'bid_amount': row['bid_amount'], 'bid_type': row['bid_type'], 'bid_hours' : row['bid_hours']}
            if not self.createBid(bid_dict):
                check = False
        return check