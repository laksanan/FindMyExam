import csv
import io
from urllib import request

def get_all_students():
    """
    Fetches student data from the Google Sheet CSV export.
    Returns a list of dictionaries.
    """
    csv_url = "https://docs.google.com/spreadsheets/d/1t3BL9BlqRuNoghb8SKSzBMZHR7Ci2Ch00yjwObGFzJY/gviz/tq?tqx=out:csv&gid=0"
    
    try:
        response = request.urlopen(csv_url)
        data = response.read().decode('utf-8')
        csv_file = io.StringIO(data)
        reader = csv.DictReader(csv_file)
        
        # Mapping CSV headers to our keys if necessary, or just using them as is.
        # Based on user description:
        # Col A: ลำดับ (Sequence)
        # Col B: Student I.D
        # Col C: Name Surname
        # Col D: ห้องสอบ (Exam Room)
        
        students = []
        for row in reader:
             # Clean keys strip whitespace
            clean_row = {k.strip(): v.strip() for k, v in row.items() if k}
            students.append(clean_row)
            
        return students
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def search_student_by_id(student_id):
    """
    Searches for a student by Student I.D.
    """
    if not student_id:
        return []
        
    all_students = get_all_students()
    results = []
    
    # Normalize input
    query_id = str(student_id).strip()
    
    for student in all_students:
        # Actual keys from CSV: 'NO.', 'Student I.D.', 'Name Surname', 'room'
        # We need to map these to our template variables or just return as is
        
        # Check if 'Student I.D.' matches query
        # Using exact key from inspection
        if student.get('Student I.D.') == query_id:
            # Create a standardized dict for the template
            result_student = {
                'Sequence': student.get('NO.', ''),
                'ID': student.get('Student I.D.', ''),
                'Name': student.get('Name Surname', ''),
                'Room': student.get('room', ''),
                'Subject': student.get('Subject', ''),
                'Date': student.get('Date', '')
            }
            results.append(result_student)
            
    return results
