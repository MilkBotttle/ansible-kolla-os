#!/usr/bin/python

# Copyright: (c) 2010, Cameron Chuang
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

def parse(servers,networks,network_require):
    parsed_config=[]
    for role, nodes in servers.items():
        node_info = {}
        node_info.update({"role": role})
        for node in nodes:
            name = node.keys()[0]
            node_info.update({"name": name})

            if node.values()[0]:
                node_info.update({"baremetal_node": node.values()[0]})
            else:
                node_info.update({"baremetal_node": "random"})

            if networks['ctlplane']['hosts'][name]:
                node_info.update({"ctlplane": networks['ctlplane']['hosts'][name]})
            else:
                node_info.update({"ctlplane": "random"})
            for net in network_require[role]:
                if networks[net]['hosts'][name]:
                    node_info.update({net: networks[net]['hosts'][name]})
                else:
                    node_info.update({net: 'random'})
            parsed_config.append(node_info)

    return parsed_config

def run_module():
    module_args = dict(
        servers=dict(type='dict', required=True),
        networks=dict(type='dict', required=True),
        network_require=dict(type='dict', required=True)
    )

    result = dict(
        changed=True,
        parsed_config=[]
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    result['parsed_config'] = parse(module.params['servers'],
                                    module.params['networks'],
                                    module.params['network_require'])
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
