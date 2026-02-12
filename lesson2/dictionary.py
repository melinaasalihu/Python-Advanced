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
print(contact_info)