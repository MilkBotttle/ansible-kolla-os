#!/bin/python
import yaml
import io
import sys
import re
import os
import glob
def _validate_servers(servers):
    msg=""
    avaliable_role = ["controller", "compute" ]
    for key in servers.keys:
        if key not in avaliable_role:
            msg += ('%s not a validate role name, avaliable %s.\n' % (key, ', '.join(avaliable_role)))
    for value in servsers.values:
        if not isinstance(value, dict):
            msg += ('%s is not a dict format.\n' % value)

def _validate_interface_mappings(mappings):
    msg = ""
    for nic_map in mappings:
        if not isinstance(nic_map, dict):
            msg += ('%s is not a valid mapping.\n' % nic_map)
            if not re.search(r'^(nic)\d$', nic_map.key):
                msg += ('% is not a valid alias name format, accept nic[0-9].\n' % nic_map.key)
            if ":" in nic_map.value:
                if not re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', nic_map.value):
                    msg += ('%s is not valid mac address.\n' % nic_map.value)
            else
                # because the value is nic's name, we won't validate the interface name.
                pass
    return msg

def _validate_networks(networks):
    avaliable_network= ["ctlplane", "tunnel", "internal", "external", "storage"]
    msg=""
    avaliable_network_property= ["vlan_id", "cidr"]
    for name in networks.keys():
        if name not in avaliable_network:
            msg += ('Network name %s is not avaliable, only avaliable %s. \n' % (name, ', '.join(avaliable_network) ) )
    for network_detail in networks.values():
        if network_detail.keys()[0] not in avaliable_network_property:
            msg += ('%s is not avaliable in network property.' % network_detail.keys()[0])
    return msg

def _read_yaml(path):
    with io.open(path, r) as s:
        return yaml.safe_load(s)

def main():
    validate_msg = ""

    for filename in glob.glob(os.path.join('nic-configs','*-mapping.yaml')):
        mapping_data = _read_yaml(filename)
        validate_msg += _validate_interface_mappings(mapping_data)

    for filename in glob.glob(os.path.join('nic-configs', '*-config.yaml')):
        nic_config_data = _read_yaml(filename)
        validate_msg _= _validate_nicconfig(nic_config_data)

    vars_data = _read_yaml('vars.yaml')
    validate_msg += _validate_networks(vars_data.get('networks'))

if __name__ == '__main__':
    main()
