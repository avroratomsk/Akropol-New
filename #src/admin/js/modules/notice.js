const notices = document.querySelectorAll(".notice");
console.log(notices)
setTimeout(() => {
  notices.forEach(notice => {
    notice.classList.add("hidden");
    setTimeout(() => notice.remove(), 500);
  });
}, 3000);