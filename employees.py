# Employee Table's Dictionary
employee={
    1001:{
        "empname":"Ashish",
        "Designation Code":'E',
        "Department":"R&D",
        "Basic": 20000,
        "HRA": 8000,
        "IT": 3000
    },
    1002:{
        "empname":"Sushma",
        "Designation Code":'C',
        "Department":"PM",
        "Basic": 30000,
        "HRA": 12000,
        "IT": 9000
    },
    1003:{
        "empname":"Rahul",
        "Designation Code":'K',
        "Department":"Account",
        "Basic": 10000,
        "HRA": 8000,
        "IT": 1000
    },
    1004:{
        "empname":"Chahat",
        "Designation Code":'R',
        "Department":"Front Desk",
        "Basic": 12000,
        "HRA": 6000,
        "IT": 2000
    },
    1005:{
        "empname":"Ranjan",
        "Designation Code":'M',
        "Department":"Engg",
        "Basic": 50000,
        "HRA": 20000,
        "IT": 20000
    },
    1006:{
        "empname":"Suman",
        "Designation Code":'E',
        "Department":"Manufacturing",
        "Basic": 23000,
        "HRA": 9000,
        "IT": 4400
    },
    1007:{
        "empname":"Tanmay",
        "Designation Code":'C',
        "Department":"PM",
        "Basic": 29000,
        "HRA": 12000,
        "IT": 10000
    }
}
#DA Table's Dictionary
DA={
    'E':{'designation':'Engineer','DA':20000},
    'C':{'designation':'Consultant','DA':32000},
    'K':{'designation':'Clerk','DA':12000},
    'R':{'designation':'Receptionist','DA':15000},
    'M':{'designation':'Manager','DA':40000}
}
id=int(input("Enter Employee id: "))
print("\n\nEmployee Details:\nEmployee Id:",id,
"\nName:",employee[id]["empname"],
"\nDepartment:",employee[id]["Department"],
"\nDesignation:",DA[employee[id]["Designation Code"]]['designation'],
"\nSalary:",employee[id]["Basic"]+employee[id]["HRA"]+employee[id]["IT"])  