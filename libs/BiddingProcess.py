##########################################################
##
## File: BiddingProcess.py
## Author: Priysha Pradhan
## Description: This is the main class where Bidding process
## is handled.
##
##########################################################

from Project import Project
from Bid import Bid

class BiddingProcess:

    def __init__(self):
        self.Bid = Bid()
        self.Project = Project()

    ##
    ## Name: getAllEligibleBids
    ## Description: This function is called to retrieve info
    ## of all eligible bids for a project. Eligible bids are
    ## the bids with create_time less than project bid_endtime
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe with all eligible bid info
    ##
    def getAllEligibleBids(self, project_id):
        project_bid_endtime = self.Project.getBidEndTimeForProject(project_id)

        all_bids = self.Bid.getAllBids()
        project_bids = all_bids[(all_bids.project_id == project_id) & (all_bids.creation_time <= project_bid_endtime)]

        return project_bids

    ##
    ## Name: getMinimumBidForProject
    ## Description: This function is called to get the bid
    ## with minimum value from list of eligible bids for a
    ## project
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe with minimum bid info
    ##
    def getMinimumBidForProject(self, project_id):

        all_bids = self.getAllEligibleBids(project_id)
        all_bids = all_bids.sort(['bid_amount'], ascending=[True])

        return all_bids.iloc[0]

    ##
    ## Name: getTopNMinimumBidsForProject
    ## Description: This function is called to retrieve
    ## top n minimum bids for a project
    ##
    ## Parameters: project_id, n
    ##
    ## Returns: returns dataframe with top n minimum bids
    ## for a project
    ##
    def getTopNMinimumBidsForProject(self, project_id, n):

        project_bids = self.getAllEligibleBids(project_id)

        top_n_min_bids = project_bids.sort(['bid_amount'], ascending=[True]).head(n)

        return top_n_min_bids

    ##
    ## Name: getMostRecentNProjects
    ## Description: This function is called to retrieve
    ## top n most recent projects
    ##
    ## Parameters: n
    ##
    ## Returns: returns dataframe with top n most recent
    ## projects' info
    ##
    def getMostRecentNProjects(self, n):
        all_projects = self.Project.getAllProjects()

        top_n_projects = all_projects.sort(['creation_time'], ascending=[False]).head(n)

        return top_n_projects

    ##
    ## Name: getAllBuyersBiddinngForAProject
    ## Description: This function is called to retrieve all
    ## the buyer IDs bidding for a project
    ##
    ## Parameters: None
    ##
    ## Returns: returns list of all buyer IDs for a project
    ##
    def getAllBuyerIDBiddinngForAProject(self, project_id):
        all_bids = self.Bid.getBidsForProject(project_id)
        buyer_ids = list(all_bids.buyer_id)
        return buyer_ids

    ##
    ## Name: setBuyerForProject
    ## Description: This function sets the buyer for a
    ## project. To do this, we need to know who won the
    ## minimum bid first.
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns True if buyer ID is set for project
    ##
    def setBuyerForProject(self, project_id):
        bid = self.getMinimumBidForProject(project_id)
        buyer_id = bid.buyer_id[0]

        return self.Project.setBuyerForProject(project_id,buyer_id)



