import csv
import numpy as np


def pre_viz(day):
    # Tweets per hour
    clock_face = {}
    for j in range(1, 25):
        clock_face['t'+str(j)] = [0]

    with open('./TESTtweets/0{0}_08_2017.csv'.format(day), 'r') as tweets:
        tw_reader = csv.reader(x.replace('\0', '') for x in tweets)
        for row in tw_reader:
            string = row[0]
            temperance = string[11:13]
            for k in range(0, 25):
                if temperance == '0{0}'.format(k):
                    clock_face['t{0}'.format(k+1)][0] += 1
                    break
                if temperance == '{0}'.format(k):
                    clock_face['t{0}'.format(k + 1)][0] += 1
                    break
                k += 1

    # Tweet polarity correlate by hour

    with open('./TESTsentiment/0{0}_08_2017.csv'.format(day), 'r') as thoughts:
        mindreader = csv.reader(x.replace('\0', '') for x in thoughts)
        iterlist = []
        lotlist = [0]
        comps_of_day = []
        for row in mindreader:
            iterlist.append(float(row[0]))
        for hour, lot in clock_face.items():
            lotlist.append(lot[0])
        compsum = 0

        moving_index = 0
        list_for_random_choice = [0]
        proximity_counter = 0
        for x in range(0, 24):
            compounds = iterlist[moving_index:(moving_index+lotlist[x+1])]
            moving_index = moving_index + lotlist[x+1]
            for item in compounds:
                compsum += item
            if compsum < -10:
                compsum = np.random.choice(list_for_random_choice)
            list_for_random_choice.append(compsum)
            proximity_counter += 1
            if proximity_counter > 4:
                del list_for_random_choice[0]
            comps_of_day.append(compsum)
            compsum = 0

    prices_by_hour = []
    with open('./TESTprices/014_08_2017.txt', 'r') as prices:
        pricereader = prices.readlines()
        pricereader = pricereader[::-1]
        for price_time in pricereader:
            new_price_time = price_time.strip('\n')
            if len(str(day)) == 1:
                if '2017-08-0{0}'.format(day) in new_price_time:
                    prices_by_hour.append(new_price_time)
            if len(str(day)) == 2:
                if '2017-08-{0}'.format(day) in new_price_time:
                    prices_by_hour.append(new_price_time)
        prices_of_day = []
        for instance in prices_by_hour:
            temp = instance.split(',')
            price = float(temp[0])
            prices_of_day.append(price)

        del lotlist[0]
        return prices_of_day, comps_of_day, lotlist
