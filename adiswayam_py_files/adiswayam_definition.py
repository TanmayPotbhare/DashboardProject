from flask import jsonify

from classes.connections import DatabaseConnection, AdiswayamHost
import mysql.connector


def total_candidates():
    host = AdiswayamHost().central
    query = " SELECT COUNT(*) AS totalCandidate FROM tbl_candidate WHERE phase = 'p1' "
    print(query)
    try:
        with DatabaseConnection(host, 'remoteAccess', 'Shubham2428@', 'aadiswayam_production') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


def total_training_center():
    host = AdiswayamHost().central
    query = " SELECT COUNT(*) AS totalTraningCenter FROM tbl_training_center WHERE phase = 'p1' "
    print(query)
    try:
        with DatabaseConnection(host, 'remoteAccess', 'Shubham2428@', 'aadiswayam_production') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


def total_training_partner():
    host = AdiswayamHost().central
    query = " SELECT COUNT(*) AS trainingPartner FROM tbl_tp WHERE phase = 'p1' "
    print(query)
    try:
        with DatabaseConnection(host, 'remoteAccess', 'Shubham2428@', 'aadiswayam_production') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


def placement_count():
    host = AdiswayamHost().central
    query = " SELECT COUNT(*) AS placementCount FROM tbl_candidate_placement JOIN tbl_candidate ON" \
            " tbl_candidate_placement.candidate_id_fk = tbl_candidate.candidate_id WHERE tbl_candidate.phase = 'p1' "
    print(query)
    try:
        with DatabaseConnection(host, 'remoteAccess', 'Shubham2428@', 'aadiswayam_production') as conn:
            result = conn.execute_query(query)
            count = result[0][0]
            print(count)
            return count
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500