# Monty Hall Problem

https://en.wikipedia.org/wiki/Monty_Hall_problem

# Deployment

```bash
# Python3 needs to be installed, one could check with:
which python3

# Execution
python3 monty-hall.py
```

# Deployment (Docker)

```bash
docker build -t mp:1.0.0 .
docker run -it mp:1.0.0

# alternatively
docker-compose run -it monty

# or even
docker-compose -f docker-compose-df.yml run -it monty
```