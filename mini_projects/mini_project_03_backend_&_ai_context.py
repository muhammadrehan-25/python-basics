#=============================================
# AI Agent Request Validator & Rate Limiter 
#=============================================

""" Discription:Make a backend module simulation which
cheack the request before sending to AI Agent.

Requirements:Take three inputs from user 
1. api_key (string)
2. user_tokens (intiger ex: how many remaining)
3. request_priority (string "High","medium","low")

logic flow: 
1.First, check whether the api_key is valid or not
   (e.g., it should not be empty and must be at least 10 characters long).
2.If the API key is invalid, return an instant error: "Invalid API Key".
3.If the API key is valid, check if user_tokens are greater than 0.
4.If tokens are 0, return an error: "Insufficient Tokens".
5.If tokens are available and the priority is "high", output: 
   "Request Routed to Fast Track AI Pipeline".
6.For all other priorities, output: "Request Queued for Standard AI Pipeline"."""

api_key=input("Enter valid API key: ").strip()
if not api_key or len(api_key)<10:
    print("Invalid API key")
else:
    user_tokens=int(input("Enter Tokens: "))
    if user_tokens<=0:
        print("Insuficient Tokens")
    else:
        request_periority=input("Enter request priority  ex:('High','Medium','Low'): ").strip().lower()

        if request_periority == 'high':
             print("Request Routed to Fast Track AI Pipeline")  
        else:
             print("Request Queued for Standard AI Pipeline.")