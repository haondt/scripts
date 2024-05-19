# Docker autostart

Auto start a docker compose stack with systemctl.

1. Create a file at /etc/systemd/system/{your-service}.service with the following contents

```service
[Unit]
Description={My Service}
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory={/path/to/docker_compose_file_dir}
ExecStart=docker compose up -d
ExecStop=docker compose down 
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

2. enable and start the service

```shell
sudo systemctl enable {your-service}
sudo systemctl start {your-service}
```
