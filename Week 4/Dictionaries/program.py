first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")
birthday = input("Enter birthday date in a format Month.Day.Year: ")

def get_dictionary_with_my_info(first_name,second_name,third_name,birthday):
    
    current_year = 2015
    year = birthday[6:]
    year =  int(year)

    info_dic = {
        "current_age": current_year - year,
        "birth_year":year,
        "first_name":first_name,
        "second_name":second_name,
        "third_name":third_name,
        }

    return info_dic


print(get_dictionary_with_my_info(first_name,second_name,third_name,birthday))
