def hint_username(username):
    if len(username) < 3:
        print("Invalid username, min 3 char long")
    elif len(username) > 15:
        print("Invalid username, max 15 char long")
    else:
        print("Valid Username")
hint_username("Vivek")

number = 10
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

x =0
while x < 5:
    print("Not there yet " + str(x))
    x =x+1
print("x= " + str(x))

def is_power_of_two(n):

  while n % 2 == 0:
    n = n / 2

  if n == 1:
    return True
  return False
print(is_power_of_two(8)) # Should be False

msg = "A kong string"
new_msg = msg.replace("k","l")
#new_msg = msg[:2] + "l" + msg[3:]
print(new_msg)
print(new_msg.index("l"))
print("str" in new_msg)
print(new_msg.index("str"))
print("heloo   how are    ".strip())

Weather = "Rainfall"
print(Weather[:4])

vivek = ["N/W", "DevOps", "Python"]
print(vivek[0])
vivek.append("Cloud")
vivek.insert(0, "Firewall")
print(vivek)
print(vivek[0])
#vivek.insert(23, "Configmgmt")
#vivek.append("Configmgmt")
print(len(vivek))
print(vivek.pop(4))    # returns last element and removes it "Cloud"
print(vivek)
z = [x for x in range(1,101) if x%3==0]
print(z)
gokul = ["301", "302", "303", "304", "305"]
vivek.append("Configmgmt")
vivek.extend(gokul)
print(vivek)















