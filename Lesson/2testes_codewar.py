eggs = int(input("Eggs"))
max_eggs_in_pot = 8
max_eggs_in_minutes = 5
timer = 0


    
if eggs > 0:
    eggs_total = eggs * max_eggs_in_minutes
    total_minutes = eggs_total / max_eggs_in_minutes
    print(total_minutes)
else:
    print("enter only positive numbers")