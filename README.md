# Ansible deploy OS for kolla-ansible with kolla-ansible baremetal
Playbooks for deploy baremetal node for kolla-ansible use openstack baremetal.

# Requirement
* Ansible >= 2.8
* openstacksdk > 0.18
* kolla-ansible baremetal
* git

# Getting Started
> After deploy the node info and nic-configs saved in
> `kolla-servers` folder.
* Edit `config.yaml` defined the role required network, vip, gateway
* Edit `nodes.csv` defined the node info.
* Edit `networks.csv` defined the network info.
* Add base network config files in `nic-configs` folder, named with
  `rolename-config.yaml`, `rolename-mapping.yaml`.
* Deploy OS run `ko full-create-server`
* Deploy complete apply network config `ko apply-nic-config`

# Reconfig network
> Note: ctlplane network doesn't support reconfig.
* Edit `config.yaml` update network in `role_used_network`
* Edit `nodes.csv` update network information
* Update nic configs
* Update config use `ko update-network-config`, update for specify node or group use
  `ko update-network-config -i kolla-os-inventory.yaml --hosts [host]`
* Apply config use `ko apply-nic-config`, apply for specify node or group use
  `ko apply-nic-config -i kolla-os-inventory.yaml --hosts [host]`

# Generate inventory file
* Run `ko generate-inventory`

# Destory all
* Run `ko destory`

# Directories and files
* `kolla-servers` - Save each node config network requuired config
   files.
> `nodename-config.yaml`    - Network config for node.
> `nodename-mapping.yaml`   - Network interface mapping for node.
* `nic-configs`             - Contain `os-nic-config` config base files.
> `rolename-config.yaml`    - Network config base file for role.
> `rolename-mapping.yaml`   - Network interface mapping base file for role.
* `config.yaml`             - Define gateway,vip, and node_required_network.
* `nodes.csv`               - Define nodes
* `networks.csv`            - Define networks

# Docs
[Config nic-config](./nic-configs/README.md)

