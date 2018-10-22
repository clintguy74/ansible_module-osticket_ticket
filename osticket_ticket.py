#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Carson Anderson <rcanderson23@gmail.com>
# GNU General Public License v3.0+

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import requests


def main():
    argument_spec = dict(
        alert=dict(type=bool, default=True),
        autorespond=dict(type=bool, default=True),
        source=dict(type=str, default="API"),
        email=dict(type=str, required=True),
        name=dict(type=str, required=True),
        subject=dict(type=str, required=True),
        message=dict(type=str, required=True),
        ip=dict(type=str, required=False),
        priority=dict(type=str, required=False),
        api_key=dict(type=str, required=True),
        url=dict(type=str, required=True)
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    result = dict(
        changed=False
    )
    alert = module.params['alert']
    autorespond = module.params['autorespond']
    source = module.params['source']
    email = module.params['email']
    name = module.params['name']
    subject = module.params['subject']
    message = module.params['message']
    ip = module.params['ip']
    priority = module.params['priority']
    api_key = module.params['api_key']
    url = module.params['url']

    payload = {
        "alert": alert,
        "autorespond": autorespond,
        "source": source,
        "email": email,
        "name": name,
        "subject": subject,
        "message": message,
        "ip": ip,
        "priority": priority
    }
    for k, v in payload.items():
        if v is None:
            payload.pop(k, None)
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key
    }
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code == 201:
        result['changed'] = True
        module.exit_json(**result)
    else:
        module.fail_json(msg=r.content)


if __name__ == '__main__':
    main()
