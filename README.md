# CR Attendance Generator 

This project helps Class Representatives (CR) quickly generate attendance
lists when teachers cannot take attendance due to time or network issues.

The system stores student ID and name in a database and generates
attendance text that can be directly copied and sent via WhatsApp or online platforms.

---

## 🚀 Features (Current)
- Student data stored in MySQL database
- Fetch student ID & name automatically
- Course-wise and date-wise attendance support (basic)

---

## 🛠️ Technologies Used
- Python
- MySQL
- mysql-connector-python

---

## 📂 Database Structure

**Database Name:** `cr_attendance`

**Table:** `students`

| Column | Type |
|------|------|
| student_id | VARCHAR |
| name | VARCHAR |

---

## ▶️ How to Run

1. Clone the repository  
```bash
git clone https://github.com/anrobbiswasantu4049/attendance_generator.git

