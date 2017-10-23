Manage privacyidea daily opearations
=======================================

# Overview

The `privacyidea` bundle exposes one command `pi:token_list`, which allow you view and 
edit details of privacyidea tokens.

By default, *no one* can use this bundle: 
  * `token:list` requires `privacyidea:read`
  * `token:delete` requires `privacyidea:write`

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

The `privacyidea` bundle requires your the privacyidea server FQDN, a username
and a password of a user with rights to the realm and objects.
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
