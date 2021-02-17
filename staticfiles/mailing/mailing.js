let expanded = false

let showCheckboxes = (checkbox_id) => {
  let checkboxes = document.getElementById(checkbox_id);
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}