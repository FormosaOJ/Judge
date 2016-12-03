# Judge

## WorkFlow
```
Fetch mission.prepare.file
Execute mission.prepare.execute
for task in mission.tasks:
    Replace string with task.macro
    Fetch task.file
    if task.scope.enable:
        Import task.scope.import from current sandbox to new sandbox
        Execute mission.tasks.execute in new sandbox
        Export task.scope.export from new sandbox to current sandbox
    else:
        Execute mission.tasks.execute in current sandbox
Fetch mission.final.file
Execute mission.final.execute
```

## Api

### [POST] /api/missions/ Request

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>token</td>
      <td>String</td>
      <td>Required</td>
      <td></td>
      <td>The access token you get from Formosa Judge Api</td>
    </tr>
    <tr>
      <td><a href="#mission">mission</a></td>
      <td>Stringified Json</td>
      <td>Required</td>
      <td></td>
      <td>The mission is a Stringified json.</td>
    </tr>
  </tbody>
</table>

```
{
    "token": String,
    "mission": Stringify(Json)
}
```

#### mission

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#return">return</a></td>
      <td>Object</td>
      <td>Required</td>
      <td></td>
      <td>When the mission is finished, the result will be sent there.</td>
    </tr>
    <tr>
        <td><a href="#prepare">prepare</a></td>
        <td>Object</td>
        <td>Optional</td>
        <td><pre><code>
{
    "file": {},
    "execute": []
}
        </code></pre></td>
        <td>Prepare stage.</td>
    </tr>
    <tr>
        <td><a href="#tasks">tasks</a></td>
        <td>Object</td>
        <td>Optional</td>
        <td><pre><code>
{
    "task": [],
    "execute": []
}
        </code></pre></td>
        <td>Tasks stage.</td>
    </tr>
    <tr>
        <td><a href="#final">final</a></td>
        <td>Object</td>
        <td>Optional</td>
        <td><pre><code>
{
    "file": {}
    "execute": []
}
        </code></pre></td>
        <td>Final stage.</td>
    </tr>
  </tbody>
</table>

```
"mission": Stringify({
    "return": Object,
    "prepare": Object,
    "tasks": Object,
    "final": Object
})
```

#### return

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>url</td>
      <td>String</td>
      <td>Required</td>
      <td></td>
      <td>This is a callback url. The mission result will be sent to this url with POST method.</td>
    </tr>
    <tr>
      <td>payload</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{}
      </code></pre></td>
      <td>If you have some other arguments, you can place here. For example, you must not want everyone can access the callback url; therefor, you can set a access token. And it must be one level key-value pairs.</td>
    </tr>
  </tbody>
</table>

```
"return": {
    "url": String,
    "payload": Object
}
```

#### prepare
#### final
Prepare and Final are the same format.

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>file</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{}
      </code></pre></td>
      <td>These are key-value pairs. Key is the filename you want it to be in the sandbox and value is the url. It will download from value(url) and save as key(filename).</td>
    </tr>
    <tr>
      <td><a href="#execute">execute</a></td>
      <td>Array</td>
      <td>Optional</td>
      <td><pre><code>
[]
      </code></pre></td>
      <td></td>
    </tr>
  </tbody>
</table>

```
"prepare" or "final": {
    "file": Object,
    "execute": Array
}
```

#### tasks

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#task">task</a></td>
      <td>Array</td>
      <td>Optional</td>
      <td><pre><code>
[]
      </code></pre></td>
      <td>More detail <a href="#task">here</a>.</td>
    </tr>
    <tr>
      <td><a href="#execute">execute</a></td>
      <td>Array</td>
      <td>Optional</td>
      <td><pre><code>
[]
      </code></pre></td>
      <td>More detail <a href="#execute">here</a>.</td>
    </tr>
  </tbody>
</table>

```
"tasks": {
    "task": Array,
    "execute": Array
}
```

#### task

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>file</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{}
      </code></pre></td>
      <td>These are key-value pairs. Key is the filename you want it to be in the sandbox and value is the url, it will download from value(url) and save as key(filename).</td>
    </tr>
    <tr>
      <td>macro</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{}
      </code></pre></td>
      <td>These are key-value pairs. It will replace key with value in the tasks.execute and the filename before execute.<br/> * Macro have a special immutated key-value pair which key is "__TASK_ID__" and value is the index in the task array and counted from 0. </td>
    </tr>
  </tbody>
</table>

```
"task": [{
    "file": Object,
    "macro": Object
}, {
    "file": Object,
    "macro": Object
}, ...]
```

#### execute

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Optional</td>
      <td><pre><code>""</code></pre></td>
      <td>This is an execute name and meaningless for this system, but it may be useful for you. </td>
    </tr>
    <tr>
      <td>command</td>
      <td>Array</td>
      <td>Required</td>
      <td></td>
      <td>What you want to execute. For example: ["ls", "-al"]. And the commands you can use are listed <a href="./command.list">here</a>.</td>
    </tr>
    <tr>
      <td>memory_limit</td>
      <td>Integer</td>
      <td>Optional</td>
      <td><pre><code>65536</code></pre></td>
      <td>How many Kib Bytes this command can use. It should be between 1 and 2097152(1KiB~2GiB). If the command uses more, it will cause error, and the error will be recorded and reported.</td>
    </tr>
    <tr>
      <td>time_limit</td>
      <td>Integer</td>
      <td>Optional</td>
      <td><pre><code>60000</code></pre></td>
      <td>How many millisecond this command can use. It should be between 1 and 60000(1ms~60s). If the command uses more, it will cause error, and the error will be recorded and reported. Specially, this value means how many cpu time the command can use; However, the command can only use 1.5 times this value in real time. (Because the sleep or other relative commands will using few cpu time but consumes a lot of real time. You can try the following command in your terminal: <pre><code>time sleep 10</code></pre>  You can get <pre><code>sleep 10  0.00s user 0.00s system 0% cpu 10.001 total</code></pre>Therefore, we limit the command can only use 1.5 times this value in real time.</td>
    </tr>
    <tr>
      <td>output_limit</td>
      <td>Integer</td>
      <td>Optional</td>
      <td><pre><code>262144</code></pre></td>
      <td>How many Kib Bytes this command can output. It should be between 1 and 262144(1KiB~256MiB). If the command uses more, it will cause error, and the error will be recorded and reported.</td>
    </tr>
    <tr id="meta">
      <td>meta</td>
      <td>String</td>
      <td>Optional</td>
      <td><pre><code>"meta"</code></pre></td>
      <td>After the command is executed, the information will be recorded in this file. It look like the following format: <pre><code>
{
    "status": "",
    "message": "",
    "memory-usage": 8568,
    "cpu-time-usage": 12,
    "real-time-usage": 48
}
      </code></pre>
      If no error occurs during the command is executing, the "status" and "message" will be empty strings; Otherwise, it will tell you what kind of error happened.
      The "memory-usage" is maximum memory used(KiB), the "cpu-time-usage" is cpu time used(ms) and the "real-time-usage" is real time used(ms).
      </td>
    </tr>
    <tr>
      <td>stdin</td>
      <td>String</td>
      <td>Optional</td>
      <td><pre><code>""</code></pre></td>
      <td>If this value is not an empty string, it will redirect standard input from the file.</td>
    </tr>
    <tr>
      <td>stdout</td>
      <td>String</td>
      <td>Optional</td>
      <td><pre><code>""</code></pre></td>
      <td>If this value is not an empty string, it will redirect standard output to the file</td>
    </tr>
    <tr>
      <td>stderr</td>
      <td>String</td>
      <td>Optional</td>
      <td><pre><code>""</code></pre></td>
      <td>If this value is not an empty string, it will redirect standard error to the file</td>
    </tr>
    <tr>
      <td>record</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{
    "enable": true,
    "stdout": 1024,
    "stderr": 1024
}
      </code></pre></td>
      <td>The "enable" is to enable the record, and the stdout/stderr are how many bytes you want to record, these value can be between 0 and 4096 (0 B~4KiB). Carefully, if you don't redirect stdout/stderr to a file, these stdout/stderr value you set is meaningless.
      </td>
    </tr>
    <tr>
      <td>scope</td>
      <td>Object</td>
      <td>Optional</td>
      <td><pre><code>
{
    "enable": false,
    "import": [],
    "export": []
}
      </code></pre></td>
      <td>The "enable" is to enable the scope. If enable the scope, it will run the command in the new sandbox, so it is necessary to import and export files you care. Notice that we will not create directories for your import and export; Therefore, import/export a file to a non-existent directory will occur error. However, import/export a directory is ok. The following are some examples may help you:<pre><code>
In the current sandbox:
/
├── a
    ├── b
    │   └── c
    ├── d
    └── e
Import a and the new sandbox will look like:
/
├── a
    ├── b
    │   └── c
    ├── d
    └── e
Import a/b and the new sandbox will look like:
/
├── b
    └── c
      </code></pre></td>
    </tr>
  </tbody>
</table>

```
"execute": [{
    "name": "",
    "command": [
        String, String, ...
    ],
    "memory_limit": Integer,
    "time_limit": Integer,
    "output_limit": Integer,
    "meta": String,
    "stdin": String,
    "stdout": String,
    "stderr": String,
    "record": {
        "enable": Boolean,
        "stdout": Integer,
        "stderr": Integer,
    },
    "scope": {
        "enable": Boolean,
        "import": [
            String, String, ...
        ],
        "export": [
            String, String, ...
        ],
    }
}, {
    ...
}, ...]
```


### [POST] /api/missions/ Response

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Structure</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>msg</td>
      <td>Object</td>
      <td><pre><code>
{
    "id": Integer
    "payload": Object
}
      </code></pre></td>
      <td>The id represents mission id, and the payload is organized by system.</td>
    </tr>
  </tbody>
</table>

### [POST] /api/missions/ Callback

This result will send to return url you filled with POST method.

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Structure</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>Integer</td>
      <td></td>
      <td>The id represents mission id</td>
    </tr>
    <tr>
      <td>mission</td>
      <td>Object</td>
      <td><pre><code>
{
    "return": {
        "url": String,
        "payload": Object,
    },
    "prepare": {
        "file": Object,
        "execute": Array
    },
    "tasks": {
        "execute": Array,
        "task": [{
            "execute": Array,
// above is new attribute as description
            "macro": Object,
            "file": Object,
        }, {
            ...
        }, ...]
    },
    "final": {
        "file": Object,
        "execute": Array
    }
}
      </code></pre></td>
      <td>It is almost like what you POST. It is only a little different at task, because each task may have different macro. Therefore, it will represents what setting it execute for each task. </td>
    </tr>
    <tr>
      <td>mission_result</td>
      <td>Object</td>
      <td><pre><code>
{
    "prepare": {
        "file": {
            "filename": {
                "status": Integer,
                "content": String
            }
        },
        "execute": [{
            "name": String,
            "meta": {
                "status": String,
                "message": String,
                "cpu-time-usage": Integer,
                "real-time-usage": Integer,
                "memory-usage": Integer
            },
            "record": {
                "stdout": String,
                "stderr": String
            }
        }]
    },
    "task": [{
        "file": Object,
        "execute": Array,
    }, {
        ...
    }, ...],
    "final": {
        "file": Object,
        "execute": Array,
    }
}
      </code></pre></td>
      <td>
        The status of file is what status code when the judge download, if it is not return 200, the judge will treat it as error. And the content of file is first 128 Bytes of the file with base64 encode(due to json cannot store binary string). The content is designer for api user to debug.<br/>
        The name of execute is same as what you submit. The meta is described <a href="#meta">here</a>. And the record stdout/stderr is encode by base64.
      </td>
    </tr>
  </tbody>
</table>

```
{
    "id": Integer,
    "mission": Stringify(Object),
    "mission_result": Stringify(Object),
    ...mission.return.payload
}
```
