import sys
sys.path.append(r'E:\projects\github\rpg-game')

inventory = {'лекарство': 0, 'таблетка': 0, 'деньги': 0}

def add_item(item_id, item_value):
    global inventory

    if item_id == 'лекарство':
            
        inventory['лекарство'] += int(item_value)

    elif item_id == 'таблетка':

        inventory['таблетка'] += int(item_value)
        
    elif item_id == 'деньги':

        inventory['деньги'] += int(item_value)
    
def remove_item(item_id, item_value):
    global inventory

    if item_id == 'лекарство':
            
        inventory['лекарство'] -= int(item_value)

    elif item_id == 'таблетка':

        inventory['таблетка'] -= int(item_value)
        
    elif item_id == 'деньги':

        inventory['деньги'] -= int(item_value)
    
def display_items():
    global inventory

    return inventory