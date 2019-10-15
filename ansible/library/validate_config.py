#!/usr/bin/python

# Copyright: (c) 2010, Cameron Chuang
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule
from ansible.errors import AnsibleError

def validate_servers(servers):
    for role, nodes in servers.items():
        if type(nodes) is not list:
            raise AnsibleError('The nodes in %s role is not a correct list.' % role)
        for node in nodes:
            if type(node) is not dict:
                raise AnsibleError('The node in %s servers section is not a correct dict.' % role)

def validate_role_used_network(role_used_network):
   for role, required in role_used_network.items():
       if type(required) is not list:
           raise AnsibleError('The %s role value, in role_used_network is not a correct list.' % role)

def validate_networks(networks, role_used_network):
    all_require_net = []
    for requires in role_used_network.values():
        all_require_net += requires
    for net in all_require_net:
        if net not in networks.keys():
            raise AnsibleError('The %s defined in role_used_network but not in network section.' % net)

    for network, net_attr in networks.items():
        if network not in all_require_net and network != 'ctlplane':
            raise AnsibleError('The %s network not defined in role_used_network' % network)

        if 'hosts' not in net_attr:
            raise AnsibleError('The "hosts" in %s network is required even the value is empty.' % network)

        if 'vlan_id' in net_attr:
            if int(net_attr['vlan_id']) not in range(0,4096):
                raise AnsibleError('The %s network vland out of range.' % network)

        if 'cidr' not in net_attr:
            raise AnsibleError('The %s network required cidr' % network)

        try:
            import ipaddress
            all_ips = ipaddress.IPv4Network(unicode(net_attr['cidr']))
        except Exception:
            raise AnsibleError('The %s network has wrong cidr.' % network)
        try:
            for host, ip in net_attr['hosts'].items():
                if ipaddress.IPv4Address(unicode(ip)) not in all_ips:
                    raise AnsibleError('The host %s ip %s not in network cidr %s.' % (host,ip,net_attr['cidr']))
        except Exception:
            raise AnsibleError('The host %s ip %s not in network cidr %s.' % (host,ip,net_attr['cidr']))

def run_module():
    module_args = dict(
        servers=dict(type='dict', required=True),
        networks=dict(type='dict', required=True),
        role_used_network=dict(type='dict', required=True)
    )

    result = dict(
        changed=True,
        msg="Config validate parsed."
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    try:
        validate_servers(module.params['servers'])
        validate_role_used_network(module.params['role_used_network'])
        validate_networks(module.params['networks'],module.params['role_used_network'])
    except AnsibleError as e:
        result['msg']=e.message
        result['failed']=True
        module.exit_json(**result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
