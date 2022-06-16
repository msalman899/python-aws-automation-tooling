import boto3
from queue import Queue
from python_aws_automation_tooling.logging import *


class Elb():
    
    def __init__(self):
        self.elb_client = boto3.client('elb')
        self.elbv2_client = boto3.client('elbv2')

    def get_all_elb(self,lb_filter={}):
    
        elb = self.get_elb(lb_filter=lb_filter)
        
        if "application" in lb_filter.get('Type',[]):
            del lb_filter['Type']
            clb = self.get_classic_elb(lb_filter=lb_filter)
            return elb + clb 

        return elb

    def get_classic_elb(self,lb_filter={}):
        """
        Return list of classic loadbalancers
        lb_filter: Map to filter elbs based on keys e.g. Scheme etc
        """

        kwargs = {}
        clb = []

        while True:
            response = self.elb_client.describe_load_balancers(LoadBalancerNames=[])

            try:
                clb.extend(response['LoadBalancerDescriptions'])
                kwargs['NextMarker'] = response['NextMarker']
            except KeyError:
                break

        if len(lb_filter.keys()) > 0:
            for k,v in lb_filter.items():
                clb = list(filter(lambda item: item.get(k) in v, clb))
        
        return clb

    def get_classic_elb_tags(self,elb=[]):
        """Return Classic ELB tags in key value pair"""

        tags = self.elb_client.describe_tags(LoadBalancerNames=elb)["TagDescriptions"][0]['Tags']
        return str({ item['Key']:item['Value'] for item in tags})

    def get_elb_tags(self,elb_arns=[]):
        """Return ELB tags in key value pair"""

        tags = self.elb_client.describe_tags(ResourceArns=elb_arns)["TagDescriptions"][0]['Tags']
        return str({ item['Key']:item['Value'] for item in tags})


    def get_elb(self,lb_filter={}):
        """
        Return list of application, network and gateway loadbalancers
        lb_filter: Map to filter elbs based on keys e.g. Type, Scheme etc
        """

        kwargs = {}
        elb = []

        while True:
            response = self.elbv2_client.describe_load_balancers(Names=[])

            try:
                elb.extend(response['LoadBalancers'])
                kwargs['NextMarker'] = response['NextMarker']
            except KeyError:
                break

        if len(lb_filter.keys()) > 0:
            for k,v in lb_filter.items():
                elb = list(filter(lambda item: item.get(k) in v, elb))

        return elb
