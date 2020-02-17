import collections

existing_pieces = \
    [('180/19.5/3.2', 0),
     ('160/19.5/3.2', 0),
     ('140/19.5/3.2', 0),
     ('200/14.5/3.2', 13),
     ('199/14.5/3.2', 2),
     ('190/14.5/3.2', 20),
     ('189/14.5/3.2', 3),
     ('170/14.5/3.2', 8),
     ('161/14.5/3.2', 2),
     ('160/14.5/3.2', 0),
     ('150/14.5/3.2', 12),
     ('141/14.5/3.2', 4),
     ('140/14.5/3.2', 0),
     ('130/14.5/3.2', 6),
     ('100/14.5/3.2', 8),
     ('90/14.5/3.2', 8),
     ('86.5/14.5/3.2', 18),
     ('45/14.5/3.2', 10),
     ('35/14.5/3.2', 18),
     ('90/9.2/3.2', 12),
     ('180/9.2/2', 33),
     ('160/9.2/2', 22),
     ('140/9.2/2', 32),
     ('120/9.2/2', 22),
     ('90/9.2/2', 32),
     ('80/9.2/2', 22),
     ('190/7/3.2', 6),
     ('170/7/3.2', 5),
     ('161/7/3.2', 4),
     ('160/7/3.2', 0),
     ('150/7/3.2', 8),
     ('141/7/3.2', 3),
     ('140/7/3.2', 0),
     ('130/7/3.2', 3),
     ('120/7/3.2', 5),
     ('100/7/3.2', 3),
     ('90/7/3.2', 2),
     ('80/7/3.2', 4),
     ('28/7/3.2', 13),
     ('24/7/3.2', 25),
     ('23/7/3.2', 0),
     ('20/7/3.2', 36),
     ('196/3.2/3.2', 18),
     ('193/3.2/3.2', 9),
     ('190/3.2/3.2', 8),
     ('180/3.2/3.2', 0),
     ('176/3.2/3.2', 0),
     ('175/3.2/3.2', 14),
     ('170/3.2/3.2', 6),
     ('161/3.2/3.2', 6),
     ('160/3.2/3.2', 0),
     ('156/3.2/3.2', 24),
     ('150/3.2/3.2', 8),
     ('141/3.2/3.2', 3),
     ('140/3.2/3.2', 0),
     ('136/3.2/3.2', 6),
     ('130/3.2/3.2', 8),
     ('126/3.2/3.2', 1),
     ('120/3.2/3.2', 3),
     ('100/3.2/3.2', 4),
     ('90/3.2/3.2', 2)]

previous_addition = \
    [('160/19.5/3.2', 2),
     ('200/14.5/3.2', 2),
     ('199/14.5/3.2', 0),
     ('190/14.5/3.2', 9),
     ('189/14.5/3.2', 2),
     ('170/14.5/3.2', 20),
     ('161/14.5/3.2', 0),
     ('150/14.5/3.2', 6),
     ('141/14.5/3.2', 4),
     ('130/14.5/3.2', 0),
     ('100/14.5/3.2', 0),
     ('90/14.5/3.2', 0),
     ('86.5/14.5/3.2', 24),
     ('45/14.5/3.2', 0),
     ('35/14.5/3.2', 8),
     ('90/9.2/3.2', 0),
     ('180/9.2/2', 5),
     ('160/9.2/2', 44),
     ('140/9.2/2', 9),
     ('120/9.2/2', 0),
     ('90/9.2/2', 6),
     ('80/9.2/2', 0),
     ('190/7/3.2', 0),
     ('170/7/3.2', 0),
     ('161/7/3.2', 0),
     ('150/7/3.2', 3),
     ('141/7/3.2', 3),
     ('130/7/3.2', 0),
     ('120/7/3.2', 0),
     ('100/7/3.2', 0),
     ('90/7/3.2', 2),
     ('80/7/3.2', 3),
     ('28/7/3.2', 0),
     ('24/7/3.2', 0),
     ('23/7/3.2', 0),
     ('20/7/3.2', 0),
     ('196/3.2/3.2', 0),
     ('193/3.2/3.2', 0),
     ('190/3.2/3.2', 0),
     ('176/3.2/3.2', 8),
     ('175/3.2/3.2', 0),
     ('170/3.2/3.2', 7),
     ('161/3.2/3.2', 0),
     ('160/3.2/3.2', 0),
     ('156/3.2/3.2', 0),
     ('150/3.2/3.2', 3),
     ('141/3.2/3.2', 2),
     ('136/3.2/3.2', 0),
     ('130/3.2/3.2', 0),
     ('126/3.2/3.2', 0),
     ('120/3.2/3.2', 0),
     ('100/3.2/3.2', 0),
     ('90/3.2/3.2', 0)]

def order_function(key):
    split = key.split('/')
    return float(split[1]) * 10000 + float(split[2]) * 100 + float(split[0]) * 1


def add_to_dict(dict, key, amount):
    if not key in dict:
        dict[key] = 0
    dict[key] = dict[key] + amount


if __name__ == '__main__':

    beds = [('windows', 160, 200), ('windows', 160, 190), ('full', 160, 190), ('full', 160, 200),
           ('windows', 140, 190), ('full', 140, 190), ('full', 140, 200), ('full', 140, 200), ('full', 120, 190), ('full', 80, 190),
           ('full', 90, 200), ('full', 180, 200), ('full', 120, 200)]
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
                add_to_dict(counter, '{0}/7/3.2'.format(round((bed[1] + 10 - 29) / 5.0)), 4)
            else:
                add_to_dict(counter, '{0}/7/3.2'.format(round((bed[1] + 10 - 29) / 3.0)), 2)
            add_to_dict(counter, '45/14.5/3.2', 2)
        add_to_dict(counter, '{0}/14.5/3.2'.format(bed[2]), 2)
        if bed[2] == 190:
            add_to_dict(counter, '175/3.2/3.2', 2)
        elif bed[2] == 200:
            add_to_dict(counter, '193/3.2/3.2', 2)
        if bed[1] == 160:
            add_to_dict(counter, '80/7/3.2', 1)
            # add_to_dict(counter, '21/7/7', 2)
        elif bed[1] == 180:
            if bed[2] == 190:
                add_to_dict(counter, '170/7/3.2', 1)
            elif bed[2] == 200:
                add_to_dict(counter, '190/7/3.2', 1)
            # add_to_dict(counter, '21/7/7', 3)
        if bed[2] == 190:
            add_to_dict(counter, '{0}/9.2/2'.format(bed[1]), 10)
        elif bed[2] == 200:
            add_to_dict(counter, '{0}/9.2/2'.format(bed[1]), 11)


    bed_heads = [('C', 120), ('C', 140), ('C', 140), ('C', 160), ('C', 160), ('C', 180), ('full', 140), ('full', 160), ('D', 140), ('D', 160), ('4pillows', 140),
                 ('4pillows', 140), ('4pillows', 160), ('4pillows', 160), ('4pillows', 160) , ('4pillows', 180), ('C', 180)]
    #bed_heads = []
    for bed_head in bed_heads:
        if bed_head[0] == 'full':
            add_to_dict(counter, '{0}/14.5/3.2'.format(bed_head[1]), 2)
            add_to_dict(counter, '{0}/3.2/3.2'.format(bed_head[1]), 1)
            add_to_dict(counter, '{0}/7/3.2'.format(bed_head[1]), 1)
            add_to_dict(counter, '86.5/14.5/3.2', 2)
        if bed_head[0] == 'windows':
            add_to_dict(counter, '{0}/14.5/3.2'.format(bed_head[1]), 2)
            add_to_dict(counter, '{0}/3.2/3.2'.format(bed_head[1]), 1)
            if bed_head[1] >= 120:
                add_to_dict(counter, '{0}/7/3.2'.format(round((bed_head[1] - 29) / 5.0)), 2)
            else:
                add_to_dict(counter, '22/7/3.2', 1)
            add_to_dict(counter, '86.5/14.5/3.2', 2)
        if bed_head[0] == 'C':
            add_to_dict(counter, '{0}/3.2/3.2'.format(bed_head[1] + 16), 6)
            add_to_dict(counter, '90/9.2/3.2', 2)
        if bed_head[0] == 'D':
            add_to_dict(counter, '{0}/14.5/3.2'.format(bed_head[1]), 2)
            add_to_dict(counter, '{0}/3.2/3.2'.format(bed_head[1]), 2)
            add_to_dict(counter, '86.5/14.5/3.2', 2)
        if bed_head[0] == '4pillows':
            add_to_dict(counter, '{0}/19.5/3.2'.format(bed_head[1]), 2)
            add_to_dict(counter, '{0}/3.2/3.2'.format(bed_head[1]), 1)
            add_to_dict(counter, '86.5/14.5/3.2', 2)


    framed_jewish_beds = [('full', 180, 200), ('windows', 160, 190), ('full', 160, 190)]
    #framed_jewish_beds = []
    for framed_jewish_bed in framed_jewish_beds:
        add_to_dict(counter, '{0}/14.5/3.2'.format(framed_jewish_bed[1] + 10), 4)
        add_to_dict(counter, '{0}/3.2/3.2'.format(framed_jewish_bed[1] + 10), 2)
        if framed_jewish_bed[0] == 'full':
            add_to_dict(counter, '{0}/7/3.2'.format(framed_jewish_bed[1] + 10), 2)
        if framed_jewish_bed[0] == 'windows':
            add_to_dict(counter, '{0}/7/3.2'.format(round((framed_jewish_bed[1] + 10 - 29) / 7)), 6)
        add_to_dict(counter, '86.5/14.5/3.2', 3)
        add_to_dict(counter, '45/14.5/3.2', 3)
        add_to_dict(counter, '{0}/14.5/3.2'.format(framed_jewish_bed[2]), 1)
        add_to_dict(counter, '{0}/14.5/3.2'.format(framed_jewish_bed[2] - 1), 1)

    # print(str(sorted(counter.items(), key=lambda x: order_function(x[0]), reverse=True)).replace(',', ',\n'))

    counter_sorted = sorted(counter.items(), key=lambda x: order_function(x[0]), reverse=True)

    for wow in counter_sorted:
        y = wow[0].split('/')
        print('אורן מוקצע פ.ע.               {0}              {1}               {2}'.format(y[1] + '/' + y[2], y[0],
                                                                                            wow[1]))

    print('now considering what we have')

    counter_diff = [(key, value-dict(existing_pieces)[key]) for (key,value) in counter_sorted if value-dict(existing_pieces)[key] > 0]

    for wow in counter_diff:
        y = wow[0].split('/')
        print('אורן מוקצע פ.ע.               {0}              {1}               {2}'.format(y[1] + '/' + y[2], y[0],
                                                                                            wow[1]))

    # res = [(key, value + dict(previous_addition)[key])for (key, value) in previous_existing_pieces]
    #
    # res = [(key, value - (counter[key] if key in counter else 0)) for (key, value) in res]
    #
    # for wow in res:
    #     y = wow[0].split('/')
    #     print('אורן מוקצע פ.ע.               {0}              {1}               {2}'.format(y[1] + '/' + y[2], y[0],
    #                                                                                         wow[1]))