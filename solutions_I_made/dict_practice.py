#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:21:41 2019

@author: callum
"""
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep_list = cars['Jeep']
    l_out = ''
    for item in jeep_list:
        l_out = l_out + item + ', '
    l_out = l_out[:-2]
    return l_out


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first = []
    for key,item in cars.items():
        first.append(item[0])
    return(first)


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grepped = []
    for key, item in cars.items():
        for car in item:
            if grep.lower() in car.lower():
                grepped.append(car)
    grepped.sort()
    return grepped


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    car_sort = {}
    for key, item in cars.items():
        item.sort()
        car_sort[key] = item
    return car_sort