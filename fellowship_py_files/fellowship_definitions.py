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
            print(f"Result for Accepted current year's count: {result}")
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

