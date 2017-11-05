##########################################################
##
## File: BiddingProcessAPI.py
## Author: Priysha Pradhan
## Description: This is the main class where Bidding process
## is handled.
##
##########################################################

from ProjectAPI import ProjectAPI
from BidAPI import BidAPI

class BiddingProcessAPI:

    def __init__(self):
        self.Bid = BidAPI()
        self.Project = ProjectAPI()

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

        project_bids = self.Bid.getBidsForProject(project_id)
        project_elgible_bids = project_bids[project_bids.creation_time <= project_bid_endtime]

        return project_elgible_bids

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



