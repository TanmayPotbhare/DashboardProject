from classes.connections import DatabaseConnection, FellowshipHost
import mysql.connector


# To fetch the count of visitors on the application
def visitor_count():
    # Read the current count from the file
    try:
        with open('visit_count.txt', 'r') as f:
            count = int(f.read().strip())
    except FileNotFoundError:
        count = 0
    # Increment in the count
    count += 1
    # Write the new count back to the file
    with open('visit_count.txt', 'w') as f:
        f.write(str(count))
    return count

# To fetch the count of Total Applications.
def applications_today():
    host = FellowshipHost().hostserver
    query = "SELECT COUNT(*) as totalCount FROM application_page" 
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            print("Connected to the database.")
            result = conn.execute_query(query)
            print(f"Result for total Applications {result}")

            # to check if the result has any unexpected value and if list 'result' has item result[0] as a dictionary with key 'totalCount'.
            if result and isinstance(result[0], dict) and 'totalCount' in result[0]:

                #to fetch the value of key 'totalCount' from dict 'result[0]' of list 'result'.
                count = result[0]['totalCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}") 
    except Exception as e:
        print(f"Unexpected Error: {e}")  


# To fetch the count of Applications for current year 2023.
def current_year_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) as currentYearCount FROM application_page where phd_registration_year='2023' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Current year's count: {result}")
            if result and isinstance(result[0], dict) and 'currentYearCount' in result[0]:
                #to fetch the value of key 'currentYearCount' from dict 'result[0]' of list 'result'.
                count = result[0]['currentYearCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# To fetch the count of Applications for year 2020.
def twenty_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) as twentyCount FROM application_page where phd_registration_year='2020' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2020 year's count: {result}")
            if result and isinstance(result[0], dict) and 'twentyCount' in result[0]:
                #to fetch the value of key 'twentyCount' from dict 'result[0]' of list 'result'.
                count = result[0]['twentyCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# To fetch the count of Applications for year 2021.
def twentyOne_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) as twentyOneCount FROM application_page where phd_registration_year='2021' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2021 year's count: {result}")
            if result and isinstance(result[0], dict) and 'twentyOneCount' in result[0]:
                #to fetch the value of key 'twentyOneCount' from dict 'result[0]' of list 'result'.
                count = result[0]['twentyOneCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# To fetch the count of Applications for year 2022.
def twentyTwo_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) as twentyTwoCount FROM application_page where phd_registration_year='2022' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2022 year's count: {result}")
            if result and isinstance(result[0], dict) and 'twentyTwoCount' in result[0]:
                #to fetch the value of key 'twentyTwoCount' from dict 'result[0]' of list 'result'.
                count = result[0]['twentyTwoCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


# To fetch the count of Applications for year 2024.
def twentyFour_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) as twentyFourCount FROM application_page where phd_registration_year='2024' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2024 year's count: {result}")
            if result and isinstance(result[0], dict) and 'twentyFourCount' in result[0]:
                #to fetch the value of key 'twentyFourCount' from dict 'result[0]' of list 'result'.
                count = result[0]['twentyFourCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# To fetch the count of Accepted applications for current year 2023.
def accepted_year_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) acceptedCurrentYear FROM application_page where phd_registration_year='2023' and final_approval='accepted' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Accepted current year's count: {result}")
            if result and isinstance(result[0], dict) and 'acceptedCurrentYear' in result[0]:
                #to fetch the value of key 'acceptedCurrentYear' from dict 'result[0]' of list 'result'.
                count = result[0]['acceptedCurrentYear']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")



# To fetch the count of Rejected applications for current year 2023.
def rejected_year_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) rejectedCurrentYear FROM application_page where phd_registration_year='2023' and final_approval='rejected' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Rejected current year's count: {result}")
            if result and isinstance(result[0], dict) and 'rejectedCurrentYear' in result[0]:
                #to fetch the value of key 'rejectedCurrentYear' from dict 'result[0]' of list 'result'.
                count = result[0]['rejectedCurrentYear']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")        


# To fetch the count of Male Applicants
def male_student_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleStudentCount FROM application_page where gender = 'male' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates count: {result}")
            if result and isinstance(result[0], dict) and 'maleStudentCount' in result[0]:
                #to fetch the value of key 'maleStudentCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleStudentCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")          

# To fetch the count of Female Applicants
def female_student_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleStudentCount FROM application_page where gender = 'female' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates count: {result}")
            if result and isinstance(result[0], dict) and 'femaleStudentCount' in result[0]:
                #to fetch the value of key 'femaleStudentCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleStudentCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# To fetch the count of Male Applicants in year 2020
def male_twenty_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleTwentyCount FROM application_page where gender = 'male' AND phd_registration_year='2020'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates in year 2020: {result}")
            if result and isinstance(result[0], dict) and 'maleTwentyCount' in result[0]:
                #to fetch the value of key 'maleTwentyCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleTwentyCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")           

# To fetch the count of Male Applicants in year 2021
def male_twentyOne_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleTwentyOneCount FROM application_page where gender = 'male' AND phd_registration_year='2021'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates in year 2021: {result}")
            if result and isinstance(result[0], dict) and 'maleTwentyOneCount' in result[0]:
                #to fetch the value of key 'maleTwentyOneCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleTwentyOneCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}") 

# To fetch the count of Male Applicants in year 2022
def male_twentyTwo_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleTwentyTwoCount FROM application_page where gender = 'male' AND phd_registration_year='2022'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates in year 2022: {result}")
            if result and isinstance(result[0], dict) and 'maleTwentyTwoCount' in result[0]:
                #to fetch the value of key 'maleTwentyTwoCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleTwentyTwoCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")         


# To fetch the count of Male Applicants in year 2023
def male_twentyThree_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleTwentyThreeCount FROM application_page where gender = 'male' AND phd_registration_year='2023'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates in year 2023: {result}")
            if result and isinstance(result[0], dict) and 'maleTwentyThreeCount' in result[0]:
                #to fetch the value of key 'maleTwentyThreeCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleTwentyThreeCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")         

# To fetch the count of Male Applicants in year 2024
def male_twentyFour_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) maleTwentyFourCount FROM application_page where gender = 'male' AND phd_registration_year='2024'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Male candidates in year 2024: {result}")
            if result and isinstance(result[0], dict) and 'maleTwentyFourCount' in result[0]:
                #to fetch the value of key 'maleTwentyFourCount' from dict 'result[0]' of list 'result'.
                count = result[0]['maleTwentyFourCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}") 

# To fetch the count of Female Applicants in year 2020
def female_twenty_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleTwentyCount FROM application_page where gender = 'female' AND phd_registration_year='2020'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates in year 2020: {result}")
            if result and isinstance(result[0], dict) and 'femaleTwentyCount' in result[0]:
                #to fetch the value of key 'femaleTwentyCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleTwentyCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}") 

# To fetch the count of Female Applicants in year 2021
def female_twentyOne_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleTwentyOneCount FROM application_page where gender = 'female' AND phd_registration_year='2021'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates in year 2021: {result}")
            if result and isinstance(result[0], dict) and 'femaleTwentyOneCount' in result[0]:
                #to fetch the value of key 'femaleTwentyOneCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleTwentyOneCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# To fetch the count of Female Applicants in year 2022
def female_twentyTwo_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleTwentyTwoCount FROM application_page where gender = 'female' AND phd_registration_year='2022'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates in year 2022: {result}")
            if result and isinstance(result[0], dict) and 'femaleTwentyTwoCount' in result[0]:
                #to fetch the value of key 'femaleTwentyTwoCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleTwentyTwoCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")    

# To fetch the count of Female Applicants in year 2023
def female_twentyThree_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleTwentyThreeCount FROM application_page where gender = 'female' AND phd_registration_year='2023'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates in year 2023: {result}")
            if result and isinstance(result[0], dict) and 'femaleTwentyThreeCount' in result[0]:
                #to fetch the value of key 'femaleTwentyThreeCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleTwentyThreeCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")     
                 
# To fetch the count of Female Applicants in year 2024
def female_twentyFour_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) femaleTwentyFourCount FROM application_page where gender = 'female' AND phd_registration_year='2024'  "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Female candidates in year 2023: {result}")
            if result and isinstance(result[0], dict) and 'femaleTwentyFourCount' in result[0]:
                #to fetch the value of key 'femaleTwentyFourCount' from dict 'result[0]' of list 'result'.
                count = result[0]['femaleTwentyFourCount']
                print(f"Count : {count}") 
                return count
            else:
                print("Unexpected result format from query.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")     
