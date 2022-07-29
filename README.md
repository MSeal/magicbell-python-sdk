# MagicBell-Python SDK

<p align="center"><img src="https://assets.noteable.io/github/2022-07-29/MB_logo_Purple_2800x660.png" width="50%" alt="magicbell logo purple"></p>
<p align="center">
This SDK provides convenient access to the <a href="https://magicbell.com/docs/rest-api/overview">MagicBell REST API</a> from applications written in Python. 
It includes helpers for creating notifications, managing users, managing projects, and executing GraphQL.
</p>
<p align="center">
<a href="https://github.com/noteable-io/magicbell-python-sdk/actions/workflows/ci.yaml">
    <img src="https://github.com/noteable-io/magicbell-python-sdk/actions/workflows/ci.yaml/badge.svg" alt="CI" />
</a>
<a href="https://codecov.io/gh/noteable-io/magicbell-python-sdk" > 
 <img src="https://codecov.io/gh/noteable-io/magicbell-python-sdk/branch/main/graph/badge.svg?token=RGNWOIPWC0" alt="codecov code coverage"/> 
 </a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/magicbell" />
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/magicbell" />
<img alt="PyPI" src="https://img.shields.io/pypi/v/magicbell">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

---------

This is an unofficial Python SDK for [MagicBell](https://magicbell.com) open sourced with ❤️ by <a href="https://noteable.io">Noteable</a>, a collaborative notebook platform that enables teams to use and visualize data, together.

[Install](#installation) | [Getting Started](#getting-started) | [Examples](./examples) | [License](./LICENSE) | [Code of Conduct](./CODE_OF_CONDUCT.md) | [Contributing](./CONTRIBUTING.md)


## Requirements

Python 3.8+

## Installation

### Poetry

```shell
poetry add magicbell
```

Then import the package:

```python
import magicbell
```

### Pip
```shell
pip install magicbell
```

Then import the package:

```python
import magicbell
```

## Getting Started

```python
import magicbell
from magicbell.configuration import Configuration

config = Configuration(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
)
async with magicbell.MagicBell(config) as mb:
    # Send a notification
    await mb.realtime.create_notification(
        magicbell.WrappedNotification(
            notification=magicbell.Notification(
                title="My first notification from python!",
                recipients=[magicbell.Recipient(email="dan@example.com")],
            )
        )
    )
```

### Authentication

Most API calls require your MagicBell project API Key and API Secret.
Some API calls (i.e. projects) require your MagicBell user JWT (enterprise only).

See the [MagicBell API documentation](https://www.magicbell.com/docs/rest-api/reference#authentication) for more information.

### Configuration

Configuration can be done explicitly using the `magicbell.Configuration` class,
or implicitly by setting environment variables with the `MAGICBELL_` prefix.

#### Explicit Configuration

```python
from magicbell.configuration import Configuration


# Create a configuration object with the required parameters
config = Configuration(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
)
```

#### Implicit Configuration

```shell
export MAGICBELL_API_KEY="YOUR_API_KEY"
export MAGICBELL_API_SECRET="YOUR_API_SECRET"
```

```python
from magicbell.configuration import Configuration


config = Configuration()
```

### Examples

For more examples see the [`examples` directory](./examples).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

-------

<p align="center">Open sourced with ❤️ by <a href="https://noteable.io">Noteable</a> for the community.</p>

<img href="https://pages.noteable.io/private-beta-access" src="https://assets.noteable.io/github/2022-07-29/noteable.png" alt="Boost Data Collaboration with Notebooks">

