Manage privacyidea daily opearations
=======================================

# Overview

The `pi` bundle exposes a set of commands which allow operators to view and
edit details of privacyidea tokens.

By default, *no one* can use this bundle: 
  * `token:list` requires `privacyidea:read`
  * `token:reset` requires `privacyidea:read` (FIXME)

# Installing

In chat:

```
@cog bundle install pi
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
echo 'pi_fqdn: <PI_SERVER_FQDN>' >> config.yaml
echo 'pi_username: <PI_USERNAME>' >> config.yaml
echo 'pi_password: <PI_PASSWORD>' >> config.yaml
cogctl dynamic-config create pi config.yaml
```

# Building

To build the Docker image, simply run:

    $ make docker

Requires Python 3.5.x, pip, make, and Docker.
