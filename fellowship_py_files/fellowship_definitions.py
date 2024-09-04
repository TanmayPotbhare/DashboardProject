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


# # To fetch the count of Applications for current year 2023.
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
    query = "SELECT final_approval, COUNT(*) as twentyCount FROM application_page WHERE phd_registration_year='2020' GROUP BY final_approval"
    twenty_counts = {'accepted': 0, 'pending': 0}  # Initialize with default values
    
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2020 year's count: {result}")
            if result:
                for row in result:
                    if row['final_approval'] in twenty_counts:
                        twenty_counts[row['final_approval']] = row['twentyCount']
            else:
                print("No data found for counts of applicants from year 2020.")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return twenty_counts

def gender_count():
    host = FellowshipHost().hostserver
    query = "SELECT gender, COUNT(*) AS StudentGenderCount FROM application_page GROUP BY gender"
    gender_counts = {'Male': 0, 'Female': 0, 'Other': 0}  # Initialize with default values

    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for gender counts: {result}")
            if result:
                for row in result:
                    if row['gender'] in gender_counts:
                        gender_counts[row['gender']] = row['StudentGenderCount']
            else:
                print("No data found for gender counts.")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return gender_counts 

# To fetch the count of Applications for year 2021 by the application status.
def twentyOne_count():
    host = FellowshipHost().hostserver
    query = "SELECT final_approval, COUNT(*) as twentyOneCount FROM application_page WHERE phd_registration_year='2021' GROUP BY final_approval"
    twentyOne_counts = {'accepted': 0, 'pending': 0}  # Initialize with default values
    
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2021 year's count: {result}")
            if result:
                for row in result:
                    if row['final_approval'] in twentyOne_counts:
                        twentyOne_counts[row['final_approval']] = row['twentyOneCount']
            else:
                print("No data found for counts of applicants from year 2021.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    return twentyOne_counts

# To fetch the count of Applications for year 2022 by the application status.
def twentyTwo_count():
    host = FellowshipHost().hostserver
    query = " SELECT final_approval, COUNT(*) as twentyTwoCount FROM application_page where phd_registration_year='2022' GROUP BY final_approval"
    twentyTwo_counts = {'accepted': 0, 'pending': 0}  # Initialize with default values
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2022 year's count: {result}")
            if result:
                for row in result:
                        if row['final_approval'] in twentyTwo_counts:
                            twentyTwo_counts[row['final_approval']] = row['twentyTwoCount']
            else:
                print("No data found for counts of applicants from year 2022.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return twentyTwo_counts    

# To fetch the count of Applications for year 2023 by the application status.
def twentyThree_count():
    host = FellowshipHost().hostserver
    query = " SELECT final_approval, COUNT(*) as twentyThreeCount FROM application_page where phd_registration_year='2023' GROUP BY final_approval"
    twentyThree_counts = {'accepted': 0, 'pending': 0}  # Initialize with default values
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2023 year's count: {result}")
            if result:
                for row in result:
                        if row['final_approval'] in twentyThree_counts:
                            twentyThree_counts[row['final_approval']] = row['twentyThreeCount']
            else:
                print("No data found for counts of applicants from year 2022.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return twentyThree_counts 


# To fetch the count of Applications for year 2024 by the application status.
def twentyFour_count():
    host = FellowshipHost().hostserver
    query = " SELECT final_approval, COUNT(*) as twentyFourCount FROM application_page where phd_registration_year='2024' GROUP BY final_approval"
    twentyFour_counts = {'accepted': 0, 'pending': 0}
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for 2024 year's count: {result}")
            if result:
                for row in result:
                    if row['final_approval'] in twentyFour_counts:
                        twentyFour_counts[row['final_approval']] = row['twentyFourCount']
            else:
                print("No data found for counts of applicants from year 2024.")  
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return twentyFour_counts

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

# To fetch the Gender wise count of all applications
def gender_count():
    host = FellowshipHost().hostserver
    query = "SELECT gender, COUNT(*) AS StudentGenderCount FROM application_page GROUP BY gender"
    gender_counts = {'Male': 0, 'Female': 0, 'Other': 0}  # Initialize with default values

    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for gender counts: {result}")
            if result:
                for row in result:
                    if row['gender'] in gender_counts:
                        gender_counts[row['gender']] = row['StudentGenderCount']
            else:
                print("No data found for gender counts.")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return gender_counts                 

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

# To fetch the count of Total disable Applicants.
def disability_yes_count():
    host = FellowshipHost().hostserver
    query = "SELECT  gender,COUNT(*) as disabiltyYesCount FROM application_page WHERE disability='Yes' GROUP BY gender"
    disabilityYes_counts = {'Male': 0, 'Female': 0, 'Other':0 }
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Candidates with disability: {result}")
            if result:
                for row in result:
                    if row['gender'] in disabilityYes_counts:
                        disabilityYes_counts[row['gender']] = row['disabiltyYesCount']
            else:
                print("No data found for counts of applicants with disability.") 
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}") 
    return disabilityYes_counts                 

# To fetch the count of Total Applicants without disability.
def disability_no_count():
    host = FellowshipHost().hostserver
    query = "SELECT  gender, COUNT(*) as disabiltyNoCount FROM application_page WHERE disability='No' GROUP BY gender"
    disabilityNo_counts = {'Male': 0, 'Female': 0, 'Other':0 }
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            print(f"Result for Candidates without disability: {result}")
            if result:
                for row in result:
                    if row['gender'] in disabilityNo_counts:
                        disabilityNo_counts[row['gender']] = row['disabiltyNoCount']
            else:
                print("No data found for counts of applicants without disability.") 
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}") 
    return disabilityNo_counts   