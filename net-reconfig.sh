if [ "x$@" == "x" ]; then
    echo "Need apply host. Use bash net-reconfig.sh -e host=hostname_or_group !"
    echo
    exit 1
fi

echo "Create deployed server network info"
ansible-playbook main.yaml -t create-network -e var_file=deployed.yaml -e deployed_server=true -v
echo "Reconfig network "
ansible-playbook -b -i kolla-os-inventory.yaml os-net-reconfig.yaml "$@"

