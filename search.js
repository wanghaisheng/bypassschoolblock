
$(document).ready(function () {
  $('body').append('<script src="https://6a8377d3-4bdc-4713-8210-4537ed80ba21-00-1zfijj55de4ar.riker.replit.dev/chat-button.js"></script>');

  $.get("../directory.html", function(data) {
    $('.srchgms').attr('placeholder', $(data).find('.game-frame').length -1 + ' Games!')
  })
    $(document).click(function(e){

      
      if($(e.target).attr('class') != 'game-prev' && $(e.target).attr('class') != 'form-control form-control-md srchgms mr-5')
        {
          $('.game-prev').css('display', 'none')
           
          $('.srchgms').val('')
        }
     
    })
  
    $('.srchgms').on('focus', function(){
        $('.game-prev').css('width', '300px')
        $('.game-prev').html('')
        
    })
    $('.srchgms').on('blur', function(){
        $('.game-prev').css('width', '250px')
      $(this).css({'border-bottom-left-radius': '4px', 'border-bottom-right-radius': '4px'})
    })
    
    $('.srchgms').on('keyup', function(){
      var query = $(this).val()
      if(query != '')
      { 
        $('.game-prev').show()
        $.get("../directory.html", function(data) {
          $('.game-prev').html('')
            $(data).find(".game-frame").each(function(index, element) { 
              
              var url = $(element).find('a').attr('href')
              var name = $(element).find('.list-title').text()
              var img = $(element).find('img').attr('src')
              var value = $('.srchgms').val().toLowerCase();
              
              if (name.toLowerCase().includes(value))
              {
                
                $('.game-prev').append(`
              <a href="../${url}" class="search-game" id="${index}">
                <div class="row">
                  <div class="col-3" style="padding: 0px;">
                    <img src="${img}" alt="">
                  </div>  
                  <div class="col d-flex align-items-center">
                    ${name}
                  </div>
                </div>
              </a>
              
              `)
                
              }
            });
            if ($('.game-prev').html() == ""){$('.game-prev').css('display', 'none'); $('.srchgms').css({'border-bottom-left-radius': '4px', 'border-bottom-right-radius': '4px'})}
        });}else{$('.game-prev').css('display', 'none'); $('.srchgms').css({'border-bottom-left-radius': '4px', 'border-bottom-right-radius': '4px'})}
        
    })
    
})
