document.getElementById('shareBtn').onclick = function() {
  FB.ui({
    client_id:'327939761408427',
    display: 'popup',
    method: 'share',
    href: '{{ request.build_absolute_uri }}{{ object.get_absolute_url }}',
  }, function(response){});
}



(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));