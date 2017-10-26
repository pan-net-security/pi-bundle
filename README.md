[privacyidea](http://www.privacyidea.org) [cog bundle](http://cog-book.operable.io) 
=======================================

# Overview

The `pi` bundle exposes a set of commands which allow privacyidea operators to view and
edit details of privacyidea objects (tokens, users).

By default, *no one* can use this bundle: 
  * `token:list` requires `pi:read`
  * `token:reset` requires `pi:read` (FIXME to `pi:write`)

# Installing

In chat:

```
/dm @cog bundle install pi
```

From the command line:

```
cogctl bundle install pi
```

# Configuring

The `pi` bundle requires the privacyidea server FQDN, a username
and a password of a user with rights to the realm and objects (tokens, users).
You can set these variables with Cog's dynamic config feature:

```bash
echo -e "---
pi_fqdn: '<PI_SERVER_FQDN>'
pi_username: '<PI_USERNAME>'
pi_password: '<PI_PASSWORD>'" >> config.yaml
cogctl dynamic-config create pi config.yaml
```

# Building

To build the Docker image, simply run:

    $ make docker

Requires Python 3.6.x, pip, make, and Docker.
