import { useState } from "react";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";

function App() {
  const [students, setStudents] = useState([]);

  const addStudent = (student) => {
    setStudents([...students, student]);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Registration System</h1>

      <StudentForm addStudent={addStudent} />

      <br />

      <StudentList students={students} />
    </div>
  );
}

export default App;
