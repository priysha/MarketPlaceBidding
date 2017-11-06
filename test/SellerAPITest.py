##########################################################
##
## File: SellerAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for SellerAPI class
## These test cases check if the SellerAPI class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

# Module Import #
import unittest
from SellerAPI import SellerAPI

##
## Class: SellerAPITest
## Description: This class is the unittest driver for SellerAPI class
##
class SellerAPITest(unittest.TestCase):
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
        self.Seller = SellerAPI()

    ##
    ## Name: testCreateSeller
    ## Description: This method tests createSeller()
    ## method for SellerAPI class
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
    ## method for SellerAPI class for existing seller
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
    ## method for SellerAPI class
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
    ## method for SellerAPI class when seller doesnt exist
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
    ## method for SellerAPI class
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
    ## Name: testGetSellerFirstName
    ## Description: This method tests getSellerFirstName()
    ## method for SellerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerFirstName(self):
        seller_id = 'priysha'
        self.assertEquals('Priysha', self.Seller.getSellerFirstName(seller_id))

    ##
    ## Name: testSetSellerFirstName
    ## Description: This method tests setSellerFirstName()
    ## method for SellerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetSellerFirstName(self):
        seller_id = 'sjacsonr'
        new_first_name = 'Foo'
        self.assertEquals(True, self.Seller.setSellerFirstName(seller_id,new_first_name))
        self.assertEquals(new_first_name, self.Seller.getSellerFirstName(seller_id))

    ##
    ## Name: testGetSellerLastName
    ## Description: This method tests getSellerLastName()
    ## method for SellerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerLastName(self):
        seller_id = 'priysha'
        self.assertEquals('Pradhan', self.Seller.getSellerLastName(seller_id))

    ##
    ## Name: testSetSellerLastName
    ## Description: This method tests setSellerLastName()
    ## method for SellerAPI class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetSellerLastName(self):
        seller_id = 'sjacsonr'
        new_last_name = 'Bar'
        self.assertEquals(True, self.Seller.setSellerLastName(seller_id,new_last_name))
        self.assertEquals(new_last_name, self.Seller.getSellerLastName(seller_id))
