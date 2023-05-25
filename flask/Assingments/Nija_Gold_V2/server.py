from flask import Flask, render_template, redirect, request, session
import random
import datetime
from init import init
from house import *
from market_fun import *

app = Flask(__name__)
app.secret_key = '1234'

level_bonus = 1
def upgrade_farm_lv2(farm_level, upgrade_cost =0):
    global level_bonus
    if (farm_level+1) == 2:
        level_bonus = 1.25
        session['farm_level'] += 1 
        session['num_move'] -= 1
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Farm ! Your Farm Level now is (lvl{session["farm_level"]})  .... {date.strftime("%c")}</span>')

        return redirect('/')
    
    elif (farm_level+1) == 3:
        level_bonus = 1.50
        session['farm_level'] += 1 
        session['num_move'] -= 2
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Farm ! Your Farm Level now is (lvl{session["farm_level"]})  .... {date.strftime("%c")}</span>')
        return redirect('/')
    
    elif (farm_level+1) == 4:
        level_bonus = 2
        session['farm_level'] += 1 
        session['num_move'] -= 3
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Farm ! Your Farm Level now is (lvl{session["farm_level"]})  .... {date.strftime("%c")}</span>')
        return redirect('/')
    
    elif (farm_level+1) == 5:
        level_bonus = 2.25
        session['farm_level'] += 1 
        session['num_move'] -= 7
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Farm ! Your Farm Level now is (lvl{session["farm_level"]})  .... {date.strftime("%c")}</span>')
        return redirect('/')
    
################# Cave Upgrade Function ################################
def upgrade_cave(cave_level,upgrade_cost):
    if (cave_level+1) == 2:
            session['cave_treasure_chance'] += 5
            session['cave_lower_income'] += 5
            session['cave_max_income'] += 5
            session['cave_level'] += 1 
            session['num_move'] -= 1
            session['money'] -= upgrade_cost
            check_upgrade_button()
            session['invest_window'] = False
            date = datetime.datetime.now()
            session['activity_list'].append(
                f'<span class="bg_light_blue"> You Level up your Cave ! Your Cave Level now is (lvl{session["cave_level"]})  .... {date.strftime("%c")}</span>')

            return redirect('/')
        
    elif (cave_level+1) == 3:
        session['cave_treasure_chance'] += 5
        session['cave_lower_income'] += 5
        session['cave_max_income'] += 5
        session['cave_level'] += 1 
        session['num_move'] -= 1
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Cave ! Your Cave Level now is (lvl{session["cave_level"]})  .... {date.strftime("%c")}</span>')

        return redirect('/')
    
    elif (cave_level+1) == 4:
        session['cave_treasure_chance'] += 5
        session['cave_lower_income'] += 10
        session['cave_max_income'] += 10
        session['cave_level'] += 1 
        session['num_move'] -= 1
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Cave ! Your Cave Level now is (lvl{session["cave_level"]})  .... {date.strftime("%c")}</span>')

        return redirect('/')
    
    elif (cave_level+1) == 5:
        session['cave_treasure_chance'] += 5
        session['cave_lower_income'] += 10
        session['cave_max_income'] += 10
        session['cave_level'] += 1 
        session['num_move'] -= 1
        session['money'] -= upgrade_cost
        check_upgrade_button()
        session['invest_window'] = False
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<span class="bg_light_blue"> You Level up your Cave ! Your Cave Level now is (lvl{session["cave_level"]})  .... {date.strftime("%c")}</span>')

        return redirect('/')

def check_upgrade_button(upgrade_cost=0):
    print(f"Cave LEvel = {session['cave_level']}")
    if session['farm_level']  >= 5 or session['cave_level'] >=5 or session['house_level'] >=5 or session['market_level'] >=5:
        session['button_disable'] = "disabled"
        session['upgrade_cost'] = "Completed"
        session['next_level'] = "Max"
        session['currency'] = ""
    
    else:
        try:
            check = int(session['money']) - int(session['upgrade_cost'])
            print(f"Money = {session['money']} / Upgrade cost = {session['upgrade_cost']}")
            if ( check >= 0):
                session['button_disable'] = ""
            else:
                session['button_disable'] = "disabled"
        except:
            session['upgrade_cost'] = upgrade_cost
            check = int(session['money']) - int(session['upgrade_cost'])
            print(f"Money = {session['money']} / Upgrade cost = {session['upgrade_cost']}")
            if ( check >= 0):
                session['button_disable'] = ""
            else:
                session['button_disable'] = "disabled"

@app.route('/')
def index():
    global init
    global level_bonus
    if init == True:
        session['money'] = 400
        session['activity_list'] = []
        session['disabled'] = ' '
        session['num_move'] = 200
        session['invest_window'] = False
        session['image_level_up'] = ""
        session['property_name'] = ""
        session['property_Level'] = "1"
        session['next_level'] = ""
        session['upgrade_details'] = ""
        session['upgrade_cost'] = ""
        session['button_disable'] = ""
        session['currency'] = "$"


        session['farm_level'] = 1
        session['farm_lower_income'] = 10
        session['farm_max_income'] = 200
        level_bonus = 1

        session['cave_level'] = 1
        session['cave_lower_income'] = 5
        session['cave_max_income'] = 10
        session['cave_treasure_chance'] = 5

        session['energy_ceil'] = 20
        session['house_level'] = 1
        

        session['market_level'] = 1
        session['base_price'] = 50
        session['taxes_value'] = 0.3
        session['buy_price'] = buy_price(session['base_price'],session['taxes_value'])  
        session['sell_price'] = sell_price(session['base_price'],session['taxes_value'])
        session['disabled_buy'] = ''






        init = False
    if session['num_move'] > session['energy_ceil']:
        session['num_move'] = session['energy_ceil']
    if session['buy_price'] > session['money'] or session['num_move'] == session['energy_ceil']:
        session['disabled_buy'] = 'disabled'
    else:
        session['disabled_buy'] = ''

    if session['money'] >= 500:
        session['disabled'] = 'disabled'
        session['disabled_buy'] = 'disabled'
        session['activity_list'].append(
            f'<span class="bg-success done text-center win">  Well Done !! You won the round !</span>')
    if session['num_move'] <= 0:
        session['disabled'] = 'disabled'
        session['disabled_buy'] = 'disabled'
        session['activity_list'].append(
            f'<span class="bg-warning text-center done ">  Game Over </span>')

    return render_template('index.html'
                            , player_money=session['money']
                            , activity=session['activity_list']
                            , activity_length=len(session['activity_list'])-1
                            , disabled=session['disabled']
                            , moves=session['num_move']
                            , invest_window=session['invest_window']
                            , property_name = session['property_name']
                            , property_level = session['property_Level']
                            , next_level = session['next_level']
                            , upgrade_details = session['upgrade_details']
                            , upgrade_cost = session['upgrade_cost']
                            , button_disabled = session['button_disable']
                            , image_level_up = session['image_level_up']
                            , farm_level = session['farm_level']
                            , farm_lower_income = session['farm_lower_income'] * level_bonus
                            , farm_max_income = session['farm_max_income'] * level_bonus
                            , currency = session['currency']
                            

                            ,cave_level =session['cave_level'] 
                            ,cave_lower_income =session['cave_lower_income']
                            ,cave_max_income =session['cave_max_income'] 
                            ,cave_treasure_chance =session['cave_treasure_chance']

                            ,house_level = session['house_level']
                            ,energy_ceil = session['energy_ceil']

                            ,market_level= session['market_level']
                            ,base_price = session['base_price']
                            ,taxes_value = session['taxes_value'] *100
                            ,buy_price = session['buy_price']
                            ,sell_price = session['sell_price']
                            ,disabled_buy = session['disabled_buy']


                            )

########### Cave Process Function ###########

def process_money_cave(generate_money,date):
    process_cave_chance()
    if session['cave_level'] <= 2:
        session['activity_list'].append(
        f'<span class="green">  Made : ({generate_money} $)  from the Cave .... {date.strftime("%c")}</span>')
    elif session['cave_level'] == 3:
        session['num_move'] -= 1
        session['activity_list'].append(
        f'<span class="green">  Made : ({generate_money} $)  from the Cave   <span class = "red"> Used : 1 Extra Energy </span> .... {date.strftime("%c")}</span>')
    elif session['cave_level'] == 4:
        session['num_move'] -= 2
        session['activity_list'].append(
        f'<span class="green">  Made : ({generate_money} $)  from the Cave   <span class = "red"> Used : 2 Extra Energy </span> .... {date.strftime("%c")}</span>')
    elif session['cave_level'] > 4:
        session['num_move'] -= 3
        session['activity_list'].append(
        f'<span class="green">  Made : ({generate_money} $)  from the Cave   <span class = "red"> Used : 3 Extra Energy </span> .... {date.strftime("%c")}</span>')
    
    return redirect('/')

################# Cave Chance Process ##################
def process_cave_chance():
    counter = 0
    chance_list = []
    while counter < session['cave_treasure_chance']  :
        generate_number = random.randint(0,100)
        if generate_number in chance_list:
            pass
        else:
            chance_list.append(generate_number)
            counter +=1
    print(f"The Chance_list = {chance_list}")
    generate_number = random.randint(0,100)
    print(f"The Chance Number  = {generate_number}")
    if generate_number in chance_list:
        print("I entered the Prize sections")

        prizes_list = [{"money" : 50},{"money" : 50},{"money" : 50},{"money" : 50},{"money" : 100},{"money" : 100}
                        ,{"energy" : 10},{"energy" : 10},{"energy" : 20}
                        ,{"upgrade" : "farm"},{"upgrade" : "house"},{"upgrade" : "market"}]
        
        generate_number = random.randint(0,len(prizes_list)-1)
        prize = prizes_list[generate_number]
        prize_key = list(prize.keys())
        prize_value=list(prize.values())
        print(f"Prize  = {prize}")
        print(f"Prize keys = {prize_key[0]}")
        print(f"Prize values = {prize_value[0]}")

        if prize_key[0] == "money":
            session['money'] += prize_value[0]
            date = datetime.datetime.now()
            session['activity_list'].append(
            f'<span class="bg-gold">  You Discoverd a Treasure !! : ({prize_value[0]} $)  from the Cave   .... {date.strftime("%c")}</span>')
        elif prize_key[0] == "energy":
            session['num_move'] += prize_value[0]
            date = datetime.datetime.now()
            session['activity_list'].append(
            f'<span class="bg-gold">  You Discoverd a Treasure !! : ({prize_value[0]} Energy)  from the Cave   .... {date.strftime("%c")}</span>')
        elif prize_key[0] == "upgrade":

            if prize_value[0] == "farm":
                session['upgrade_cost'] = 0
                upgrade_farm_lv2(session['farm_level'],session['upgrade_cost'])
                date = datetime.datetime.now()
                session['activity_list'].append(
                f'<span class="bg-gold">  You Discoverd a Treasure !! : A FREE ({prize_value[0]} Upgrade!!!!!)  from the Cave   .... {date.strftime("%c")}</span>')

            elif prize_value[0] == "house":
                session['upgrade_cost'] = 0
                session['house_level'] , session['money'], session['num_move'],session['energy_ceil'] = upgrade_house(session['house_level'],session['upgrade_cost'],session['money'],session['num_move'],session['energy_ceil'])
                date = datetime.datetime.now()
                session['activity_list'].append(
                f'<span class="bg-gold">  You Discoverd a Treasure !! : A FREE ({prize_value[0]} Upgrade!!!!!)  from the Cave   .... {date.strftime("%c")}</span>')



@app.route('/process_money', methods=['POST'])
def process_money():
    global init
    
    if request.form['property'] == "farm":
        session['num_move'] -= 1
        generate_money = random.randint(10, 20) * level_bonus
        session['money'] += generate_money
        date = datetime.datetime.now()
        if session['farm_level'] <= 2:
            session['activity_list'].append(
            f'<span class="green">  Made : ({generate_money} $)  from the Farms .... {date.strftime("%c")}</span>')
        elif session['farm_level'] == 3:
            session['num_move'] -= 2
            session['activity_list'].append(
            f'<span class="green">  Made : ({generate_money} $)  from the Farms   <span class = "red"> Used : 1 Extra Energy </span> .... {date.strftime("%c")}</span>')
        elif session['farm_level'] == 4:
            session['num_move'] -= 3
            session['activity_list'].append(
            f'<span class="green">  Made : ({generate_money} $)  from the Farms   <span class = "red"> Used : 2 Extra Energy </span> .... {date.strftime("%c")}</span>')
        elif session['farm_level'] > 4:
            session['num_move'] -= 4
            session['activity_list'].append(
            f'<span class="green">  Made : ({generate_money} $)  from the Farms   <span class = "red"> Used : 3 Extra Energy </span> .... {date.strftime("%c")}</span>')
        
        return redirect('/')
    
    elif request.form['property'] == "cave":
        session['num_move'] -= 1
        generate_money = random.randint(session['cave_lower_income'], session['cave_max_income'])
        session['money'] += generate_money
        date = datetime.datetime.now()
        process_money_cave(generate_money,date)
        return redirect('/')

    
    elif request.form['property'] == "buy":
        date = datetime.datetime.now()
        session['money'] , session['num_move'] = buy(session['base_price'],session['money'],session['taxes_value'],session['num_move'])
        session['activity_list'].append(
            f'<span class="">  You bought: (1 Energy)  from the Market at price  <span class = "red"> {session["buy_price"]}$ </span> .... {date.strftime("%c")}</span>')

        return redirect('/')
    
    elif request.form['property'] == "sell":
        date = datetime.datetime.now()
        session['money'] , session['num_move'] = sell(session['base_price'],session['money'],session['taxes_value'],session['num_move'])
        session['activity_list'].append(
            f'<span class="">  You Sold: (1 Energy)  at the Market at price <span class = "green"> {session["sell_price"]}$ </span> .... {date.strftime("%c")}</span>')

        return redirect('/')
    
    elif request.form['property'] == "reset":
        init = True
        return redirect('/')

#Setting Up Upgrade page for 4 properties
@app.route('/process_level_up', methods=['POST'])
def process_level_up():
    session['invest_window'] = True
    
    match request.form['invest_window_button']:
            case "invest_farm":
                session['property_name'] = "Farm"
                session['image_level_up'] = "farm2.jpg"
                session['property_Level'] = session['farm_level']
                next_level = int(session['property_Level']) + 1
                session['next_level'] = next_level
                match next_level:
                    case 2:
                        session['upgrade_details'] = "+25% production income"
                        session['upgrade_cost'] = 50
                        check_upgrade_button()
                    case 3:
                        session['upgrade_details'] = "+50% production income"
                        session['upgrade_cost'] = 150
                        check_upgrade_button()
                    case 4:
                        session['upgrade_details'] = "+100% production income   <span class = 'red'> -3 Energy </span>"
                        session['upgrade_cost'] = 250
                        check_upgrade_button()
                    case 5:
                        session['upgrade_details'] = "+125% production income    <span class = 'red'> -7 Energy </span>"
                        session['upgrade_cost'] = 350
                        check_upgrade_button()
                    case _:
                        session['upgrade_details'] = "No more Upgrades Available"
                        check_upgrade_button()
                return redirect('/')
        
            case "invest_cave":
                session['property_name'] = "Cave"
                session['image_level_up'] = "cave2.jpg"
                session['property_Level'] = session['cave_level']
                next_level = int(session['property_Level']) + 1
                session['next_level'] = next_level
                match next_level:
                    case 2:
                        session['upgrade_details'] = "<ul class = 'fs-2'><li>+5$ production income </li> <li>+5% Finding a Treasure Chance</li> </ul> "
                        session['upgrade_cost'] = 75
                        check_upgrade_button()
                    case 3:
                        session['upgrade_details'] = "<ul class = 'fs-2'><li>+5$ production income </li> <li>+5% Finding a Treasure Chance</li><li><span class = 'red'> -1 Extra Energy pre Exploration </span></li> </ul> "
                        session['upgrade_cost'] = 125
                        check_upgrade_button()
                    case 4:
                        session['upgrade_details'] = "<ul class = 'fs-2'><li>+10$ production income </li> <li>+5% Finding a Treasure Chance</li><li><span class = 'red'> -1 Extra Energy pre Exploration </span></li> </ul>   "
                        session['upgrade_cost'] = 210
                        check_upgrade_button()
                    case 5:
                        session['upgrade_details'] = "<ul class = 'fs-2'><li>+5$ production income </li> <li>+5% Finding a Treasure Chance</li><li><span class = 'red'> -1 Extra Energy pre Exploration </span></li> </ul>"
                        session['upgrade_cost'] = 300
                        check_upgrade_button()
                    case _:
                        session['upgrade_details'] = "No more Upgrades Available"
                        check_upgrade_button()

            case "invest_house":
                session['property_name'] = "House"
                session['image_level_up'] = "home2.jpg"
                session['property_Level'] = session['house_level']
                next_level = int(session['property_Level']) + 1
                session['next_level'] = next_level
                session['upgrade_details'],session['upgrade_cost'] = check_house_level(next_level)
                check_upgrade_button()

            case "invest_market":
                session['property_name'] = "Market"
                session['image_level_up'] = "market2.jpg"
                session['property_Level'] = session['market_level']
                next_level = int(session['property_Level']) + 1
                session['next_level'] = next_level
                session['upgrade_details'],session['upgrade_cost'] = check_market_level(next_level)
                check_upgrade_button()
            case _:
                pass
                
        
    if request.form['invest_window_button'] == "cancel":
        session['invest_window'] = False
        return redirect('/')
    elif request.form['invest_window_button'] == "level_up_Farm":
        upgrade_farm_lv2(session['farm_level'],session['upgrade_cost'])
    elif request.form['invest_window_button'] == "level_up_Cave":
        upgrade_cave(session['cave_level'],session['upgrade_cost'])
    elif  request.form['invest_window_button'] == "level_up_House":
        session['house_level'] , session['money'], session['num_move'],session['energy_ceil'] = upgrade_house(session['house_level'],session['upgrade_cost'],session['money'],session['num_move'],session['energy_ceil'])
    elif  request.form['invest_window_button'] == "level_up_Market":
        session['market_level'] , session['money'], session['taxes_value'] = upgrade_market(session['market_level'],session['money'],session['upgrade_cost'],session['taxes_value'])
        session['buy_price'] = buy_price(session['base_price'],session['taxes_value'])  
        session['sell_price'] = sell_price(session['base_price'],session['taxes_value'])
        session['invest_window'] = False



    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
