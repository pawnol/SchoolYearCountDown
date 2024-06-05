let countDownDate;
let intervalID;
let json_data;

// Get necessary files and start counter
const xhr = new XMLHttpRequest();
xhr.open("GET", "/datesjson");
xhr.send()
xhr.responseType = "json";
xhr.onreadystatechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    json_data = xhr.response;
    updateEvent();
    remainingTime()
    intervalID = setInterval(remainingTime, 1000);
  }
  else {
    console.log(`Error: ${xhr.status}`)
  }
};

// Refresh counter
function remainingTime() {
  let now = new Date();

  let distance = countDownDate - now;
  if (distance < 0) {
    updateEvent();
    distance = countDownDate - now;
  }
  let days = Math.floor(distance / (1000 * 60 * 60 * 24));
  let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("days").textContent = days;
  document.getElementById("hours").textContent = hours;
  document.getElementById("minutes").textContent = minutes;
  document.getElementById("seconds").textContent = seconds;
  if (days == 1) {
    document.getElementById("days-label").textContent = "Day";
  }
  else {
    document.getElementById("days-label").textContent = "Days";
  }
  if (hours == 1) {
    document.getElementById("hours-label").textContent = "Hour";
  }
  else {
    document.getElementById("hours-label").textContent = "Hours";
  }
  if (minutes == 1) {
    document.getElementById("minutes-label").textContent = "Minute";
  }
  else {
    document.getElementById("minutes-label").textContent = "Minutes";
  }
  if (seconds == 1) {
    document.getElementById("seconds-label").textContent = "Second";
  }
  else {
    document.getElementById("seconds-label").textContent = "Seconds";
  }
}

function getNextEvent(events) {
  let now = new Date();

  // Find the first event that is current
  let nextEvent;
  for(let e of events.events) {
    let date = new Date(e.date);
    if (date > now) {
      nextEvent = e;
      break;
    }
  }
  
  // Check the rest of the events to see if it would beat it
  for(let e of events.events) {
    let date = new Date(e.date);
    let nextDate = new Date(nextEvent.date);
    if (date > now && date < nextDate) {
      nextEvent = e;
    }
  }
  return nextEvent;
}

function updateEvent() {
  let event = getNextEvent(json_data);
  countDownDate = new Date(event.date);
  document.getElementById("date").textContent = countDownDate.toLocaleString();
  if (event.summary.toLowerCase().includes("first")) {
    document.getElementById("background").className = "first-day"
    document.getElementById("icon").setAttribute("href", "static/images/pencil.ico");
  }
  else {
    document.getElementById("background").className = "last-day"
    document.getElementById("icon").setAttribute("href", "static/images/sun.ico");
  }
  document.getElementById("event-title").textContent = event.summary;
}