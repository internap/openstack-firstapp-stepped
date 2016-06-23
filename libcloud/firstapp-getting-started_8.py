#! /usr/bin/env bash

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import os_client_config

cloud_config = os_client_config.OpenStackConfig().get_one_cloud(
    'internap', region_name='nyj01')

provider = get_driver(Provider.OPENSTACK)
conn = provider(cloud_config.config['auth']['username'],
                cloud_config.config['auth']['password'],
                ex_force_auth_url=cloud_config.config['auth']['auth_url'],
                ex_force_auth_version='2.0_password',
                ex_tenant_name=cloud_config.config['auth']['project_name'],
                ex_force_service_region=cloud_config.region)

# step-8
print( 'Destroying all test instances')
instances = conn.list_nodes()
for instance in instances:
    if "testing for libcloud" in instance.name:
        conn.destroy_node(instance)

print( 'Done! Congrats!')
