car = 100
space_car = 4
driver = 30
passnger =90
car_not_driven = car - driver
car_driven = driver
car_pool_capacity = car_driven  * space_car
average_passenger  = passnger / car_driven

print " there are", car , "avaiable"
print "There only", driver, "in heere"
print "there has" ,car_not_driven, "empty car"
print "we can trnaspoort" , car_pool_capacity, " people today"
print "we have " , passnger, " passnger today"
print "there are avergage", average_passenger , "peoplein car"
