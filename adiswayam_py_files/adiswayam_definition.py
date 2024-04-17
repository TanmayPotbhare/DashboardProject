from classes.connections import DatabaseConnection, AdiswayamHost
import mysql.connector


def test():
    host = AdiswayamHost().hostserver
    query = "SELECT COUNT(*) FROM tbl_batch;"
    try:
        with DatabaseConnection(host, 'root', 'A>(I?mx|pt220uzE', 'aadiswayam_portaldb') as conn:
            if conn.is_connected():
                print('Connected to the database!')
            else:
                print('Failed to connect to the database.')
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")