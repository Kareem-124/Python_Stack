


def buy_price(base_price,taxes):
    return (base_price*taxes + base_price)

def sell_price(base_price,taxes):
    return ( base_price - base_price*taxes)

def buy(base_price,money,taxes,num_move):
    base_price = buy_price(base_price,taxes)
    money -= base_price
    num_move += 1
    return money, num_move

def sell(base_price,money,taxes,num_move):
    base_price = sell_price(base_price,taxes)
    money += base_price
    num_move -= 1
    return money, num_move


def check_market_level(next_level):
    base_price = 50
    print(f"I am at the Market_function , next_level balue = {next_level}")
    match next_level:
        case 2:
            upgrade_details = f"<ul class = 'fs-2'><li>Reduce the Taxes by 5% </li> <li> New Buy Price = {buy_price(base_price,0.25)} </li> <li> New Sell Price = {sell_price(base_price,0.25)} </li> </ul> "
            upgrade_cost = 100
            return upgrade_details , upgrade_cost 
        case 3:
            upgrade_details = f"<ul class = 'fs-2'><li>Reduce the Taxes by 5% </li> <li> New Buy Price = {buy_price(base_price,0.20)} </li> <li> New Sell Price = {sell_price(base_price,0.20)} </li> </ul> "
            upgrade_cost = 200
            return upgrade_details , upgrade_cost 
        case 4:
            upgrade_details = f"<ul class = 'fs-2'><li>Reduce the Taxes by 5% </li> <li> New Buy Price = {buy_price(base_price,0.15)} </li> <li> New Sell Price = {sell_price(base_price,0.15)} </li> </ul> "
            upgrade_cost = 300
            return upgrade_details , upgrade_cost 
        case 5:
            upgrade_details = f"<ul class = 'fs-2'><li>Reduce the Taxes by 5% </li> <li> New Buy Price = {buy_price(base_price,0.10)} </li> <li> New Sell Price = {sell_price(base_price,0.10)} </li> </ul> "
            upgrade_cost = 400
            return upgrade_details , upgrade_cost 
        case _:
            upgrade_details = "No more Upgrades Available"
            return upgrade_details , upgrade_cost 
        
def upgrade_market(level,money,upgrade_cost,taxes_value):
    level +=1
    taxes_value -=0.05
    money -= upgrade_cost
    return level , money , taxes_value



