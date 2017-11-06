###############################################################
##
## File: BuyerDashboardAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BuyerDashboardAPI
##  class. These test cases check if the BuyerDashboardAPI class
## is interacting with the db correctly and returning data
## in correct format.
##
###############################################################

# Module Import #
import unittest
from BuyerDashboardAPI import BuyerDashboardAPI
from BiddingProcessAPI import BiddingProcessAPI
from ProjectAPI import ProjectAPI
from BidAPI import BidAPI

##
## Class: BuyerDashboardAPITest
## Description: This class is the unittest driver for BuyerDashboardAPI class
##
##TODO: Add more test cases
class BuyerDashboardAPITest(unittest.TestCase):

    ##
    ## Name: testGetBuyerInfo
    ## Description: This method tests getBuyerInfo()
    ## method for BuyerDashboardAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBuyerInfo(self):
        buyer_id = 'priysha'
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(False, BuyerDashboard.getBuyerInfo().empty)
        self.assertEquals('Priysha',BuyerDashboard.getBuyerInfo().first_name[0])

    ##
    ## Name: testGetAllBidsForBuyer
    ## Description: This method tests getAllBidsForBuyer()
    ## method for BuyerDashboardAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBidsForBuyer(self):
        buyer_id = 'mwimmersc'
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(False, BuyerDashboard.getAllBidsForBuyer().empty)
        self.assertEquals(True, '22.85' in str(BuyerDashboard.getAllBidsForBuyer().bid_amount.values))

    ##
    ## Name: testGetAllBidsForBuyerNone
    ## Description: This method tests getAllBidsForBuyer()
    ## method for BuyerDashboardAPI class when no bids exist under
    ## that buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBidsForBuyerNone(self):
        buyer_id = 'abc'
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(True, BuyerDashboard.getAllBidsForBuyer().empty)

    ##
    ## Name: testGetAllProjectsUnderBuyer
    ## Description: This method tests getAllProjectsUnderBuyer()
    ## method for BuyerDashboardAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsUnderBuyer(self):
        BidProcess = BiddingProcessAPI()
        Project = ProjectAPI()
        project_id = 9
        result_1 = BidProcess.setBuyerForProject(project_id)
        self.assertEquals(True, result_1)
        buyer_id = 'pbris4'
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(False, BuyerDashboard.getAllProjectsUnderBuyer().empty)
        self.assertEquals('pbris4', Project.getProjectInfo(project_id).buyer_id[0])

    ##
    ## Name: testGetAllProjectsUnderBuyerNone
    ## Description: This method tests getAllProjectsUnderBuyer()
    ## method for BuyerDashboardAPI class when no projects exist under
    ## that buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsUnderBuyerNone(self):
        buyer_id = 'rmuzzim'
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(True, BuyerDashboard.getAllProjectsUnderBuyer().empty)

    ##
    ## Name: testCreateANewBidFixed
    ## Description: This method tests addNewBid()
    ## method for BuyerDashboardAPI class, this test is
    ## for creating a bid of fixed type
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateANewBidFixed(self):
        buyer_id = 'oparrind'
        project_id = 22
        bid_amount = 37000
        bid_type = 'fixed'
        bid_hours = 0
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        Bid = BidAPI()
        self.assertEquals(True, BuyerDashboard.addNewBid(project_id, bid_amount, bid_type, bid_hours))
        self.assertEquals(True, project_id in Bid.getBidsForBuyer(buyer_id).project_id.values)

    ##
    ## Name: testCreateANewBidFixed
    ## Description: This method tests addNewBid()
    ## method for BuyerDashboardAPI class, this test is
    ## for creating a bid of hourly type
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateANewBidHourly(self):
        buyer_id = 'smarr9'
        project_id = 22
        bid_amount = 370
        bid_type = 'hourly'
        bid_hours = 10000
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        Bid = BidAPI()
        self.assertEquals(True, BuyerDashboard.addNewBid(project_id, bid_amount,bid_type,bid_hours))
        self.assertEquals(True, project_id in Bid.getBidsForBuyer(buyer_id).project_id.values)

    ##
    ## Name: testCreateANewBidFixed
    ## Description: This method tests addNewBid()
    ## method for BuyerDashboardAPI class, this test is
    ## for creating a bid which has exceeded the project bid_end_time
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateANewBidAfterTime(self):
        project_id = 27
        buyer_id = 'pbris4'
        bid_amount = 370
        BuyerDashboard = BuyerDashboardAPI(buyer_id)
        self.assertEquals(False, BuyerDashboard.addNewBid(project_id,bid_amount))