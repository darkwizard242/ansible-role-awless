[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-awless.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-awless) ![Ansible Role](https://img.shields.io/ansible/role/47541?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47541?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47541?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awless&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-awless) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-awless?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-awless?color=orange&style=flat-square)

# Ansible Role: awless

Role to install (_by default_) [awless](https://github.com/wallix/awless) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
awless_app: awless
awless_version: 0.1.11
awless_osarch: linux-amd64
awless_dl_url: "https://github.com/wallix/{{ awless_app }}/releases/download/v{{ awless_version }}/{{ awless_app }}-{{ awless_osarch }}.tar.gz"
awless_bin_path: /usr/local/bin
```

### Variables table:

Variable        | Value (default)                                                                                                                  | Description
--------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
awless_app      | awless                                                                                                                           | Defines the app to install i.e. **awless**
awless_version  | 0.1.11                                                                                                                           | Defined to dynamically fetch the desired version to install. Defaults to: **0.1.11**
awless_osarch   | linux-amd64                                                                                                                      | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux-amd64**
awless_dl_url   | <https://github.com/wallix/{{> awless_app }}/releases/download/v{{ awless_version }}/{{ awless_app }}-{{ awless_osarch }}.tar.gz | Defines URL to download the awless binary from.
awless_bin_path | /usr/local/bin                                                                                                                   | Defined to dynamically set the appropriate path to store awless binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **awless**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awless
```

For customizing behavior of role (i.e. specifying the desired **awless** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awless
  vars:
    awless_version: 0.1.10
```

For customizing behavior of role (i.e. placing binary of **awless** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awless
  vars:
    awless_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-awless/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
