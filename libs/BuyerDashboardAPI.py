##########################################################
##
## File: BuyerDashboardAPI.py
## Author: Priysha Pradhan
## Description: This class works for Buyer's
## dashboard, all the requirements for buyer can be retrived
## using these methods.
##
##########################################################

from ProjectAPI import ProjectAPI
from BidAPI import BidAPI
from BuyerAPI import BuyerAPI
from datetime import datetime

class BuyerDashboardAPI:

    def __init__(self, buyerId):
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
        buyer_bids = self.Bid.getBidsForBuyer(self.buyerId)
        return buyer_bids

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
        buyer_projects = self.Project.getAllProjectsForBuyers(self.buyerId)

        return buyer_projects

    ##
    ## Name: createANewBid
    ## Description: This function lets buyer create a new bid
    ## for listed projects
    ##
    ## Parameters: None
    ##
    ## Returns: returns True if bid is created else False
    ##
    def createANewBid(self, project_id, bid_amount):
        project_bid_endtime = self.Project.getBidEndTimeForProject(project_id)
        if datetime.now() > project_bid_endtime:
            bid = {'project_id': project_id , 'buyer_id' : self.buyerId, 'bid_amount' : bid_amount}
            return self.Bid.createBid(bid)
        else:
            print("Time exceeded for the bid to be added for project: " + project_id)
            return False