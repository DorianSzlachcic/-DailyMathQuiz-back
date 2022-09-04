from apscheduler.schedulers.blocking import BlockingScheduler
from os.path import exists
import json

from equation import generate_equation

sched = BlockingScheduler()

@sched.scheduled_job("cron", day_of_week="*", hour=0)
def generate_equations_to_json_file():
    data = {}
    n = 2
    for i in range(1,11):
        data[i] = str(generate_equation(n, -2*i + 35))
        n += 1 if i % 4 == 0 else 0
    
    with open('equations.json','w') as file:
        json.dump(data, file)


if(not exists('equations.json')):
    generate_equations_to_json_file()

sched.start()