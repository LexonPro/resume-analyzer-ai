async function analyze() {
  const file = document.getElementById("resume").files[0];
  const jd = document.getElementById("jd").value;

  if (!file || !jd) {
    alert("Upload resume & enter job description");
    return;
  }

  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  const formData = new FormData();
  formData.append("file", file);
  formData.append("job_description", jd);

  const res = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();

  document.getElementById("loader").classList.add("hidden");
  document.getElementById("result").classList.remove("hidden");

  document.getElementById("score").innerText = data.score;
  document.getElementById("progress-bar").style.width = data.score + "%";

  const keywordsDiv = document.getElementById("keywords");
  keywordsDiv.innerHTML = "";

  data.missing_keywords.forEach(k => {
    const span = document.createElement("span");
    span.innerText = k;
    keywordsDiv.appendChild(span);
  });
}