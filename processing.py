import datetime
from statistics import mean

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

import persistance


def plot_days():
    all_weights = persistance.get_all()
    grouped_weights = {}

    for i in all_weights:
        grouped_weights.setdefault(i["date-stamp"].date(), [])
        grouped_weights[i["date-stamp"].date()].append(i["weight"])

    dates = []
    average_weights = []
    for i in grouped_weights:
        dates.append(i)
        average_weights.append(round(mean(grouped_weights[i]), 1))

    plot(dates, average_weights)


def plot_weeks():
    all_weights = persistance.get_all()
    all_dates = []

    for i in all_weights:
        all_dates.append(i["date-stamp"].date())

    grouped_weights = {min(all_dates): []}

    while list(grouped_weights.keys())[-1] < max(all_dates) - datetime.timedelta(days=7):
        grouped_weights[list(grouped_weights.keys())[-1] + datetime.timedelta(days=7)] = []

    i = 0
    for date_weight in all_weights:
        week_bin = list(grouped_weights.keys())[i]
        next_week_bin = week_bin + datetime.timedelta(days=7)
        if date_weight["date-stamp"].date() < next_week_bin:
            grouped_weights[week_bin].append(date_weight["weight"])
        else:
            grouped_weights[next_week_bin].append(date_weight["weight"])
            i += 1

    dates = []
    average_weights = []
    for i in grouped_weights:
        dates.append(i)
        average_weights.append(round(mean(grouped_weights[i]), 1))

    plot(dates, average_weights)


def plot_all():
    all_weights = persistance.get_all()
    weights = []
    date_times = []

    for i in all_weights:
        weights.append(i["weight"])
        date_times.append(i["date-stamp"])

    plot(date_times, weights)


def plot(date_times, weights):
    fig, ax = plt.subplots()

    plt.plot(date_times, weights, marker='o')
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")

    plt.tight_layout()
    plt.gcf().subplots_adjust(bottom=0.20)

    scale_factor = 1.025
    y_min, y_max = plt.ylim()
    plt.ylim(y_min / scale_factor, y_max * scale_factor)

    try:
        x_values = np.linspace(0, 1, len(weights))
        coeffs = np.polyfit(x_values, weights, deg=1)
        poly_eqn = np.poly1d(coeffs)
        y_hat = poly_eqn(x_values)
        plt.plot(date_times, y_hat)
    except ValueError:
        print("Not enough date to draw polyfit")

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    _ = plt.xticks(rotation=45)

    plt.grid(linestyle='--')

    plt.show()


if __name__ == "__main__":
    with plt.style.context('fivethirtyeight'):
        plot_weeks()
