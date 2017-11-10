###############################################################
##
## File: ProjectBidDBTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for ProjectBidDB class
## These test cases check if the ProjectBidDB class is interacting
## with the db correctly and returning data in correct format
##
###############################################################

# Module Import #
import unittest
from ProjectBidDB import ProjectBidDB

##
## Class: ProjectDBTest
## Description: This class is the unittest driver for ProjectDB class
##
class ProjectBidDBTest(unittest.TestCase):
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
        self.ProjectBidDB = ProjectBidDB()

    ##
    ## Name: testGetAllEligibleBidsForProject
    ## Description: This method tests getAllProjects()
    ## method for ProjectDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllEligibleBidsForProject(self):
        project_id = 1
        result = self.ProjectBidDB.getAllEligibleBidsForProject(project_id)
        self.assertEquals(False, result.empty)
        self.assertEquals(True, '2' in result.bid_id.values)

    ##
    ## Name: testGetMinimumBidForProject
    ## Description: This method tests getMinimumBidForProject()
    ## method for ProjectDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetMinimumBidForProject(self):
        project_id = 10
        result = self.ProjectBidDB.getMinimumBidForProject(project_id)
        self.assertEquals(False, result.empty)
        self.assertEquals(round(343.83,2), round(float(result.bid_amount[0]),2))

