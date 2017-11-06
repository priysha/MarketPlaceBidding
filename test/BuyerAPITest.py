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
    ## Name: testCreateExistingBuyer
    ## Description: This method tests createBuyer()
    ## method for BuyerAPI class for existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateExistingBuyer(self):
        buyer_dict = {'buyer_id': 'foo', 'first_name': 'foo', 'last_name': 'bar',
                      'location': '', 'skills': ''}

        #should pass
        self.assertEquals(False, self.Buyer.createBuyer(buyer_dict))

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

    ##
    ## Name: testGetNonExistingBuyerInfo
    ## Description: This method tests getBuyerInfo()
    ## method for BuyerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetNonExistingBuyerInfo(self):
        buyer_id = 'xyz'
        self.assertEquals(True, self.Buyer.getBuyerInfo(buyer_id).empty)

    ##
    ## Name: testGetBuyerFirstName
    ## Description: This method tests getBuyerFirstName()
    ## method for BuyerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBuyerFirstName(self):
        buyer_id = 'priysha'
        self.assertEquals('Priysha', self.Buyer.getBuyerFirstName(buyer_id))

    ##
    ## Name: testGetBuyerFirstName
    ## Description: This method tests setBuyerFirstName()
    ## method for BuyerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetBuyerFirstName(self):
        buyer_id = 'emccooker'
        new_first_name = 'Bar'
        self.assertEquals(True, self.Buyer.setBuyerFirstName(buyer_id,new_first_name))
        self.assertEquals(new_first_name, self.Buyer.getBuyerFirstName(buyer_id))

    ##
    ## Name: testGetBuyerLastName
    ## Description: This method tests getBuyerLastName()
    ## method for BuyerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBuyerLastName(self):
        buyer_id = 'gcaddiesi'
        self.assertEquals('Caddies', self.Buyer.getBuyerLastName(buyer_id))

    ##
    ## Name: testSetBuyerLastName
    ## Description: This method tests setBuyerLastName()
    ## method for BuyerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetBuyerLastName(self):
        buyer_id = 'odargann'
        new_last_name = 'Bar'
        self.assertEquals(True, self.Buyer.setBuyerLastName(buyer_id,new_last_name))
        self.assertEquals(new_last_name, self.Buyer.getBuyerLastName(buyer_id))
