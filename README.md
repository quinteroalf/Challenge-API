# Challenge-API
Welcome to the XalDigital Challenge

To consume the service with sample data we have 3 methods

1.-GET
https://5ca4-2806-2f0-1000-1041-295a-88f1-3b20-56a2.ngrok.io/api/samples

2.- POST
https://5ca4-2806-2f0-1000-1041-295a-88f1-3b20-56a2.ngrok.io/api/samples/add

  {
   "first_name": "alfredo",
   "last_name": "mar", 
	 "company_name": "MachineL",
	 "address": "castro",
   "city": "tijuana",
   "state": "BC",
	 "zip": 22115,
	 "phone1": "6641992851",
   "email": "quintero@gmail.com",   
	 "department": "Sales"
  }
  
  
  3.- PUT
  
  https://5ca4-2806-2f0-1000-1041-295a-88f1-3b20-56a2.ngrok.io/api/samples/update/alfredo
  
   {   
   "last_name": "nunez", 
	 "company_name": "last",
	 "address": "post",
   "city": "24",
   "state": "BC",
	 "zip": 22115,
	 "phone1": "5555",
   "email": "quintero@gmail.com",   
	 "department": "IT"
  }
