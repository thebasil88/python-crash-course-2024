# Chapter 2
# strings
first_name = "ada"
last_name = "lovelace"
name = f"{first_name} {last_name}"
print(name.title())
print(name.upper())
print(name.lower())

message = f"Hello, {name.title()}"
print(message)

print("Languages:\n\tPython\n\tC\n\tJavascript\n\tPHP")

favorite_language = "python "
print(favorite_language.rstrip())

nonstarch_url = "https://nostarch.com"
print (nonstarch_url.removeprefix("https://"))

# numbers
mynum = 5
my_float = 3.5
#long assign
big_number = 14_000_000_000
#multiassign
x,y,z = 0,0,0

#constants
# no built in contsants, but use all caps
MAX_CONNECTIONS =  5000