function calculateMinimumLectures(totalLectures, attendedLectures) {
  let ans = 0;

  // Formula to compute
  if (attendedLectures < Math.ceil(0.7 * totalLectures))
    ans = Math.ceil((0.7 * totalLectures - attendedLectures) / 0.3);
  else ans = 0;

  return ans;
}

function fetchAttendance() {
  const enrollmentNumber = document.getElementById("enrollmentNumber").value;
  fetchAttendanceData(enrollmentNumber);
}

function displayAttendanceData(attendanceData) {
  const container = document.getElementById("attendanceContainer");
  const table = document.createElement("table");
  table.classList.add("attendance-table");

  const headers = [
    "Course",
    "Class Type",
    "Total",
    "Percentage",
    "Minimum 70% Attendance",
  ];

  const headerRow = document.createElement("tr");
  headers.forEach((headerText) => {
    const th = document.createElement("th");
    th.textContent = headerText;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  attendanceData.forEach((courseData) => {
    const { Course, "Class Type": ClassType, Total, Percentage } = courseData;
    const parts = Total.split("/").map((item) => parseInt(item.trim()));

    const attendedLectures = parts[0];
    const totalLectures = parts[1];

    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td>${Course}</td>
            <td>${ClassType}</td>
            <td>${Total}</td>
            <td>${Percentage}</td>
            <td class="min-attendance">${calculateMinimumLectures(
              totalLectures,
              attendedLectures
            )}</td>
        `;
    table.appendChild(tr);
  });

  container.appendChild(table);
}

function fetchAttendanceData(enrollmentNumber) {
  const fileName = `${enrollmentNumber}_attendance.txt`;

  fetch(fileName)
    .then((response) => response.text())
    .then((data) => {
      const lines = data.split("\n");
      const attendanceData = [];
      let currentCourseData = {};
      lines.forEach((line) => {
        if (line.startsWith("Course:")) {
          currentCourseData = {};
          const parts = line.split(":");
          currentCourseData.Course = parts[1].trim();
        } else if (line.startsWith("Class Type:")) {
          const parts = line.split(":");
          currentCourseData["Class Type"] = parts[1].trim();
        } else if (line.startsWith("Total:")) {
          const parts = line.split(":");
          currentCourseData.Total = parts[1].trim();
        } else if (line.startsWith("Percentage:")) {
          const parts = line.split(":");
          currentCourseData.Percentage = parts[1].trim();
          attendanceData.push(currentCourseData);
        }
      });
      displayAttendanceData(attendanceData);
    })
    .catch((error) => console.error("Error fetching data:", error));
}
