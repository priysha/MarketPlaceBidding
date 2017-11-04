##########################################################
##
## File: BuyerDashboard.py
## Author: Priysha Pradhan
## Description: This class works for Buyer's
## dashboard, all the requirements for buyer can be retrived
## using these methods.
##
##########################################################

from Project import Project
from Bid import Bid
from Buyer import Buyer

class BuyerDashboard:

    def __init__(self, buyerId):
        self.Project = Project()
        self.Bid = Bid()
        self.Buyer = Buyer()
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
        all_bids = self.Bid.getAllBids()
        all_bids = all_bids[all_bids.buyer_id == self.buyerId]
        return all_bids

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
        all_projects = self.Project.getAllProjects()
        buyer_projects = all_projects[all_projects.buyer_id == self.buyerId]

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
    def createANewBid(self, project_id, buyer_id, bid_amount):
        bid = {'project_id': project_id , 'buyer_id' : buyer_id, 'bid_amount' : bid_amount}
        return self.Bid.createBid(bid)