# Ansible deploy OS for kolla-ansible with undercloud
Playbooks for deploy baremetal node for kolla-ansible use TripleO
undercloud.

# Requirement
* Ansible >= 2.8,< 2.9
* openstacksdk
* TripleO undercloud
* git

# Install
* Clone `git clone https://github.com/MilkBotttle/ansible-kolla-os.git`
* Copy cli to bin `sudo cp ansible-kolla-os/ko /usr/bin`

# Getting Started
> After create-server the node info and nic-configs saved in
> `kolla-servers` folder.
* Edit `config.yaml` defined the role required network, vip, gateway
* Edit `nodes.csv` defined the node info.
* Edit `networks.csv` defined the network info.
* Add base network config files in `nic-configs` folder, named with
  `rolename-config.yaml`, `rolename-mapping.yaml`.
* Deploy OS run `ko create-server`

# Configure deployed node network or reconfig network
> Note: ctlplane network doesn't support reconfig.
* Edit nic-configs and config files for new network
* Run `ko reconfig-network`, reconfig network for specify node or group 
  `ko reconfig-network -i kolla-os-inventory.yaml --hosts controller`

# Generate inventory file 
* Run `ko generate-inventory`

# Destory all
* Run `ko destory`

# Directories and files
* `kolla-servers` - Save each node config network requuired config
   files.
> `nodename-config.yaml` - Network config for node.
> `nodename-mapping.yaml` - Network interface mapping for node.
* `nic-configs` - Contain `os-nic-config` config base files.
> `rolename-config.yaml` - Network config base file for role.
> `rolename-mapping.yaml` - Network interface mapping base file for role.
* `config.yaml` - Define nodes and networks.

# Docs
[Config nic-config](./nic-configs/README.md)

