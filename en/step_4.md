## Run on a schedule

Use a systemd timer to play your cheerful sound every hour.

--- task ---

Create the service file.

```bash
sudo nano /etc/systemd/system/hourly.service
```

--- /task ---

--- task ---

Add this content:

```bash
[Unit]
Description="Run Python script"

[Service]
ExecStart=/usr/bin/python3 /home/username/cheerful.py
Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse/"
```

**Note**: Change `username` to your username.

--- /task ---

--- task ---

Create the timer file.

```bash
sudo nano /etc/systemd/system/hourly.timer
```

--- /task ---

--- task ---

Add this content:

```bash
[Unit]
Description="Run hourly.service on the hour, every hour"

[Timer]
OnCalendar=minutely

[Install]
WantedBy=timers.target
```

**Note**: This script uses `minutely` frequency so we can test it works easily. We will change the frequency later.

--- /task ---

--- task ---

Save and exit nano by pressing `Ctrl + x` and then press `y` and `Enter` when you are prompted to save.

--- /task ---

--- task ---

Tell systemd to start your timer during the boot sequence.

```bash
sudo systemctl daemon-reload
sudo systemctl enable hourly.timer
sudo systemctl start hourly.timer
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
sudo nano /etc/systemd/system/hourly.timer
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
sudo systemctl enable hourly.timer
sudo systemctl start hourly.timer
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

If you want to stop your timer, you can enter:

```bash
sudo systemctl stop hourly.timer
```
