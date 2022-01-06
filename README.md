# Cron job: Eth Gas Alert
---

### Save program to home directory
```sh

# make a new directory in you home directory
cd ~
mkdir cron_jobs
cd cron_jobs
# save program in the new directory 
```


### Define cron job
```sh
crontab -e
# use 'vi' or 'vim' for an editor unless you have a favorite

# adding the new cron job

# notifications for ETH gas prices
* * * * * ~/cron_jobs/crypo_gas_tracker/py_venv/py/bin/python ~/cron_jobs/crypo_gas_tracker/main.py
```

Confirm the job when closing the editor. You should be good to go now.

## **Note**
This program will send notifications directly to a specific Slack channel. If you are not part of the channel, you will not receive notifications.