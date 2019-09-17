#!/bin/bash
set -x
mkdir -p /etc/os-net-config

cat << EOF > /etc/os-net-config/mapping.yaml
{{ mapping_content }}
EOF

cat << EOF > /etc/os-net-config/config.yaml
{{ nic_config_content }}
EOF
os-net-config -d -c /etc/os-net-config/config.yaml 2>&1 | tee /var/log/os-nic-config.log
