invited_person = [ 'Abdul', 'Gafur', 'Nilima','Anwara']
print(invited_person[0]+" You are invited.")
print(invited_person[1]+" you are also invited here.")
invited_person.insert(0,'Nabib')
invited_person.insert(3,'Sujan')
invited_person.append('Ahamed')
message = "Welcome "
print(invited_person)
print(message + invited_person[0])

print(message + invited_person[1])

print(message + invited_person[2])

print(message + invited_person[3])

print(message + invited_person[4])
print(message + invited_person[5])
print(message + invited_person[6])

print(invited_person)

print("I can only invite only two people for dinner.")
sry_msg = " sorry for not inviting."
print(invited_person[-1]+sry_msg)
invited_person.pop()
print(invited_person[-1]+sry_msg)
invited_person.pop()
print(invited_person[-1]+sry_msg)
invited_person.pop()
print(invited_person[-1]+sry_msg)
invited_person.pop()
print(invited_person[-1]+sry_msg)
invited_person.pop()
print(invited_person)

print(invited_person[0] + " you're still invited.")
print(invited_person[1] + " you're still invited.")

del invited_person[0]
del invited_person[0]
print(invited_person)