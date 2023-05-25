from server import check_upgrade_button

def check_house_level(next_level):
    match next_level:
        case 2:
            upgrade_details = "<ul class = 'fs-2'><li>+ 10 Energy Storage </li> <li> +2 Energy</li> </ul> "
            upgrade_cost = 100
            check_upgrade_button(upgrade_cost)
            return upgrade_details , upgrade_cost 
        case 3:
            upgrade_details = "<ul class = 'fs-2'><li>+ 14 Energy Storage </li> <li> +3 Energy</li> </ul> "
            upgrade_cost = 220
            check_upgrade_button(upgrade_cost)
            return upgrade_details , upgrade_cost 
        case 4:
            upgrade_details = "<ul class = 'fs-2'><li>+ 21 Energy Storage </li> <li> +4 Energy</li> </ul> "
            upgrade_cost = 340
            check_upgrade_button(upgrade_cost)
            return upgrade_details , upgrade_cost 
        case 5:
            upgrade_details = "<ul class = 'fs-2'><li>+ 30 Energy Storage </li> <li> +5 Energy</li> </ul> "
            upgrade_cost = 400
            check_upgrade_button(upgrade_cost)
            return upgrade_details , upgrade_cost 
        case _:
            upgrade_details = "No more Upgrades Available"
            upgrade_cost = 999
            check_upgrade_button(upgrade_cost)
            return upgrade_details , upgrade_cost 




def upgrade_house(house_level,upgrade_cost,money,num_move,energy_storage):
    if house_level+1 == 2:
        house_level += 1
        money -= upgrade_cost
        num_move += 2
        energy_storage += 10
        return house_level, money , num_move , energy_storage
    elif house_level+1 == 3:
        house_level += 1
        money -= upgrade_cost
        num_move += 3
        energy_storage += 14
        return house_level, money , num_move , energy_storage
    elif house_level+1 == 4:
        house_level += 1
        money -= upgrade_cost
        num_move += 4
        energy_storage += 21
        return house_level, money , num_move , energy_storage
    elif house_level+1 == 5:
        house_level += 1
        money -= upgrade_cost
        num_move += 5
        energy_storage += 30
        return house_level, money , num_move , energy_storage