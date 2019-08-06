import collections


def order_function(key):
    split = key.split('/')
    return float(split[1])*1000 + float(split[0])

def add_to_dict(dict, key, amount):
    if not key in dict:
        dict[key] = 0
    dict[key] = dict[key] + amount


if __name__ == '__main__':
    beds = [('windows', 140, 190), ('windows', 140, 190), ('windows', 140, 190), ('windows', 140, 190), ('full', 160, 200), ('windows', 120, 190)]
    counter = {}
    for bed in beds:
        add_to_dict(counter, '{0}/14.5/3.2'.format(bed[1] + 10), 4)
        add_to_dict(counter, '{0}/3.2/3.2'.format(bed[1] + 10), 2)
        add_to_dict(counter, '86.5/14.5/3.2', 2)
        if bed[0] == 'full':
            add_to_dict(counter, '{0}/7/3.2'.format(bed[1] + 10), 2)
            add_to_dict(counter, '35/14.5/3.2', 2)
        elif bed[0] == 'windows':
            if bed[1] >= 120:
                add_to_dict(counter, '{0}/7/3.2'.format(round((bed[1] + 10 - 29)/5.0)), 4)
            else:
                add_to_dict(counter, '24/7/3.2', 2)
            add_to_dict(counter, '45/14.5/3.2', 2)
        add_to_dict(counter, '{0}/14.5/3.2'.format(bed[2]), 2)
        if bed[2] == 190:
            add_to_dict(counter, '175/3.2/3.2', 2)
        elif bed[2] == 200:
            add_to_dict(counter, '193/3.2/3.2', 2)
        if bed[1] == 160:
            add_to_dict(counter, '80/7/3.2', 1)
            add_to_dict(counter, '21/7/7', 2)
        elif bed[1] == 180:
            if bed[2] == 190:
                add_to_dict(counter, '170/7/3.2', 1)
            elif bed[2] == 200:
                add_to_dict(counter, '190/7/3.2', 1)
            add_to_dict(counter, '21/7/7', 3)
        if bed[2] == 190:
            add_to_dict(counter, '{0}/9.2/2'.format(bed[1]), 10)
        elif bed[2] == 200:
            add_to_dict(counter, '{0}/9.2/2'.format(bed[1]), 11)

    #print(str(sorted(counter.items(), key=lambda x: order_function(x[0]), reverse=True)).replace(',', ',\n'))

    for wow in sorted(counter.items(), key=lambda x: order_function(x[0]), reverse=True):
        y = wow[0].split('/')
        print('אורן מוקצע פ.ע.               {0}              {1}               {2}'.format(y[1] + '/' + y[2], y[0], wow[1]))
