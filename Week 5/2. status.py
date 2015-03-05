def status_count(students):
    
    final_dict = {
        "finalized":[],
        "not_finalized":[]
        }
   
    for each_dictionary in students:
        current_status = each_dictionary["status"]
        if current_status == "finalized":
            final_dict[current_status] += [each_dictionary["name"]]
        else:
            final_dict[current_status] += [each_dictionary["name"]]
            
    return final_dict

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))
