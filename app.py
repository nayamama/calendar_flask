import os
from flask import Flask, render_template, request, jsonify, g
import datetime
from calendar import HTMLCalendar
from helpers import AppCalendar
import pytz
import configparser

app = Flask(__name__, static_url_path='/static')
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


@app.context_processor
def get_date():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Shanghai"))
    context = {
        "year": pst_now.year,
        "month": pst_now.month,
        "day": pst_now.day,
        "hour": pst_now.hour,
        "minute": pst_now.minute,
        "weekday": pst_now.weekday()
    }
    return context


@app.route('/')
def hello_world():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Shanghai"))
    str_month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    context = {
        "year": pst_now.year,
        "month": pst_now.month,
        "month_str": str_month[pst_now.month],
        "next_month_str": str_month[pst_now.month + 1],
        "day": pst_now.day,
        "hour": pst_now.hour,
        "minute": pst_now.minute,
        "weekday": pst_now.weekday(),
        #"month_table": HTMLCalendar(firstweekday=pst_now.weekday()).formatmonth(pst_now.year, pst_now.month, True)
    }
    table = AppCalendar().formatmonth(pst_now.year, pst_now.month, True)
    return render_template('index.html', table=table, context=context)


@app.route('/<name>')
def hello_name(name):
    return "hello {}".format(name)


if __name__ == '__main__':
    app.run()
