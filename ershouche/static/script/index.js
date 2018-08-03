
$(function(){
	 
	/*$('.banShow').cycle(
	{
		
		fx:'fade',
		timeout:6000,
		next:'.nexts',
		prev:'.prevs'
	}
	); */
   
	$('.c-item').hover(function(){
		
		$(this).toggleClass('active');
	});
	
	$(window).bind('scroll',function(e){
		var sTop=$(window).scrollTop();
		if(sTop<=460){
			
			$('.head-search').hide();
			$('#header .logo').hide();
			$('.nav a:first').css('padding-left','0px');
		}else{
			$('.head-search').fadeIn();
			$('#header .logo').show();
			$('.nav a:first').css('padding-left','20px');
		}
	});
	
	$(".slide").slide({titCell:'.hd li',mainCell:".bd ul",effect:"fold",autoPlay:true,vis:1});
	
	$('.mDiv').hover(function(){
		$(this).addClass('active');
	})
	$('.jpTit a').each(function(index){
		$(this).click(function(){
			$(this).addClass('on').siblings().removeClass('on');
			$('.jpDl').eq(index).fadeIn().siblings().hide();
		})
	});
})


function register() {
	var mobile = $('#mobile_1_2').val()
	var name = $('#user_name').val()
	var password = $('#password').val()
	var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    // $.post('register/', {'mobile':mobile,'name':name,'password':password}, function (msg) {
		// alert(msg.msg)
    // })
	$.ajax({
		url: 'register/',
		type: 'POST',
		dataType: 'json',
		headers: {'X-CSRFToken': csrf},
		data: {'mobile':mobile,'name':name,'password':password},
		success: function (msg) {
			if (msg.code==200) {
				$('.sell-phone-error').text('注册成功')
				$('.sell-phone-error').show()
			} else {
				$('.sell-phone-error').text(msg.msg)
				$('.sell-phone-error').show()
			}
        },
		error: function (msg) {
			alert('111')
        }
	})

}
$(document).ready(function () {
	$('.sell-phone-error').hide()
})

function login() {
	var mobile = $('#mobile_login').val()
	var password = $('#password_login').val()
	var csrf = $('input[name="csrfmiddlewaretoken"]').val()
	$.ajax({
		url: 'login/',
		type: 'POST',
		dataType: 'json',
		headers: {'X-CSRFToken': csrf},
		data: {'mobile':mobile,'password':password},
		success: function (msg) {
			if (msg.code==200) {
				$('.sell-phone-error').text('登录成功')
				$('.sell-phone-error').show()
			} else {
				$('.sell-phone-error').text(msg.msg)
				$('.sell-phone-error').show()
			}
        },
		error: function (msg) {
			alert('111')
        }
	})
}