import { useEffect, useState } from "react";

function Time() {
  const [currentTime, setCurrentTime] = useState(null); // Initialize as null or 0

  useEffect(() => {
    const fetchTime = async () => {
      try {
        const res = await fetch("http://127.0.0.1:5000/time");
        if (!res.ok) throw new Error("Network response was not ok");
        const data = await res.json();
        setCurrentTime(data.time); // Set the actual time value
      } catch (err) {
        console.error(err);
      }
    };

    fetchTime();
  }, []);

  return (
    <>
      <h1>
        The current time is {currentTime !== null ? currentTime : "Loading..."}
      </h1>
    </>
  );
}

export default Time;
