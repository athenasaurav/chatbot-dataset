
/* module for importing other js files */
function include(file) {
  const script = document.createElement('script');
  script.src = file;
  script.type = 'text/javascript';
  script.defer = true;

  document.getElementsByTagName('head').item(0).appendChild(script);
}



// Bot pop-up intro
document.addEventListener("DOMContentLoaded", () => {
  const elemsTap = document.querySelector(".tap-target");
  // eslint-disable-next-line no-undef
  const instancesTap = M.TapTarget.init(elemsTap, {});
  instancesTap.open();
  setTimeout(() => {
    instancesTap.close();
  }, 4000);
});

/* import components */
include('./static/js/components/index.js');

window.addEventListener('load', () => {
  // initialization
  $(document).ready(() => {
    // Bot pop-up intro
    $("div").removeClass("tap-target-origin");

    // drop down menu for close, restart conversation & clear the chats.
    $(".dropdown-trigger").dropdown();

    // initiate the modal for displaying the charts,
    // if you dont have charts, then you comment the below line
    $(".modal").modal();

    // enable this if u have configured the bot to start the conversation.
    // showBotTyping();
    // $("#userInput").prop('disabled', true);

    // if you want the bot to start the conversation
    customActionTrigger();
  });
  // Toggle the chatbot screen
  $("#profile_div").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
  });

  // clear function to clear the chat contents of the widget.
  $("#clear").click(() => {
    $(".chats").fadeOut("normal", () => {
      $(".chats").html("");
      $(".chats").fadeIn(0, "linear");
      customActionTrigger();
    });
  });

  // close function to close the widget.
  $("#close").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
    scrollToBottomOfResults();
  });
  
});

var e = jQuery.Event("keypress");
e.which = 13; 
e.keyCode = 13;

function ButtonClick_feedback()
{
  textbox.val('Feedback');
  var e = $.Event( "keypress", { which: 13 } );
  $('#userInput').trigger(e);
  $('#feedbackField').hide(e);
}
function chatScrollDown(){
  const chats = document.getElementById("chats");
  chats.scrollTop = chats.scrollHeight - chats.clientHeight;
  console.log(chats.scrollTop);
}

function toggleFullscreen(elem) {
  elem = elem || document.documentElement;

  if (!document.fullscreenElement && !document.mozFullScreenElement &&
    !document.webkitFullscreenElement && !document.msFullscreenElement) {
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
      document.getElementById("btnFullscreen").className = "fa fa-compress"
    } else if (elem.msRequestFullscreen) {
      elem.msRequestFullscreen();
      document.getElementById("btnFullscreen").className = "fa fa-compress"
    } else if (elem.mozRequestFullScreen) {
      elem.mozRequestFullScreen();
      document.getElementById("btnFullscreen").className = "fa fa-compress"
    } else if (elem.webkitRequestFullscreen) {
      elem.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
      document.getElementById("btnFullscreen").className = "fa fa-compress"
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
      document.getElementById("btnFullscreen").className = "fa fa-expand"
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
      document.getElementById("btnFullscreen").className = "fa fa-expand"
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
      document.getElementById("btnFullscreen").className = "fa fa-expand"
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
      document.getElementById("btnFullscreen").className = "fa fa-expand"
    }
  }
}


document.getElementById('btnFullscreen').addEventListener('click', function(){
  toggleFullscreen(chatcontainer);
  chatScrollDown();  


});

// speech
var speechRecognition = window.webkitSpeechRecognition
var recognition = new speechRecognition()
var textbox = $("#userInput")
var content = ''
recognition.continuous = true
// recognition is started
recognition.onstart = function() {
}
recognition.onspeechend = function() {
}
recognition.onerror = function() {
}
recognition.onresult = function(event) {
 var current = event.resultIndex;
 var transcript = event.results[current][0].transcript
 content = transcript
 textbox.val(content)
}

$('#sendVoice').on('mousedown',function(){
  recognition.start();
  
}).on('mouseup',function(){
  recognition.stop();
});

