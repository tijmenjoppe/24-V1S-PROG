#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: Lineaire regressie

(c) 2023 Hogeschool Utrecht,
Peter van den Berg (petervandenberg@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
import csv
import matplotlib.pyplot as plt


def gradient_descent(x, y, num_iterations=1000, learning_rate=0.0001):
    """
    Traint de coefficienten a en b voor het lineaire regressiemodel ŷ = a + b * x met de gradient descent methode.

    Args:
        x (list): de onafhankelijke waarden van de observaties
        y (list): de afhankelijke waarden van de observaties
        num_iterations (int): aantal iteraties om te leren
        learning_rate (float): leerconstante

    Returns:
        [float, float]: de berekende coefficienten
    """
    coefficients = [0, 0]
    for _ in range(num_iterations):  # <XXX
        for i in range(len(x)):
            prediction = coefficients[0] + coefficients[1] * x[i]
            error = prediction - y[i]
            coefficients[0] -= error * learning_rate
            coefficients[1] -= error * x[i] * learning_rate  # XXX>

    return coefficients



if __name__ == '__main__':
    lengte = []
    breedte = []

    with open('data_iris.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            lengte.append(float(row[0]))
            breedte.append(float(row[1]))

    print(len(lengte))
    print(len(breedte))

    plt.scatter(lengte, breedte)

    (a, b) = gradient_descent(lengte, breedte, num_iterations=1500, learning_rate=0.0001)
    print(a, b)

    x_1 = 1
    x_2 = 7

    y_1 = a + b * x_1
    y_2 = a + b * x_2

    print('x1', x_1, 'y1', y_1)
    print('x2', x_2, 'y2', y_2)

    plt.plot([x_1, x_2], [y_1, y_2], c='red')

    x_tijmen = 10
    y_tijmen = a + b * x_tijmen

    plt.scatter(x_tijmen, y_tijmen, c='green')

    plt.savefig('iris_scatter.png')
