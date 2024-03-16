# raspberrypi-tmp

## Poetryを使った方法

### Install

```sh
$ poetry install --no-root --with dev
```

### Add library

```sh
$ poetry shell

$ poetry add [library name]

# for development
$ poetry add -D [library name]
```

## pipを使った方法

### Install

```sh
$ pip3 install -r requirements.txt
```

### Add library

```sh
$ pip3 install [library name]
```

### output library list

```sh
$ pip freeze > requirements.txt
```


## Execute program

`main.py` is entrypoint file

```sh
$ poetry shell
$ python3.9 main.py
$ exit

or

$ source .venv/bin/activate
$ python3.9 main.py
$ deactivate
```
