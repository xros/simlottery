import random
__author__ = "Alexander Liu"

class RandomLottery(object):
    """To generate random lottery numbers
    """

    lottery_numbers = []
    number_amount = 6
    number_range = (1, 49)
    unique = False
    sort = True

    def __init__(self, number_amount=6, number_range=(1,49), unique=False, sort=True):
        """
        number_amount   :   lottery number amount, type int
        number_range    :   lottery number range, type tuple 
        unique          :   True -  number unique, False - number duplicated
        sort            :   True -  return sorted number, False - not sorted
        """
        self.number_amount=number_amount
        self.number_range=number_range
        self.unique = unique

    def get_number_list(self):

        x = 0 

        # not unique
        if not self.unique:
            tmp_list_not_unique = []
            while x < self.number_amount:
                x += 1
                the_random_int = random.randint(self.number_range[0], self.number_range[-1])
                tmp_list_not_unique.append(the_random_int)
                self.lottery_numbers = tmp_list_not_unique 
        # unique
        else:
            tmp_list = []
            while x < self.number_amount:
                x += 1
                while True:
                    the_random_int = random.randint(self.number_range[0], self.number_range[-1])
                    if the_random_int in tmp_list:
                        # Do not break the loop, and re-generate a new random int
                        pass
                    else:
                        # Break the inner loop
                        tmp_list.append(the_random_int)
                        break
            self.lottery_numbers = tmp_list

        if self.sort:
            self.lottery_numbers.sort()

        return self.lottery_numbers




# The simple script demo 
#lottery_numbers = []
#x = 0
#
#while x < 6:
#    lottery_numbers.append(random.randint(1, 49))
#    x += 1
#
#lottery_numbers.sort()
#
#print(lottery_numbers)
