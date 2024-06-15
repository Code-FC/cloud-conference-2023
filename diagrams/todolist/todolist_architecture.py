from diagrams import Edge, Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.database import CacheForRedis


with Diagram("Totolist landscape", 
             filename="todolist_architecture",
             show=False):
    client = Client("Web browser")

    with Cluster("Azure"):
        webapp = AppServices("Web Apps")                
        sqlDatabase = SQLDatabases("SQL Database")    
        CacheForRedis = CacheForRedis("Cache")
    
    client >>  webapp 
    
    webapp >> sqlDatabase    
    
    webapp >> CacheForRedis

    
