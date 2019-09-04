echo "Create deployed server network info"
ansible-playbook main.yaml -t create-network -e deployed_server=true -v
echo "Reconfig network "
ansible-playbook -b -i kolla-os-inventory.yaml os-net-reconfig.yaml "$@"

