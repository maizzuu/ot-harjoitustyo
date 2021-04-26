from entities.month import Month

def print_month(month=Month):
    total = (month.food + month.living + month.hobbies
                 + month.transportation + month.culture + month.other)
    if month.username[-1] == "s":
        print(f"""
        {month.username}' {month.month} of {month.year}
        
        Food: {month.food}
        Living: {month.living}
        Hobbies: {month.hobbies}
        Transportation: {month.transportation}
        Culture: {month.transportation}
        Other: {month.other}

        Total spending: {total}

        """)
    else:
        print(f"""
        {month.username}'s {month.month} of {month.year}
        
        Food: {month.food}
        Living: {month.living}
        Hobbies: {month.hobbies}
        Transportation: {month.transportation}
        Culture: {month.transportation}
        Other: {month.other}

        Total spending: {total}

        """)
