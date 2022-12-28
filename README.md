# oanda_accessor_pyv20
This app lets you easily load candle data of Foreign Currency from Oanda API.

## Dependencies

You have to setup followging packages or modules on your host machine.

- docker
- docker compose

## Setup development environment

```bash
$ docker compose build
$ docker compose run package_base bash

# Run unit test
/opt# pipenv run pytest
```

## How to use


```bash
$ pipenv run python
Loading .env environment variables...
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Python 3.8.1 (default, Feb  2 2020, 08:37:37) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

```python
# TODO: modify after making a module
>>> from oanda_accessor_pyv20 import OandaInterface
>>> o_interface = OandaInterface(instrument="GBP_JPY", account_id="101-000-00000000-000", access_token="11111111222222221111111122222222-11111111222222221111111122222222")
>>> result = o_interface.load_specify_length_candles()
>>> result["candles"]
       open     high      low    close  volume  complete                 time
0   160.006  160.052  159.995  160.044     968      True  2022-12-23 17:00:00
1   160.046  160.066  160.004  160.056     728      True  2022-12-23 17:05:00
...
58  159.988  160.121  159.954  160.015     629      True  2022-12-23 21:50:00
59  160.010  160.138  159.952  160.029     166      True  2022-12-23 21:55:00
```
