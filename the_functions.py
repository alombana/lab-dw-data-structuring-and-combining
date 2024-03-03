def cleaning_one(data):
    data.rename(columns=lambda x: x.replace(" ","_").replace("ST","state").lower(), inplace=True)
    
    data['gender']=data['gender'].apply(str)
    data['state']=data['state'].apply(str)
    data['education']=data['education'].apply(str)
    data['customer_lifetime_value']=data['customer_lifetime_value'].apply(str)
    data['vehicle_class']=data['vehicle_class'].astype(str)
    data['number_of_open_complaints']=data['number_of_open_complaints'].apply(str)
    
    return data

def invalid_values(gender):
    replacements=[('nan','nan'), ('Femal','F'),('Male','M'), ('female','F')]
    for x, y in replacements:
        gender=gender.replace(x,y)
    return gender

def invalid_values_1(state):
    replacements=[('AZ','Arizona'), ('Cali','California'),('WA','Washington'), ('nan','NaN')]
    for x, y in replacements:
        state=state.replace(x,y)
    return state

def invalid_values_2(education):
    replacements=[('Bachelors','Bacherlo')]
    for x, y in replacements:
        education=education.replace(x,y)
    return education

def invalid_values_3(vehicle_class):
    replacements=[('Sports Car','Luxury'),('Luxury SUV','Luxury'),('Luxury Car','Luxury')]
    for x, y in replacements:
        vehicle_class=vehicle_class.replace(x,y)
    return vehicle_class

def invalid_values_4(number_of_open_complaints):
    try:
        
        if number_of_open_complaints=='nan':
            return number_of_open_complaints
        else:
            number_of_open_complaints=number_of_open_complaints.split('/')[1]
            return int(number_of_open_complaints)
    except IndexError:
        return int(number_of_open_complaints)
    
    
        
    
        

def cleaning_two(data):

    data['gender']=data['gender'].apply(invalid_values)
    data['state']=data['state'].apply(invalid_values_1)
    data['education']=data['education'].apply(invalid_values_2)
    data['vehicle_class']=data['vehicle_class'].apply(invalid_values_3)
    data['number_of_open_complaints']=data['number_of_open_complaints'].apply(invalid_values_4)

    data['customer_lifetime_value'] = data['customer_lifetime_value'].apply(lambda x: x.replace("%","") if "%" in x else x.replace('nan','0'))

    data['customer_lifetime_value'] = data['customer_lifetime_value'].apply(lambda x: float(x) if x!='nan' else x.replace('0', 0))

    return data
    
    
def run_all(data):
    cleaning_one(data)
    cleaning_two(data)
    
    return data
    
