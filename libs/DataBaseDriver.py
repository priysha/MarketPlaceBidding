##########################################################
##
## File: DataBaseDriver.py
## Author: Priysha Pradhan
## Description: This class is a base class to setup DB
## connection and run MySql db queries
##
##########################################################

# Module Import #
import pymysql
import pandas as pd
from constants import *
import logging
import logging.config
logging.config.fileConfig(LOGGING_CONF)
##
## Class: DataBaseDriver
## Description: This class is a base class for MySql db connection and queries
##
class DataBaseDriver(object):

    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - DataBaseDriver constructor")
        self.conn = pymysql.connect(host=DB_HOST,
                                    user=DB_USER,
                                    passwd=DB_PASSWORD,
                                    db=DB_NAME)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.logger.info("IN - DataBaseDriver destructor")
        self.cursor.close()
        self.conn.close()

    ##
    ## Name: getConn
    ## Description: Getter function that returns the MySql connector
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: Return the MySql connector
    ##
    def getConn(self):
        self.logger.info("IN - DataBaseDriver getConn")
        return self.conn

    ##
    ## Name: getCursor
    ## Description: Getter function that returns the MySql cursor
    ##
    ## Parameters: conn
    ##
    ## Returns: Return the MySql cursor
    ##
    def getCursor(self):
        self.logger.info("IN - DataBaseDriver getCursor")
        return self.cursor

    ##
    ## Name: commitConn
    ## Description: This function commits the db connection
    ##
    ## Parameters: conn
    ##
    ## Returns: none
    ##
    def commitConn(self):
        self.logger.info("IN - DataBaseDriver commitConn")
        self.conn.commit()

    ##
    ## Name: executeQuery
    ## Description: This function runs given query
    ## and returns value if SELECT query is run
    ##
    ## Parameters: query
    ##
    ## Returns: True if the query runs successfully
    ## returns query result in list for select query
    ##
    def executeQuery(self, query):
        self.logger.info("IN - DataBaseDriver executeQuery")
        try:
            self.cursor.execute(query)
            self.commitConn()
            self.logger.debug("Query executed and committed")

            if "SELECT" in query or "SHOW" in query:
                db_resp = self.cursor.fetchall()
                self.logger.debug("Query data fetched")
                return db_resp
            else:
                return True

        except Exception as e:
            self.logger.error("\nError in database query: " + query +
                          "\nError Status:\n" + str(e))
            return False

    ##
    ## Name: prepareSelectQuery
    ## Description: This function prepares select query
    ## using given params
    ##
    ## Parameters: table_name, fields, where_clause
    ##
    ## Returns: returns select query result if successful
    ##
    def prepareSelectQuery(self, table_name, fields, where_clause='1=1'):
        self.logger.info("IN - DataBaseDriver prepareSelectQuery")
        selectQuery = "SELECT " + fields + " FROM " + table_name + " WHERE " + where_clause
        self.logger.debug("Query: " + selectQuery)
        return self.executeQuery(selectQuery)

    ##
    ## Name: prepareInsertQuery
    ## Description: This function prepares insert query
    ## using given params
    ##
    ## Parameters: table_name, fields, values
    ##
    ## Returns: True if the query runs successfully
    ##
    def prepareInsertQuery(self, table_name, fields, values):
        self.logger.info("IN - DataBaseDriver prepareSelectQuery")
        insertQuery = " INSERT INTO " + table_name + fields + " VALUES " + values
        self.logger.debug("Query: " + insertQuery)
        return self.executeQuery(insertQuery)

    ##
    ## Name: prepareUpdateQuery
    ## Description: This function prepares update query
    ## using given params
    ##
    ## Parameters: table_name, setVal, where_clause
    ##
    ## Returns: True if the query runs successfully
    ##
    def prepareUpdateQuery(self, table_name, setVal, where_clause='1=1'):
        self.logger.info("IN - DataBaseDriver prepareUpdateQuery")
        updateQuery = "UPDATE " + table_name + " SET " + setVal + " WHERE " + where_clause
        self.logger.debug("Query: " + updateQuery)
        return self.executeQuery(updateQuery)

    ##
    ## Name: runUpdateQuery
    ## Description: This function prepares delete query
    ## using given params
    ##
    ## Parameters: table_name, where_clause
    ##
    ## Returns: True if the query runs successfully
    ##
    def prepareDeleteQuery(self, table_name, where_clause='1=1'):
        self.logger.info("IN - DataBaseDriver prepareDeleteQuery")
        deleteQuery = "DELETE FROM " + table_name + " WHERE " + where_clause
        self.logger.debug("Query: " + deleteQuery)
        return self.executeQuery(deleteQuery)

    ##
    ## Name: prepareReplaceQuery
    ## Description: This function prepares replace query
    ## using given params
    ##
    ## Parameters: table_name, fields, values
    ##
    ## Returns: True if the query runs successfully
    ##
    def prepareReplaceQuery(self, table_name, fields, values):
        self.logger.info("IN - DataBaseDriver prepareReplaceQuery")
        replaceQuery = " REPLACE INTO " + table_name + fields + " VALUES " + values
        self.logger.debug("Query: " + replaceQuery)
        return self.executeQuery(replaceQuery)

    ##
    ## Name: runUpdateQuery
    ## Description: This function runs the update query
    ##
    ## Parameters: query, type
    ##
    ## Returns: True if the query runs successfully
    ##
    def runUpdateQuery(self, query):
        self.logger.info("IN - DataBaseDriver runUpdateQuery")
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query)
            self.commitConn()
            self.logger.debug("UPDATE query executed and committed")
            return True

        except Exception as e:
            self.logger.error("\nError executing SQL UPDATE query: " + query
                          + "\nError status:" + str(e))
            return False

    ##
    ## Name: runDeleteQuery
    ## Description: This function runs the delete query
    ##
    ## Parameters: query, type
    ##
    ## Returns: True if the query runs successfully
    ##
    def runDeleteQuery(self, query):
        self.logger.info("IN - DataBaseDriver runDeleteQuery")
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query)
            self.commitConn()
            self.logger.debug("DELETE query executed and committed")
            return True

        except Exception as e:
            self.logger.error("\nError executing SQL DELETE query: " + query
                          + "\nError status:" + str(e))
            return False

    ##
    ## Name: selectDfQuery
    ## Description: This function returns the select query
    ## result in a pandas dataframe format
    ##
    ## Parameters: query
    ##
    ## Returns: dataframe with select query result
    ##
    def runSelectDfQuery(self, query):
        self.logger.info("IN - DataBaseDriver runSelectDfQuery")
        self.logger.debug("Query: " + query)
        try:
            df = pd.read_sql(query, con=self.conn)
            self.logger.debug("SELECT df query executed and dataframe fetched")
            self.logger.debug("Returned dataframe size" + str(len(df.index)))
            return df

        except Exception as e:
            df = pd.DataFrame()
            self.logger.error("\nError executing SQL SELECT DF query: " + query
                          + "\nError status:" + str(e))
            return df

    ##
    ## Name: selectQuery
    ## Description: This function returns the select query
    ##
    ## Parameters: query
    ##
    ## Returns: select query result
    ##
    def runSelectQuery(self, query):
        self.logger.info("IN - DataBaseDriver runSelectQuery")
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.logger.debug("SELECT query executed and data fetched")
            self.logger.debug("Returned result size" + str(len(result)))
            return result

        except Exception as e:
            self.logger.error("\nError executing SQL SELECT query: " + query
                          + "\nError status:" + str(e))
            return False

    ##
    ## Name: insertQuery
    ## Description: This function inserts the query into db
    ##
    ## Parameters: query, params
    ##
    ## Returns: returns True if successful
    ##
    def runInsertQuery(self,query, params):
        self.logger.info("IN - DataBaseDriver prepareSelectQuery")
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query, params)
            self.commitConn()
            self.logger.debug("INSERT query executed and committed")
            return True

        except Exception as e:
            self.logger.error("\nError executing SQL INSERT query: " + query
                          + "\nError status:" + str(e))
            return False


    ##
    ## Name: runReplaceQuery
    ## Description: This function replaces the query into db
    ##
    ## Parameters: query, params
    ##
    ## Returns: returns True if successful
    ##
    def runReplaceQuery(self,query, params):
        self.logger.info("IN - DataBaseDriver runReplaceQuery")
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query, params)
            self.commitConn()
            self.logger.debug("REPLACE query executed and committed")
            return True

        except Exception as e:
            self.logger.error("\nError executing SQL REPLACE query: " + query
                          + "\nError status:" + str(e))
            return False

    ##
    ## Name: runTruncateTableQuery
    ## Description: This function truncates table
    ## in the db
    ##
    ## Parameters: table_name
    ##
    ## Returns: returns True if successful
    ##
    def runTruncateTableQuery(self, table_name):
        self.logger.info("IN - DataBaseDriver runTruncateTableQuery")
        query = "TRUNCATE TABLE " + table_name
        self.logger.debug("Query: " + query)
        try:
            self.cursor.execute(query)
            self.commitConn()
            self.logger.debug("TRUNCATE query executed and committed")
            return True

        except Exception as e:
            self.logger.error("\nError executing SQL TRUNCATE query: " + query
                          + "\nError status:" + str(e))
            return False


