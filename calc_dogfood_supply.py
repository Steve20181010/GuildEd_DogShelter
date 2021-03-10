import random

PRM_SMLLDOGS_LBS = 10
PRM_MED_DOGS_LBS = 20
PRM_LRG_DOGS_LBS = 30

PRM_AMT_MULTIPLIER = .2
ALLOWED_DOGS = 30


def calc_order_quantity(s, m, l, lo):

    # print("{},{},{},{}".format(s, m, l, lo))
    amt_all_dogs = int(s)*PRM_SMLLDOGS_LBS + int(m)*PRM_MED_DOGS_LBS + int(l)*PRM_LRG_DOGS_LBS
    amt_minus_lo = amt_all_dogs-int(lo)
    amt_discount_overage = amt_minus_lo*PRM_AMT_MULTIPLIER
    amt_to_order = amt_minus_lo + amt_discount_overage

    return amt_to_order


def validate_input(s,m,l):

    msg = ''
    total_dogs = int(s)+int(m)+int(l)

    if total_dogs > ALLOWED_DOGS:
        msg = "Total number of dogs entered, {}, exceeds number of dogs allowed, {}. Please try again...".format(total_dogs, ALLOWED_DOGS)

    return msg


if __name__ == "__main__":
    print("Enter number of small dogs ==> ")
    small_dog_amt = input()

    print("Enter number of medium dogs ==> ")
    med_dog_amt = input()

    print("Enter number of large dogs ==> ")
    lrg_dog_amt = input()

    print("Enter number of leftover from last month ==> ")
    lft_ovr = input()

    error_msg = validate_input(small_dog_amt, med_dog_amt, lrg_dog_amt)

    if error_msg:
        print("ERROR: {}".format(error_msg))
    else:
        order_amt = calc_order_quantity(small_dog_amt, med_dog_amt, lrg_dog_amt, lft_ovr)
        print("Calulated amount to order: {} lbs of dog food.".format(order_amt))
