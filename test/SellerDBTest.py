##########################################################
##
## File: SellerDBTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for SellerDB class
## These test cases check if the SellerDB class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

# Module Import #
import unittest
from SellerDB import SellerDB

##
## Class: SellerDBTest
## Description: This class is the unittest driver for SellerDB class
##
class SellerDBTest(unittest.TestCase):
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
        self.Seller = SellerDB()

    ##
    ## Name: testCreateSeller
    ## Description: This method tests createSeller()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateSeller(self):

        seller_dict = {'seller_id': 'foo', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'job_title': '', 'company': ''}

        #should pass
        self.assertEquals(True, self.Seller.createSeller(seller_dict))

        self.assertEquals(True, 'Priysha' in self.Seller.getAllSellers().first_name.values)

    ##
    ## Name: testCreateExistingSeller
    ## Description: This method tests createSeller()
    ## method for SellerDB class for existing seller
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateExistingSeller(self):

        seller_dict = {'seller_id': 'priysha', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'job_title': '', 'company': ''}

        #should pass
        self.assertEquals(False, self.Seller.createSeller(seller_dict))

    ##
    ## Name: testGetSellerInfo
    ## Description: This method tests getSellerInfo()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerInfo(self):

        seller_id = 'priysha'
        self.assertEquals('Pradhan', self.Seller.getSellerInfo(seller_id).last_name[0])

    ##
    ## Name: testGetNonExistingSellerInfo
    ## Description: This method tests getSellerInfo()
    ## method for SellerDB class when seller doesnt exist
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetNonExistingSellerInfo(self):

        seller_id = 'xyz'
        self.assertEquals(True, self.Seller.getSellerInfo(seller_id).empty)

    ##
    ## Name: testGetAllSellers
    ## Description: This method tests getAllSellers()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllSellers(self):
        seller_id = 'priysha'
        result = self.Seller.getAllSellers()
        self.assertEquals(False, result.empty)
        self.assertEquals(True, seller_id in result.seller_id.values)

    ##
    ## Name: testRemoveSeller
    ## Description: This method tests removeSeller()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testRemoveSeller(self):
        seller_id = 'bwetherbyb'
        self.assertEquals(True, self.Seller.removeSeller(seller_id))
        self.assertEquals(True, self.Seller.getSellerInfo(seller_id).empty)