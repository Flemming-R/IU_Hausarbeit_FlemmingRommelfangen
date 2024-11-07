# Schema für das ER-Diagramm als Mermaid-Code
database_schema_mermaid='''
    erDiagram
        %% Faktentabelle
        ENROLLMENT_FACTS {
            int Enrollment_ID PK
            int Student_ID FK
            int Course_ID FK
            int Professor_ID FK
            date Enrollment_Date
            string Grade
        }

        %% Dimensionstabelle: Student
        STUDENT_DIMENSION {
            int Student_ID PK
            string First_Name
            string Last_Name
            date Date_of_Birth
            date Enrollment_Date
            string Email
        }

        %% Dimensionstabelle: Course
        COURSE_DIMENSION {
            int Course_ID PK
            string Course_Name
            int Credits
            int Department_ID FK
        }

        %% Dimensionstabelle: Professor
        PROFESSOR_DIMENSION {
            int Professor_ID PK
            string First_Name
            string Last_Name
            string Email
        }

        %% Dimensionstabelle: Department
        DEPARTMENT_DIMENSION {
            int Department_ID PK
            string Department_Name
        }

        %% Beziehungen
        ENROLLMENT_FACTS }|--|| STUDENT_DIMENSION : "belongs to"
        ENROLLMENT_FACTS }|--|| COURSE_DIMENSION : "involves"
        ENROLLMENT_FACTS }|--|| PROFESSOR_DIMENSION : "taught by"
        COURSE_DIMENSION }|--|| DEPARTMENT_DIMENSION : "part of"
    '''

# HTML und JavaScript-Code zum Rendern des Mermaid-Diagramms
mermaid_html = f"""
<div class="mermaid">
{database_schema_mermaid}
</div>
<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
mermaid.initialize({{ startOnLoad: true }});
</script>
"""

