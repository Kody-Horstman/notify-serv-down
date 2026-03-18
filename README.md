# notify-serv-down

## Purpose
Used to identify timeframe of home server network discruption from a computer on the same network.

## Usage
Make executable:
```bash
chmod +x notify-serv-down.py
```

Run:
```bash
.\notify-serv-down.py
```

Run (immune to hangups; daemonized):
```bash
nohup python3 notify-serv-down.py &
```

To kill:
```bash
ps aux | grep notify-serv-down.py
kill <PID>
```
Replace <PID> with the pid of your process.

Kill (one-liner):
```bash
kill <(ps aux | grep notify-serv-down.py | awk 'NR==1 {print $2}')
```