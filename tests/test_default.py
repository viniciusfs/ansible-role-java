import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_java_package(Package):
    java = Package('java-1.7.0-openjdk')

    assert java.is_installed
