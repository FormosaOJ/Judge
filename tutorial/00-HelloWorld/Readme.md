## 00-HelloWorld

This tutorial will help you understand the followings:

1. Post a basic mission to the api server.
2. Receive the callback and parse the mission result.

### Build a callback server

1. First of all, you need to build a callback server. And [here](./../../server) is the tutorial to build it.  
2. Then copy config.py.sample to config.py and set the config.  
3. Run ```python3 mission.py``` to send a basic mission to the api server.  
4. After a few seconds, the response will post to your callback server, and it will look like:

```
{
    "id": "51",
    "mission": {
        "final": {
            "execute": [],
            "file": {}
        },
        "prepare": {
            "execute": [
                {

                    "command": [
                        "echo",
                        "hello world"
                    ],
                    "memory_limit": 65536,
                    "meta": "meta",
                    "name": "",
                    "output_limit": 262144,
                    "record": {
                        "enable": true,
                        "stderr": 1024,
                        "stdout": 1024
                    },
                    "scope": {
                        "enable": false,
                        "export": [],
                        "import": []
                    },
                    "stderr": "",
                    "stdin": "",
                    "stdout": "output.txt",
                    "time_limit": 60000
                }
            ],
            "file": {}

        },
        "return": {
            "payload": {},
            "url": "your callback server url"
        },
        "tasks": {
            "execute": [],
            "task": []
        },
        "tick": false
    },
    "mission_result": {
        "final": {
            "execute": [],
            "file": {}
        },
        "prepare": {
            "execute": [{
                    "meta": {
                        "cpu-time-usage": 0,
                        "memory-usage": 1724,
                        "message": "",
                        "real-time-usage": 43,
                        "status": ""
                    },
                    "name": "",
                    "record": {
                        "stderr": "",
                        "stdout": "aGVsbG8gd29ybGQK"
                    }
                }
            ],
            "file": {}
        },
        "task": []
    }
}
```

The id is mission id given by api server.  
The mission is what you post and add lots of default values, you will understand more clearly how the commands have been executed.  
The mission_result is most important part we care about. Every execute has a meta, it will let you know how many time, memory it used. And the record is encoded by base64. Decoding "aGVsbG8gd29ybGQK" will get "hello world". One more thing you need to keep in mind, if you want to record stdout/stderr, you must set the redirect file with stdout and stderr; Otherwise, it will not be recorded.
