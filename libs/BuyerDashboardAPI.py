##########################################################
##
## File: BuyerDashboardAPI.py
## Author: Priysha Pradhan
## Description: This class works for Buyer's
## dashboard, all the requirements for buyer can be retrived
## using these methods.
##
##########################################################

# Module Import #
from ProjectAPI import ProjectAPI
from BidAPI import BidAPI
from BuyerAPI import BuyerAPI
from datetime import datetime
from constants import *
import logging.config
import pandas as pd
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BuyerDashboardAPI
## Description: This class is the driver for Buyer dashboard
##
class BuyerDashboardAPI:

    def __init__(self, buyerId):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BuyerDashboardAPI constructor")
        self.Project = ProjectAPI()
        self.Bid = BidAPI()
        self.Buyer = BuyerAPI()
        self.buyerId = buyerId

    ##
    ## Name: getBuyerInfo
    ## Description: This function is called to retrieve a
    ## buyer's info from db
    ##
    ## Parameters: None
    ##
    ## Returns: returns dataframe with buyer's info
    ##
    def getBuyerInfo(self):
        self.logger.info("IN - BuyerDashboardAPI getBuyerInfo method")
        buyer_info = self.Buyer.getBuyerInfo(self.buyerId)
        return buyer_info

    ##
    ## Name: getAllBidsForBuyer
    ## Description: This function is called to retrieve all
    ## the bids put by the buyer
    ##
    ## Parameters: None
    ##
    ## Returns: returns dataframe with buyer's bids
    ##
    def getAllBidsForBuyer(self):
        self.logger.info("IN - BuyerDashboardAPI getAllBidsForBuyer method")
        buyer_bids = self.Bid.getBidsForBuyer(self.buyerId)
        if not buyer_bids.empty:
            return buyer_bids
        else:
            return pd.DataFrame()

    ##
    ## Name: getAllProjectsUnderBuyer
    ## Description: This function is called to retrieve all
    ## the projects won by the buyer
    ##
    ## Parameters: None
    ##
    ## Returns: returns dataframe with buyer's listed projects
    ##
    def getAllProjectsUnderBuyer(self):
        self.logger.info("IN - BuyerDashboardAPI getAllProjectsUnderBuyer method")
        buyer_projects = self.Project.getAllProjectsForBuyers(self.buyerId)
        if not buyer_projects.empty:
            return buyer_projects
        else:
            return pd.DataFrame()

    ##
    ## Name: addNewBid
    ## Description: This function lets buyer add a new bid
    ## for listed projects, bid is not created if time to
    ## create bid has exceeded the project_bid_endtime
    ##
    ## Parameters: None
    ##
    ## Returns: returns True if bid is created else False
    ##
    def addNewBid(self, project_id, bid_amount, bid_type='fixed', bid_hours=0):
        self.logger.info("IN - BuyerDashboardAPI addNewBid method")
        project_bid_endtime = self.Project.getBidEndTimeForProject(project_id)
        self.logger.debug("Project" + str(project_id) + " bidding ends at: " + str(project_bid_endtime)
                          +"\nCurrent time: " + str(datetime.now()))
        if str(datetime.now()) <= str(project_bid_endtime):
            bid = {'project_id': project_id , 'buyer_id' : self.buyerId, 'bid_amount' : bid_amount, 'bid_type' : bid_type, 'bid_hours' : bid_hours}
            return self.Bid.createBid(bid)
        else:
            self.logger.debug("Time exceeded for the bid to be added for project: " + str(project_id))
            return False