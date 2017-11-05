###############################################################
##
## File: BiddingProcessAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BiddingProcessAPI
##  class. These test cases check if the BiddingProcessAPI class
## is interacting with the db correctly and returning data
## in correct format.
##
###############################################################

# Module Import #
import unittest
from BiddingProcessAPI import BiddingProcessAPI
from ProjectAPI import ProjectAPI

##
## Class: BiddingProcessAPITest
## Description: This class is the unittest driver for BiddingProcessAPI class
##
class BiddingProcessAPITest(unittest.TestCase):

    ##
    ## Name: setUp
    ## Description: Fixture that runs prior to the execution of any test.
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def setUp(self):
        self.BidProcess = BiddingProcessAPI()

    ##
    ## Name: testGetAllEligibleBids
    ## Description: This method tests getAllEligibleBids()
    ## method for BiddingProcessAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllEligibleBids(self):
        project_id = 2
        self.assertEquals(False, self.BidProcess.getAllEligibleBids(project_id).empty)

    ##
    ## Name: testGetMinimumBidForProject
    ## Description: This method tests getMinimumBidForProject()
    ## method for BiddingProcessAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetMinimumBidForProject(self):
        project_id = 18
        result_1 = self.BidProcess.getMinimumBidForProject(project_id)
        self.assertEquals(False,result_1.empty)
        self.assertEquals('nkingman7', result_1.buyer_id[0])

    ##
    ## Name: testGetMostRecentNProjects
    ## Description: This method tests getMostRecentNProjects()
    ## method for BiddingProcessAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetMostRecentNProjects(self):
        n = 5
        result_1 = self.BidProcess.getMostRecentNProjects(n)
        self.assertEquals(False, result_1.empty)
        n = 100
        result_2 = self.BidProcess.getMostRecentNProjects(n)
        self.assertEquals(False, result_2.empty)

    ##
    ## Name: testGetAllBuyerIDBiddingForAProject
    ## Description: This method tests getAllBuyerIDBiddingForAProject()
    ## method for BiddingProcessAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBuyerIDBiddingForAProject(self):
        project_id = 8
        result_1 = self.BidProcess.getAllBuyerIDBiddingForAProject(project_id)
        self.assertEquals(False, len(result_1)<1)
        self.assertEquals(True, 'priysha' in result_1)

    ##
    ## Name: testSetBuyerForProject
    ## Description: This method tests setBuyerForProject()
    ## method for BiddingProcessAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetBuyerForProject(self):
        Project = ProjectAPI()
        project_id = 18
        buyer_id = 'nkingman7'
        result_1 = self.BidProcess.setBuyerForProject(project_id)
        self.assertEquals(True,result_1)
        result_2 = Project.getBuyerForProject(project_id)
        self.assertEquals(buyer_id, result_2)
