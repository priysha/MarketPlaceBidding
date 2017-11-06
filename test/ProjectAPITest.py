###############################################################
##
## File: ProjectAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for ProjectAPI class
## These test cases check if the ProjectAPI class is interacting
## with the db correctly and returning data in correct format
##
###############################################################

# Module Import #
import unittest
from ProjectAPI import ProjectAPI

##
## Class: ProjectAPITest
## Description: This class is the unittest driver for ProjectAPI class
##
##TODO: Add more test cases
class ProjectAPITest(unittest.TestCase):
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
        self.Project = ProjectAPI()

    ##
    ## Name: testGetAllProjects
    ## Description: This method tests getAllProjects()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjects(self):
        self.assertEquals(False, self.Project.getAllProjects().empty)
        self.assertEquals(True, 'bkusick3' in self.Project.getAllProjects().seller_id.values)

    ##
    ## Name: testCreateProject
    ## Description: This method tests createProject()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateProject(self):
        project_dict = {'project_name' : 'abc' , 'location' : 'NC', 'bid_end_time' : '2017-11-05', 'seller_id' : 'priysha',
                        'description': 'abc', 'skills':'abc'}
        #should pass
        self.assertEquals(True, self.Project.createProject(project_dict))

        self.assertEquals(True, 'priysha' in self.Project.getAllProjects().seller_id.values)

    ##
    ## Name: testGetAllProjectsForSellers
    ## Description: This method tests getAllProjectsForSellers()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsForSellers(self):
        seller_id = 'priysha'
        self.assertEquals(False, self.Project.getAllProjectsForSellers(seller_id).empty)

    ##
    ## Name: testGetAllProjectsForSellersEmpty
    ## Description: This method tests getAllProjectsForSellers()
    ## method for ProjectAPI class where no project exists for
    ## that seller
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsForSellersEmpty(self):
        seller_id = 'bedlingtont'
        self.assertEquals(True, self.Project.getAllProjectsForSellers(seller_id).empty)

    ##
    ## Name: testGetAllProjectsForBuyers
    ## Description: This method tests getAllProjectsForBuyers()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsForBuyers(self):
        buyer_id = 'priysha'
        self.assertEquals(True, self.Project.setBuyerForProject(2,buyer_id))
        self.assertEquals(False, self.Project.getAllProjectsForBuyers(buyer_id).empty)

    ##
    ## Name: testGetAllProjectsForBuyersEmpty
    ## Description: This method tests getAllProjectsForBuyers()
    ## method for ProjectAPI class where no project exists
    ## for that buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllProjectsForBuyersEmpty(self):
        buyer_id = 'pkillought'
        self.assertEquals(True, self.Project.getAllProjectsForSellers(buyer_id).empty)

    ##
    ## Name: testGetAllProjectsForSellers
    ## Description: This method tests getAllProjectsForSellers()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetProjectId(self):
        project_dict = {'project_name': 'foo', 'location': 'NC', 'bid_end_time': '2017-12-05', 'seller_id': 'priysha',
                        'description': 'bar', 'skills': 'abc'}
        # should pass
        self.assertEquals(True, self.Project.createProject(project_dict))
        self.assertIsNotNone(self.Project.getProjectId(project_dict['project_name'],project_dict['seller_id']))

    ##
    ## Name: testGetBidEndTimeForProject
    ## Description: This method tests getBidEndTimeForProject()
    ## method for ProjectAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidEndTimeForProject(self):
        seller_id = 'priysha'
        project_name = 'Bigtax'

        project_id = self.Project.getProjectId(project_name,seller_id)
        self.assertIsNotNone(self.Project.getBidEndTimeForProject(project_id))


    ##
    ## Name: testGetProjectInfoForExistingProject
    ## Description: This method tests getProjectInfo()
    ## method for ProjectAPI class for existing project
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetProjectInfoForExistingProject(self):
        project_id = 10
        project_name = 'It'

        result_1 = self.Project.getProjectInfo(project_id)
        self.assertEquals(False, result_1.empty)
        self.assertEquals(project_name, result_1.project_name[0])

    ##
    ## Name: testGetProjectInfoForNonExistingProject
    ## Description: This method tests getProjectInfo()
    ## method for ProjectAPI class for non-existing project
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetProjectInfoForNonExistingProject(self):
        project_id = 400

        result_1 = self.Project.getProjectInfo(project_id)
        self.assertEquals(True, result_1.empty)
