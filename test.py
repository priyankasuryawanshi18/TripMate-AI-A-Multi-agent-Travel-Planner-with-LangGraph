from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


#res=tavily_search("Best hotels in india")
#print(res)

res=search_flights("plan a 7 days japan trip from bangladesh")
print(res)