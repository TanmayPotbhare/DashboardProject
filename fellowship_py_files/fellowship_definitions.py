from classes.connections import DatabaseConnection, FellowshipHost
import mysql.connector


def visitor_count():
    # Read the current count from the file
    try:
        with open('visit_count.txt', 'r') as f:
            count = int(f.read().strip())
    except FileNotFoundError:
        count = 0
    # Increment the count
    count += 1
    # Write the new count back to the file
    with open('visit_count.txt', 'w') as f:
        f.write(str(count))
    return count


def applications_today():
    host = FellowshipHost().hostserver
    query = "SELECT COUNT(*) FROM application_page"
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def current_year_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) FROM application_page where phd_registration_year='2023' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def accepted_year_count():
    host = FellowshipHost().hostserver
    query = " SELECT COUNT(*) FROM application_page where phd_registration_year='2023' and final_approval='accepted' "
    try:
        with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")