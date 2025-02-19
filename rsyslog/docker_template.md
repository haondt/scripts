# Docker template

This template allows you to funnel docker logs into rsyslog, centralizing them for easy parsing through something like Grafana Alloy.

### Setup

Ensure rsyslog is installed

```sh
sudo apt install rsyslog
```

Create the template

`/etc/rsyslog.d/docker.conf`

```
template(name="DockerLogFile" type="string" string="/var/log/docker/%programname:8:999%.log")

if $programname startswith 'docker-' then {
  ?DockerLogFile
}
```

Restart rsyslog

```sh
sudo systemctl restart rsyslog
```

Point docker logs at syslog, this can be done per-container

`docker-compose.yml`

```
services:
  myservice:
    ...
    logging:
      driver: syslog
      options:
        tag: docker-myservice
```

this will deposit the logs for `myservice` in `/var/log/docker/myservice.log`.
