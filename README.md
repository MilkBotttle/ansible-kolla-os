# Ansible deploy OS for kolla-ansible with undercloud

# Requirement
* Ansible > 2.4
* openstacksdk
* undercloud

# Getting Started
* Edit `config.yaml` defined the nodes and network information
* Add base network config files in `nic-configs` folder, named with `rolename-config.yaml`, `rolename-mapping.yaml`.
* Deploy OS run `./ko create-server`

# Configure deployed node network or reconfig network
> Note: ctlplane network doesn't support reconfig.
* Edit nic-configs and config files for new network
* Run `./ko reconfig-network`, reconfig network for specify node or group `./ko reconfig-network -i kolla-os-inventory.yaml --hosts controller`

# Generate inventory file 
* Run `./ko generate-inventory`

# Directories and files
* `kolla-servers` - Contain config network requuired config files for each node.
> `nodename-config.yaml` - Network config for node.
> `nodename-mapping.yaml` - Network interface mapping for node.
* `nic-configs` - Contain `os-nic-config` config base files.
> `rolename-config.yaml` - Network config base file for role.
> `rolename-mapping.yaml` - Network interface mapping base file for role.
* `config.yaml` - Define node and network.

# Docs
[Config nic-config](./nic-configs/README.md)

