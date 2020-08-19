from covid import Covid
covid=Covid()
print("Total active covid case=",covid.get_total_active_cases())
print("Total death due to covid=",covid.get_total_deaths())
print("Total covid confirmed cases=",covid.get_total_confirmed_cases())
print(covid.get_status_by_country_name("india"))
