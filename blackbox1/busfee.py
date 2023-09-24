def busTicketDiscount(ticket_type, between5_70):
    '''
    ticket type
    1. yearly_ticket
    2. monthly_ticket
    3. daily_ticket
    age: 0 to inf

    discount:
    bellow 5 year old or above 70: 50% for yearly or 30% for monthly

    calculate bus ticket
    '''
    if ticket_type not in [1, 2, 3]:
        raise ValueError('invalid age or ticket_type')
    
    match ticket_type:
        case 1:
            if not between5_70:
                dis = 50
            else:
                dis = 10
            pass
        case 2:
            if not between5_70:
                dis = 30
            else:
                dis = 0
            pass
        case 3:
            if not between5_70:
                dis = 10
            else:
                dis = 0
            pass

    return ticket_type, dis
