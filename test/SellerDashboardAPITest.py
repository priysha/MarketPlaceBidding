###############################################################
##
## File: SellerDashboardAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for SellerDashboardAPI
##  class. These test cases check if the SellerDashboardAPI class
## is interacting with the db correctly and returning data
## in correct format.
##
###############################################################

import unittest
from SellerDashboardAPI import SellerDashboardAPI
from ProjectAPI import ProjectAPI
##
## Class: SellerDashboardAPITest
## Description: This class is the unittest driver for SellerDashboardAPI class
##
class SellerDashboardAPITest(unittest.TestCase):

    ##
    ## Name: testGetSellerInfo
    ## Description: This method tests getSellerInfo()
    ## method for SellerDashboard class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerInfo(self):
        seller_id = 'priysha'
        SellerDashboard = SellerDashboardAPI(seller_id)
        self.assertEquals(False, SellerDashboard.getSellerInfo().empty)
        self.assertEquals('Priysha',SellerDashboard.getSellerInfo().first_name[0])

    ##
    ## Name: testGetAllProjectsUnderSeller
    ## Description: This method tests getAllProjectsUnderSeller()
    ## method for SellerDashboardAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsUnderSeller(self):
        seller_id = 'wlefloche'
        SellerDashboard = SellerDashboardAPI(seller_id)
        self.assertEquals(False, SellerDashboard.getAllProjectsUnderSeller().empty)
        self.assertEquals(True, 'Veribet'in SellerDashboard.getAllProjectsUnderSeller().project_name.values)

    ##
    ## Name: testAddANewProject
    ## Description: This method tests addANewProject()
    ## method for SellerDashboardAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testAddANewProject(self):
        project_name = 'abc'
        location = 'NC'
        bid_end_time ='2017-11-04'
        description = 'abc'
        seller_id = 'priysha'
        SellerDashboard = SellerDashboardAPI(seller_id)
        Project = ProjectAPI()
        self.assertEquals(True, SellerDashboard.addANewProject(project_name,location,bid_end_time,description))
        result = Project.getAllProjectsForSellers(seller_id).project_name
        self.assertEquals(True, 'abc' in result.values)