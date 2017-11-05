##########################################################
##
## File: BuyerDashboardAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BuyerDashboardAPI
##  class. These test cases check if the Buyer class is
## interacting with the db correctly and returning data
## in correct format.
##
##########################################################

import unittest
from BuyerDashboardAPI import BuyerDashboardAPI
from ProjectAPI import ProjectAPI
from BidAPI import BidAPI
from BuyerAPI import BuyerAPI
import pandas as pd

##
## Class: BiddingProcessAPITest
## Description: This class is the unittest driver for BiddingProcessAPI class
##
class BuyerDashboardAPITest(unittest.TestCase):

    ##
    ## Name: setUp
    ## Description: Fixture that runs prior to the execution of any test.
    ## In the setUp, we are adding some fake testing data in the db
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def setUp(self):
        self.BuyerDashboard = BuyerDashboardAPI()
        self.Project = ProjectAPI()
        self.Bid = BidAPI()
        self.Buyer = BuyerAPI()
        projects = pd.read_csv("./test/projects.csv")
        self.Project.load(projects)
        bids = pd.read_csv("./test/bids.csv")

        self.Bid.load(bids)



    ##
    ## Name: tearDown
    ## Description: Fixture that runs after the execution of all tests.
    ## This will remove the db entries made in the setUp
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    # def tearDown(self):
    #     self.Project.runTruncateTableQuery('project')
    #     self.Project.runTruncateTableQuery('bid')