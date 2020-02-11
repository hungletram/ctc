function tel() {
  alert('Đã gọi');
};

// datetime

var d = new Date();

function formatdt(d) {
  var day = ['Chủ nhật','Thứ hai','Thứ ba','Thứ tư','Thứ năm','Thứ sáu','Thứ bảy'][d.getDay()];
  var dd = d.getDate();
  var mm = d.getMonth() + 1;
  var yy = d.getFullYear();
  var h = d.getHours() > 9? d.getHours(): '0'+d.getHours();
  var m = d.getMinutes() > 9? d.getMinutes(): '0'+d.getMinutes();
  var zone = -d.getTimezoneOffset() / 60;
  var gmt = zone >= 0? '+'+zone : zone;
  return day+', '+[dd,mm,yy].join('/')+', '+[h,m].join(':')+' (GMT'+gmt+')';
};

document.getElementById('topdate').innerHTML = formatdt(d);

// scroll with page

window.onscroll = function() {myFunction()};

var header = document.getElementById("ontop");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

// alert(d / -60)