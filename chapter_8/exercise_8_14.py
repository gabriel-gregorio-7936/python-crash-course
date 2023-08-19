def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    return car_info

car_profile = make_car('BMW', 'BMW M3', color='black', type='4 doors')

print(car_profile)