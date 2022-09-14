import boto3
from python_aws_automation_tooling.logging import *


class Rds():
    
    def __init__(self):
        self.boto_client = boto3.client('rds')

    def get_rds_instances(self,exclude_replica=True,exclude_cluster_nodes=True):
        """
        Return list of all RDS instances
        exclude_replica: flag to exclude replica
        """

        rds_instances = []

        paginator = self.boto_client.get_paginator('describe_db_instances').paginate()
        for page in paginator:
            rds_instances.extend(page['DBInstances'])

        if exclude_cluster_nodes:
            rds_instances = list(filter(lambda item: ("DBClusterIdentifier" not in item or "ReadReplicaSourceDBInstanceIdentifier" in item), rds_instances))

        if exclude_replica:
            rds_instances = list(filter(lambda item: "ReadReplicaSourceDBInstanceIdentifier" not in item, rds_instances))
        
        return rds_instances

    def get_rds_clusters(self):
        """
        Return list of all RDS clusters
        """

        rds_clusters = []

        paginator = self.boto_client.get_paginator('describe_db_clusters').paginate()
        for page in paginator:
            rds_clusters.extend(page['DBClusters'])
        
        return rds_clusters
