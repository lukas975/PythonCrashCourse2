guest_list = ["Ime1", "Ime2", "ime3"]
print(guest_list)
guest_list[1] = "Ime4"
print(guest_list)
guest_list.insert(0, "Ime5")
print(guest_list)
guest_list.insert(2, "Ime6")
print(guest_list)
guest_list.append("Ime7")
print(guest_list)

print(f"Sorry: {guest_list.pop()}")
print(f"Sorry: {guest_list.pop()}")
print(f"Sorry: {guest_list.pop()}")
print(f"Sorry: {guest_list.pop()}")

print(guest_list)
del guest_list[1]
del guest_list[0]
print(guest_list)
