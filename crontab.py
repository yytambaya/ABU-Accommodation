from crontab import CronTab
cron = CronTab(tab="""* * * * * command""")
job = cron.new(command='python log.py')
job.minute.every(1)
cron.write()
print("Task is written")
print(job.is_valid())
for job in cron:
    print(job)