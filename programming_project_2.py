x = int (input ("How many days has passed since the voyager launched?:"))
y = 917784
z = x*y
milestokm = z*1.609344
milestoau = z/92955887.6
milestoly = x/186282.397051

print ("It has moved",z,"miles from earth")
print ("It has moved",milestokm,"kilometers from earth")
print ("It has moved",milestoau,"astronimical units from earth")
print ("It has moved",milestoly,"lightyears from earth")
