# Ansible role: java

Installs Java OpenJDK on CentOS/RHEL systems.


## Role Variables

* `java_version`:
    - Description: OpenJDK version to install
    - Default: `1.7.0`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.java }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
