##########################################################
##
## File: ProjectBidDB.py
## Author: Priysha Pradhan
## Description: This is the main class where Bidding process
## is handled.
##
##########################################################

# Module Import #
from ProjectDB import ProjectDB
from BidDB import BidDB
from constants import *
import logging.config
import json
import datetime
import pandas as pd
import DataBaseDriver
logging.config.fileConfig(LOGGING_CONF)

##
## Class: ProjectBidDB
## Description: This class is the driver for Bidding process
##
class ProjectBidDB(DataBaseDriver.DataBaseDriver):

    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - ProjectBidDB constructor")
        DataBaseDriver.DataBaseDriver.__init__(self)
        self.Bid = BidDB()
        self.Project = ProjectDB()

    ##
    ## Name: getAllEligibleBids
    ## Description: This function is called to retrieve info
    ## of all eligible bids for a project. Eligible bids are
    ## the bids with create_time less than project bid_endtime
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe with all eligible bid info
    ## if exists else returns empty dataframe
    ##
    def getAllEligibleBidsForProject(self, project_id):
        self.logger.info("IN - ProjectBidDB.getAllEligibleBids")
        project_query = "SELECT bid_end_time FROM " + ProjectDB.projectTablename + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + project_query)
        bid_end_time = self.runSelectDfQuery(project_query).bid_end_time[0]
        try:
            bid_query = "SELECT bid_id, project_id, buyer_id, bid_amount, bid_type, " \
                        "bid_hours, creation_time FROM " + BidDB.bidTablename + \
                        " WHERE project_id = " + str(project_id) + " AND creation_time <= '" + str(bid_end_time) + "'"
            self.logger.debug("Query: " + bid_query)
            eligible_bids =  self.runSelectDfQuery(bid_query)
            return eligible_bids
        except ValueError, e:
            self.logger.error("Bid end date returned is not correct: " + str(e))

    ##
    ## Name: getMinimumBidForProject
    ## Description: This function is called to get the bid
    ## with minimum value from list of eligible bids for a
    ## project
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe with minimum bid info if bids exist
    ## else returns empty dataframe
    ##
    def getMinimumBidForProject(self, project_id):
        self.logger.info("IN - ProjectBidDB.getMinimumBidForProject")
        all_bids = self.getAllEligibleBidsForProject(project_id)
        if len(all_bids.index)>0:
            min_bid = all_bids.bid_id[0]
            min_amount = float('inf')
            for index,row in all_bids.iterrows():
                bid_amount = self.Bid.getBidAmount(row['bid_id'])
                if bid_amount < min_amount:
                    min_amount = bid_amount
                    min_bid = row['bid_id']

            min_bid_info = self.Bid.getBidInfo(min_bid)

            return min_bid_info
        self.logger.info("No eligible minimum bid")
        return pd.DataFrame()

