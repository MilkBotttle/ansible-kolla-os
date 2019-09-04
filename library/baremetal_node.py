#!/usr/bin/python

from ansible.module_utils.basic import *

from ansible.module_utils.openstack import openstack_cloud_from_module, openstack_full_argument_spec, openstack_module_kwargs

def _exit_hostvars(module, baremetal, changed=False):
    module.exit_json(changed=changed, node=baremetal)

def _get_baremetal_node_info(baremetal):

    output= {}
    output.update({'name': baremetal.name})
    output.update({'driver': baremetal.driver})
    output.update({'driver_info': baremetal.driver_info})
    output.update({'uuid': baremetal.id})
    output.update({'updated_at': baremetal.updated_at})
    output.update({'properties': baremetal.properties})
    output.update({'power_state': baremetal.power_state})
    output.update({'instance_info': baremetal.instance_info})
    output.update({'instance_id': baremetal.instance_id})
    return output

def _show_baremetal_node(module, cloud, node=None):
    if node:
        b = cloud.baremetal.get_node(node)
        output = _get_baremetal_node_info(b)
        _exit_hostvars(module, output)
    else:
        multi_outputs = []
        baremetal_list = cloud.baremetal.nodes()
        for b in baremetal_list:
            output = _get_baremetal_node_info(b)
            multi_outputs.append(output)
        _exit_hostvars(module, multi_outputs)

def main():

    argument_spec = openstack_full_argument_spec(
        name_or_uuid=dict(required=False),
    )
    module = AnsibleModule(argument_spec)
    sdk, cloud = openstack_cloud_from_module(module)
    try:
        if module.params['name_or_uuid']:
            _show_baremetal_node(module, cloud, module.params['name_or_uuid'])
        else:
            _show_baremetal_node(module, cloud)
    except Exception as e:
        module.fail_json(msg="Error in show baremetal node: %s" % e.message)

if __name__ == '__main__':
    main()
