# Config rolename-config.yaml
This config base on `os-net-config` config, but the `ip_address` and `vlan_id` value replace by Ansible.
You can directly write the ip and vlan id in config file is fine.

Aaliable replace string in config:
> * ip address: network name, example `external`
> * vlan id: networ-name_vlan_id, example `internal_vlan_id`

# Example config and mapping file
* controller-config.yaml:
```
network_config:
  - type: interface
    name: nic1
    use_dhcp: false

  - type: interface
    name: eno1
    use_dhcp: false
    addresses:
      - ip_netmask: ctlplane

  - type: linux_bond
    name: bond0
    bonding_options: "mode=4"
    members:
      - type: interface
        name: enp94s0f1
      - type: interface
        name: enp94s0f0

  - type: vlan
    vlan_id: storage_vlan_id
    device: bond0
    addresses:
      - ip_netmask: storage

  - type: vlan
    vlan_id: external_vlan_id
    device: bond0
    addresses:
      - ip_netmask: external
    routes:
      - default: true
        next_hop: default_gateway

  - type: vlan
    vlan_id: internal_vlan_id
    device: bond0
    addresses:
      - ip_netmask: internal

  - type: vlan
    vlan_id: tunnel_vlan_id
    device: bond0
    addresses:
      - ip_netmask: tunnel
```

* compute-mapping.yaml:
```
interface_mapping:
    nic1: eno2
    nic2: eno3
```
