contact_info ={"Festa": "123-345",
               "Melina": "333-000"
}
melina_phone = contact_info["Melina"]
print(melina_phone)

contact_info["Melina"]= "444-666"
print(contact_info)

contact_info["Egzonbaba"]= "444-666"
print(contact_info)

del contact_info["Festa"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {

    "Festa":{
        "phone_number" : "123-456",
        "email" : "festa@gmail.com",
        "home_address" : "bregu",
        "birthday" :"03/02/2003"
    },
    "Sara": {
        "phone_number": "123-433",
        "email": "sara@gmail.com",
        "home_address": "bregu",
        "birthday": "05/01/2000"
    },
    "Egzon": {
        "phone_number": "111-456",
        "email": "egzon@gmail.com",
        "home_address": "fk",
        "birthday": "26/02/2008"
    }
}

print(contact_information)

sara_information = contact_information["Sara"]
print(sara_information)

contacts = {
    "Festa":("123-456", "festa@gmail.com"),
    "Sara": ("123-433", "sara@gmail.com"),
    "Egzon": ("111-456","egzon@gmail.com")
}

festa_info = contacts ["Festa"]
phone_number = festa_info[0]
print(phone_number)
email = festa_info[1]
print(email)

phone_number,email = contacts["Festa"]


