import requests
import os
from datetime import date


def request_and_write(fname):
    r = requests.get('https://leetcode.com/api/problems/all/')
    data = r.json()
    questions = data['stat_status_pairs']

    with open(fname, 'w+') as f:
        f.writelines(
            'question_id, title, difficulty, total_submitted, total_accepted\n')
        for q in questions[:5]:
            s = q['stat']
            question_id = s['frontend_question_id']
            title = s['question__title']
            difficulty = q['difficulty']['level']
            total_submitted = s['total_submitted']
            total_acepted = s['total_acs']
            f.writelines(','.join(map(
                str, [question_id, title, difficulty, total_submitted, total_acepted])) + '\n')

fname = "authenticated-question-{}.csv".format(date.today().strftime("%Y-%m-%d"))
if fname not in os.listdir():
    request_and_write(fname)
