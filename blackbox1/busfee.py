def busTicket(ticket_type, age):
    '''
    ticket type
    1. yearly_ticket: 210$
    2. monthly_ticket: 20.0$
    3. daily_ticket: 1.0$
    age: 0 to inf

    discount:
    0 to 5 year old: 100% 
    5 to 10 year old: 30%
    10 to 70 year old: 0%
    above 70 : 100%

    calculate bus ticket
    '''
    if age < 0 or age // 1 != age:
        raise ValueError('invalid age')
    if age >= 0 and age < 5:
        discount = 100
    elif age >= 5 and age <10:
        discount = 30
    elif age >= 10 and age < 70:
        discount = 0
    else:
        discount = 100

    discount = 1 - discount/100
    if ticket_type == 1:
        fee = discount * 210
        pass
    elif ticket_type == 2:
        fee = discount * 20
        pass
    elif ticket_type == 3:
        fee = discount * 1
        pass
    else:
        raise ValueError('Invalid ticket type it must be 1: yearly, 2:montlyh, 3:daily')
    
    return (ticket_type, fee)