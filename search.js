$(document).ready(function () {
    $('.srchgms').on('focus', function(){
        $('.game-prev').show()

    })
    $('.srchgms').on('blur', function(){
        $('.game-prev').hide()
        $(this).val('')
    })
    
    $('.srchgms').on('keyup', function(){
        var query = $(this).val()
        
        $.get("../directory.html", function(data) {
            $(data).find(".list-title").each(function(index, element) {
                
            });
        });
        
    })
    
})