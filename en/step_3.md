## Run on boot

You can use `systemd` to run your code when Raspberry Pi starts up.

**Note** `systemd` is only available from Jessie versions of the Raspbian OS.

--- task ---

Open Terminal and type:

```bash
sudo nano /lib/systemd/system/greeting.service
```

--- /task ---

--- task ---

Define a new unit 

Set the `Description` to 'Greeting Sound' and set it to run after the multi-user environment is available. 

```bash
[Unit]
Description=Greeting Sound
After=multi-user.target
```

--- /task ---

--- task ---

Configure the service.

1. Set the `Type` to 'idle' so the 'ExecStart' command runs only when everything else has loaded.

1. Set the `ExecStart` parameter to the command to run.

1. Set the `Environment` parameter to allow the sound player to find the pulse audio server.

```bash
[Unit]
Description=Greeting Sound
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/username/start.py
Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse/"
```

**Note** Replace `username` with your username!

--- /task ---

--- task ---

Add a `WantedBy` directive set to 'multi-user.target', so a directory called multi-user.target.wants is created within /etc/systemd/system (if not already available) and a symbolic link to the your unit is placed within. Disabling your unit removes the link and the dependency relationship.

```bash
[Unit]
Description=Greeting Sound
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/username/start.py
Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse/"


[Install]
WantedBy=multi-user.target
```
--- /task ---

--- task ---

Save and exit nano by pressing `Ctrl + x` and then press `y` when you are prompted to save.

--- /task ---

--- task ---

Set the permission on the unit file to `644`.

```bash
sudo chmod 644 /lib/systemd/system/greeting.service
```

--- /task ---

--- task ---

Tell systemd to start your unit file during the boot sequence.

```bash
sudo systemctl daemon-reload
sudo systemctl enable greeting.service
```

--- /task ---

--- task ---

**Test**: Reboot your Raspberry Pi to check your service runs.

```bash
sudo reboot
```

--- /task ---