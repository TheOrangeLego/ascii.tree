# ASCII TREE

A small project that pretty prints an ASCII representation of a data hierarchy tree.

### Execution

To run the project, run the following in the directory of your language of choice

* `py3` - `python3 tree.py <file>`

### Sample

Given the file `data.json` with the content

```
{
  "foo": {
    "bar": {
      "thing1": {},
      "thing2": {}
    },
    "foo": {},
    "foobar": {}
  }
}
```

the project will generate the following output

```
foo/
├── bar/
│   ├── thing1
│   └── thing2
├── foo
└── foobar
```

### Requirements

Below are the requirements to run each language implementation of the project

* `py3` - Python 3.8+
