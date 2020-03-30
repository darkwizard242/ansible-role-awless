import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_awless_binary_exists(host):
    assert host.file('/usr/local/bin/awless').exists


def test_awless_binary_file(host):
    assert host.file('/usr/local/bin/awless').is_file


def test_awless_binary_which(host):
    assert host.check_output('which awless') == '/usr/local/bin/awless'
