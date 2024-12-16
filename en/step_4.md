## Run on a schedule

Use a systemd timer to play your cheerful sound every hour.

--- task ---

Create the service file.

```bash
sudo nano /etc/systemd/system/hourly_cheerful.service
```

--- /task ---

--- task ---

Add this content:

```bash
[Unit]
Description=Run play_cheerful Python script

[Service]
ExecStart=/usr/bin/python3 /home/username/play_cheerful.py
Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse/"
```

**Note**: Change `username` to your username.

--- /task ---

--- task ---

Create the timer file.

```bash
sudo nano /etc/systemd/system/hourly_cheerful.timer
```

**Note** The filename (before the .timer extension) is the same as the service. This creates a link to the service.

--- /task ---

--- task ---

Add this content:

```bash
[Unit]
Description=Run hourly_cheerful.service on the hour, every hour

[Timer]
OnCalendar=minutely

[Install]
WantedBy=timers.target
```

**Notes**: 

- This script uses `minutely` frequency so we can test it works easily. We will change the frequency later.

- If you name the files differently (e.g., play_cheerful.service and hourly_cheerful.timer), you must explicitly specify the service name in the `[Timer]` section of the timer file using the `Unit=` directive:

```bash
[Timer]
OnCalendar=minutely
Unit=play_cheerful.service
```

--- /task ---

--- task ---

Save and exit nano by pressing `Ctrl + x` and then press `y` and `Enter` when you are prompted to save.

--- /task ---

--- task ---

Tell systemd to start your timer during the boot sequence.

```bash
sudo systemctl daemon-reload
sudo systemctl enable hourly_cheerful.timer
sudo systemctl start hourly_cheerful.timer
```

--- /task ---

--- task ---

Make sure your headphones or speakers are connected to your Raspberry Pi.

--- /task ---

--- task ---

**Test** your timer works by waiting until the system clock changes to the next minute.

You should hear your cheerful sound every minute.

--- /task ---

--- task ---

Open the timer again.

```bash
sudo nano /etc/systemd/system/hourly_cheerful.timer
```

--- /task ---

--- task ---

Change the value for OnCalendar so it runs on the hour:

```bash
[Timer]
OnCalendar=hourly
```

--- /task ---

--- task ---

Reload, enable and start your timer.

```bash
sudo systemctl daemon-reload
sudo systemctl enable hourly_cheerful.timer
sudo systemctl start hourly_cheerful.timer
```

--- /task ---

--- task ---

You can check your timer by using:

```bash
systemctl list-timers --all
```

--- /task ---

--- task ---

**Test** your timer works by waiting until the system clock changes to the next hour.

You should now hear your cheerful sound every hour.

--- /task ---

### Stopping and disabling the timer

If you want to stop your timer, you can enter:

```bash
sudo systemctl stop hourly_cheerful.timer
```

If you want to disable the timer, you can use:

```bash
sudo systemctl disable hourly_cheerful.timer
```
