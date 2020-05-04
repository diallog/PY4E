#! /usr/bin/env python3

# source: https://wiki.python.org/moin/SimplePrograms
# this is #3

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))
