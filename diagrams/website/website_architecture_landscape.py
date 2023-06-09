from diagrams import Edge, Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.azure.web import AppServices
from diagrams.azure.network import CDNProfiles
from diagrams.azure.database import SQLDatabases
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.storage import StorageAccounts


with Diagram("Website landscape", 
             filename="landscape_architecture",
             show=False):
    client = Client("Web browser")

    with Cluster("Azure"):
        webapp = AppServices("Web Apps")                
        cdn = CDNProfiles("CDN")
        appInsights = ApplicationInsights("Application Insights")
        

        with Cluster("Storage") as storage:
            sqlDatabase = SQLDatabases("SQL Database")    
            sa = StorageAccounts("Videos")
    
    client >> Edge(label="1", color="darkgreen") >> webapp
    client >> Edge(label="4", color="blue") >> cdn
    webapp >> Edge(label="2", color="darkgreen") >> appInsights
    webapp >> Edge(label="3", color="darkgreen") >> sqlDatabase 
    webapp >> sa   
    

    # changing test diagramas



    
