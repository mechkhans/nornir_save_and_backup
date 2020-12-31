# nornir_save_and_backup
Save and Backup configurations of your network equipment by using Nornir and Scrapli.

The python script named "nornir_save_and_backup.py" is pretty lightweight, and has been kept as simple as possible.

In its simplest explanation, Nornir works with yaml files that feed information to the code.

-- The directory named Inventory stores 4 yaml files:

   - hosts.yaml
   - groups.yaml
   - defaults.yaml

- hosts.yaml as the name implies contains the management information (hostname, and mgmt IP) for network devices.

- groups.yaml classifies devices into their respective operation system and/or vendors.

- defaults.yaml can or cannot be empty, but as we would use the same creds for all of our devices, defaults.yaml has the read-only (RO) creds in it. 

- config.yaml makes use of the YAMLInventory plugin for grouping the hosts, groups, and defaults.
(https://github.com/nornir-automation/nornir_utils/blob/master/nornir_utils/plugins/inventory/yaml_inventory.py)

collect_config function in the script first creates a directory called 'configs' if not already present, and then creates directories per the name of platform (a.k.a vendor), and finally writes file with name of the txt file same as the hostname of the device.

A few notes on Scrapli:

- Enable secret in Scrapli is passed with 'auth_secondary' keyword, if 'auth_secondary' is specified under a host, then scrapli would escalate privelege without any user intervention.

- If you chose telnet as transport, you would need to specify the port number.

- If there are unique username and passwords for whatever reason, take a look at the inventory/hosts.yaml for an example on how to set unique username, password, and enable secret password. Also the hosts.yaml has an example for use-cases in brownfield networks.