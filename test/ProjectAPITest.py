##########################################################
##
## File: ProjectAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for ProjectAPI class
## These test cases check if the Seller class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

import unittest
from ProjectAPI import ProjectAPI
import pandas as pd

##
## Class: SellerAPITest
## Description: This class is the unittest driver for ProjectAPI class
##
class ProjectAPITest(unittest.TestCase):
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
        self.Project = ProjectAPI()

        df = pd.read_csv("./test/projects.csv")
        self.Project.load(df)

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
    def tearDown(self):
        # delete all the data
        self.Project.runTruncateTableQuery('seller')

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
        project_name = 'Redhold'

        project_id = self.Project.getProjectId(project_name,seller_id)
        self.assertIsNotNone(self.Project.getBidEndTimeForProject(project_id))

