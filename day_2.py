sample_data = {
    "status": "success",
    "status_code": 1,
    "message": "Printing information.",
    "data": {
        "orderinfo": [
            {
                "title": "Restaurant Management System",
                "token_no": "12",
                "ordertime": "06:43:30 PM",
                "orderdate": "14/02/2022",
                "order_id": "271",
                "customerName": "Walkin",
                "customerPhone": "8801717426371",
                "waiter": "Pravin Meshram",
                "tableno": "51",
                "tableName": "Table-3",
                "kitcheninfo": [
                    {
                        "kitchenName": "Arabian",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Bangla",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Bengali Food",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Beverage",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Chinese",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Common",
                        "ip": "",
                        "port": "",
                        "isitemexist": 1,
                        "iteminfo": [
                            {
                                "itemName": "Bangla Set Menu Rice Boarta",
                                "variantName": "1:2",
                                "qty": "1",
                                "notes": "",
                                "isaddons": 0,
                                "addonsinfo": [
                                    {
                                        "add_onsName": "",
                                        "add_onsqty": ""
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "kitchenName": "Dessert",
                        "ip": "lmklm",
                        "port": "dsfdfd.com",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "French",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Indian",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "indian food",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Italian",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Japanese",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "Lunch Package",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "MAIN",
                        "ip": "",
                        "port": "",
                        "isitemexist": 1,
                        "iteminfo": [
                            {
                                "itemName": "Pasta",
                                "variantName": "Spicy",
                                "qty": "1",
                                "notes": "No meets will be added",
                                "isaddons": 1,
                                "addonsinfo": [
                                    {
                                        "add_onsName": "souc",
                                        "add_onsqty": "1"
                                    },
                                    {
                                        "add_onsName": "Butter",
                                        "add_onsqty": "1"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "kitchenName": "Maxican",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    },
                    {
                        "kitchenName": "salad",
                        "ip": "",
                        "port": "",
                        "isitemexist": 0
                    }
                ]
            }
        ]
    }
}

""" Q1: - Print status.
Expected Output: success """
# Answer:
# print(sample_data['status'])

""" Q2: - Print status code
Expected Output: 1 """
# Answer:
# print(sample_data['status_code'])

""" Q3: - Print massage 
Expected Output: Printing information. """
# Answer:
# print(sample_data['message'])

""" Q4: - Print title 
Expected Output: Restaurant Management System """
# Answer:
# print(sample_data['data']['orderinfo'][0]['title'])
# for i in sample_data['data']['orderinfo']:
#     print(i["title"])

""" Q5: - Print token_no 
Expected Output: 12 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['token_no'])
# for i in sample_data['data']['orderinfo']:
#     print(i["token_no"])


""" Q6: - Print ordertime 
Expected Output: 06:43:30 PM """
# Answer:
# print(sample_data['data']['orderinfo'][0]['ordertime'])
# for i in sample_data['data']['orderinfo']:
#     print(i["ordertime"])


""" Q7: - Print orderdate 
Expected Output: 14/02/2022 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['orderdate'])
# for i in sample_data['data']['orderinfo']:
#     print(i["orderdate"])


""" Q8: - Print order_id 
Expected Output: 271 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['order_id'])
# for i in sample_data['data']['orderinfo']:
#     print(i["order_id"])


""" Q9: - Print customerName 
Expected Output: Walkin """
# Answer:
# print(sample_data['data']['orderinfo'][0]['customerName'])
# for i in sample_data['data']['orderinfo']:
#     print(i["customerName"])


""" Q10: - Print customerPhone 
Expected Output: 8801717426371 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['customerPhone'])
# for i in sample_data['data']['orderinfo']:
#     print(i["customerPhone"])


""" Q11: - Print waiter 
Expected Output: Pravin Meshram """
# Answer:
# print(sample_data['data']['orderinfo'][0]['waiter'])
# for i in sample_data['data']['orderinfo']:
#     print(i["waiter"])

""" Q12: - Print tableno 
Expected Output: 51 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['tableno'])
# for i in sample_data['data']['orderinfo']:
#     print(i["tableno"])


""" Q13: - Print tableName 
Expected Output: Table-3 """
# Answer:
# print(sample_data['data']['orderinfo'][0]['tableName'])
# for i in sample_data['data']['orderinfo']:
#     print(i["tableName"])


""" Q14: - Print all kitchen name 
Expected Output: Arabian, Bangla, Bengali Food, Beverage, Chinese, Common, etc. """
# Answer:
# print(sample_data['data']['orderinfo'][0]['kitcheninfo'][0]['kitchenName'])
# for i in sample_data['data']['orderinfo']:
#    for j in (i["kitcheninfo"]):
#        print(j['kitchenName'])

""" Q15: - If isitemexist = 1 
then print itemName, variantName, qty, notes. """

""" Q16: - If isaddons = 1 
then print all add_onsName and add_onsqty. """

""" Q17: - Print all "addonsinfo" length 
Expected Output: 1, 2 """
