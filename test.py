#import utils
from utils import find_max

the_list = list(map(int, input('Enter values : ').split()))
x = find_max(the_list)
print(x)