# Ansible deploy OS for kolla-ansible with undercloud

# Requirement
* Ansible > 2.4
* openstacksdk
* undercloud

# Getting Started
* Edit `vars.yaml` fit in requirement.
* Edit 
* Deploy OS for kolla-ansible
```
ansible-playbook main.yaml
```
# Configure deployed node
* Edit nic-configs
# Directories
* `kolla-servers` - Contain nic-config, interface-mapping for each node generate by Ansible.
* `nic-configs` - Contain nic-config source file for Ansible generate node's nic-config.

# TODO Feature
[ ] Reconfig network
[ ] Remove node
[ ] Add gen nic-config tag for update nic-config
