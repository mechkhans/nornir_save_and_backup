#!/usr/bin/env python3
import pathlib
from nornir import InitNornir
from nornir_utils.plugins.tasks.files import write_file
from nornir_scrapli.tasks import send_commands

""" 
   initiate the nr function to point to the inventory files 
"""

nr = InitNornir(config_file="inventory/config.yaml")

""" 
    use nornir filters to group devices by platform.
    
"""

eosd = nr.filter(platform="eos")
iosd = nr.filter(platform="ios")
junosd = nr.filter(platform="junos")

""" 
    - collect_config function creates the config directory if absent. 
    - has commands section to include different commands on different flavors of OS.
"""


def collect_config(task):
    config_dir = "configs"
    entry_dir = config_dir + "/" + str(task.host.groups[0])
    pathlib.Path(config_dir).mkdir(exist_ok=True)
    pathlib.Path(entry_dir).mkdir(exist_ok=True)

    commands = {"junos": ["show configuration | display set"],
                "eos": ["copy running-config startup-config", "show running-config"],
                "ios": ["write memory", "show running-config"]}

    write_contents = []

    out = task.run(task=send_commands, commands=commands[task.host.platform])

    write_contents.append(out.result)

    task.run(task=write_file, content=", ".join(write_contents),
             filename=f"" + str(entry_dir) + "/" + str(task.host.name) + ".txt")


def main():
    main_result = eosd.run(task=collect_config)
    main_result = iosd.run(task=collect_config)
    main_result = junosd.run(task=collect_config)


main()
