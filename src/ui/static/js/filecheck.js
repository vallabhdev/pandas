function findFileExtension(filename) {
  var parts = filename.split('.');
  return parts[parts.length - 1];
}

function isImage(filename) {
  var ext = findFileExtension(filename);
  const supported_ext = ["jpg", "jpeg", "bmp", "png"]
  return supported_ext.indexOf(ext) !== -1
}

function get_size_in_mb(file) {
    return ((file.size/1024)/1024).toFixed(4);
}

function check_file()
{
    var upload_btn = document.getElementById("file_id");
    file = upload_btn.files[0];
    var size_in_MB = get_size_in_mb(file);
    var submit_btn = document.getElementById("submit_btn")

    if(!isImage(file.name)) {
        alert("Images only please. Supported formats: jpg, jpeg, png, bmp");
        upload_btn.value = ""
        submit_btn.disabled = true
    } else if(size_in_MB > 1) {
        alert("That's a nice photo, but too big. Try one that is smaller than 1MB.");
        upload_btn.value = ""
        submit_btn.disabled = true
    } else {
        submit_btn.disabled = false
    }
};