#!/usr/bin/env python3

import json

import requests

import config

if __name__ == "__main__":
    data = {
        'token': config.token,
        'mission': json.dumps({
            'return': {
                'url': config.return_url,
            },
            'prepare': {
                'file': {
                    'hello world.py': 'https://raw.githubusercontent.com/FormosaOJ/Judge/master/tutorial/01-HelloWorld-File/hello%20world.py'
                },
                'execute': [{
                    'command': [
                        'python3',
                        'hello world.py',
                    ],
                    'stdout': 'command0.txt',
                    'record': {
                        'enable': False,
                    }
                }, {
                    'command': [
                        'python3',
                        'hello world.py',
                    ],
                    'stdout': 'command1.txt',
                    'record': {
                        'enable': False,
                    },
                    'scope': {
                        'enable': True,
                        'import': ['hello world.py']
                    }
                }, {
                    'command': [
                        'python3',
                        'hello world.py',
                    ],
                    'stdout': 'command2.txt',
                    'record': {
                        'enable': False,
                    },
                    'scope': {
                        'enable': True,
                        'import': ['hello world.py'],
                        'export': ['command2.txt'],
                    }
                }, {
                    'command': [
                        'ls',
                    ],
                    'stdout': 'command3.txt',
                    'record': {
                        'stdout': 1024,
                    }
                }]
            }
        })
    }
    res = requests.post(config.api_url, data=data)
    print(res.status_code)
    print(json.dumps(json.loads(res.text), indent=4, sort_keys=True))
