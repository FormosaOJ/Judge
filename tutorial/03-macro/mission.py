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
            },
            'tasks': {
                'task': [{
                    'macro': {
                        '__OUTPUT__': 'FIRST',
                        '__TIME_LIMIT__': '500',
                    }
                }, {
                    'macro': {
                        '__OUTPUT__': 'SECOND',
                        '__TIME_LIMIT__': '1000',
                    }
                }, {
                    'macro': {
                        '__OUTPUT__': 'THIRD',
                        '__TIME_LIMIT__': '1500',
                    }
                }],
                'execute': [{
                    'command': [
                        'python3',
                        'hello world.py',
                    ],
                    'time_limit': '__TIME_LIMIT__',
                    'stdout': '__TASK_ID__.__OUTPUT__.txt',
                    'record': {
                        'enable': False,
                    }
                }]
            },
            'final': {
                'execute': [{
                    'command': ['ls'],
                    'stdout': 'output.txt',
                    'record': {
                        'enable': True,
                        'stdout': 1024,
                    }
                }]
            }
        })
    }
    res = requests.post(config.api_url, data=data)
    print(res.status_code)
    print(json.dumps(json.loads(res.text), indent=4, sort_keys=True))
