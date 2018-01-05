import subprocess as sp # needed to execute clear screen

# clear the screen
tmp = sp.call('clear',shell=True)

# create a dictionary
credentials = { "user1": "user1"
              , "user2": "foo"
              , "user3": 1234
              , "user4": "qwerty" }
print( "Printing all users\" passwords:" )
print( "User 1 password: " + str( credentials["user1"] ) )
print( "User 2 password: " + str( credentials["user2"] ) )
print( "User 3 password: " + str( credentials["user3"] ) )
print( "User 4 password: " + str( credentials["user4"] ) )
print( "" )

# add new key value pairs
credentials["user5"] = "peewee"
credentials["user6"] = 789
print( "Printing all registered users" )
print( str( credentials ) + "\n" )

# remove a user
del credentials["user3"]
print( "Printing all registered users" )
print( str( credentials ) + "\n" )

# looping through all entries in a dictionary
print( "Printing all key-value pairs in dictionary:" )
for key, value in credentials.items():
    print( "Key: " + str( key ) )
    print( "Value: " + str( value ) )
print( "" )

# looping through all keys in a dictionary
print( "Printing all keys in dictionary:" )
for key in credentials.keys():
    print( "Key: " + str( key ) )
print( "" )
