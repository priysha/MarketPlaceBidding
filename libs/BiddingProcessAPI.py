##########################################################
##
## File: BiddingProcessAPI.py
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
import pandas as pd
logging.config.fileConfig(LOGGING_CONF)

##
## Class: BiddingProcessAPI
## Description: This class is the driver for Bidding process
##
class BiddingProcessAPI:

    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - BiddingProcessAPI constructor")
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
    def getAllEligibleBids(self, project_id):
        self.logger.info("IN - BiddingProcessAPI getAllEligibleBids method")
        project_bid_endtime = self.Project.getBidEndTimeForProject(project_id)
        project_bids = self.Bid.getBidsForProject(project_id)
        if not project_bids.empty:
            project_elgible_bids = project_bids[project_bids.creation_time <= project_bid_endtime]
            if not project_elgible_bids.empty:
                return project_elgible_bids
        self.logger.info("No eligible bids")
        return pd.DataFrame()

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
        self.logger.info("IN - BiddingProcessAPI getAllEligibleBids method")
        all_bids = self.getAllEligibleBids(project_id)
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

    ##
    ## Name: getMostRecentNProjects
    ## Description: This function is called to retrieve
    ## top n most recent projects
    ##
    ## Parameters: n
    ##
    ## Returns: returns dataframe with top n most recent
    ## projects' info if exists else returns empty dataframe
    ##
    def getMostRecentNProjects(self, n):
        self.logger.info("IN - BiddingProcessAPI getMostRecentNProjects method")
        all_projects = self.Project.getAllProjects()
        if len(all_projects.index)>0:
            top_n_projects = all_projects.sort_values(['creation_time'], ascending=[False]).head(n)
            return top_n_projects
        self.logger.info("No projects to display")
        return pd.DataFrame()

    ##
    ## Name: getAllBuyerIDBiddingForAProject
    ## Description: This function is called to retrieve all
    ## the buyer IDs bidding for a project
    ##
    ## Parameters: None
    ##
    ## Returns: returns list of all buyer IDs for a project
    ##
    ##
    def getAllBuyerIDBiddingForAProject(self, project_id):
        self.logger.info("IN - BiddingProcessAPI getAllBuyerIDBiddingForAProject method")
        all_bids = self.Bid.getBidsForProject(project_id)
        if len(all_bids.index)>0:
            buyer_ids = list(all_bids.buyer_id)
            return buyer_ids
        self.logger.info("No buyers")
        return []
    ##
    ## Name: setBuyerForProject
    ## Description: This function sets the buyer for a
    ## project. To do this, we need to know who won the
    ## minimum bid first.
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns True if buyer ID is set for project
    ##
    def setBuyerForProject(self, project_id):
        self.logger.info("IN - BiddingProcessAPI setBuyerForProject method")
        bid = self.getMinimumBidForProject(project_id)
        buyer_id = bid.buyer_id[0]
        return self.Project.setBuyerForProject(project_id,buyer_id)



