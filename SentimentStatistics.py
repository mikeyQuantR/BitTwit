import numpy as np


def analyzer(list_of_compounds, fcountlist, date):
    maxfollow = max(fcountlist)
    lot = maxfollow/10
    i = 0
    while i < len(fcountlist):
        if fcountlist[i] >= 9*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.9
        if 8*lot <= fcountlist[i] < 9*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.8
        if 7 * lot <= fcountlist[i] < 8*lot:
            list_of_compounds[i] = list_of_compounds[i]* 1.7
        if 6*lot <= fcountlist[i] < 7*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.6
        if 5*lot <= fcountlist[i] < 6*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.5
        if 4*lot <= fcountlist[i] < 5*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.4
        if 3*lot <= fcountlist[i] < 4*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.3
        if 2*lot <= fcountlist[i] < 3*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.2
        if 1*lot <= fcountlist[i] < 2*lot:
            list_of_compounds[i] = list_of_compounds[i]*1.1
        if 0 <= fcountlist[i] < lot:
            list_of_compounds[i] = list_of_compounds[i]*1

    variance = np.var(list_of_compounds, ddof=1)
    median = np.median(list_of_compounds)
    average = np.average(list_of_compounds)

    statstr = '{0},{1},{2}'.format(variance, median, average)

    with open('./stats/{0}_{1}_{2}.txt'.format(date.tm_mday, date.tm_mon, date.tm_year), 'w+') as statsfile:
        statsfile.write(statstr)
        statsfile.close()