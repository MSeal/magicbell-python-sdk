# magicbell

![magicbell logo purple](./assets/MB_logo_Purple_2800x660.png)

An unofficial Python SDK for [MagicBell](https://magicbell.com).

- API Version: 1.0
- Package Version: 0.1.0

## Requirements

Python 3.8+

## Installation & Usage

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
