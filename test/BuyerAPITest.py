##############################################################
##
## File: BuyerAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BuyerAPI class
## These test cases check if the BuyerAPI class is interacting
## with the db correctly and returning data in correct format
##
###############################################################

# Module Import #
import unittest
from BuyerAPI import BuyerAPI

##
## Class: BuyerAPITest
## Description: This class is the unittest driver for BuyerAPI class
##
class BuyerAPITest(unittest.TestCase):
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
        self.Buyer = BuyerAPI()


    ##
    ## Name: testCreateBuyer
    ## Description: This method tests createBuyer()
    ## method for BuyerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBuyers(self):

        self.assertEquals(False, self.Buyer.getAllBuyers().empty)

    ##
    ## Name: testCreateBuyer
    ## Description: This method tests createBuyer()
    ## method for BuyerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateBuyer(self):

        buyer_dict = {'buyer_id': 'foo', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'skills': ''}

        #should pass
        self.assertEquals(True, self.Buyer.createBuyer(buyer_dict))

        self.assertEquals(True, 'Priysha' in self.Buyer.getAllBuyers().first_name.values)

    ##
    ## Name: testGetBuyerInfo
    ## Description: This method tests getBuyerInfo()
    ## method for BuyerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBuyerInfo(self):

        buyer_id = 'priysha'
        self.assertEquals('Pradhan', self.Buyer.getBuyerInfo(buyer_id).last_name[0])

